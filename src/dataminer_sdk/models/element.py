from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List, TYPE_CHECKING
from dataminer_sdk.models.base import BaseDMAType
from dataminer_sdk.models.enums import (
    AuthType,
    ElementObjectType,
    PrivType,
    SecurityLevelType,
    SlowPollType,
    ElementStateType,
)

if TYPE_CHECKING:
    from dataminer_sdk.models.misc import DMAObject, DMASerialPortInfo


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAElementSNMPPortInfo(BaseDMAType):
    """
    Represents DMA Element SNMP Port Info.

    Attributes:
        DeviceAddress (Optional[str]): The address of the device itself, in case a gateway IP address is specified in IPAddress.
        GetCommunity (Optional[str]): The community string used to retrieve values.
        IPAddress (Optional[str]): The IP address of the device.
        Network (Optional[str]): Determines whether the device is accessible through the first or second network interface of the DMA, or if this is automatically selected.
        PortNumber (Optional[int]): The SNMP port number.
        SetCommunity (Optional[str]): The community string used to write values.
    """

    DeviceAddress: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The address of the device itself, in case a gateway IP address is specified in IPAddress."
        },
    )
    GetCommunity: Optional[str] = field(
        default=None, metadata={"doc": "The community string used to retrieve values."}
    )
    IPAddress: Optional[str] = field(
        default=None, metadata={"doc": "The IP address of the device."}
    )
    Network: Optional[str] = field(
        default=None,
        metadata={
            "doc": "Determines whether the device is accessible through the first or second network interface of the DMA, or if this is automatically selected."
        },
    )
    PortNumber: Optional[int] = field(
        default=None, metadata={"doc": "The SNMP port number."}
    )
    SetCommunity: Optional[str] = field(
        default=None, metadata={"doc": "The community string used to write values."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAElementSNMPV3PortInfo(BaseDMAType):
    """
    Represents DMA Element SNMP V3 Port Info.

    Attributes:
        AuthPassword (Optional[str]): The password used for authentication.
        AuthType (Optional[AuthType]): The type of authentication used: "HMAC_MD5" or "HMAC_SHA".
        DeviceAddress (Optional[str]): The address of the device itself, in case a gateway IP address is specified in IPAddress.
        IPAddress (Optional[str]): The IP address of the device.
        Network (Optional[str]): Determines whether the device is accessible through the first or second network interface of the DMA, or if this is automatically selected.
        PortNumber (Optional[int]): The SNMP port number.
        PrivPassword (Optional[str]): The encryption password.
        PrivType (Optional[PrivType]): The privacy type used: "DES" or "AES128".
        SecurityLevel (Optional[SecurityLevelType]): The security level used: "authPriv", "authNoPriv", or "noAuthNoPriv".
        Username (Optional[str]): The name of the user.
    """

    AuthPassword: Optional[str] = field(
        default=None, metadata={"doc": "The password used for authentication."}
    )
    AuthType: Optional["AuthType"] = field(
        default=None,
        metadata={"doc": 'The type of authentication used: "HMAC_MD5" or "HMAC_SHA".'},
    )
    DeviceAddress: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The address of the device itself, in case a gateway IP address is specified in IPAddress."
        },
    )
    IPAddress: Optional[str] = field(
        default=None, metadata={"doc": "The IP address of the device."}
    )
    Network: Optional[str] = field(
        default=None,
        metadata={
            "doc": "Determines whether the device is accessible through the first or second network interface of the DMA, or if this is automatically selected."
        },
    )
    PortNumber: Optional[int] = field(
        default=None, metadata={"doc": "The SNMP port number."}
    )
    PrivPassword: Optional[str] = field(
        default=None, metadata={"doc": "The encryption password."}
    )
    PrivType: Optional["PrivType"] = field(
        default=None, metadata={"doc": 'The privacy type used: "DES" or "AES128".'}
    )
    SecurityLevel: Optional[SecurityLevelType] = field(
        default=None,
        metadata={
            "doc": 'The security level used: "authPriv", "authNoPriv", or "noAuthNoPriv".'
        },
    )
    Username: Optional[str] = field(
        default=None, metadata={"doc": "The name of the user."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAElementBasePortInfo(BaseDMAType):
    """
    Represents DMA Element Base Port Info.

    Attributes:
        ElementTimeoutTime (Optional[int]): The number of seconds after which the element goes into timeout.
        TimeoutTime (Optional[int]): The number of seconds after which the element goes into slow poll mode.
        Retries (Optional[int]): The number of retries after which the element goes into slow poll mode.
        DMASerialPortInfo (Optional[DMASerialPortInfo]): Element configuration info when using a serial connection.
        DMAElementSNMPPortInfo (Optional[DMAElementSNMPPortInfo]): Element configuration info when using an SNMPv1 or SNMPv2 connection.
        DMAElementSNMPV3PortInfo (Optional[DMAElementSNMPV3PortInfo]): Element configuration info when using an SNMPv3 connection.
    """

    ElementTimeoutTime: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The number of seconds after which the element goes into timeout."
        },
    )
    TimeoutTime: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The number of seconds after which the element goes into slow poll mode."
        },
    )
    Retries: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The number of retries after which the element goes into slow poll mode."
        },
    )
    DMASerialPortInfo: Optional["DMASerialPortInfo"] = field(
        default=None,
        metadata={"doc": "Element configuration info when using a serial connection."},
    )
    DMAElementSNMPPortInfo: Optional["DMAElementSNMPPortInfo"] = field(
        default=None,
        metadata={
            "doc": "Element configuration info when using an SNMPv1 or SNMPv2 connection."
        },
    )
    DMAElementSNMPV3PortInfo: Optional["DMAElementSNMPV3PortInfo"] = field(
        default=None,
        metadata={"doc": "Element configuration info when using an SNMPv3 connection."},
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAElementID(BaseDMAType):
    """
    Represents DMA Element ID.

    Attributes:
        DataMinerID (Optional[int]): The ID of the DataMiner Agent.
        ID (Optional[int]): The ID of the element.
    """

    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the DataMiner Agent."}
    )
    ID: Optional[int] = field(default=None, metadata={"doc": "The ID of the element."})


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAElementLite(BaseDMAType):
    """
    Represents DMA Element Lite.

    Attributes:
        DataMinerID (Optional[int]): The ID of the DataMiner Agent.
        ID (Optional[int]): The ID of the element, if relevant.
        Name (Optional[str]): The name of the element, if relevant.
        ProtocolName (Optional[str]): The name of the protocol, if relevant.
        ProtocolVersion (Optional[str]): The version of the protocol, if relevant.
        State (Optional[str]): The current state of the element, if relevant.
        IsCPE (Optional[bool]): Indicates whether the object is a CPE element.
        IsSLA (Optional[bool]): Indicates whether the object is an SLA element.
        IsDVE (Optional[bool]): Indicates whether the object is a DVE element.
        IsDerived (Optional[bool]): Indicates whether the object is a derived element.
        IsSpectrum (Optional[bool]): Indicates whether the object is a spectrum element.
        HasTrendTemplate (Optional[bool]): Indicates whether a trend template has been assigned to the object.
        Type (Optional[ElementObjectType]): Indicates the type of object: “Element”, “Service” or “Redundancy Group”.
        IsEnhancedService (Optional[bool]): Indicates whether the object is an enhanced service.
        IsServiceTemplate (Optional[bool]): Indicates whether the object is a service template.
    """

    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the DataMiner Agent."}
    )
    ID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the element, if relevant."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the element, if relevant."}
    )
    ProtocolName: Optional[str] = field(
        default=None, metadata={"doc": "The name of the protocol, if relevant."}
    )
    ProtocolVersion: Optional[str] = field(
        default=None, metadata={"doc": "The version of the protocol, if relevant."}
    )
    State: Optional[str] = field(
        default=None, metadata={"doc": "The current state of the element, if relevant."}
    )
    IsCPE: Optional[bool] = field(
        default=None, metadata={"doc": "Indicates whether the object is a CPE element."}
    )
    IsSLA: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the object is an SLA element."},
    )
    IsDVE: Optional[bool] = field(
        default=None, metadata={"doc": "Indicates whether the object is a DVE element."}
    )
    IsDerived: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the object is a derived element."},
    )
    IsSpectrum: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the object is a spectrum element."},
    )
    HasTrendTemplate: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether a trend template has been assigned to the object."
        },
    )
    Type: Optional[ElementObjectType] = field(
        default=None,
        metadata={
            "doc": "Indicates the type of object: “Element”, “Service” or “Redundancy Group”."
        },
    )
    IsEnhancedService: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the object is an enhanced service."},
    )
    IsServiceTemplate: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the object is a service template."},
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAElementPage(BaseDMAType):
    """
    Represents DMA Element Page.

    Attributes:
        DataMinerID (Optional[int]): The ID of the DataMiner Agent.
        ElementID (Optional[int]): The ID of the element.
        Name (Optional[str]): The name of the Data Display page.
        AlarmState (Optional[str]): The current alarm state of the Data Display page.
        Position (Optional[int]): The position of the page in the list of pages of the element specified in ElementID.
        Children (Optional[List[str]]): The subpages of this page.
        IsSeparator (Optional[bool]): Whether the page is an actual page or merely a separator.
        IsPopup (Optional[bool]): Whether or not the page is a popup page.
        IsWeb (Optional[bool]): Whether or not the page is a webpage.
        IsSpectrum (Optional[bool]): Whether or not the page is a spectrum page.
        IsGeneralParameters (Optional[bool]): Whether or not the page is a “General Parameters” page.
        Url (Optional[str]): If IsWeb is true, this field contains the URL of the web page.
        LastChangeUTC (Optional[int]): The time when the page was last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT).
    """

    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the DataMiner Agent."}
    )
    ElementID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the element."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the Data Display page."}
    )
    AlarmState: Optional[str] = field(
        default=None,
        metadata={"doc": "The current alarm state of the Data Display page."},
    )
    Position: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The position of the page in the list of pages of the element specified in ElementID."
        },
    )
    Children: Optional[List[str]] = field(
        default=None, metadata={"doc": "The subpages of this page."}
    )
    IsSeparator: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether the page is an actual page or merely a separator."},
    )
    IsPopup: Optional[bool] = field(
        default=None, metadata={"doc": "Whether or not the page is a popup page."}
    )
    IsWeb: Optional[bool] = field(
        default=None, metadata={"doc": "Whether or not the page is a webpage."}
    )
    IsSpectrum: Optional[bool] = field(
        default=None, metadata={"doc": "Whether or not the page is a spectrum page."}
    )
    IsGeneralParameters: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the page is a “General Parameters” page."},
    )
    Url: Optional[str] = field(
        default=None,
        metadata={
            "doc": "If IsWeb is true, this field contains the URL of the web page."
        },
    )
    LastChangeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The time when the page was last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAElementConfiguration(BaseDMAType):
    """
    Represents DMA Element Configuration.

    Attributes:
        Name (Optional[str]): The name of the element. A limit of at most 150 characters applies.
        Description (Optional[str]): The description of the element.
        ProtocolName (Optional[str]): The name of the element’s protocol.
        ProtocolVersion (Optional[str]): The version of the element’s protocol.
        Type (Optional[str]): The element type configured in the protocol (e.g. “Information Platform” in a Microsoft protocol).
        AlarmTemplate (Optional[str]): The alarm template used to monitor the element.
        TrendTemplate (Optional[str]): The trend template used to track the element’s trend data.
        ForceAgent (Optional[str]): Used in a Failover setup to always make an element run on a particular DMA.
        IPAddress (Optional[str]): The IP address of the device.
        IPAddressMask (Optional[str]): The subnet mask of the device.
        CreateDVEs (Optional[bool]): Indicates whether the element can create DVE child elements.
        EnableSnmpAgent (Optional[bool]): Indicates whether a virtual SNMP agent is enabled for the element.
        EnableTelnet (Optional[bool]): Indicates whether the element’s Telnet interface is enabled.
        IsHidden (Optional[bool]): Indicates whether the element is hidden.
        IsReadOnly (Optional[bool]): Indicates whether the element is a read-only element.
        IsReplicationActive (Optional[bool]): Indicates whether the element is replicated.
        KeepOnline (Optional[bool]): Used in a Failover setup to indicate that the element needs to keep running even when the DMA is offline
        SnmpReadCommunityString (Optional[str]): The community string used to read values from the device.
        SnmpWriteCommunityString (Optional[str]): The community string used to set values on the device.
        ReplicationInfo_Domain (Optional[str]): The domain from where the element is replicated.
        ReplicationInfo_Host (Optional[str]): The host from where the element is replicated.
        ReplicationInfo_Password (Optional[str]): The password used to connect to the DMA from which the element is replicated.
        ReplicationInfo_DataMinerID (Optional[int]): The DataMiner ID of the element that is replicated.
        ReplicationInfo_ElementID (Optional[int]): The element ID of the element that is replicated.
        ReplicationInfo_User (Optional[str]): The username used to connect to the DMA from which the element is replicated.
        TimeoutTime (Optional[int]): The time after which an element goes into timeout (between 0 and 120,000 ms).
        SlowPoll_Base (Optional[SlowPollType]): “TIME”, “NUMBER” or “NO”.
        SlowPoll_Value (Optional[int]): Depending on the Base configuration, this is a time value (between 1000 and 300,000 ms), the number of timeouts (between 1 and 500), or empty, respectively.
        SlowPoll_PingInterval (Optional[int]): Between 1000 and 300,000 ms.
        State (Optional[ElementStateType]): The element state, which can be Undefined, Active, Hidden, Paused, Stopped, Deleted, Error, Restart or Masked.
        Ports (Optional[List[DMAElementBasePortInfo]]): The different ports of the element.
    """

    Name: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The name of the element. A limit of at most 150 characters applies."
        },
    )
    Description: Optional[str] = field(
        default=None, metadata={"doc": "The description of the element."}
    )
    ProtocolName: Optional[str] = field(
        default=None, metadata={"doc": "The name of the element’s protocol."}
    )
    ProtocolVersion: Optional[str] = field(
        default=None, metadata={"doc": "The version of the element’s protocol."}
    )
    Type: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The element type configured in the protocol (e.g. “Information Platform” in a Microsoft protocol)."
        },
    )
    AlarmTemplate: Optional[str] = field(
        default=None,
        metadata={"doc": "The alarm template used to monitor the element."},
    )
    TrendTemplate: Optional[str] = field(
        default=None,
        metadata={"doc": "The trend template used to track the element’s trend data."},
    )
    ForceAgent: Optional[str] = field(
        default=None,
        metadata={
            "doc": "Used in a Failover setup to always make an element run on a particular DMA."
        },
    )
    IPAddress: Optional[str] = field(
        default=None, metadata={"doc": "The IP address of the device."}
    )
    IPAddressMask: Optional[str] = field(
        default=None, metadata={"doc": "The subnet mask of the device."}
    )
    CreateDVEs: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the element can create DVE child elements."
        },
    )
    EnableSnmpAgent: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether a virtual SNMP agent is enabled for the element."
        },
    )
    EnableTelnet: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the element’s Telnet interface is enabled."
        },
    )
    IsHidden: Optional[bool] = field(
        default=None, metadata={"doc": "Indicates whether the element is hidden."}
    )
    IsReadOnly: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the element is a read-only element."},
    )
    IsReplicationActive: Optional[bool] = field(
        default=None, metadata={"doc": "Indicates whether the element is replicated."}
    )
    KeepOnline: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Used in a Failover setup to indicate that the element needs to keep running even when the DMA is offline"
        },
    )
    SnmpReadCommunityString: Optional[str] = field(
        default=None,
        metadata={"doc": "The community string used to read values from the device."},
    )
    SnmpWriteCommunityString: Optional[str] = field(
        default=None,
        metadata={"doc": "The community string used to set values on the device."},
    )
    ReplicationInfo_Domain: Optional[str] = field(
        default=None,
        metadata={"doc": "The domain from where the element is replicated."},
    )
    ReplicationInfo_Host: Optional[str] = field(
        default=None, metadata={"doc": "The host from where the element is replicated."}
    )
    ReplicationInfo_Password: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The password used to connect to the DMA from which the element is replicated."
        },
    )
    ReplicationInfo_DataMinerID: Optional[int] = field(
        default=None,
        metadata={"doc": "The DataMiner ID of the element that is replicated."},
    )
    ReplicationInfo_ElementID: Optional[int] = field(
        default=None,
        metadata={"doc": "The element ID of the element that is replicated."},
    )
    ReplicationInfo_User: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The username used to connect to the DMA from which the element is replicated."
        },
    )
    TimeoutTime: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The time after which an element goes into timeout (between 0 and 120,000 ms)."
        },
    )
    SlowPoll_Base: Optional[SlowPollType] = field(
        default=None, metadata={"doc": "“TIME”, “NUMBER” or “NO”."}
    )
    SlowPoll_Value: Optional[int] = field(
        default=None,
        metadata={
            "doc": "Depending on the Base configuration, this is a time value (between 1000 and 300,000 ms), the number of timeouts (between 1 and 500), or empty, respectively."
        },
    )
    SlowPoll_PingInterval: Optional[int] = field(
        default=None, metadata={"doc": "Between 1000 and 300,000 ms."}
    )
    State: Optional[ElementStateType] = field(
        default=None,
        metadata={
            "doc": "The element state, which can be Undefined, Active, Hidden, Paused, Stopped, Deleted, Error, Restart or Masked."
        },
    )
    Ports: Optional[List[DMAElementBasePortInfo]] = field(
        default=None, metadata={"doc": "The different ports of the element."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAElement(BaseDMAType):
    """
    Represents DMA Element.

    Attributes:
        DataMinerID (Optional[int]): The ID of the DataMiner Agent.
        ID (Optional[int]): The ID of the element.
        Name (Optional[str]): The name of the element.
        Description (Optional[str]): The description of the element.
        AlarmState (Optional[str]): The current alarm state of the element.
        AlarmStateCappedIncluded (Optional[str]): The maximum alarm severity when the element is included (only for elements that are part of a service).
        AlarmStateCappedNotUsed (Optional[str]): The maximum alarm severity when the element is not used (only for elements that are part of a service).
        IsTimeout (Optional[bool]): Whether the element is in timeout.
        Views (Optional[List[DMAObject]]): The list of views in which the element can be found.
        Services (Optional[List[DMAObject]]): The list of services of which the element is a part.
        ProtocolName (Optional[str]): The name of the protocol.
        ProtocolVersion (Optional[str]): The version of the protocol.
        State (Optional[str]): The current state of the element.
        IsCPE (Optional[bool]): Whether the element is a CPE element.
        IsSLA (Optional[bool]): Whether the element is an SLA element.
        IsSpectrum (Optional[bool]): Whether the element is a spectrum element.
        IsDVE (Optional[bool]): Whether the element is a DVE element.
        IsDerived (Optional[bool]): Whether the element is a derived element.
        IsMonitored (Optional[bool]): Whether an alarm template has been assigned to the element.
        HasTrendTemplate (Optional[bool]): Whether a trend template has been assigned to the element.
        HasVisio (Optional[bool]): Whether a Visio file has been linked to the element.
        HideParameters (Optional[bool]): Only used for CPE elements. If the “CPEOnly” option is used in the element protocol, HideParameters will be true, indicating that only the CPE UI should be displayed in the client, and not the Data Display pages. However, clients can ignore this property if necessary, as it is still possible to retrieve parameters with the web APIs even when HideParameters is true.
        Type (Optional[ElementObjectType]): “Element”, “Service” or “Redundancy Group”.
        PollingIP (Optional[str]): The polling IP of the element.
        ProtocolType (Optional[str]): The protocol type as defined in the protocol (DMAElement.Type is either "Element" or "Service").
        LastChangeUTC (Optional[int]): The time when the element was last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT).
        IsEnhancedService (Optional[bool]): Whether the element is an enhanced service.
        IsServiceTemplate (Optional[bool]): Whether the element is a service template.
    """

    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the DataMiner Agent."}
    )
    ID: Optional[int] = field(default=None, metadata={"doc": "The ID of the element."})
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the element."}
    )
    Description: Optional[str] = field(
        default=None, metadata={"doc": "The description of the element."}
    )
    AlarmState: Optional[str] = field(
        default=None, metadata={"doc": "The current alarm state of the element."}
    )
    AlarmStateCappedIncluded: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The maximum alarm severity when the element is included (only for elements that are part of a service)."
        },
    )
    AlarmStateCappedNotUsed: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The maximum alarm severity when the element is not used (only for elements that are part of a service)."
        },
    )
    IsTimeout: Optional[bool] = field(
        default=None, metadata={"doc": "Whether the element is in timeout."}
    )
    Views: Optional[List[DMAObject]] = field(
        default=None,
        metadata={"doc": "The list of views in which the element can be found."},
    )
    Services: Optional[List[DMAObject]] = field(
        default=None,
        metadata={"doc": "The list of services of which the element is a part."},
    )
    ProtocolName: Optional[str] = field(
        default=None, metadata={"doc": "The name of the protocol."}
    )
    ProtocolVersion: Optional[str] = field(
        default=None, metadata={"doc": "The version of the protocol."}
    )
    State: Optional[str] = field(
        default=None, metadata={"doc": "The current state of the element."}
    )
    IsCPE: Optional[bool] = field(
        default=None, metadata={"doc": "Whether the element is a CPE element."}
    )
    IsSLA: Optional[bool] = field(
        default=None, metadata={"doc": "Whether the element is an SLA element."}
    )
    IsSpectrum: Optional[bool] = field(
        default=None, metadata={"doc": "Whether the element is a spectrum element."}
    )
    IsDVE: Optional[bool] = field(
        default=None, metadata={"doc": "Whether the element is a DVE element."}
    )
    IsDerived: Optional[bool] = field(
        default=None, metadata={"doc": "Whether the element is a derived element."}
    )
    IsMonitored: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether an alarm template has been assigned to the element."},
    )
    HasTrendTemplate: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether a trend template has been assigned to the element."},
    )
    HasVisio: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether a Visio file has been linked to the element."},
    )
    HideParameters: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Only used for CPE elements. If the “CPEOnly” option is used in the element protocol, HideParameters will be true, indicating that only the CPE UI should be displayed in the client, and not the Data Display pages. However, clients can ignore this property if necessary, as it is still possible to retrieve parameters with the web APIs even when HideParameters is true."
        },
    )
    Type: Optional[ElementObjectType] = field(
        default=None, metadata={"doc": "“Element”, “Service” or “Redundancy Group”."}
    )
    PollingIP: Optional[str] = field(
        default=None, metadata={"doc": "The polling IP of the element."}
    )
    ProtocolType: Optional[str] = field(
        default=None,
        metadata={
            "doc": 'The protocol type as defined in the protocol (DMAElement.Type is either "Element" or "Service").'
        },
    )
    LastChangeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The time when the element was last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )
    IsEnhancedService: Optional[bool] = field(
        default=None, metadata={"doc": "Whether the element is an enhanced service."}
    )
    IsServiceTemplate: Optional[bool] = field(
        default=None, metadata={"doc": "Whether the element is a service template."}
    )
