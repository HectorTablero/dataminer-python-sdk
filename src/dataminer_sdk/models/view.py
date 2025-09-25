from dataclasses import dataclass, field
from typing import Optional, List
from dataminer_sdk.models.base import BaseDMAType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAView(BaseDMAType):
    """
    Represents DMA View.

    Attributes:
        ID (Optional[int]): The ID of the view.
        Name (Optional[str]): The name of the view.
        AlarmState (Optional[str]): The current alarm state of the view.
        IsTimeout (Optional[bool]): Indicates whether the view is in a timeout state.
        ParentID (Optional[int]): The ID of the parent view.
        HasVisio (Optional[bool]): Indicates whether a Visio file is linked to the view.
        HasChilds (Optional[bool]): Indicates whether the view has child views.
        HasElements (Optional[bool]): Indicates whether the view has child elements
        LastChangeUTC (Optional[int]): The time when the view was last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT).
        IsEnhanced (Optional[bool]): Indicates whether the view is an enhanced view.
    """

    ID: Optional[int] = field(default=None, metadata={"doc": "The ID of the view."})
    Name: Optional[str] = field(default=None, metadata={"doc": "The name of the view."})
    AlarmState: Optional[str] = field(
        default=None, metadata={"doc": "The current alarm state of the view."}
    )
    IsTimeout: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the view is in a timeout state."},
    )
    ParentID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the parent view."}
    )
    HasVisio: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether a Visio file is linked to the view."},
    )
    HasChilds: Optional[bool] = field(
        default=None, metadata={"doc": "Indicates whether the view has child views."}
    )
    HasElements: Optional[bool] = field(
        default=None, metadata={"doc": "Indicates whether the view has child elements"}
    )
    LastChangeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The time when the view was last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )
    IsEnhanced: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the view is an enhanced view."},
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAViewTree(BaseDMAType):
    """
    Represents DMA View Tree.

    Attributes:
        ID (Optional[int]): The ID of the view.
        Name (Optional[str]): The name of the view.
        IsEnhanced (Optional[bool]): Indicates whether the view is an enhanced view.
        Childs (Optional[List[DMAViewTree]]): The child views within the view.
    """

    ID: Optional[int] = field(default=None, metadata={"doc": "The ID of the view."})
    Name: Optional[str] = field(default=None, metadata={"doc": "The name of the view."})
    IsEnhanced: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the view is an enhanced view."},
    )
    Childs: Optional[List["DMAViewTree"]] = field(
        default=None, metadata={"doc": "The child views within the view."}
    )
