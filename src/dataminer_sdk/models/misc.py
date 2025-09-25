from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List, Any, TYPE_CHECKING
from dataminer_sdk.models.base import BaseDMAType
from dataminer_sdk.models.enums import (
    DMAStatusType,
    DMAPropertyType,
    ElementStateType,
    ParityType,
    RecentType,
    SerialType,
    FlowControlType,
)

if TYPE_CHECKING:
    from dataminer_sdk.models.alarm import DMAAlarmColors
    from dataminer_sdk.models.license import DMALicenses
    from dataminer_sdk.models.security import DMASecurity
    from dataminer_sdk.models.user import DMAUser, DMAUserGroup


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAObject(BaseDMAType):
    """
    Represents DMA Object.

    Attributes:
        DataMinerID (Optional[int]): The ID of the DataMiner Agent.
        ID (Optional[int]): The ID of the view, service, element, ...
        Name (Optional[str]): The name of the view, service, element, ...
    """

    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the DataMiner Agent."}
    )
    ID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the view, service, element, ..."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the view, service, element, ..."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAInfo(BaseDMAType):
    """
    Represents DMA Info.

    Attributes:
        ID (Optional[int]): The ID of the DataMiner Agent.
        Name (Optional[str]): The name of the DataMiner Agent.
        PrimaryIP (Optional[str]): The primary IP address of the DataMiner Agent.
        Cluster (Optional[str]): The name of the DMS cluster.
        Status (Optional[DMAStatusType]): The status of the DMA: "Disconnected", "Running", "Starting", "Unknown" or "Switching".
        IsFailOver (Optional[bool]): Whether or not the DataMiner Agent is a member of a redundant pair of DataMiner Agents.
        LastChangeUTC (Optional[int]): The time when the object last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT).
    """

    ID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the DataMiner Agent."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the DataMiner Agent."}
    )
    PrimaryIP: Optional[str] = field(
        default=None, metadata={"doc": "The primary IP address of the DataMiner Agent."}
    )
    Cluster: Optional[str] = field(
        default=None, metadata={"doc": "The name of the DMS cluster."}
    )
    Status: Optional[DMAStatusType] = field(
        default=None,
        metadata={
            "doc": 'The status of the DMA: "Disconnected", "Running", "Starting", "Unknown" or "Switching".'
        },
    )
    IsFailOver: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the DataMiner Agent is a member of a redundant pair of DataMiner Agents."
        },
    )
    LastChangeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The time when the object last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMACache(BaseDMAType):
    """
    Represents DMA Cache.

    Attributes:
        ChangedObjects (Optional[Any]): All items added or changed since the last cache update. Depending on the method, these items can be of type DMAAlarm, DMAElement, etc.
        UnchangedObjects (Optional[Any]): The IDs of all items that have not been changed since the last cache update.
    """

    ChangedObjects: Optional[Any] = field(
        default=None,
        metadata={
            "doc": "All items added or changed since the last cache update. Depending on the method, these items can be of type DMAAlarm, DMAElement, etc."
        },
    )
    UnchangedObjects: Optional[Any] = field(
        default=None,
        metadata={
            "doc": "The IDs of all items that have not been changed since the last cache update."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAColor(BaseDMAType):
    """
    Represents DMA Color.

    Attributes:
        R (Optional[int]): Red
        G (Optional[int]): Green
        B (Optional[int]): Blue
    """

    R: Optional[int] = field(default=None, metadata={"doc": "Red"})
    G: Optional[int] = field(default=None, metadata={"doc": "Green"})
    B: Optional[int] = field(default=None, metadata={"doc": "Blue"})


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAGenericProperty(BaseDMAType):
    """
    Represents DMA Generic Property.

    Attributes:
        Key (Optional[str]): The key associated with the value in Value.
        Value (Optional[Any]): The value associated with the key in Key.
        Type (Optional[DMAPropertyType]): The type of value: “String”, “Integer”, “Double”, “Long”, “Boolean” or “Array”.
    """

    Key: Optional[str] = field(
        default=None, metadata={"doc": "The key associated with the value in Value."}
    )
    Value: Optional[Any] = field(
        default=None, metadata={"doc": "The value associated with the key in Key."}
    )
    Type: Optional[DMAPropertyType] = field(
        default=None,
        metadata={
            "doc": "The type of value: “String”, “Integer”, “Double”, “Long”, “Boolean” or “Array”."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMASerialPortInfo(BaseDMAType):
    """
    Represents DMA Serial Port Info.

    Attributes:
        Baudrate (Optional[int]): The baud rate for the serial port.
        BusAddress (Optional[str]): The bus address for the serial port.
        Databits (Optional[int]): The data bits setting of the serial port.
        FlowControl (Optional[FlowControlType]): The flow control setting of the serial port: "No", "CTS_RTS", "CTS_DTR", "DSR_RTS", "DSR_DTR", or "XON_XOFF".
        IPAddress (Optional[str]): The polling IP of the device.
        IPPort (Optional[int]): The IP port of the device.
        LocalIPPort (Optional[int]): The local IP port of the device.
        Network (Optional[str]): Determines whether the device is accessible through the first or second network interface of the DMA, or if this is automatically selected.
        Parity (Optional[ParityType]): The parity setting of the serial port: "No", "Even", "Odd", "Mark", or "Space"
        SerialPort (Optional[str]): The name/number of the serial port.
        Stopbits (Optional[float]): The stop bits setting of the serial port.
        Type (Optional[SerialType]): "Serial", "TCP" or "UDP".
    """

    Baudrate: Optional[int] = field(
        default=None, metadata={"doc": "The baud rate for the serial port."}
    )
    BusAddress: Optional[str] = field(
        default=None, metadata={"doc": "The bus address for the serial port."}
    )
    Databits: Optional[int] = field(
        default=None, metadata={"doc": "The data bits setting of the serial port."}
    )
    FlowControl: Optional[FlowControlType] = field(
        default=None,
        metadata={
            "doc": 'The flow control setting of the serial port: "No", "CTS_RTS", "CTS_DTR", "DSR_RTS", "DSR_DTR", or "XON_XOFF".'
        },
    )
    IPAddress: Optional[str] = field(
        default=None, metadata={"doc": "The polling IP of the device."}
    )
    IPPort: Optional[int] = field(
        default=None, metadata={"doc": "The IP port of the device."}
    )
    LocalIPPort: Optional[int] = field(
        default=None, metadata={"doc": "The local IP port of the device."}
    )
    Network: Optional[str] = field(
        default=None,
        metadata={
            "doc": "Determines whether the device is accessible through the first or second network interface of the DMA, or if this is automatically selected."
        },
    )
    Parity: Optional[ParityType] = field(
        default=None,
        metadata={
            "doc": 'The parity setting of the serial port: "No", "Even", "Odd", "Mark", or "Space"'
        },
    )
    SerialPort: Optional[str] = field(
        default=None, metadata={"doc": "The name/number of the serial port."}
    )
    Stopbits: Optional[float] = field(
        default=None, metadata={"doc": "The stop bits setting of the serial port."}
    )
    Type: Optional[SerialType] = field(
        default=None, metadata={"doc": '"Serial", "TCP" or "UDP".'}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMATimeZoneInfo(BaseDMAType):
    """
    Represents DMA Time Zone Info.

    Attributes:
        DisplayValue (Optional[str]): The display name of the time zone.
        Value.Name (Optional[str]): The unique name of the time zone (e.g. “Romance Standard Time”).
        Value.Labels (Optional[List[str]]): The different time zone names corresponding with this time zone.
        Value.Timestamps (Optional[List[int]]): The different start and end times corresponding with the labels.
        Value.Offsets (Optional[List[int]]): The offset values (compared to UTC) corresponding with the labels and timestamps.
    """

    DisplayValue: Optional[str] = field(
        default=None, metadata={"doc": "The display name of the time zone."}
    )
    Value_Name: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The unique name of the time zone (e.g. “Romance Standard Time”)."
        },
    )
    Value_Labels: Optional[List[str]] = field(
        default=None,
        metadata={
            "doc": "The different time zone names corresponding with this time zone."
        },
    )
    Value_Timestamps: Optional[List[int]] = field(
        default=None,
        metadata={
            "doc": "The different start and end times corresponding with the labels."
        },
    )
    Value_Offsets: Optional[List[int]] = field(
        default=None,
        metadata={
            "doc": "The offset values (compared to UTC) corresponding with the labels and timestamps."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAConnectAndInfo(BaseDMAType):
    """
    Represents DMA Connect And Info.

    Attributes:
        Connection (Optional[str]): The connection string.
        Message (Optional[str]): If the connection attempt failed, Message will contain an error message.
        MessageType (Optional[str]): If the connection attempt failed, MessageType will indicate the type of error that occurred.
        DMAVersion (Optional[str]): The version of the DataMiner software.
        AlarmColors (Optional[DMAAlarmColors]): The alarm colors used on the DataMiner Agent.
        Time (Optional[str]): The DMS time.
        TimeUTC (Optional[int]): The DMS time in UTC format (milliseconds since midnight January 1, 1970 GMT).
        LastChangeUTC (Optional[int]): The time when the object was last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT).
        Security (Optional[DMASecurity]): The user permissions of the specified user account.
        Licenses (Optional[DMALicenses]): Array indicating which licenses are or are not available on the DMA.
        User (Optional[DMAUser]): The user login, full name and email address of each user.
        UserGroups (Optional[DMAUserGroup]): The IDs and names of the user groups.
        SLNetConnectionID (Optional[str]): The SLNet connection ID.
        Cookie (Optional[str]): The encoded timestamp, client info hash, username and password
        ClusterInfo_IsCassandraActive (Optional[bool]): Indicates whether the DMA uses a Cassandra database.
        ClusterInfo_IsSearchActive (Optional[bool]): Indicates whether the DMA uses an indexing database.
        HasDelegatedAuthentication (Optional[bool]): Indicates whether authentication is delegated to a third-party system.
    """

    Connection: Optional[str] = field(
        default=None, metadata={"doc": "The connection string."}
    )
    Message: Optional[str] = field(
        default=None,
        metadata={
            "doc": "If the connection attempt failed, Message will contain an error message."
        },
    )
    MessageType: Optional[str] = field(
        default=None,
        metadata={
            "doc": "If the connection attempt failed, MessageType will indicate the type of error that occurred."
        },
    )
    DMAVersion: Optional[str] = field(
        default=None, metadata={"doc": "The version of the DataMiner software."}
    )
    AlarmColors: Optional[DMAAlarmColors] = field(
        default=None, metadata={"doc": "The alarm colors used on the DataMiner Agent."}
    )
    Time: Optional[str] = field(default=None, metadata={"doc": "The DMS time."})
    TimeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The DMS time in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )
    LastChangeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The time when the object was last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )
    Security: Optional[DMASecurity] = field(
        default=None,
        metadata={"doc": "The user permissions of the specified user account."},
    )
    Licenses: Optional[DMALicenses] = field(
        default=None,
        metadata={
            "doc": "Array indicating which licenses are or are not available on the DMA."
        },
    )
    User: Optional[DMAUser] = field(
        default=None,
        metadata={"doc": "The user login, full name and email address of each user."},
    )
    UserGroups: Optional[DMAUserGroup] = field(
        default=None, metadata={"doc": "The IDs and names of the user groups."}
    )
    SLNetConnectionID: Optional[str] = field(
        default=None, metadata={"doc": "The SLNet connection ID."}
    )
    Cookie: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The encoded timestamp, client info hash, username and password"
        },
    )
    ClusterInfo_IsCassandraActive: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the DMA uses a Cassandra database."},
    )
    ClusterInfo_IsSearchActive: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the DMA uses an indexing database."},
    )
    HasDelegatedAuthentication: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether authentication is delegated to a third-party system."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMARecent(BaseDMAType):
    """
    Represents DMA Recent.

    Attributes:
        Type (Optional[RecentType]): “Element” or “Service”
        DataMinerID (Optional[int]): The ID of the DataMiner Agent.
        ID (Optional[int]): The ID of the element or the service.
        Name (Optional[str]): The name of the element or the service.
        SubText (Optional[str]): The name of the protocol (only if Type is “Element”).
        AlarmState (Optional[str]): The current alarm state of the element or the service.
        IsTimeout (Optional[bool]): Whether the element or service is in timeout.
        ElementState (Optional[str]): State of the element: “Active”, “Paused”, “Stopped”, “Error”, “Masked” or “Hidden”.
        Position (Optional[int]): Position of the element/service in the list of most recent or nearby items. The smaller the number, the higher the item is on the list.
        IsPinned (Optional[bool]): Whether the element/service is pinned in the Recent list.
        Latitude (Optional[float]): Latitude of the element/service (if specified in the properties of the element/service).
        Longitude (Optional[float]): Longitude of the element/service (if specified in the properties of the element/service).
    """

    Type: Optional[RecentType] = field(
        default=None, metadata={"doc": "“Element” or “Service”"}
    )
    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the DataMiner Agent."}
    )
    ID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the element or the service."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the element or the service."}
    )
    SubText: Optional[str] = field(
        default=None,
        metadata={"doc": "The name of the protocol (only if Type is “Element”)."},
    )
    AlarmState: Optional[str] = field(
        default=None,
        metadata={"doc": "The current alarm state of the element or the service."},
    )
    IsTimeout: Optional[bool] = field(
        default=None, metadata={"doc": "Whether the element or service is in timeout."}
    )
    ElementState: Optional[ElementStateType] = field(
        default=None,
        metadata={
            "doc": "State of the element: “Active”, “Paused”, “Stopped”, “Error”, “Masked” or “Hidden”."
        },
    )
    Position: Optional[int] = field(
        default=None,
        metadata={
            "doc": "Position of the element/service in the list of most recent or nearby items. The smaller the number, the higher the item is on the list."
        },
    )
    IsPinned: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether the element/service is pinned in the Recent list."},
    )
    Latitude: Optional[float] = field(
        default=None,
        metadata={
            "doc": "Latitude of the element/service (if specified in the properties of the element/service)."
        },
    )
    Longitude: Optional[float] = field(
        default=None,
        metadata={
            "doc": "Longitude of the element/service (if specified in the properties of the element/service)."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMARegionalSettings(BaseDMAType):
    """
    Represents DMA Regional Settings.

    Attributes:
        ListDelimiter (Optional[str]): The list separator.
        NumberDecimalDelimiter (Optional[str]): The decimal symbol.
        NumberGroupDelimiter (Optional[str]): The digit grouping symbol.
        TimeZone_DisplayValue (Optional[str]): The display name of the time zone.
        TimeZone_Value_Name (Optional[str]): The unique name of the time zone (e.g. “Romance Standard Time”).
        TimeZone_Value_Labels (Optional[List[str]]): The different time zone names corresponding with this time zone.
        TimeZone_Value_TimeStamps (Optional[List[int]]): The different start and end times corresponding with the labels.
        TimeZone_Value_Offsets (Optional[List[int]]): The offset values (compared to UTC) corresponding with the labels and timestamps.
    """

    ListDelimiter: Optional[str] = field(
        default=None, metadata={"doc": "The list separator."}
    )
    NumberDecimalDelimiter: Optional[str] = field(
        default=None, metadata={"doc": "The decimal symbol."}
    )
    NumberGroupDelimiter: Optional[str] = field(
        default=None, metadata={"doc": "The digit grouping symbol."}
    )
    TimeZone_DisplayValue: Optional[str] = field(
        default=None, metadata={"doc": "The display name of the time zone."}
    )
    TimeZone_Value_Name: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The unique name of the time zone (e.g. “Romance Standard Time”)."
        },
    )
    TimeZone_Value_Labels: Optional[List[str]] = field(
        default=None,
        metadata={
            "doc": "The different time zone names corresponding with this time zone."
        },
    )
    TimeZone_Value_TimeStamps: Optional[List[int]] = field(
        default=None,
        metadata={
            "doc": "The different start and end times corresponding with the labels."
        },
    )
    TimeZone_Value_Offsets: Optional[List[int]] = field(
        default=None,
        metadata={
            "doc": "The offset values (compared to UTC) corresponding with the labels and timestamps."
        },
    )
