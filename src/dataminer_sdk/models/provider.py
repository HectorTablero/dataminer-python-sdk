from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, TYPE_CHECKING
from dataminer_sdk.models.base import BaseDMAType

if TYPE_CHECKING:
    from dataminer_sdk.models.misc import DMAColor


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAProviderInfo(BaseDMAType):
    """
    Represents DMA Provider Info.

    Attributes:
        CompanyName (Optional[str]): The company name of the provider.
        ContactUsEmail (Optional[str]): The contact email address of the provider.
        DataMinerLogoVisible (Optional[bool]): Whether the DataMiner logo is displayed.
        Name (Optional[str]): The name of the provider.
        ProductName (Optional[str]): The name of the product (e.g. DataMiner).
        TechsupportAddress1 (Optional[str]): The first line of the address of tech support.
        TechsupportAddress2 (Optional[str]): The second line of the address of tech support.
        TechsupportAddress3 (Optional[str]): The third line of the address of tech support.
        TechsupportEmail (Optional[str]): The tech support email address.
        TechsupportName (Optional[str]): The tech support name.
        TechsupportWWW (Optional[str]): The tech support URL.
        WWW (Optional[str]): The website of the provider.
    """

    CompanyName: Optional[str] = field(
        default=None, metadata={"doc": "The company name of the provider."}
    )
    ContactUsEmail: Optional[str] = field(
        default=None, metadata={"doc": "The contact email address of the provider."}
    )
    DataMinerLogoVisible: Optional[bool] = field(
        default=None, metadata={"doc": "Whether the DataMiner logo is displayed."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the provider."}
    )
    ProductName: Optional[str] = field(
        default=None, metadata={"doc": "The name of the product (e.g. DataMiner)."}
    )
    TechsupportAddress1: Optional[str] = field(
        default=None, metadata={"doc": "The first line of the address of tech support."}
    )
    TechsupportAddress2: Optional[str] = field(
        default=None,
        metadata={"doc": "The second line of the address of tech support."},
    )
    TechsupportAddress3: Optional[str] = field(
        default=None, metadata={"doc": "The third line of the address of tech support."}
    )
    TechsupportEmail: Optional[str] = field(
        default=None, metadata={"doc": "The tech support email address."}
    )
    TechsupportName: Optional[str] = field(
        default=None, metadata={"doc": "The tech support name."}
    )
    TechsupportWWW: Optional[str] = field(
        default=None, metadata={"doc": "The tech support URL."}
    )
    WWW: Optional[str] = field(
        default=None, metadata={"doc": "The website of the provider."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAProviderTheme(BaseDMAType):
    """
    Represents DMA Provider Theme.

    Attributes:
        Name (Optional[str]): The name of the provider.
        DisplayName (Optional[str]): The name of the provider as displayed in the UI.
        AccentColor (Optional[DMAColor]): The accent color of the theme. This is for example used in the header and in the Alarm Console footer background.
        AccentTextColor (Optional[DMAColor]): The text color used when the background has the accent color.
        BackGroundColor (Optional[DMAColor]): The background color.
        Background (Optional[str]): The background image.
        Logo (Optional[str]): The product logo (base64-encoded string).
        LogoLarge (Optional[str]): The large version of the product logo (base64-encoded string).
    """

    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the provider."}
    )
    DisplayName: Optional[str] = field(
        default=None,
        metadata={"doc": "The name of the provider as displayed in the UI."},
    )
    AccentColor: Optional[DMAColor] = field(
        default=None,
        metadata={
            "doc": "The accent color of the theme. This is for example used in the header and in the Alarm Console footer background."
        },
    )
    AccentTextColor: Optional[DMAColor] = field(
        default=None,
        metadata={
            "doc": "The text color used when the background has the accent color."
        },
    )
    BackGroundColor: Optional[DMAColor] = field(
        default=None, metadata={"doc": "The background color."}
    )
    Background: Optional[str] = field(
        default=None, metadata={"doc": "The background image."}
    )
    Logo: Optional[str] = field(
        default=None, metadata={"doc": "The product logo (base64-encoded string)."}
    )
    LogoLarge: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The large version of the product logo (base64-encoded string)."
        },
    )
