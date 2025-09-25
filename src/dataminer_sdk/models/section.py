from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List, TYPE_CHECKING
from dataminer_sdk.models.base import BaseDMAType
from dataminer_sdk.models.enums import SectionDefinitionFieldType

if TYPE_CHECKING:
    from dataminer_sdk.models.booking import DMABookingManager
    from dataminer_sdk.models.misc import DMAColor


@dataclass(slots=True, frozen=True, kw_only=True)
class DMASectionDefinitionField(BaseDMAType):
    """
    Represents DMA Section Definition Field.

    Attributes:
        ID (Optional[str]): The ID of the job section definition field.
        Name (Optional[str]): The name of the job section definition field.
        Type (Optional[SectionDefinitionFieldType]): Type that the value must have. The following types are supported: string, double, long, DateTime, TimeSpan and bool.
        IsMultiSelectionFilter (Optional[bool]): Determines whether multiple instances of the section are allowed.
        ShowInListView (Optional[bool]): Determines whether the field is shown in the list view of the Jobs app.
        IsRequired (Optional[bool]): Determines whether filling in this field is mandatory when a job is created.
        ReadOnly (Optional[bool]): Indicates whether the field is part of the default section definition.
        AutoIncrementPrefix (Optional[str]): For an “auto increment” section definition field, this field can optionally contain a prefix for the auto increment counter.
        AutoIncrementSuffix (Optional[str]): For an “auto increment” section definition field, this field can optionally contain a suffix for the auto increment counter.
        IsReadOnly (Optional[bool]): Determines whether the client can change this field.
        IsHidden (Optional[bool]): Determines whether the field is hidden.
        Tooltip (Optional[str]): The tooltip that should be displayed for this field.
    """

    ID: Optional[str] = field(
        default=None, metadata={"doc": "The ID of the job section definition field."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the job section definition field."}
    )
    Type: Optional[SectionDefinitionFieldType] = field(
        default=None,
        metadata={
            "doc": "Type that the value must have. The following types are supported: string, double, long, DateTime, TimeSpan and bool."
        },
    )
    IsMultiSelectionFilter: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Determines whether multiple instances of the section are allowed."
        },
    )
    ShowInListView: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Determines whether the field is shown in the list view of the Jobs app."
        },
    )
    IsRequired: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Determines whether filling in this field is mandatory when a job is created."
        },
    )
    ReadOnly: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the field is part of the default section definition."
        },
    )
    AutoIncrementPrefix: Optional[str] = field(
        default=None,
        metadata={
            "doc": "For an “auto increment” section definition field, this field can optionally contain a prefix for the auto increment counter."
        },
    )
    AutoIncrementSuffix: Optional[str] = field(
        default=None,
        metadata={
            "doc": "For an “auto increment” section definition field, this field can optionally contain a suffix for the auto increment counter."
        },
    )
    IsReadOnly: Optional[bool] = field(
        default=None,
        metadata={"doc": "Determines whether the client can change this field."},
    )
    IsHidden: Optional[bool] = field(
        default=None, metadata={"doc": "Determines whether the field is hidden."}
    )
    Tooltip: Optional[str] = field(
        default=None,
        metadata={"doc": "The tooltip that should be displayed for this field."},
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMASectionDefinition(BaseDMAType):
    """
    Represents DMA Section Definition.

    Attributes:
        Name (Optional[str]): The name of the job section.
        ID (Optional[str]): The ID of the job section.
        ReadOnly (Optional[bool]): Indicates whether the job section can be modified.
        IsHidden (Optional[bool]): Indicates whether the job section is hidden.
        BookingLinkInfo_BookingManager (Optional[DMABookingManager]): The DataMiner ID, element ID and name of the Booking Manager element that is used, in case the section is linked to a booking.
        BookingLinkInfo_BookingScript (Optional[str]): The script that should be executed when a user clicks an action in the job section, in case the section is linked to a booking.
        Fields (Optional[List[DMASectionDefinitionField]]): See DMASectionDefinitionField.
        Info_Icon (Optional[str]): The name of the icon associated with this section.
        Info_Color (Optional[List[int]]): The background color of the section, in RGB format.
        Info_Column (Optional[int]): The column of the Jobs app containing this job section.
        Info_Index (Optional[int]): The row of the Jobs app containing this job section.
        Info_FieldIndices (Optional[List[str]]): Determines the position and order of the fields in the section.
        Info_MultiSelectionFilters (Optional[List[str]]): The IDs of the drop-down fields that are configured as filter, if available.
        Info_ShowInListView (Optional[List[str]]): Determines whether the section is shown as a column in the list of jobs in the Jobs app.
        CustomSectionDefinitionExtensionID (Optional[str]): The section definition ID of the section definition that is created in case a field is added to the default section.
        AllowMultipleInstances (Optional[bool]): Indicates whether multiple instances of the job section will be allowed.
    """

    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the job section."}
    )
    ID: Optional[str] = field(
        default=None, metadata={"doc": "The ID of the job section."}
    )
    ReadOnly: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the job section can be modified."},
    )
    IsHidden: Optional[bool] = field(
        default=None, metadata={"doc": "Indicates whether the job section is hidden."}
    )
    BookingLinkInfo_BookingManager: Optional[DMABookingManager] = field(
        default=None,
        metadata={
            "doc": "The DataMiner ID, element ID and name of the Booking Manager element that is used, in case the section is linked to a booking."
        },
    )
    BookingLinkInfo_BookingScript: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The script that should be executed when a user clicks an action in the job section, in case the section is linked to a booking."
        },
    )
    Fields: Optional[List[DMASectionDefinitionField]] = field(
        default=None, metadata={"doc": "See DMASectionDefinitionField."}
    )
    Info_Icon: Optional[str] = field(
        default=None,
        metadata={"doc": "The name of the icon associated with this section."},
    )
    Info_Color: Optional[List[int]] = field(
        default=None,
        metadata={"doc": "The background color of the section, in RGB format."},
    )
    Info_Column: Optional[int] = field(
        default=None,
        metadata={"doc": "The column of the Jobs app containing this job section."},
    )
    Info_Index: Optional[int] = field(
        default=None,
        metadata={"doc": "The row of the Jobs app containing this job section."},
    )
    Info_FieldIndices: Optional[List[str]] = field(
        default=None,
        metadata={
            "doc": "Determines the position and order of the fields in the section."
        },
    )
    Info_MultiSelectionFilters: Optional[List[str]] = field(
        default=None,
        metadata={
            "doc": "The IDs of the drop-down fields that are configured as filter, if available."
        },
    )
    Info_ShowInListView: Optional[List[str]] = field(
        default=None,
        metadata={
            "doc": "Determines whether the section is shown as a column in the list of jobs in the Jobs app."
        },
    )
    CustomSectionDefinitionExtensionID: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The section definition ID of the section definition that is created in case a field is added to the default section."
        },
    )
    AllowMultipleInstances: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether multiple instances of the job section will be allowed."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMASectionDomainConfig(BaseDMAType):
    """
    Represents DMA Section Domain Config.

    Attributes:
        SectionDefinitionID (Optional[str]): The ID of the job section definition.
        SectionDefinitionInfo_Icon (Optional[str]): The name of the icon associated with this section.
        SectionDefinitionInfo_Color (Optional[DMAColor]): The background color of the section, in RGB format.
        SectionDefinitionInfo_Column (Optional[int]): The position of the column containing this section in the Jobs app layout.
        SectionDefinitionInfo_Index (Optional[int]): The row containing this section in the Jobs app layout.
        SectionDefinitionInfo_FieldIndices (Optional[List[str]]): Determines the position and order of the fields in the section.
        SectionDefinitionInfo_MultiSelectionFilters (Optional[List[str]]): The IDs of the drop-down fields that are configured as filter, if available.
        SectionDefinitionInfo_ShowInListView (Optional[List[str]]): Determines whether the section is shown as a column in the list of jobs in the Jobs app.
        SectionDefinitionInfo_AllowMultipleInstances (Optional[bool]): Indicates whether multiple instances of the job section will be allowed.
        SectionDefinitionInfo_CustomSectionDefinitionExtensionID (Optional[str]): The section definition ID of the section definition that is created in case a field is added to the default section.
    """

    SectionDefinitionID: Optional[str] = field(
        default=None, metadata={"doc": "The ID of the job section definition."}
    )
    SectionDefinitionInfo_Icon: Optional[str] = field(
        default=None,
        metadata={"doc": "The name of the icon associated with this section."},
    )
    SectionDefinitionInfo_Color: Optional[DMAColor] = field(
        default=None,
        metadata={"doc": "The background color of the section, in RGB format."},
    )
    SectionDefinitionInfo_Column: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The position of the column containing this section in the Jobs app layout."
        },
    )
    SectionDefinitionInfo_Index: Optional[int] = field(
        default=None,
        metadata={"doc": "The row containing this section in the Jobs app layout."},
    )
    SectionDefinitionInfo_FieldIndices: Optional[List[str]] = field(
        default=None,
        metadata={
            "doc": "Determines the position and order of the fields in the section."
        },
    )
    SectionDefinitionInfo_MultiSelectionFilters: Optional[List[str]] = field(
        default=None,
        metadata={
            "doc": "The IDs of the drop-down fields that are configured as filter, if available."
        },
    )
    SectionDefinitionInfo_ShowInListView: Optional[List[str]] = field(
        default=None,
        metadata={
            "doc": "Determines whether the section is shown as a column in the list of jobs in the Jobs app."
        },
    )
    SectionDefinitionInfo_AllowMultipleInstances: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether multiple instances of the job section will be allowed."
        },
    )
    SectionDefinitionInfo_CustomSectionDefinitionExtensionID: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The section definition ID of the section definition that is created in case a field is added to the default section."
        },
    )
