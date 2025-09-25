from dataclasses import dataclass, field
from typing import Optional, List
from dataminer_sdk.models.base import BaseDMAType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMATimelineChange(BaseDMAType):
    """
    Represents DMA Timeline Change.

    Attributes:
        TimeUTC (Optional[int]): The time when a change occurred.
        Value (Optional[str]): The changed value.
    """

    TimeUTC: Optional[int] = field(
        default=None, metadata={"doc": "The time when a change occurred."}
    )
    Value: Optional[str] = field(default=None, metadata={"doc": "The changed value."})


@dataclass(slots=True, frozen=True, kw_only=True)
class DMATimeline(BaseDMAType):
    """
    Represents DMA Timeline.

    Attributes:
        Changes (Optional[List[DMATimelineChange]]): Array of timeline change objects, consisting of: TimeUTC: The time when a change occurred. Value: The changed value.
        TimeStartUTC (Optional[int]): The start time of the interval for which timeline changes are returned.
        TimeEndUTC (Optional[int]): The end time of the interval for which timeline changes are returned.
    """

    Changes: Optional[List[DMATimelineChange]] = field(
        default=None,
        metadata={
            "doc": "Array of timeline change objects, consisting of: TimeUTC: The time when a change occurred. Value: The changed value."
        },
    )
    TimeStartUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The start time of the interval for which timeline changes are returned."
        },
    )
    TimeEndUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The end time of the interval for which timeline changes are returned."
        },
    )
