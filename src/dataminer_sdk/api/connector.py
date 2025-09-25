import requests
import httpx
from ..utils.decorators import auto_async_methods
from .enums import TransportMode, SOAPVersion
from .exceptions import UnsupportedTransportMode
from urllib.parse import urlencode
from typing import Optional, Tuple


class BaseConnector:
    """
    DataMiner API connector supporting hybrid sync/async calls.
    Supports SOAP and URL GET modes.
    """

    def __init__(
        self,
        hostname: str,
        username: str,
        password: str,
        client_app_name: str = "PythonClient",
        client_app_version: str = "1.0",
        client_computer_name: str = "Unset",
        transport_mode: TransportMode = TransportMode.URL,
        soap_version: SOAPVersion = SOAPVersion.SOAP12,
        auto_reconnect: bool = True,
        use_https: Optional[bool] = None,
        use_2fa: bool = False,
    ):
        self._hostname = hostname
        self._username = username
        self._password = password
        self._client_app_name = client_app_name
        self._client_app_version = client_app_version
        self._client_computer_name = client_computer_name
        self._transport_mode = transport_mode
        self._soap_version = soap_version
        self._auto_reconnect = auto_reconnect
        self._use_2fa = use_2fa

        self._use_https = use_https
        if self._use_https is None:
            self._use_https = self._ping_https()
        self._url = (
            f"{'https' if self._use_https else 'http'}://{hostname}/API/v1/soap.asmx"
        )

        self._connection_token = None

    # --- Connection Management ---

    def _connect(
        self, async_: bool = False, transport_mode: Optional[TransportMode] = None
    ):
        params = {
            "host": self._hostname,
            "login": self._username,
            "password": self._password,
            "clientAppName": self._client_app_name,
            "clientAppVersion": self._client_app_version,
            "clientComputerName": self._client_computer_name,
        }
        return self._call_api(
            "ConnectApp", params, async_=async_, transport_mode=transport_mode
        )

    @property
    def connection_token(self):
        if not self._connection_token and self._auto_reconnect:
            if self._use_2fa:
                raise NotImplementedError("2FA is not implemented yet.")
            return self._connect()
        return self._connection_token

    def _ping_https(self) -> bool:
        test_url = f"https://{self._hostname}/API/v1/soap.asmx"
        try:
            resp = requests.get(test_url, timeout=3, verify=False)
            return resp.status_code == 200
        except requests.RequestException:
            return False

    def _call_api(
        self,
        method: str,
        params: dict,
        async_: bool = False,
        transport_mode: Optional[TransportMode] = TransportMode.SOAP,
    ):
        if async_:
            return self._call_api_async(method, params, transport_mode)
        else:
            return self._call_api_sync(method, params, transport_mode)

    # --- Synchronous Calls ---

    def _call_api_sync(
        self, method: str, params: dict, transport_mode: Optional[TransportMode]
    ):
        if transport_mode == TransportMode.SOAP:
            return self._call_soap(params, method)
        elif transport_mode == TransportMode.URL:
            return self._call_url(params, method)
        else:
            raise UnsupportedTransportMode(
                f"Transport mode {transport_mode} is not supported."
            )

    def _call_url(self, params: dict, method: str):
        url = self._get_api_content_url(params, method)
        resp = requests.get(url, verify=False)
        resp.raise_for_status()
        return resp.content.decode("utf-8")

    def _call_soap(self, params: dict, method: str):
        envelope, headers = self._get_api_content_soap(params, method)

        resp = requests.post(self._url, data=envelope, headers=headers, verify=False)
        resp.raise_for_status()
        return resp.content.decode("utf-8")

    # --- Async Calls ---

    async def _call_api_async(
        self, method: str, params: dict, transport_mode: Optional[TransportMode]
    ):
        if transport_mode == TransportMode.SOAP:
            return await self._call_soap_async(params, method)
        elif transport_mode == TransportMode.URL:
            return await self._call_url_async(params, method)
        else:
            raise UnsupportedTransportMode(
                f"Transport mode {transport_mode} is not supported."
            )

    async def _call_url_async(self, params: dict, method: str):
        async with httpx.AsyncClient() as client:
            url = self._get_api_content_url(params, method)
            resp = await client.get(url)
            resp.raise_for_status()
            return resp.text

    async def _call_soap_async(self, params: dict, method: str):
        envelope, headers = self._get_api_content_soap(params, method)
    
        async with httpx.AsyncClient() as client:
            resp = await client.post(self._url, data=envelope, headers=headers)  # type: ignore
            resp.raise_for_status()
            return resp.text
        
    # --- API Call Content ---

    def _get_api_content_url(self, params: dict, method: str) -> str:
        qs = urlencode(params)
        return f"{self._url}/{method}?{qs}"

    def _get_api_content_soap(self, params: dict, method: str) -> Tuple[str, dict]:
        body = "".join(f"<{k}>{v}</{k}>" for k, v in params.items())
        soap = "soap" if self._soap_version == SOAPVersion.SOAP11 else "soap12"
        envelope = f"""<?xml version="1.0" encoding="utf-8"?>
<{soap}:Envelope
    xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
    xmlns:xsd="http://www.w3.org/2001/XMLSchema"
    xmlns:{soap}="http://schemas.xmlsoap.org/soap/envelope/">
  <{soap}:Body>
    <{method} xmlns="http://www.skyline.be/api/v1">
      {body}
    </{method}>
  </{soap}:Body>
</{soap}:Envelope>"""
        
        if self._soap_version == SOAPVersion.SOAP12:
            headers = {
                "Content-Type": "application/soap+xml; charset=utf-8",
            }
        else:
            headers = {
                "Content-Type": "text/xml; charset=utf-8",
                "SOAPAction": f"http://www.skyline.be/api/v1/{method}",
            }

        return envelope, headers


# This is the class that will be used by the users of the SDK
@auto_async_methods
class DataMinerConnector(BaseConnector):
    pass
