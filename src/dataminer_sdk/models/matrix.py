from dataclasses import dataclass, field
from typing import Optional
from dataminer_sdk.models.base import BaseDMAType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAMatrixConnection(BaseDMAType):
    """
    Represents DMA Matrix Connection.

    Attributes:
        Input (Optional[int]): The connected input.
        Output (Optional[int]): The connected output.
        InputLabel (Optional[str]): The label of the connected input.
        OutputLabel (Optional[str]): The label of the connected output.
    """

    Input: Optional[int] = field(default=None, metadata={"doc": "The connected input."})
    Output: Optional[int] = field(
        default=None, metadata={"doc": "The connected output."}
    )
    InputLabel: Optional[str] = field(
        default=None, metadata={"doc": "The label of the connected input."}
    )
    OutputLabel: Optional[str] = field(
        default=None, metadata={"doc": "The label of the connected output."}
    )
