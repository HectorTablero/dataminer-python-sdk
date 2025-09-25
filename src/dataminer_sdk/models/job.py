from dataclasses import dataclass, field
from typing import Optional, List
from dataminer_sdk.models.base import BaseDMAType
from dataminer_sdk.models.enums import JobSectionType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAJobFieldValueDisplay(BaseDMAType):
    """
    Represents DMA Job Field Value Display.

    Attributes:
        ID (Optional[str]): The ID of the field.
        Name (Optional[str]): The name of the field that will be displayed when a user creates or edits a job.
        Value (Optional[str]): The value of the field.
        DisplayValue (Optional[str]): The displayed field value.
        Type (Optional[str]): The type of field. For an overview of the different types, refer to “Configuring a job field” in the DataMiner Help.
        IsMultiSelectionFilter (Optional[bool]): Determines whether users will be able to filter on the value selected for the field, in case the field is of type Dropdown.
        ShowInListView (Optional[bool]): Determines whether the field is displayed in the list view of the Jobs app.
        IsRequired (Optional[bool]): Determines whether the field must always be filled in when a job is created.
        IsHidden (Optional[bool]): Determines whether the field is displayed in the Jobs app.
        IsReadOnly (Optional[bool]): Determines whether users will be able to modify the field.
        Tooltip (Optional[str]): The text that will be displayed as a tooltip for the field.
    """

    ID: Optional[str] = field(default=None, metadata={"doc": "The ID of the field."})
    Name: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The name of the field that will be displayed when a user creates or edits a job."
        },
    )
    Value: Optional[str] = field(
        default=None, metadata={"doc": "The value of the field."}
    )
    DisplayValue: Optional[str] = field(
        default=None, metadata={"doc": "The displayed field value."}
    )
    Type: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The type of field. For an overview of the different types, refer to “Configuring a job field” in the DataMiner Help."
        },
    )
    IsMultiSelectionFilter: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Determines whether users will be able to filter on the value selected for the field, in case the field is of type Dropdown."
        },
    )
    ShowInListView: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Determines whether the field is displayed in the list view of the Jobs app."
        },
    )
    IsRequired: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Determines whether the field must always be filled in when a job is created."
        },
    )
    IsHidden: Optional[bool] = field(
        default=None,
        metadata={"doc": "Determines whether the field is displayed in the Jobs app."},
    )
    IsReadOnly: Optional[bool] = field(
        default=None,
        metadata={"doc": "Determines whether users will be able to modify the field."},
    )
    Tooltip: Optional[str] = field(
        default=None,
        metadata={"doc": "The text that will be displayed as a tooltip for the field."},
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAJobSection(BaseDMAType):
    """
    Represents DMA Job Section.

    Attributes:
        ID (Optional[str]): The ID of the job section.
        SectionDefinitionID (Optional[str]): The ID of the job section definition.
        Name (Optional[str]): The name of the job section.
        Type (Optional[JobSectionType]): The type of job section (Fields or Booking).
        Fields (Optional[List[DMAJobFieldValueDisplay]]): See DMAJobFieldValueDisplay.
    """

    ID: Optional[str] = field(
        default=None, metadata={"doc": "The ID of the job section."}
    )
    SectionDefinitionID: Optional[str] = field(
        default=None, metadata={"doc": "The ID of the job section definition."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the job section."}
    )
    Type: Optional[JobSectionType] = field(
        default=None, metadata={"doc": "The type of job section (Fields or Booking)."}
    )
    Fields: Optional[List[DMAJobFieldValueDisplay]] = field(
        default=None, metadata={"doc": "See DMAJobFieldValueDisplay."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAJob(BaseDMAType):
    """
    Represents DMA Job.

    Attributes:
        ID (Optional[str]): The ID of the job.
        DomainID (Optional[str]): The domain of the job.
        Name (Optional[str]): The name of the job.
        TimeStartUTC (Optional[int]): The start time of the job in UTC format (milliseconds since midnight January 1, 1970 GMT).
        TimeEndUTC (Optional[int]): The end time of the job in UTC format (milliseconds since midnight January 1, 1970 GMT).
        Sections (Optional[List[DMAJobSection]]): The sections of the job.
    """

    ID: Optional[str] = field(default=None, metadata={"doc": "The ID of the job."})
    DomainID: Optional[str] = field(
        default=None, metadata={"doc": "The domain of the job."}
    )
    Name: Optional[str] = field(default=None, metadata={"doc": "The name of the job."})
    TimeStartUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The start time of the job in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )
    TimeEndUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The end time of the job in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )
    Sections: Optional[List[DMAJobSection]] = field(
        default=None, metadata={"doc": "The sections of the job."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAJobDomainLite(BaseDMAType):
    """
    Represents DMA Job Domain Lite.

    Attributes:
        ID (Optional[str]): The ID of the job domain.
        Name (Optional[str]): The name of the job domain.
        IsHidden (Optional[bool]): Indicates whether the job domain is hidden.
    """

    ID: Optional[str] = field(
        default=None, metadata={"doc": "The ID of the job domain."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the job domain."}
    )
    IsHidden: Optional[bool] = field(
        default=None, metadata={"doc": "Indicates whether the job domain is hidden."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAJobFieldFilter(BaseDMAType):
    """
    Represents DMA Job Field Filter.

    Attributes:
        FieldID (Optional[str]): The ID of the job field.
        SectionDefinitionID (Optional[str]): The ID of the section definition.
        Values (Optional[List[str]]): The field values that are used as a filter.
    """

    FieldID: Optional[str] = field(
        default=None, metadata={"doc": "The ID of the job field."}
    )
    SectionDefinitionID: Optional[str] = field(
        default=None, metadata={"doc": "The ID of the section definition."}
    )
    Values: Optional[List[str]] = field(
        default=None, metadata={"doc": "The field values that are used as a filter."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAJobFieldPossibleValues(BaseDMAType):
    """
    Represents DMA Job Field Possible Values.

    Attributes:
        Values (Optional[List[str]]): The possible values of the field.
        CanLoadMore (Optional[bool]): Indicates whether additional values can be loaded.
        Total (Optional[int]): The total number of all values, before filters are applied.
        HiddenValues (Optional[List[str]]): The possible values of the field that have been deleted and are therefore hidden.
    """

    Values: Optional[List[str]] = field(
        default=None, metadata={"doc": "The possible values of the field."}
    )
    CanLoadMore: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether additional values can be loaded."},
    )
    Total: Optional[int] = field(
        default=None,
        metadata={"doc": "The total number of all values, before filters are applied."},
    )
    HiddenValues: Optional[List[str]] = field(
        default=None,
        metadata={
            "doc": "The possible values of the field that have been deleted and are therefore hidden."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAJobSuggestion(BaseDMAType):
    """
    Represents DMA Job Suggestion.

    Attributes:
        FieldID (Optional[str]): The ID of the job field.
        Value (Optional[str]): The value of the job field.
        Score (Optional[float]): Score indicating to what extent the job field matches the input.
    """

    FieldID: Optional[str] = field(
        default=None, metadata={"doc": "The ID of the job field."}
    )
    Value: Optional[str] = field(
        default=None, metadata={"doc": "The value of the job field."}
    )
    Score: Optional[float] = field(
        default=None,
        metadata={
            "doc": "Score indicating to what extent the job field matches the input."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAJobTemplate(BaseDMAType):
    """
    Represents DMA Job Template.

    Attributes:
        ID (Optional[str]): The ID of the job template.
        Name (Optional[str]): The name of the job template.
        Template (Optional[DMAJob]): The job fields and sections included in the template, with their values. When the template is applied, these values are copied to the target job.
    """

    ID: Optional[str] = field(
        default=None, metadata={"doc": "The ID of the job template."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the job template."}
    )
    Template: Optional[DMAJob] = field(
        default=None,
        metadata={
            "doc": "The job fields and sections included in the template, with their values. When the template is applied, these values are copied to the target job."
        },
    )
