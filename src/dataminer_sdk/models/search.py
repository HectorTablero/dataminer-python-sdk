from dataclasses import dataclass, field
from typing import Optional
from dataminer_sdk.models.base import BaseDMAType
from dataminer_sdk.models.enums import AlarmStateType, SearchType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMASearchItem(BaseDMAType):
    """
    Represents DMA Search Item.

    Attributes:
        DataMinerID (Optional[int]): The ID of the DataMiner Agent.
        ElementID (Optional[int]): The ID of the element or the service (only if Type is “Element” or “Service”).
        ID (Optional[int]): The ID of the view (only if Type is “View”).
        Name (Optional[str]): The name of the element, service or view.
        Description (Optional[str]): “Element”, “Service” or “View”.
        Type (Optional[SearchType]): The type of the item: “Element”, “Service” or “View”.
        AlarmState (Optional[AlarmStateType]): The current alarm severity of the element, service or view.
        IsTimeout (Optional[bool]): Whether or not the element/service/view is in timeout.
        Match (Optional[str]): The text (name, protocol, ...) that matches the query.
    """

    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the DataMiner Agent."}
    )
    ElementID: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The ID of the element or the service (only if Type is “Element” or “Service”)."
        },
    )
    ID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the view (only if Type is “View”)."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the element, service or view."}
    )
    Description: Optional[str] = field(
        default=None, metadata={"doc": "“Element”, “Service” or “View”."}
    )
    Type: Optional[SearchType] = field(
        default=None,
        metadata={"doc": "The type of the item: “Element”, “Service” or “View”."},
    )
    AlarmState: Optional[AlarmStateType] = field(
        default=None,
        metadata={"doc": "The current alarm severity of the element, service or view."},
    )
    IsTimeout: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the element/service/view is in timeout."},
    )
    Match: Optional[str] = field(
        default=None,
        metadata={"doc": "The text (name, protocol, ...) that matches the query."},
    )
