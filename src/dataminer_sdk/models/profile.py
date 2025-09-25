from dataclasses import dataclass, field
from typing import Optional, List
from dataminer_sdk.models.base import BaseDMAType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAProfileParameterLink(BaseDMAType):
    """
    Represents DMA Profile Parameter Link.

    Attributes:
        ProtocolName (Optional[str]): The name of the protocol of a parameter linked to a profile parameter.
        ProtocolVersion (Optional[str]): The version of the protocol of a parameter linked to a profile parameter.
        ParameterID (Optional[int]): The ID of a parameter linked to a profile parameter.
        Index (Optional[str]): The index of a parameter linked to a profile parameter.
    """

    ProtocolName: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The name of the protocol of a parameter linked to a profile parameter."
        },
    )
    ProtocolVersion: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The version of the protocol of a parameter linked to a profile parameter."
        },
    )
    ParameterID: Optional[int] = field(
        default=None,
        metadata={"doc": "The ID of a parameter linked to a profile parameter."},
    )
    Index: Optional[str] = field(
        default=None,
        metadata={"doc": "The index of a parameter linked to a profile parameter."},
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAProfileParameterLite(BaseDMAType):
    """
    Represents DMA Profile Parameter Lite.

    Attributes:
        ID (Optional[str]): The ID of the profile parameter
        Name (Optional[str]): The name of the profile parameter
        Links (Optional[List[DMAProfileParameterLink]]): The parameters the profile parameter is linked to.
    """

    ID: Optional[str] = field(
        default=None, metadata={"doc": "The ID of the profile parameter"}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the profile parameter"}
    )
    Links: Optional[List[DMAProfileParameterLink]] = field(
        default=None,
        metadata={"doc": "The parameters the profile parameter is linked to."},
    )
