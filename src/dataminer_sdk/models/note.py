from dataclasses import dataclass, field
from typing import Optional
from dataminer_sdk.models.base import BaseDMAType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMANote(BaseDMAType):
    """
    Represents DMA Note.

    Attributes:
        CreatedBy (Optional[str]): The user who created the note.
        Description (Optional[str]): The content of the note.
        ID (Optional[int]): The ID of the note.
        ModifiedBy (Optional[str]): The user who last modified the note.
        Summary (Optional[str]): The title of the note.
        TimeCreatedUTC (Optional[int]): The time when the note was created.
        TimeModifiedUTC (Optional[int]): The time when the note was last modified.
        TimeExpiresUTC (Optional[int]): The time when the note will expire.
    """

    # TODO: Check if it really returns a string for CreatedBy and ModifiedBy instead of a DMAUser object
    CreatedBy: Optional[str] = field(
        default=None, metadata={"doc": "The user who created the note."}
    )
    Description: Optional[str] = field(
        default=None, metadata={"doc": "The content of the note."}
    )
    ID: Optional[int] = field(default=None, metadata={"doc": "The ID of the note."})
    ModifiedBy: Optional[str] = field(
        default=None, metadata={"doc": "The user who last modified the note."}
    )
    Summary: Optional[str] = field(
        default=None, metadata={"doc": "The title of the note."}
    )
    TimeCreatedUTC: Optional[int] = field(
        default=None, metadata={"doc": "The time when the note was created."}
    )
    TimeModifiedUTC: Optional[int] = field(
        default=None, metadata={"doc": "The time when the note was last modified."}
    )
    TimeExpiresUTC: Optional[int] = field(
        default=None, metadata={"doc": "The time when the note will expire."}
    )
