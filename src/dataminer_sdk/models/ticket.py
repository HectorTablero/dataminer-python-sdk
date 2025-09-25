from dataclasses import dataclass, field
from typing import Optional, List
from dataminer_sdk.models.base import BaseDMAType
from dataminer_sdk.models.enums import ResourceType, TicketFieldType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMATicket(BaseDMAType):
    """
    Represents DMA Ticket.

    Attributes:
        Fields (Optional[List[DMATicketFieldValueDisplay]]): An array containing an entry for each field with its value.
        DataMinerID (Optional[int]): The DMA ID of the Agent where the ticket was created.
        ID (Optional[int]): The ID of the ticket.
        UID (Optional[str]): The unique GUID identifier of the ticket. Deprecated.
        TicketTypeID (Optional[str]): The GUID of the ticket type.
        TimeCreatedUTC (Optional[int]): The time when the ticket was created, in UTC format (milliseconds since midnight January 1, 1970 GMT).
        LinkFields (Optional[List[DMATicketLinkField]]): Array containing the linked DataMiner resources. For every DataMiner Object field, it contains a DMATicketLinkField entry with a DMATicketLinkValue array with its linked DataMiner resources.
        StateColor (Optional[str]): The color corresponding with the ticket state.
        IsClosed (Optional[bool]): Indicates whether the ticket is closed.
    """

    Fields: Optional[List["DMATicketFieldValueDisplay"]] = field(
        default=None,
        metadata={"doc": "An array containing an entry for each field with its value."},
    )
    DataMinerID: Optional[int] = field(
        default=None,
        metadata={"doc": "The DMA ID of the Agent where the ticket was created."},
    )
    ID: Optional[int] = field(default=None, metadata={"doc": "The ID of the ticket."})
    UID: Optional[str] = field(
        default=None,
        metadata={"doc": "The unique GUID identifier of the ticket. Deprecated."},
    )
    TicketTypeID: Optional[str] = field(
        default=None, metadata={"doc": "The GUID of the ticket type."}
    )
    TimeCreatedUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The time when the ticket was created, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )
    LinkFields: Optional[List["DMATicketLinkField"]] = field(
        default=None,
        metadata={
            "doc": "Array containing the linked DataMiner resources. For every DataMiner Object field, it contains a DMATicketLinkField entry with a DMATicketLinkValue array with its linked DataMiner resources."
        },
    )
    StateColor: Optional[str] = field(
        default=None, metadata={"doc": "The color corresponding with the ticket state."}
    )
    IsClosed: Optional[bool] = field(
        default=None, metadata={"doc": "Indicates whether the ticket is closed."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMATicketField(BaseDMAType):
    """
    Represents DMA Ticket Field.

    Attributes:
        Name (Optional[str]): The system name of the field
        DisplayName (Optional[str]): The name of the field that is displayed for the user.
        Type (Optional[TicketFieldType]): The type of field. The following values are possible: "Boolean", "Double", "DateTime", "DataMiner Object", "DropDown", "Email", "Integer", "Text", "Url", "User", or "State".
        PossibleValues (Optional[List[DMATicketFieldPossibleValue]]): In case a field is of a type that allows the user to select different values, this array contains the different values.
        ShowColumnInTicketOverview (Optional[bool]): Determines whether the field is displayed as a column in the Ticketing app.
        SingleSelectionFilter (Optional[bool]): Determines whether it will be possible to use the field as a single selection filter in the Ticketing overview.
        MultiSelectionFilter (Optional[bool]): Determines whether it will be possible to use this field as a multiple selection filter in the Ticketing overview.
        IsRequired (Optional[bool]): Determines whether this field must always be filled in.
        DefaultValue (Optional[str]): The default value of the ticket, if applicable.
        ExternalFieldName (Optional[str]): The name of the corresponding field in a third-party ticketing system, if any.
        IsExternalMaster (Optional[bool]): Determines whether the value found in the DataMiner ticket is kept when it is merged with a ticket from a third-party system.
        AlarmProperty (Optional[str]): The alarm property that the ticket field is linked to.
        CustomAlarmPropertyName (Optional[str]): The custom alarm property that the ticket field is linked to.
        CustomAlarmPropertyType (Optional[str]): The type of custom alarm property (element, view, alarm, etc.) that the field is linked to.
        StaticTextValue (Optional[str]): The static text value assigned to the field, if any.
        Concatenations (Optional[List[DMATicketFieldConcatItem]]): Concatenation of multiple alarm fields and static text, if configured. Note that this requires the CorrelationTicketAction soft-launch flag. See Soft-launch options.
        IsSearchDisplayField (Optional[bool]): Determines whether the field is displayed when users search for tickets.
    """

    Name: Optional[str] = field(
        default=None, metadata={"doc": "The system name of the field"}
    )
    DisplayName: Optional[str] = field(
        default=None,
        metadata={"doc": "The name of the field that is displayed for the user."},
    )
    Type: Optional[TicketFieldType] = field(
        default=None,
        metadata={
            "doc": 'The type of field. The following values are possible: "Boolean", "Double", "DateTime", "DataMiner Object", "DropDown", "Email", "Integer", "Text", "Url", "User", or "State".'
        },
    )
    PossibleValues: Optional[List["DMATicketFieldPossibleValue"]] = field(
        default=None,
        metadata={
            "doc": "In case a field is of a type that allows the user to select different values, this array contains the different values."
        },
    )
    ShowColumnInTicketOverview: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Determines whether the field is displayed as a column in the Ticketing app."
        },
    )
    SingleSelectionFilter: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Determines whether it will be possible to use the field as a single selection filter in the Ticketing overview."
        },
    )
    MultiSelectionFilter: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Determines whether it will be possible to use this field as a multiple selection filter in the Ticketing overview."
        },
    )
    IsRequired: Optional[bool] = field(
        default=None,
        metadata={"doc": "Determines whether this field must always be filled in."},
    )
    DefaultValue: Optional[str] = field(
        default=None,
        metadata={"doc": "The default value of the ticket, if applicable."},
    )
    ExternalFieldName: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The name of the corresponding field in a third-party ticketing system, if any."
        },
    )
    IsExternalMaster: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Determines whether the value found in the DataMiner ticket is kept when it is merged with a ticket from a third-party system."
        },
    )
    AlarmProperty: Optional[str] = field(
        default=None,
        metadata={"doc": "The alarm property that the ticket field is linked to."},
    )
    CustomAlarmPropertyName: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The custom alarm property that the ticket field is linked to."
        },
    )
    CustomAlarmPropertyType: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The type of custom alarm property (element, view, alarm, etc.) that the field is linked to."
        },
    )
    StaticTextValue: Optional[str] = field(
        default=None,
        metadata={"doc": "The static text value assigned to the field, if any."},
    )
    Concatenations: Optional[List["DMATicketFieldConcatItem"]] = field(
        default=None,
        metadata={
            "doc": "Concatenation of multiple alarm fields and static text, if configured. Note that this requires the CorrelationTicketAction soft-launch flag. See Soft-launch options."
        },
    )
    IsSearchDisplayField: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Determines whether the field is displayed when users search for tickets."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMATicketFieldConcatItem(BaseDMAType):
    """
    Represents DMA Ticket Field Concat Item.

    Attributes:
        AlarmProperty (Optional[str]): Defines which alarm property is used in the concatenation.
        CustomAlarmPropertyName (Optional[str]): The custom property name if AlarmProperty = "PropertiesDict".
        CustomAlarmPropertyType (Optional[str]): The type of custom property.
        StaticTextValue (Optional[str]): The static text to use if AlarmProperty = "StaticText".
    """

    # TODO: Enum for AlarmProperty
    AlarmProperty: Optional[str] = field(
        default=None,
        metadata={"doc": "Defines which alarm property is used in the concatenation."},
    )
    CustomAlarmPropertyName: Optional[str] = field(
        default=None,
        metadata={
            "doc": 'The custom property name if AlarmProperty = "PropertiesDict".'
        },
    )
    CustomAlarmPropertyType: Optional[str] = field(
        default=None, metadata={"doc": "The type of custom property."}
    )
    StaticTextValue: Optional[str] = field(
        default=None,
        metadata={"doc": 'The static text to use if AlarmProperty = "StaticText".'},
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMATicketFieldPossibleValue(BaseDMAType):
    """
    Represents DMA Ticket Field Possible Value.

    Attributes:
        Display (Optional[str]): The possible ticket field value displayed to the user.
        Value (Optional[int]): The value of the ticket field value in the database.
    """

    Display: Optional[str] = field(
        default=None,
        metadata={"doc": "The possible ticket field value displayed to the user."},
    )
    Value: Optional[int] = field(
        default=None,
        metadata={"doc": "The value of the ticket field value in the database."},
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMATicketFieldValueDisplay(BaseDMAType):
    """
    Represents DMA Ticket Field Value Display.

    Attributes:
        DisplayName (Optional[str]): The display name of the field.
        Name (Optional[str]): The system name of the field.
        Value (Optional[int]): The value of the ticket field value in the database.
        DisplayValue (Optional[str]): The ticket field value as it is displayed to the user.
        Type (Optional[str]): The type of ticket field.
    """

    DisplayName: Optional[str] = field(
        default=None, metadata={"doc": "The display name of the field."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The system name of the field."}
    )
    Value: Optional[int] = field(
        default=None,
        metadata={"doc": "The value of the ticket field value in the database."},
    )
    DisplayValue: Optional[str] = field(
        default=None,
        metadata={"doc": "The ticket field value as it is displayed to the user."},
    )
    # TODO: Enum for Type
    Type: Optional[str] = field(
        default=None, metadata={"doc": "The type of ticket field."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMATicketLinkField(BaseDMAType):
    """
    Represents DMA Ticket Link Field.

    Attributes:
        Name (Optional[str]): The system name of the field.
        DisplayName (Optional[str]): The display name of the field.
        Values (Optional[List[DMATicketLinkValue]]): Array of the linked DataMiner resources.
    """

    Name: Optional[str] = field(
        default=None, metadata={"doc": "The system name of the field."}
    )
    DisplayName: Optional[str] = field(
        default=None, metadata={"doc": "The display name of the field."}
    )
    Values: Optional[List["DMATicketLinkValue"]] = field(
        default=None, metadata={"doc": "Array of the linked DataMiner resources."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMATicketLinkValue(BaseDMAType):
    """
    Represents DMA Ticket Link Value.

    Attributes:
        Type (Optional[ResourceType]): The type of DataMiner resource: "Element", "Service", "Redundancy Group", "Alarm", or "View".
        Value (Optional[List[int]]): The DataMiner ID and resource ID.
    """

    Type: Optional[ResourceType] = field(
        default=None,
        metadata={
            "doc": 'The type of DataMiner resource: "Element", "Service", "Redundancy Group", "Alarm", or "View".'
        },
    )
    Value: Optional[List[int]] = field(
        default=None, metadata={"doc": "The DataMiner ID and resource ID."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMATicketType(BaseDMAType):
    """
    Represents DMA Ticket Type.

    Attributes:
        Name (Optional[str]): The name of the ticket type.
        ID (Optional[str]): The GUID of the ticket type.
        IsMasked (Optional[bool]): Indicates whether the ticket type is masked.
        UsedExternal (Optional[bool]): Indicates whether the ticket type is used by a third-party ticketing system.
    """

    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the ticket type."}
    )
    ID: Optional[str] = field(
        default=None, metadata={"doc": "The GUID of the ticket type."}
    )
    IsMasked: Optional[bool] = field(
        default=None, metadata={"doc": "Indicates whether the ticket type is masked."}
    )
    UsedExternal: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the ticket type is used by a third-party ticketing system."
        },
    )
