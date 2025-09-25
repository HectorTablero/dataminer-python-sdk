from dataclasses import dataclass, field
from typing import Optional, List
from dataminer_sdk.models.base import BaseDMAType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAUser(BaseDMAType):
    """
    Represents DMA User.

    Attributes:
        Login (Optional[str]): The user’s login name
        FullName (Optional[str]): The full name of the user.
        EmailAddress (Optional[str]): The email address of the user.
        GroupIds (Optional[List[int]]): The IDs of the groups the user is a member of.
    """

    Login: Optional[str] = field(
        default=None, metadata={"doc": "The user’s login name"}
    )
    FullName: Optional[str] = field(
        default=None, metadata={"doc": "The full name of the user."}
    )
    EmailAddress: Optional[str] = field(
        default=None, metadata={"doc": "The email address of the user."}
    )
    GroupIds: Optional[List[int]] = field(
        default=None, metadata={"doc": "The IDs of the groups the user is a member of."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAUserGroup(BaseDMAType):
    """
    Represents DMA User Group.

    Attributes:
        ID (Optional[int]): The ID of the user group.
        Type (Optional[str]): The name of the user group.
    """

    ID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the user group."}
    )
    Type: Optional[str] = field(
        default=None, metadata={"doc": "The name of the user group."}
    )
