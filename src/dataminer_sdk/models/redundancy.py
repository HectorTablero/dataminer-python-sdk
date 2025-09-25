from dataclasses import dataclass, field
from typing import Optional, List
from dataminer_sdk.models.base import BaseDMAType
from dataminer_sdk.models.enums import (
    RedundancyType,
    RedundancyStatusType,
    RedundancyGroupStatusType,
    RedundancyGroupModeType,
)


@dataclass(slots=True, frozen=True, kw_only=True)
class DMARedundancyElement(BaseDMAType):
    """
    Represents DMA Redundancy Element.

    Attributes:
        DataMinerID (Optional[int]): The ID of the DataMiner Agent.
        ID (Optional[int]): The ID of the element.
        Name (Optional[str]): The name of the element.
        AlarmState (Optional[str]): The current alarm state of the element.
        State (Optional[str]): The current state of the element.
        RedundancyType (Optional[RedundancyType]): The type of redundancy element: “Primary”, “Backup” or “State”.
        RedundancyStatus (Optional[str]): The status of the element within the redundancy group: “Failed”, “Available”, “Unavailable”, “Error”, “Switching” or “Operational for primary element [element name]”, ...
        IsInMaintenance (Optional[bool]): Whether or not the element is in maintenance.
        LastChangeUTC (Optional[int]): The time when the object was last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT).
    """

    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the DataMiner Agent."}
    )
    ID: Optional[int] = field(default=None, metadata={"doc": "The ID of the element."})
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the element."}
    )
    AlarmState: Optional[str] = field(
        default=None, metadata={"doc": "The current alarm state of the element."}
    )
    State: Optional[str] = field(
        default=None, metadata={"doc": "The current state of the element."}
    )
    RedundancyType: Optional["RedundancyType"] = field(
        default=None,
        metadata={
            "doc": "The type of redundancy element: “Primary”, “Backup” or “State”."
        },
    )
    # TODO: Consider using an enum (it might be tricky because of the "Operational for primary element [element name]" value)
    RedundancyStatus: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The status of the element within the redundancy group: “Failed”, “Available”, “Unavailable”, “Error”, “Switching” or “Operational for primary element [element name]”, ..."
        },
    )
    IsInMaintenance: Optional[bool] = field(
        default=None, metadata={"doc": "Whether or not the element is in maintenance."}
    )
    LastChangeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The time when the object was last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMARedundancyVirtualElement(BaseDMAType):
    """
    Represents DMA Redundancy Virtual Element.

    Attributes:
        DataMinerID (Optional[int]): The ID of the DataMiner Agent.
        DerivedID (Optional[int]): The ID of the derived element.
        DerivedName (Optional[str]): The name of the derived element.
        RedundancyStatus (Optional[str]): The status of the virtual element: “Primary is operational”, “Backup is operational”, “Unavailable”, “Error” or “Switching”.
        LastChangeUTC (Optional[int]): The time when the object was last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT).
    """

    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the DataMiner Agent."}
    )
    DerivedID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the derived element."}
    )
    DerivedName: Optional[str] = field(
        default=None, metadata={"doc": "The name of the derived element."}
    )
    RedundancyStatus: Optional[RedundancyStatusType] = field(
        default=None,
        metadata={
            "doc": "The status of the virtual element: “Primary is operational”, “Backup is operational”, “Unavailable”, “Error” or “Switching”."
        },
    )
    LastChangeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The time when the object was last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMARedundancyGroup(BaseDMAType):
    """
    Represents DMA Redundancy Group.

    Attributes:
        DataMinerID (Optional[int]): The ID of the DataMiner Agent.
        ID (Optional[int]): The ID of the redundancy group.
        Name (Optional[str]): The name of the redundancy group.
        AlarmState (Optional[str]): The current alarm state of the redundancy group.
        Status (Optional[RedundancyGroupStatusType]): The status of the redundancy group: “Undefined”, “Available”, “Operational”, “Unavailable”, “Error” or “Switching”.
        Mode (Optional[RedundancyGroupModeType]): The redundancy mode: “Undefined”, “Automatic”, “ManualSwitchBack” or “Manual”.
        VirtualElements (Optional[List[DMARedundancyVirtualElement]]): The list of virtual elements in the redundancy group.
        Elements (Optional[List[DMARedundancyElement]]): The list of elements in the redundancy group.
        LastChangeUTC (Optional[int]): The time when the redundancy group was last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT).
    """

    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the DataMiner Agent."}
    )
    ID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the redundancy group."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the redundancy group."}
    )
    AlarmState: Optional[str] = field(
        default=None,
        metadata={"doc": "The current alarm state of the redundancy group."},
    )
    Status: Optional[RedundancyGroupStatusType] = field(
        default=None,
        metadata={
            "doc": "The status of the redundancy group: “Undefined”, “Available”, “Operational”, “Unavailable”, “Error” or “Switching”."
        },
    )
    Mode: Optional[RedundancyGroupModeType] = field(
        default=None,
        metadata={
            "doc": "The redundancy mode: “Undefined”, “Automatic”, “ManualSwitchBack” or “Manual”."
        },
    )
    VirtualElements: Optional[List[DMARedundancyVirtualElement]] = field(
        default=None,
        metadata={"doc": "The list of virtual elements in the redundancy group."},
    )
    Elements: Optional[List[DMARedundancyElement]] = field(
        default=None, metadata={"doc": "The list of elements in the redundancy group."}
    )
    LastChangeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The time when the redundancy group was last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )
