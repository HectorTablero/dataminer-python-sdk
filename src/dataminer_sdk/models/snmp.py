from dataclasses import dataclass, field
from typing import Optional
from dataminer_sdk.models.base import BaseDMAType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMASnmpManager(BaseDMAType):
    """
    Represents DMA Snmp Manager.

    Attributes:
        ID (Optional[int]): The ID of the SNMP Manager.
        Name (Optional[str]): The name of the SNMP Manager.
        IPAddress (Optional[str]): The IP address of the SNMP Manager
        CommunityString (Optional[str]): The Get community string of the SNMP Manager
        Version (Optional[int]): The SNMP version: SNMPv1, SNMPv2 or SNMPv3
        IsEnabled (Optional[bool]): Indicates whether the SNMP Manager is currently enabled.
    """

    ID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the SNMP Manager."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the SNMP Manager."}
    )
    IPAddress: Optional[str] = field(
        default=None, metadata={"doc": "The IP address of the SNMP Manager"}
    )
    CommunityString: Optional[str] = field(
        default=None, metadata={"doc": "The Get community string of the SNMP Manager"}
    )
    Version: Optional[int] = field(
        default=None, metadata={"doc": "The SNMP version: SNMPv1, SNMPv2 or SNMPv3"}
    )
    IsEnabled: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the SNMP Manager is currently enabled."},
    )
