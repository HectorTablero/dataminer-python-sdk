from dataclasses import dataclass, field
from typing import Optional, List
from dataminer_sdk.models.base import BaseDMAType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAProtocolPage(BaseDMAType):
    """
    Represents DMA Protocol Page.

    Attributes:
        ProtocolName (Optional[str]): The name of the protocol.
        ProtocolVersion (Optional[str]): The version of the protocol.
        Name (Optional[str]): The name of the page.
        Position (Optional[int]): The position of the page in the list of pages of the protocol (zero-based).
        Children (Optional[List[str]]): The subpages of this page.
        IsSeparator (Optional[bool]): Indicates whether the page is a separator.
        IsPopup (Optional[bool]): Indicates whether the page is a pop-up page.
        IsWeb (Optional[bool]): Indicates whether the page is an embedded webpage.
        IsSpectrum (Optional[bool]): Indicates whether the page is a spectrum page.
        IsGeneralParameters (Optional[bool]): Indicates whether the page is the general parameters page.
        LastChangeUTC (Optional[int]): The time when the page was last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT).
    """

    ProtocolName: Optional[str] = field(
        default=None, metadata={"doc": "The name of the protocol."}
    )
    ProtocolVersion: Optional[str] = field(
        default=None, metadata={"doc": "The version of the protocol."}
    )
    Name: Optional[str] = field(default=None, metadata={"doc": "The name of the page."})
    Position: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The position of the page in the list of pages of the protocol (zero-based)."
        },
    )
    Children: Optional[List[str]] = field(
        default=None, metadata={"doc": "The subpages of this page."}
    )
    IsSeparator: Optional[bool] = field(
        default=None, metadata={"doc": "Indicates whether the page is a separator."}
    )
    IsPopup: Optional[bool] = field(
        default=None, metadata={"doc": "Indicates whether the page is a pop-up page."}
    )
    IsWeb: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the page is an embedded webpage."},
    )
    IsSpectrum: Optional[bool] = field(
        default=None, metadata={"doc": "Indicates whether the page is a spectrum page."}
    )
    IsGeneralParameters: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the page is the general parameters page."},
    )
    LastChangeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The time when the page was last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAFunctionDefinitionLite(BaseDMAType):
    """
    Represents DMA Function Definition Lite.

    Attributes:
        ID (Optional[str]): The ID of the function definition.
        Name (Optional[str]): The name of the function definition.
        Parent (Optional[DMAFunctionDefinitionLite]): The parent function definition (if any) of the function definition.
    """

    ID: Optional[str] = field(
        default=None, metadata={"doc": "The ID of the function definition."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the function definition."}
    )
    Parent: Optional["DMAFunctionDefinitionLite"] = field(
        default=None,
        metadata={
            "doc": "The parent function definition (if any) of the function definition."
        },
    )
