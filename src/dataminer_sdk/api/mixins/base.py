# from collections.abc import Coroutine
# import requests
# import httpx
# from dataminer_sdk.api.mixins.parameter import ParameterMixin
# from dataminer_sdk.utils.decorators import auto_async_methods
# from dataminer_sdk.api.enums import TransportMode, SOAPVersion
# from dataminer_sdk.api.exceptions import UnsupportedTransportMode
# from dataminer_sdk.utils.xml import extract_result
# from urllib.parse import urlencode
# from typing import Any, Dict, Literal, Optional, Tuple, Union, overload

# # TEMP: Disable insecure request warnings for self-signed certs
# import urllib3
# import warnings

# warnings.simplefilter("ignore", urllib3.exceptions.InsecureRequestWarning)


# class BaseConnector:
#     """
#     Base class for connecting to the DataMiner API.

#     Supports both synchronous and asynchronous calls, SOAP and URL transport
#     modes, automatic reconnection, and optional HTTPS detection.
#     """

#     def __init__(
#         self,
#         hostname: str,
#         username: str,
#         password: str,
#         client_app_name: str = "PythonClient",
#         client_app_version: str = "1.0",
#         client_computer_name: str = "Unset",
#         transport_mode: TransportMode = TransportMode.URL,
#         soap_version: SOAPVersion = SOAPVersion.SOAP11,
#         auto_reconnect: bool = True,
#         use_https: Optional[bool] = None,
#         use_2fa: bool = False,
#     ):
#         """
#         Initialize a new BaseConnector.

#         Args:
#             hostname: DataMiner server hostname.
#             username: Username for authentication.
#             password: Password for authentication.
#             client_app_name: Name of the client application.
#             client_app_version: Version of the client application.
#             client_computer_name: Name of the client computer.
#             transport_mode: Default transport mode (SOAP or URL).
#             soap_version: SOAP version to use (SOAP11 or SOAP12).
#             auto_reconnect: Automatically reconnect if the token is missing.
#             use_https: Force HTTPS if True, HTTP if False, autodetect if None.
#             use_2fa: Whether to use two-factor authentication (not yet implemented).
#         """
#         self._hostname = hostname
#         self._username = username
#         self._password = password
#         self._client_app_name = client_app_name
#         self._client_app_version = client_app_version
#         self._client_computer_name = client_computer_name
#         self._transport_mode = transport_mode
#         self._soap_version = soap_version
#         self._auto_reconnect = auto_reconnect
#         self._use_2fa = use_2fa

#         self._use_https = use_https
#         if self._use_https is None:
#             self._use_https = self._ping_https()
#         self._url = (
#             f"{'https' if self._use_https else 'http'}://{hostname}/API/v1/soap.asmx"
#         )

#         self._connection_token = None

#     # --- Connection Management ---

#     def _connect(self, transport_mode: Optional[TransportMode] = None):
#         """
#         Establish a connection with the DataMiner API.

#         Args:
#             transport_mode: Override transport mode for this call.

#         Returns:
#             API response content.
#         """
#         params = {
#             "host": self._hostname,
#             "login": self._username,
#             "password": self._password,
#             "clientAppName": self._client_app_name,
#             "clientAppVersion": self._client_app_version,
#             "clientComputerName": self._client_computer_name,
#         }
#         self._connection_token = extract_result(
#             "ConnectApp",
#             self._call_api(
#                 "ConnectApp", params, async_=False, transport_mode=transport_mode
#             ),  # type: ignore
#         )

#     @property
#     def connection_token(self):
#         """
#         Return the current connection token.

#         If no token is set and auto-reconnect is enabled, attempts to
#         establish a new connection. Raises if 2FA is enabled.
#         """
#         if not self._connection_token and self._auto_reconnect:
#             if self._use_2fa:
#                 raise NotImplementedError("2FA is not implemented yet.")
#             self._connect()
#             return self._connection_token
#         return self._connection_token

#     def _ping_https(self) -> bool:
#         """
#         Test whether HTTPS is supported by the server.

#         Returns:
#             True if HTTPS responds with status 200, False otherwise.
#         """
#         test_url = f"https://{self._hostname}/API/v1/soap.asmx"
#         try:
#             resp = requests.get(test_url, timeout=3, verify=False)
#             return resp.status_code == 200
#         except requests.RequestException:
#             return False

#     @overload
#     def _call_api(
#         self,
#         method: str,
#         params: Dict[str, Any],
#         transport_mode: Optional[TransportMode] = ...,
#         *,
#         async_: Literal[False] = ...,
#         _attempted_reconnect: bool = ...,
#     ) -> Optional[str]: ...

#     @overload
#     def _call_api(
#         self,
#         method: str,
#         params: Dict[str, Any],
#         transport_mode: Optional[TransportMode] = ...,
#         *,
#         async_: Literal[True],
#         _attempted_reconnect: bool = ...,
#     ) -> Coroutine[Any, Any, Optional[str]]: ...

#     def _call_api(
#         self,
#         method: str,
#         params: dict,
#         transport_mode: Optional[TransportMode] = TransportMode.SOAP,
#         async_: bool = False,
#         _attempted_reconnect: bool = False,
#     ) -> Union[Optional[str], Coroutine[Any, Any, Optional[str]]]:
#         """
#         Call the DataMiner API using sync or async mode.

#         Args:
#             method: API method name.
#             params: API parameters.
#             transport_mode: Transport mode (SOAP or URL).

#         Returns:
#             API response content.
#         """
#         transport_mode = transport_mode or self._transport_mode
#         try:
#             if async_:
#                 return self._call_api_async(method, params, transport_mode)
#             else:
#                 return self._call_api_sync(method, params, transport_mode)
#         except (requests.HTTPError, httpx.RequestError):
#             if self._auto_reconnect and not _attempted_reconnect:
#                 self._connection_token = None  # Force reconnect next time
#                 return self._call_api(
#                     method,
#                     params,
#                     async_=async_,
#                     transport_mode=transport_mode,
#                     _attempted_reconnect=True,
#                 )
#             else:
#                 raise

#     # --- Synchronous Calls ---

#     def _call_api_sync(
#         self, method: str, params: dict, transport_mode: Optional[TransportMode]
#     ):
#         """
#         Perform a synchronous API call.

#         Args:
#             method: API method name.
#             params: API parameters.
#             transport_mode: Transport mode (SOAP or URL).

#         Returns:
#             API response content.

#         Raises:
#             UnsupportedTransportMode: If the transport mode is invalid.
#         """
#         if transport_mode == TransportMode.SOAP:
#             return self._call_soap(params, method)
#         elif transport_mode == TransportMode.URL:
#             return self._call_url(params, method)
#         else:
#             raise UnsupportedTransportMode(
#                 f"Transport mode {transport_mode} is not supported."
#             )

#     def _call_url(self, params: dict, method: str):
#         """
#         Perform a synchronous URL GET request.

#         Args:
#             params: Query parameters.
#             method: API method name.

#         Returns:
#             Response content as a UTF-8 string.
#         """
#         url = self._get_api_content_url(params, method)
#         resp = requests.get(url, verify=False)
#         resp.raise_for_status()
#         return resp.content.decode("utf-8")

#     def _call_soap(self, params: dict, method: str):
#         """
#         Perform a synchronous SOAP request.

#         Args:
#             params: Request parameters.
#             method: API method name.

#         Returns:
#             Response content as a UTF-8 string.
#         """
#         envelope, headers = self._get_api_content_soap(params, method)

#         resp = requests.post(self._url, data=envelope, headers=headers, verify=False)
#         resp.raise_for_status()
#         return resp.content.decode("utf-8")

#     # --- Async Calls ---

#     async def _call_api_async(
#         self, method: str, params: dict, transport_mode: Optional[TransportMode]
#     ):
#         """
#         Perform an asynchronous API call.

#         Args:
#             method: API method name.
#             params: API parameters.
#             transport_mode: Transport mode (SOAP or URL).

#         Returns:
#             API response content.

#         Raises:
#             UnsupportedTransportMode: If the transport mode is invalid.
#         """
#         if transport_mode == TransportMode.SOAP:
#             return await self._call_soap_async(params, method)
#         elif transport_mode == TransportMode.URL:
#             return await self._call_url_async(params, method)
#         else:
#             raise UnsupportedTransportMode(
#                 f"Transport mode {transport_mode} is not supported."
#             )

#     async def _call_url_async(self, params: dict, method: str):
#         """
#         Perform an asynchronous URL GET request.

#         Args:
#             params: Query parameters.
#             method: API method name.

#         Returns:
#             Response text.
#         """
#         async with httpx.AsyncClient() as client:
#             url = self._get_api_content_url(params, method)
#             resp = await client.get(url)
#             resp.raise_for_status()
#             return resp.text

#     async def _call_soap_async(self, params: dict, method: str):
#         """
#         Perform an asynchronous SOAP request.

#         Args:
#             params: Request parameters.
#             method: API method name.

#         Returns:
#             Response text.
#         """
#         envelope, headers = self._get_api_content_soap(params, method)

#         async with httpx.AsyncClient() as client:
#             resp = await client.post(self._url, data=envelope, headers=headers)  # type: ignore
#             resp.raise_for_status()
#             return resp.text

#     # --- API Call Content ---

#     def _get_api_content_url(self, params: dict, method: str) -> str:
#         """
#         Build the full URL for a URL transport API call.

#         Args:
#             params: Query parameters.
#             method: API method name.

#         Returns:
#             Fully qualified URL string.
#         """
#         qs = urlencode(params)
#         return f"{self._url}/{method}?{qs}"

#     def _get_api_content_soap(self, params: dict, method: str) -> Tuple[str, dict]:
#         """
#         Build the SOAP envelope and headers for a SOAP request.

#         Args:
#             params: Request parameters.
#             method: API method name.

#         Returns:
#             A tuple of (SOAP envelope XML string, HTTP headers dict).
#         """
#         body = "".join(f"<{k}>{v}</{k}>" for k, v in params.items())
#         soap = "soap" if self._soap_version == SOAPVersion.SOAP11 else "soap12"
#         envelope = f"""<?xml version="1.0" encoding="utf-8"?>
# <{soap}:Envelope
#     xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
#     xmlns:xsd="http://www.w3.org/2001/XMLSchema"
#     xmlns:{soap}="http://schemas.xmlsoap.org/soap/envelope/">
#   <{soap}:Body>
#     <{method} xmlns="http://www.skyline.be/api/v1">
#       {body}
#     </{method}>
#   </{soap}:Body>
# </{soap}:Envelope>"""

#         if self._soap_version == SOAPVersion.SOAP12:
#             headers = {
#                 "Content-Type": "application/soap+xml; charset=utf-8",
#             }
#         else:
#             headers = {
#                 "Content-Type": "text/xml; charset=utf-8",
#                 "SOAPAction": f"http://www.skyline.be/api/v1/{method}",
#             }

#         return envelope, headers

#     # --- Utility Methods ---

#     def extract_result(self, method: str, content: str) -> str:
#         """
#         Extract the <MethodResult> value from the API response XML.

#         Args:
#             method: API method name.
#             content: Full API response XML.

#         Returns:
#             The text content of the <MethodResult> element.
#         """
#         return extract_result(method, content)
