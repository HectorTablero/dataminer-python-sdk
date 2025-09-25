from dataclasses import dataclass, field
from typing import Optional
from dataminer_sdk.models.base import BaseDMAType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAStatistics(BaseDMAType):
    """
    Represents DMA Statistics.

    Attributes:
        ID (Optional[int]): The DMA ID.
        AmountElements (Optional[int]): The number of elements on the DMA.
        AmountElementsActive (Optional[int]): The number of active elements on the DMA.
        AmountServices (Optional[int]): The number of services on the DMA.
    """

    ID: Optional[int] = field(default=None, metadata={"doc": "The DMA ID."})
    AmountElements: Optional[int] = field(
        default=None, metadata={"doc": "The number of elements on the DMA."}
    )
    AmountElementsActive: Optional[int] = field(
        default=None, metadata={"doc": "The number of active elements on the DMA."}
    )
    AmountServices: Optional[int] = field(
        default=None, metadata={"doc": "The number of services on the DMA."}
    )
