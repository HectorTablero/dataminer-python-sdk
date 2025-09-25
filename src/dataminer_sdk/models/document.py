from dataclasses import dataclass, field
from typing import Optional, List
from dataminer_sdk.models.base import BaseDMAType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMADocument(BaseDMAType):
    """
    Represents DMA Document.

    Attributes:
        Name (Optional[str]): The name of the document.
        Description (Optional[str]): The description of the document.
        Comments (Optional[str]): The comments that have been added to the document.
        IsHyperlink (Optional[bool]): Indicates whether the document is a hyperlink.
        DateUTC (Optional[int]): The date when the document was added.
    """

    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the document."}
    )
    Description: Optional[str] = field(
        default=None, metadata={"doc": "The description of the document."}
    )
    Comments: Optional[str] = field(
        default=None,
        metadata={"doc": "The comments that have been added to the document."},
    )
    IsHyperlink: Optional[bool] = field(
        default=None, metadata={"doc": "Indicates whether the document is a hyperlink."}
    )
    DateUTC: Optional[int] = field(
        default=None, metadata={"doc": "The date when the document was added."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMADocumentFolder(BaseDMAType):
    """
    Represents DMA Document Folder.

    Attributes:
        Name (Optional[str]): The name of the document folder.
        Subfolders (Optional[List[DMADocumentFolder]]): The subfolders of the current document folder.
        Documents (Optional[List[DMADocument]]): The documents in this folder.
    """

    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the document folder."}
    )
    Subfolders: Optional[List["DMADocumentFolder"]] = field(
        default=None, metadata={"doc": "The subfolders of the current document folder."}
    )
    Documents: Optional[List[DMADocument]] = field(
        default=None, metadata={"doc": "The documents in this folder."}
    )
