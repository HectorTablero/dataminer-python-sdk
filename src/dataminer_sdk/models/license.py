from dataclasses import dataclass, field
from typing import Optional
from dataminer_sdk.models.base import BaseDMAType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMALicenseInfo(BaseDMAType):
    """
    Represents DMA License Info.

    Attributes:
        ID (Optional[int]): The ID of the DataMiner Agent.
        Name (Optional[str]): The name of the DataMiner Agent.
        AmountElementsMaximum (Optional[int]): The maximum number of elements allowed on the DataMiner Agent.
        AmountElementsActive (Optional[int]): The number of elements that are currently active on the DataMiner Agent.
    """

    ID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the DataMiner Agent."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the DataMiner Agent."}
    )
    AmountElementsMaximum: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The maximum number of elements allowed on the DataMiner Agent."
        },
    )
    AmountElementsActive: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The number of elements that are currently active on the DataMiner Agent."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMALicenses(BaseDMAType):
    """
    Represents DMA Licenses.

    Attributes:
        AssetManager (Optional[bool]): Indicates whether the Asset Manager license is available on the DMA.
        Automation (Optional[bool]): Indicates whether the Automation license is available on the DMA.
        Correlation (Optional[bool]): Indicates whether the Correlation license is available on the DMA.
        Maps (Optional[bool]): Indicates whether the Maps license is available on the DMA.
        Mobile (Optional[bool]): Indicates whether the Mobile license is available on the DMA.
        MobileExtended (Optional[bool]): Indicates whether the Mobile Extended license is available on the DMA.
        MobileGateway (Optional[bool]): Indicates whether the Mobile Gateway license is available on the DMA.
        Reporter (Optional[bool]): Indicates whether the Reporter license is available on the DMA.
        ResourceManager (Optional[bool]): Indicates whether the Resource Manager license is available on the DMA.
        Scheduler (Optional[bool]): Indicates whether the Scheduler license is available on the DMA.
        Spectrum (Optional[bool]): Indicates whether the Spectrum license is available on the DMA.
        Ticketing (Optional[bool]): Indicates whether the Ticketing license is available on the DMA.
    """

    AssetManager: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the Asset Manager license is available on the DMA."
        },
    )
    Automation: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the Automation license is available on the DMA."
        },
    )
    Correlation: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the Correlation license is available on the DMA."
        },
    )
    Maps: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the Maps license is available on the DMA."},
    )
    Mobile: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the Mobile license is available on the DMA."
        },
    )
    MobileExtended: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the Mobile Extended license is available on the DMA."
        },
    )
    MobileGateway: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the Mobile Gateway license is available on the DMA."
        },
    )
    Reporter: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the Reporter license is available on the DMA."
        },
    )
    ResourceManager: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the Resource Manager license is available on the DMA."
        },
    )
    Scheduler: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the Scheduler license is available on the DMA."
        },
    )
    Spectrum: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the Spectrum license is available on the DMA."
        },
    )
    Ticketing: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the Ticketing license is available on the DMA."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAThirdPartyNotice(BaseDMAType):
    """
    Represents DMA Third Party Notice.

    Attributes:
        Title (Optional[str]): The title of the notice.
        License (Optional[str]): The license information.
    """

    Title: Optional[str] = field(
        default=None, metadata={"doc": "The title of the notice."}
    )
    License: Optional[str] = field(
        default=None, metadata={"doc": "The license information."}
    )
