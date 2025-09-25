from dataclasses import dataclass, field
from typing import Optional
from dataminer_sdk.models.base import BaseDMAType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMADashboard(BaseDMAType):
    """
    Represents DMA Dashboard.

    Attributes:
        Name (Optional[str]): The name of the dashboard.
        Folder (Optional[str]): The dashboard folder.
        Path (Optional[str]): The path of the dashboard, which can be used to build a URL to open that dashboard by adding it after http(s)://[DMA IP].
    """

    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the dashboard."}
    )
    Folder: Optional[str] = field(
        default=None, metadata={"doc": "The dashboard folder."}
    )
    Path: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The path of the dashboard, which can be used to build a URL to open that dashboard by adding it after http(s)://[DMA IP]."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAButtonPanelInfo(BaseDMAType):
    """
    Represents DMA Button Panel Info.

    Attributes:
        Name (Optional[int]): The ID of the parameter containing the button name.
        X (Optional[int]): The ID of the parameter containing the position of the button on the X-axis.
        Y (Optional[int]): The ID of the parameter containing the position of the button on the Y-axis.
        Type (Optional[int]): The ID of the parameter detailing the type of button.
        AdvancedLayout (Optional[int]): The ID of the parameter containing the advanced button layout.
        CSS (Optional[int]): The ID of the parameter containing the CSS to apply to HTML content of the button.
        Container (Optional[int]): The ID of the parameter detailing the container the button belongs to.
        ActiveContainer (Optional[int]): The ID of the parameter containing the current active button panel container.
        PanelAdvancedLayout (Optional[int]): The ID of the parameter containing the general panel layout.
        PossibleOperations (Optional[int]): The ID of the parameter containing the possible operations of the button.
        Operation (Optional[int]): The ID of the parameter containing the button operations.
        ContainerLayout (Optional[int]): The ID of the parameter containing the container layout.
        Width (Optional[int]): The ID of the parameter containing the width of the button.
        Height (Optional[int]): The ID of the parameter containing the height of the button.
        ContainerTable (Optional[int]): The ID of the parameter listing the containers.
    """

    Name: Optional[int] = field(
        default=None,
        metadata={"doc": "The ID of the parameter containing the button name."},
    )
    X: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The ID of the parameter containing the position of the button on the X-axis."
        },
    )
    Y: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The ID of the parameter containing the position of the button on the Y-axis."
        },
    )
    Type: Optional[int] = field(
        default=None,
        metadata={"doc": "The ID of the parameter detailing the type of button."},
    )
    AdvancedLayout: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The ID of the parameter containing the advanced button layout."
        },
    )
    CSS: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The ID of the parameter containing the CSS to apply to HTML content of the button."
        },
    )
    Container: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The ID of the parameter detailing the container the button belongs to."
        },
    )
    ActiveContainer: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The ID of the parameter containing the current active button panel container."
        },
    )
    PanelAdvancedLayout: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The ID of the parameter containing the general panel layout."
        },
    )
    PossibleOperations: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The ID of the parameter containing the possible operations of the button."
        },
    )
    Operation: Optional[int] = field(
        default=None,
        metadata={"doc": "The ID of the parameter containing the button operations."},
    )
    ContainerLayout: Optional[int] = field(
        default=None,
        metadata={"doc": "The ID of the parameter containing the container layout."},
    )
    Width: Optional[int] = field(
        default=None,
        metadata={"doc": "The ID of the parameter containing the width of the button."},
    )
    Height: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The ID of the parameter containing the height of the button."
        },
    )
    ContainerTable: Optional[int] = field(
        default=None,
        metadata={"doc": "The ID of the parameter listing the containers."},
    )
