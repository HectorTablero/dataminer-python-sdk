from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List, TYPE_CHECKING
from dataminer_sdk.models.base import BaseDMAType
from dataminer_sdk.models.enums import (
    VisioRegionActionType,
    VisioRegionContentType,
    VisioRegionShapeType,
    VisioRegionType,
)

if TYPE_CHECKING:
    from dataminer_sdk.models.misc import DMAGenericProperty


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAVisio(BaseDMAType):
    """
    Represents DMA Visio.

    Attributes:
        DataMinerID (Optional[int]): The ID of the DataMiner Agent.
        ID (Optional[int]): The ID of the element, service or view.
        Page (Optional[int]): The index number of the Visio page.
        PNG (Optional[str]): The base64-encoded PNG image.
        Width (Optional[int]): The width of the PNG image (in pixels).
        Height (Optional[int]): The height of the PNG image (in pixels).
        Regions (Optional[List[DMAVisioRegion]]): The regions in the Visio page.
        Error (Optional[str]): If the requested Visio page could not be retrieved, this field will contain the error message.
        Pages (Optional[List[DMAVisioPage]]): All pages in the Visio file.
        LastChangeUTC (Optional[int]): The time when the object was last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT).
    """

    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the DataMiner Agent."}
    )
    ID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the element, service or view."}
    )
    Page: Optional[int] = field(
        default=None, metadata={"doc": "The index number of the Visio page."}
    )
    PNG: Optional[str] = field(
        default=None, metadata={"doc": "The base64-encoded PNG image."}
    )
    Width: Optional[int] = field(
        default=None, metadata={"doc": "The width of the PNG image (in pixels)."}
    )
    Height: Optional[int] = field(
        default=None, metadata={"doc": "The height of the PNG image (in pixels)."}
    )
    Regions: Optional[List["DMAVisioRegion"]] = field(
        default=None, metadata={"doc": "The regions in the Visio page."}
    )
    Error: Optional[str] = field(
        default=None,
        metadata={
            "doc": "If the requested Visio page could not be retrieved, this field will contain the error message."
        },
    )
    Pages: Optional[List["DMAVisioPage"]] = field(
        default=None, metadata={"doc": "All pages in the Visio file."}
    )
    LastChangeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The time when the object was last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAVisioPage(BaseDMAType):
    """
    Represents DMA Visio Page.

    Attributes:
        ID (Optional[int]): The ID of the Visio page.
        Name (Optional[str]): The name of the Visio page.
        IsVisible (Optional[bool]): Indicates whether the page is initially displayed or not. The latter can for example be the case for a pop-up page.
    """

    ID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the Visio page."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the Visio page."}
    )
    IsVisible: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the page is initially displayed or not. The latter can for example be the case for a pop-up page."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAVisioRegion(BaseDMAType):
    """
    Represents DMA Visio Region.

    Attributes:
        RegionID (Optional[int]): The ID of the region.
        xCoord (Optional[int]): The X coordinate of the top-left corner of the region (number of pixels measured from the left).
        yCoord (Optional[int]): The Y coordinate of the top-left corner of the region (number of pixels measured from the left).
        Width (Optional[int]): The width of the region (in pixels).
        Height (Optional[int]): The height of the region (in pixels).
        Shape (Optional[VisioRegionShapeType]): The shape of the region: “rect” (= rectangle), “circle”, “poly” (= polygon), etc. Note: At present, only “rect” is supported.
        ContentType (Optional[VisioRegionContentType]): The type of content: “Action”, “Url”, “Scroll”, “ParameterControl” or “SetVarControl”.
        Type (Optional[VisioRegionType]): The type of region: “NavigateView”, “NavigateElement”, “NavigateService”, “Url”, “Scroll”, “ParameterControl” or “SetVarControl”.
        ExtraData (Optional[List[DMAGenericProperty]]): Additional data. Examples: If Type is “NavigateElement”, ExtraData will contain the DataMiner ID and the Element ID. If Type is “SetVarControl”, ExtraData will contain extra values and filters.
        Actions (Optional[List[DMAVisioRegionAction]]): The actions in the region.
        ChildRegions (Optional[List[DMAVisioRegion]]): The child regions in the region.
        ActionSequence (Optional[List[DMAVisioRegionAction]]): The actions in the region in the order in which they should occur.
        ScrollRegionPNG (Optional[str]): The base64-encoded PNG image (only if Type or ContentType is “Scroll”).
        ScrollRegionPNGWidth (Optional[int]): The width in pixels of the image in ScrollRegionPNG (only if Type or ContentType is “Scroll”).
        ScrollRegionPNGHeight (Optional[int]): The height in pixels of the image in ScrollRegionPNG (only if Type or ContentType is “Scroll”).
    """

    RegionID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the region."}
    )
    xCoord: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The X coordinate of the top-left corner of the region (number of pixels measured from the left)."
        },
    )
    yCoord: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The Y coordinate of the top-left corner of the region (number of pixels measured from the left)."
        },
    )
    Width: Optional[int] = field(
        default=None, metadata={"doc": "The width of the region (in pixels)."}
    )
    Height: Optional[int] = field(
        default=None, metadata={"doc": "The height of the region (in pixels)."}
    )
    Shape: Optional[VisioRegionShapeType] = field(
        default=None,
        metadata={
            "doc": "The shape of the region: “rect” (= rectangle), “circle”, “poly” (= polygon), etc. Note: At present, only “rect” is supported."
        },
    )
    ContentType: Optional[VisioRegionContentType] = field(
        default=None,
        metadata={
            "doc": "The type of content: “Action”, “Url”, “Scroll”, “ParameterControl” or “SetVarControl”."
        },
    )
    Type: Optional[VisioRegionType] = field(
        default=None,
        metadata={
            "doc": "The type of region: “NavigateView”, “NavigateElement”, “NavigateService”, “Url”, “Scroll”, “ParameterControl” or “SetVarControl”."
        },
    )
    ExtraData: Optional[List[DMAGenericProperty]] = field(
        default=None,
        metadata={
            "doc": "Additional data. Examples: If Type is “NavigateElement”, ExtraData will contain the DataMiner ID and the Element ID. If Type is “SetVarControl”, ExtraData will contain extra values and filters."
        },
    )
    Actions: Optional[List["DMAVisioRegionAction"]] = field(
        default=None, metadata={"doc": "The actions in the region."}
    )
    ChildRegions: Optional[List["DMAVisioRegion"]] = field(
        default=None, metadata={"doc": "The child regions in the region."}
    )
    ActionSequence: Optional[List["DMAVisioRegionAction"]] = field(
        default=None,
        metadata={
            "doc": "The actions in the region in the order in which they should occur."
        },
    )
    ScrollRegionPNG: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The base64-encoded PNG image (only if Type or ContentType is “Scroll”)."
        },
    )
    ScrollRegionPNGWidth: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The width in pixels of the image in ScrollRegionPNG (only if Type or ContentType is “Scroll”)."
        },
    )
    ScrollRegionPNGHeight: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The height in pixels of the image in ScrollRegionPNG (only if Type or ContentType is “Scroll”)."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAVisioRegionAction(BaseDMAType):
    """
    Represents DMA Visio Region Action.

    Attributes:
        ActionID (Optional[str]): The ID of the action.
        PageID (Optional[int]): The index number of the Visio page.
        ShapeUniqueID (Optional[int]): The ID of the Visio shape.
        Text (Optional[str]): The text shown in the shape (i.e. the text of the hyperlink). Only used by DataMiner Cube.
        Description (Optional[str]): The text that will be shown in a tooltip when hovering over the shape. Only used by DataMiner Cube. Not used by the DataMiner web apps.
        Type (Optional[VisioRegionActionType]): The type of the region. At present, the following types are supported: “Card”, “Script”, “Navigate”, “WebLink”, “Set”, “ResetLatch”, “RedundancyGroupSwitch”, “SetVar” and “Popup”
        NeedsSendBack (Optional[bool]): This flag is used to check if a call to the server has to be made. Only used by DataMiner Cube. For the DataMiner web apps, this flag is always true.
        ExtraData (Optional[List[DMAGenericProperty]]): Additional data.
    """

    ActionID: Optional[str] = field(
        default=None, metadata={"doc": "The ID of the action."}
    )
    PageID: Optional[int] = field(
        default=None, metadata={"doc": "The index number of the Visio page."}
    )
    ShapeUniqueID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the Visio shape."}
    )
    Text: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The text shown in the shape (i.e. the text of the hyperlink). Only used by DataMiner Cube."
        },
    )
    Description: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The text that will be shown in a tooltip when hovering over the shape. Only used by DataMiner Cube. Not used by the DataMiner web apps."
        },
    )
    Type: Optional[VisioRegionActionType] = field(
        default=None,
        metadata={
            "doc": "The type of the region. At present, the following types are supported: “Card”, “Script”, “Navigate”, “WebLink”, “Set”, “ResetLatch”, “RedundancyGroupSwitch”, “SetVar” and “Popup”"
        },
    )
    NeedsSendBack: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "This flag is used to check if a call to the server has to be made. Only used by DataMiner Cube. For the DataMiner web apps, this flag is always true."
        },
    )
    ExtraData: Optional[List[DMAGenericProperty]] = field(
        default=None, metadata={"doc": "Additional data."}
    )
