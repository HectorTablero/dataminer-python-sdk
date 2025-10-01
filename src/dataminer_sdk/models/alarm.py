from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List, TYPE_CHECKING
from dataminer_sdk.models.base import BaseDMAType

if TYPE_CHECKING:
    from dataminer_sdk.models.misc import DMAColor, DMAObject
    from dataminer_sdk.models.property import DMAProperty
    from dataminer_sdk.models.trend import DMABaseline
    from dataminer_sdk.models.parameter import DMAHysteresisInfo
    from dataminer_sdk.models.enums import DMAComparerType, AlarmStateType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmFilterItem(BaseDMAType):
    """
    Represents DMA Alarm Filter Item.

    Attributes:
        Match (Optional[bool]): Set to True by default, but can be set to False for a negative filter.
    """

    Match: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Set to True by default, but can be set to False for a negative filter."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmFilterConstant(DMAAlarmFilterItem):
    """
    Represents DMA Alarm Filter Constant.
    """

    pass


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmFilterAll(DMAAlarmFilterItem):
    """
    Represents DMA Alarm Filter All.
    """

    pass


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmFilterAny(DMAAlarmFilterItem):
    """
    Represents DMA Alarm Filter Any.
    """

    pass


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmFilterStatus(DMAAlarmFilterItem):
    """
    Represents DMA Alarm Filter Status.

    Attributes:
        States (Optional[List[str]]): The states.
    """

    States: Optional[List[str]] = field(default=None, metadata={"doc": "The states."})


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmFilterSeverity(DMAAlarmFilterItem):
    """
    Represents DMA Alarm Filter Severity.

    Attributes:
        Severities (Optional[List[str]]): The severities.
    """

    Severities: Optional[List[str]] = field(
        default=None, metadata={"doc": "The severities."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmFilterAlarmType(DMAAlarmFilterItem):
    """
    Represents DMA Alarm Filter Alarm Type.

    Attributes:
        Types (Optional[List[str]]): The types.
    """

    Types: Optional[List[str]] = field(default=None, metadata={"doc": "The types."})


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmFilterView(DMAAlarmFilterItem):
    """
    Represents DMA Alarm Filter View.

    Attributes:
        ViewID (Optional[int]): The view ID.
    """

    ViewID: Optional[int] = field(default=None, metadata={"doc": "The view ID."})


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmFilterDataMiner(DMAAlarmFilterItem):
    """
    Represents DMA Alarm Filter DataMiner.

    Attributes:
        DataMinerID (Optional[int]): The DataMiner ID.
    """

    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The DataMiner ID."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmFilterService(DMAAlarmFilterItem):
    """
    Represents DMA Alarm Filter Service.

    Attributes:
        DataMinerID (Optional[int]): The DataMiner ID.
        ServiceID (Optional[int]): The service ID.
    """

    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The DataMiner ID."}
    )
    ServiceID: Optional[int] = field(default=None, metadata={"doc": "The service ID."})


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmFilterElement(DMAAlarmFilterItem):
    """
    Represents DMA Alarm Filter Element.

    Attributes:
        DataMinerID (Optional[int]): The DataMiner ID.
        ElementID (Optional[int]): The element ID.
    """

    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The DataMiner ID."}
    )
    ElementID: Optional[int] = field(default=None, metadata={"doc": "The element ID."})


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmFilterParameter(DMAAlarmFilterItem):
    """
    Represents DMA Alarm Filter Parameter.

    Attributes:
        DataMinerID (Optional[int]): The DataMiner ID.
        ElementID (Optional[int]): The element ID.
        ParameterID (Optional[int]): The parameter ID.
        TableIndex (Optional[str]): The table index.
    """

    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The DataMiner ID."}
    )
    ElementID: Optional[int] = field(default=None, metadata={"doc": "The element ID."})
    ParameterID: Optional[int] = field(
        default=None, metadata={"doc": "The parameter ID."}
    )
    TableIndex: Optional[str] = field(
        default=None, metadata={"doc": "The table index."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmFilterSavedFilter(DMAAlarmFilterItem):
    """
    Represents DMA Alarm Filter Saved Filter.

    Attributes:
        Filter (Optional[str]): The filter.
    """

    Filter: Optional[str] = field(default=None, metadata={"doc": "The filter."})


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmTemplateConditionRule(BaseDMAType):
    """
    Represents DMA Alarm Template Condition Rule.

    Attributes:
        ParameterID (Optional[int]): The ID of the parameter used in the rule.
        Comparer (Optional[DMAComparerType]): One of the following values: - Equals = 0, - NotEquals = 1 - LessThan = 2 - GreaterThan = 3 - WildcardEquals = 4 - WildcardNotEquals = 5
        Value (Optional[str]): The value the parameter is compared with.
    """

    ParameterID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the parameter used in the rule."}
    )
    Comparer: Optional[DMAComparerType] = field(
        default=None,
        metadata={
            "doc": "One of the following values: - Equals = 0, - NotEquals = 1 - LessThan = 2 - GreaterThan = 3 - WildcardEquals = 4 - WildcardNotEquals = 5"
        },
    )
    Value: Optional[str] = field(
        default=None, metadata={"doc": "The value the parameter is compared with."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmTemplateGroupEntry(BaseDMAType):
    """
    Represents DMA Alarm Template Group Entry.

    Attributes:
        Name (Optional[str]): The name of the alarm template that is part of the alarm template group.
        IsEnabled (Optional[bool]): Whether the alarm template is enabled.
        IsScheduled (Optional[bool]): Whether the alarm template is scheduled.
    """

    Name: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The name of the alarm template that is part of the alarm template group."
        },
    )
    IsEnabled: Optional[bool] = field(
        default=None, metadata={"doc": "Whether the alarm template is enabled."}
    )
    IsScheduled: Optional[bool] = field(
        default=None, metadata={"doc": "Whether the alarm template is scheduled."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmTemplateScheduleEntry(BaseDMAType):
    """
    Represents DMA Alarm Template Schedule Entry.

    Attributes:
        Day (Optional[str]): The day of the week to which the schedule entry applies: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday.
        From (Optional[str]): The time when the schedule entry begins.
        To (Optional[str]): The time when the schedule entry ends.
    """

    Day: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The day of the week to which the schedule entry applies: Sunday, Monday, Tuesday, Wednesday, Thursday, Friday or Saturday."
        },
    )
    From: Optional[str] = field(
        default=None, metadata={"doc": "The time when the schedule entry begins."}
    )
    To: Optional[str] = field(
        default=None, metadata={"doc": "The time when the schedule entry ends."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAKeyValuePair(BaseDMAType):
    """
    Represents a DMA Key Value Pair.

    Attributes:
        Key (Optional[AlarmStateType]): The key.
        Value (Optional[str]): The value.
    """

    Key: Optional[AlarmStateType] = field(default=None, metadata={"doc": "The key."})
    Value: Optional[str] = field(default=None, metadata={"doc": "The value."})


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmColors(BaseDMAType):
    """
    Represents DMA Alarm Colors.

    Attributes:
        Critical (Optional[DMAColor]): The color used for critical alarms.
        Error (Optional[DMAColor]): The color used for errors.
        Information (Optional[DMAColor]): The color used for information events.
        Initial (Optional[DMAColor]): The color used for initial parameter values.
        Major (Optional[DMAColor]): The color used for major alarms.
        Masked (Optional[DMAColor]): The color used for masked alarms.
        Minor (Optional[DMAColor]): The color used for minor alarms.
        Normal (Optional[DMAColor]): The color used for normal parameter values.
        Notice (Optional[DMAColor]): The color used for notices.
        NotMonitored (Optional[DMAColor]): The color used for values of parameters that are not monitored.
        Timeout (Optional[DMAColor]): The color used for timeouts.
        Undefined (Optional[DMAColor]): The color used for undefined values.
        Warning (Optional[DMAColor]): The color used for warnings.
        LastChangeUTC (Optional[int]): The time when the object was last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT).
    """

    Critical: Optional[DMAColor] = field(
        default=None, metadata={"doc": "The color used for critical alarms."}
    )
    Error: Optional[DMAColor] = field(
        default=None, metadata={"doc": "The color used for errors."}
    )
    Information: Optional[DMAColor] = field(
        default=None, metadata={"doc": "The color used for information events."}
    )
    Initial: Optional[DMAColor] = field(
        default=None, metadata={"doc": "The color used for initial parameter values."}
    )
    Major: Optional[DMAColor] = field(
        default=None, metadata={"doc": "The color used for major alarms."}
    )
    Masked: Optional[DMAColor] = field(
        default=None, metadata={"doc": "The color used for masked alarms."}
    )
    Minor: Optional[DMAColor] = field(
        default=None, metadata={"doc": "The color used for minor alarms."}
    )
    Normal: Optional[DMAColor] = field(
        default=None, metadata={"doc": "The color used for normal parameter values."}
    )
    Notice: Optional[DMAColor] = field(
        default=None, metadata={"doc": "The color used for notices."}
    )
    NotMonitored: Optional[DMAColor] = field(
        default=None,
        metadata={
            "doc": "The color used for values of parameters that are not monitored."
        },
    )
    Timeout: Optional[DMAColor] = field(
        default=None, metadata={"doc": "The color used for timeouts."}
    )
    Undefined: Optional[DMAColor] = field(
        default=None, metadata={"doc": "The color used for undefined values."}
    )
    Warning: Optional[DMAColor] = field(
        default=None, metadata={"doc": "The color used for warnings."}
    )
    LastChangeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The time when the object was last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmCountData(BaseDMAType):
    """
    Represents DMA Alarm Count Data.

    Attributes:
        Normal (Optional[int]): The number of alarms with severity "normal".
        Warning (Optional[int]): The number of alarms with severity "warning".
        Minor (Optional[int]): The number of alarms with severity "minor".
        Major (Optional[int]): The number of alarms with severity "major".
        Critical (Optional[int]): The number of alarms with severity "critical".
        Timeout (Optional[int]): The number of alarms with severity "timeout".
    """

    Normal: Optional[int] = field(
        default=None, metadata={"doc": 'The number of alarms with severity "normal".'}
    )
    Warning: Optional[int] = field(
        default=None, metadata={"doc": 'The number of alarms with severity "warning".'}
    )
    Minor: Optional[int] = field(
        default=None, metadata={"doc": 'The number of alarms with severity "minor".'}
    )
    Major: Optional[int] = field(
        default=None, metadata={"doc": 'The number of alarms with severity "major".'}
    )
    Critical: Optional[int] = field(
        default=None, metadata={"doc": 'The number of alarms with severity "critical".'}
    )
    Timeout: Optional[int] = field(
        default=None, metadata={"doc": 'The number of alarms with severity "timeout".'}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmDetails(BaseDMAType):
    """
    Represents DMA Alarm Details.

    Attributes:
        Category (Optional[str]): Custom category that can be assigned to a parameter using the information template.
        CorrectiveAction (Optional[str]): Description of corrective actions that should be taken, which can be customized with the information template.
        ComponentInfo (Optional[str]): Information on the nature of the alarm. Used in DMS Business Intelligence.
        Comments (Optional[str]): Comments that have been added to the alarm, either by DataMiner users or by the system.
        KeyPoint (Optional[str]): The exact location in the signal chain where the error has occurred. Used in DMS Business Intelligence.
        OfflineImpact (Optional[str]): Indicates whether the alarm has an impact during the offline window of an SLA. Used in DMS Business Intelligence.
        AffectedView (Optional[DMAObject]): The DataMiner ID, ID and name of the view affected by the alarm.
        AffectedServices (Optional[List[DMAObject]]): The DataMiner ID, ID and name of the services affected by the alarm.
        AffectedVirtualFunctions (Optional[List[DMAObject]]): The DataMiner ID, ID and name of the virtual functions affected by the alarm.
        PropertiesAlarm (Optional[List[DMAProperty]]): The properties of the alarm.
        PropertiesElement (Optional[List[DMAProperty]]): The properties of the affected element.
        PropertiesService (Optional[List[DMAProperty]]): The properties of the affected service(s).
        PropertiesView (Optional[List[DMAProperty]]): The properties of the affected view.
        PropertiesProtocol (Optional[List[DMAProperty]]): The properties of the affected protocol.
    """

    Category: Optional[str] = field(
        default=None,
        metadata={
            "doc": "Custom category that can be assigned to a parameter using the information template."
        },
    )
    CorrectiveAction: Optional[str] = field(
        default=None,
        metadata={
            "doc": "Description of corrective actions that should be taken, which can be customized with the information template."
        },
    )
    ComponentInfo: Optional[str] = field(
        default=None,
        metadata={
            "doc": "Information on the nature of the alarm. Used in DMS Business Intelligence."
        },
    )
    Comments: Optional[str] = field(
        default=None,
        metadata={
            "doc": "Comments that have been added to the alarm, either by DataMiner users or by the system."
        },
    )
    KeyPoint: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The exact location in the signal chain where the error has occurred. Used in DMS Business Intelligence."
        },
    )
    OfflineImpact: Optional[str] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the alarm has an impact during the offline window of an SLA. Used in DMS Business Intelligence."
        },
    )
    AffectedView: Optional[DMAObject] = field(
        default=None,
        metadata={
            "doc": "The DataMiner ID, ID and name of the view affected by the alarm."
        },
    )
    AffectedServices: Optional[List[DMAObject]] = field(
        default=None,
        metadata={
            "doc": "The DataMiner ID, ID and name of the services affected by the alarm."
        },
    )
    AffectedVirtualFunctions: Optional[List[DMAObject]] = field(
        default=None,
        metadata={
            "doc": "The DataMiner ID, ID and name of the virtual functions affected by the alarm."
        },
    )
    PropertiesAlarm: Optional[List[DMAProperty]] = field(
        default=None, metadata={"doc": "The properties of the alarm."}
    )
    PropertiesElement: Optional[List[DMAProperty]] = field(
        default=None, metadata={"doc": "The properties of the affected element."}
    )
    PropertiesService: Optional[List[DMAProperty]] = field(
        default=None, metadata={"doc": "The properties of the affected service(s)."}
    )
    PropertiesView: Optional[List[DMAProperty]] = field(
        default=None, metadata={"doc": "The properties of the affected view."}
    )
    PropertiesProtocol: Optional[List[DMAProperty]] = field(
        default=None, metadata={"doc": "The properties of the affected protocol."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmFilterV2(BaseDMAType):
    """
    Represents DMA Alarm Filter V2.

    Attributes:
        History (Optional[bool]): Set to True to retrieve history alarms. By default set to False, so only active alarms are retrieved.
        SlidingWindow (Optional[bool]): Set to True to retrieve alarms in a sliding window.
        FilterItem (Optional[DMAAlarmFilterItem]): See DMAAlarmFilterItem.
        StartTime (Optional[int]): The start time, indicated as milliseconds since the Unix epoch. Only alarms newer than this UTC timestamp are retrieved.
        EndTime (Optional[int]): The end time, indicated as milliseconds since the Unix epoch. Only alarms older than this UTC timestamp are retrieved.
        Masked (Optional[bool]): Set to true to retrieve masked alarms. (Default: false.)
        InfoEvents (Optional[bool]): Set to true to retrieve information events. (Default: false.)
        FullAlarmTree (Optional[bool]): Set to true to include the full alarm tree. By default set to false, so only the top-level alarms are retrieved.
        Columns (Optional[List[str]]): Can contain one or more of the following values, corresponding to Alarm Console columns: - status - comment - source - creation time - root creation time - category - description - corrective action - component info - key point - offline impact - interface impact - interfaces - view impact - views - function impact - functions - alarm.propertyname (propertyname being the name of the alarm property) - element.propertyname (propertyname being the name of the element property) - service.propertyname (propertyname being the name of the service property) - view.propertyname (propertyname being the name of the view property) - protocol.propertyname (propertyname being the name of the protocol property)
        Limit (Optional[int]): The maximum number of alarms to include. (By default: 100.)
        SortBy (Optional[List[str]]): The field(s) by which the alarms should be sorted.
        SortAscending (Optional[bool]): Determines whether alarms should be sorted in ascending or descending order.
        Search (Optional[str]): An additional search string that will be applied on top of the alarm filter specified in FilterItem.
    """

    History: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Set to True to retrieve history alarms. By default set to False, so only active alarms are retrieved."
        },
    )
    SlidingWindow: Optional[bool] = field(
        default=None,
        metadata={"doc": "Set to True to retrieve alarms in a sliding window."},
    )
    FilterItem: Optional[DMAAlarmFilterItem] = field(
        default=None, metadata={"doc": "See DMAAlarmFilterItem."}
    )
    StartTime: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The start time, indicated as milliseconds since the Unix epoch. Only alarms newer than this UTC timestamp are retrieved."
        },
    )
    EndTime: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The end time, indicated as milliseconds since the Unix epoch. Only alarms older than this UTC timestamp are retrieved."
        },
    )
    Masked: Optional[bool] = field(
        default=None,
        metadata={"doc": "Set to true to retrieve masked alarms. (Default: false.)"},
    )
    InfoEvents: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Set to true to retrieve information events. (Default: false.)"
        },
    )
    FullAlarmTree: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Set to true to include the full alarm tree. By default set to false, so only the top-level alarms are retrieved."
        },
    )
    Columns: Optional[List[str]] = field(
        default=None,
        metadata={
            "doc": "Can contain one or more of the following values, corresponding to Alarm Console columns: - status - comment - source - creation time - root creation time - category - description - corrective action - component info - key point - offline impact - interface impact - interfaces - view impact - views - function impact - functions - alarm.propertyname (propertyname being the name of the alarm property) - element.propertyname (propertyname being the name of the element property) - service.propertyname (propertyname being the name of the service property) - view.propertyname (propertyname being the name of the view property) - protocol.propertyname (propertyname being the name of the protocol property)"
        },
    )
    Limit: Optional[int] = field(
        default=None,
        metadata={"doc": "The maximum number of alarms to include. (By default: 100.)"},
    )
    SortBy: Optional[List[str]] = field(
        default=None,
        metadata={"doc": "The field(s) by which the alarms should be sorted."},
    )
    SortAscending: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Determines whether alarms should be sorted in ascending or descending order."
        },
    )
    Search: Optional[str] = field(
        default=None,
        metadata={
            "doc": "An additional search string that will be applied on top of the alarm filter specified in FilterItem."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmPage(BaseDMAType):
    """
    Represents DMA Alarm Page.

    Attributes:
        Index (Optional[int]): The index of the page.
        Name (Optional[str]): User-friendly display title of the page, e.g. "Today", "4 weeks ago" or "Last month" when grouped on Time, or "Critical", "Warning", "Timeout", etc. when grouped on Severity
        Amount (Optional[int]): The number of alarms matching the input filter.
        AlarmState (Optional[AlarmStateType]): The highest alarm level of the alarms matching the input filter.
        Filter (Optional[List]): See DMAAlarmFilterV2.
        AlarmStates (Optional[List[DMAKeyValuePair]]): DMAKeyValuePair objects, containing the severity as Key and the number of alarms with that severity as Value.
    """

    Index: Optional[int] = field(
        default=None, metadata={"doc": "The index of the page."}
    )
    Name: Optional[str] = field(
        default=None,
        metadata={
            "doc": 'User-friendly display title of the page, e.g. "Today", "4 weeks ago" or "Last month" when grouped on Time, or "Critical", "Warning", "Timeout", etc. when grouped on Severity'
        },
    )
    Amount: Optional[int] = field(
        default=None,
        metadata={"doc": "The number of alarms matching the input filter."},
    )
    AlarmState: Optional[AlarmStateType] = field(
        default=None,
        metadata={
            "doc": "The highest alarm level of the alarms matching the input filter."
        },
    )
    Filter: Optional[List[DMAAlarmFilterV2]] = field(
        default=None, metadata={"doc": "See DMAAlarmFilterV2."}
    )
    AlarmStates: Optional[List[DMAKeyValuePair]] = field(
        default=None,
        metadata={
            "doc": "DMAKeyValuePair objects, containing the severity as Key and the number of alarms with that severity as Value."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmPageUpdate(BaseDMAType):
    """
    Represents DMA Alarm Page Update.

    Attributes:
        Index (Optional[int]): The index of the corresponding input filter (required when using WebSocket updates).
        Amount (Optional[int]): The number of alarms matching the input filter.
        AlarmState (Optional[str]): The highest alarm level of the alarms matching the input filter.
    """

    Index: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The index of the corresponding input filter (required when using WebSocket updates)."
        },
    )
    Amount: Optional[int] = field(
        default=None,
        metadata={"doc": "The number of alarms matching the input filter."},
    )
    AlarmState: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The highest alarm level of the alarms matching the input filter."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmStateData(BaseDMAType):
    """
    Represents DMA Alarm State Data.

    Attributes:
        Normal (Optional[float]): The relative duration of the "normal" alarm state.
        Warning (Optional[float]): The relative duration of the "warning" alarm state.
        Minor (Optional[float]): The relative duration of the "minor" alarm state.
        Major (Optional[float]): The relative duration of the "major" alarm state.
        Critical (Optional[float]): The relative duration of the "critical" alarm state.
        Timeout (Optional[float]): The relative duration of the "timeout" alarm state.
        NotMonitored (Optional[float]): The relative duration of the "not monitored" alarm state.
        Undefined (Optional[float]): The relative duration of the "undefined" alarm state.
    """

    Normal: Optional[float] = field(
        default=None,
        metadata={"doc": 'The relative duration of the "normal" alarm state.'},
    )
    Warning: Optional[float] = field(
        default=None,
        metadata={"doc": 'The relative duration of the "warning" alarm state.'},
    )
    Minor: Optional[float] = field(
        default=None,
        metadata={"doc": 'The relative duration of the "minor" alarm state.'},
    )
    Major: Optional[float] = field(
        default=None,
        metadata={"doc": 'The relative duration of the "major" alarm state.'},
    )
    Critical: Optional[float] = field(
        default=None,
        metadata={"doc": 'The relative duration of the "critical" alarm state.'},
    )
    Timeout: Optional[float] = field(
        default=None,
        metadata={"doc": 'The relative duration of the "timeout" alarm state.'},
    )
    NotMonitored: Optional[float] = field(
        default=None,
        metadata={"doc": 'The relative duration of the "not monitored" alarm state.'},
    )
    Undefined: Optional[float] = field(
        default=None,
        metadata={"doc": 'The relative duration of the "undefined" alarm state.'},
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmTemplate(BaseDMAType):
    """
    Represents DMA Alarm Template.

    Attributes:
        Name (Optional[str]): The name of the alarm template.
        ProtocolName (Optional[str]): The name of the protocol to which the alarm template is applied.
        ProtocolVersion (Optional[str]): The version of the protocol to which the alarm template is applied.
        Description (Optional[str]): The description of the alarm template.
        IsScheduleEnabled (Optional[bool]): Whether an alarm template schedule is enabled.
        Type (Optional[str]): Template in case of a regular alarm template, Group in case of an alarm template group.
        IsUsedInGroup (Optional[bool]): Whether the alarm template is used in a group.
        Conditions (Optional[List[DMAAlarmTemplateCondition]]): See DMAAlarmTemplateCondition.
        Parameters (Optional[List[DMAAlarmTemplateParameter]]): See DMAAlarmTemplateParameter.
        GroupEntries (Optional[List[DMAAlarmTemplateGroupEntry]]): See DMAAlarmTemplateGroupEntry.
        Schedule (Optional[List[DMAAlarmTemplateScheduleEntry]]): See DMAAlarmTemplateScheduleEntry.
    """

    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the alarm template."}
    )
    ProtocolName: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The name of the protocol to which the alarm template is applied."
        },
    )
    ProtocolVersion: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The version of the protocol to which the alarm template is applied."
        },
    )
    Description: Optional[str] = field(
        default=None, metadata={"doc": "The description of the alarm template."}
    )
    IsScheduleEnabled: Optional[bool] = field(
        default=None, metadata={"doc": "Whether an alarm template schedule is enabled."}
    )
    Type: Optional[str] = field(
        default=None,
        metadata={
            "doc": "Template in case of a regular alarm template, Group in case of an alarm template group."
        },
    )
    IsUsedInGroup: Optional[bool] = field(
        default=None, metadata={"doc": "Whether the alarm template is used in a group."}
    )
    Conditions: Optional[List["DMAAlarmTemplateCondition"]] = field(
        default=None, metadata={"doc": "See DMAAlarmTemplateCondition."}
    )
    Parameters: Optional[List["DMAAlarmTemplateParameter"]] = field(
        default=None, metadata={"doc": "See DMAAlarmTemplateParameter."}
    )
    GroupEntries: Optional[List["DMAAlarmTemplateGroupEntry"]] = field(
        default=None, metadata={"doc": "See DMAAlarmTemplateGroupEntry."}
    )
    Schedule: Optional[List["DMAAlarmTemplateScheduleEntry"]] = field(
        default=None, metadata={"doc": "See DMAAlarmTemplateScheduleEntry."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmTemplateCondition(BaseDMAType):
    """
    Represents DMA Alarm Template Condition.

    Attributes:
        ID (Optional[int]): The ID of the condition.
        Rules (Optional[List[DMAAlarmTemplateConditionRule]]): See DMAAlarmTemplateConditionRule.
        Name (Optional[str]): The name of the condition.
    """

    ID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the condition."}
    )
    Rules: Optional[List["DMAAlarmTemplateConditionRule"]] = field(
        default=None, metadata={"doc": "See DMAAlarmTemplateConditionRule."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the condition."}
    )

@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarm(BaseDMAType):
    """
    Represents a DataMiner Alarm object.

    This is a read-only snapshot of an alarm at a specific time.

    Attributes:
        DataMinerID (Optional[int]): The ID of the DataMiner Agent where the element was created.
        HostingAgentID (Optional[int]): The ID of the DataMiner Agent that is currently hosting the element.
        ID (Optional[int]): The ID of the alarm.
        RootAlarmID (Optional[int]): The ID of the root alarm (i.e. the first alarm in the alarm tree).
        ElementID (Optional[int]): The ID of the element.
        ElementName (Optional[str]): The name of the element.
        IsElementMasked (Optional[bool]): Whether or not the element is masked.
        ParameterID (Optional[int]): The ID of the parameter.
        ParameterName (Optional[str]): The name of the parameter.
        TableIndex (Optional[str]): The table index (if the parameter is a table parameter).
        DisplayValue (Optional[str]): The display value (if the parameter is a table parameter).
        AlarmState (Optional[AlarmStateType]): The current state of the alarm.
        Type (Optional[str]): The type of alarm (e.g. “New Alarm”, “Escalated From Warning”).
        IsAggregation (Optional[bool]): Whether the alarm originates from an aggregation element.
        IsMasked (Optional[bool]): Whether or not the alarm is masked.
        Services (Optional[List[str]]): The names of the services affected by the alarm.
        TimeOfArrival (Optional[str]): The time the alarm was created (local time).
        TimeOfArrivalUTC (Optional[int]): UTC timestamp (ms since epoch) of alarm creation.
        RootTime (Optional[str]): Local time of the first alarm in the alarm tree.
        RootTimeUTC (Optional[int]): UTC timestamp (ms since epoch) of first alarm.
        IsTrending (Optional[bool]): Whether the parameter is being trended.
        IsOwner (Optional[bool]): Whether someone has taken ownership of the alarm.
        OwnerName (Optional[str]): The name of the person who owns the alarm.
        LastChangeUTC (Optional[int]): UTC timestamp (ms since epoch) of the last alarm change.
        IsCleared (Optional[bool]): Whether the alarm is cleared.
    """

    DataMinerID: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The ID of the DataMiner Agent where the element was created."
        },
    )
    HostingAgentID: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The ID of the DataMiner Agent that is currently hosting the element."
        },
    )
    ID: Optional[int] = field(default=None, metadata={"doc": "The ID of the alarm."})
    RootAlarmID: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The ID of the root alarm (i.e. the first alarm in the alarm tree)."
        },
    )
    ElementID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the element."}
    )
    ElementName: Optional[str] = field(
        default=None, metadata={"doc": "The name of the element."}
    )
    IsElementMasked: Optional[bool] = field(
        default=None, metadata={"doc": "Whether or not the element is masked."}
    )
    ParameterID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the parameter."}
    )
    ParameterName: Optional[str] = field(
        default=None, metadata={"doc": "The name of the parameter."}
    )
    TableIndex: Optional[str] = field(
        default=None,
        metadata={"doc": "The table index (if the parameter is a table parameter)."},
    )
    DisplayValue: Optional[str] = field(
        default=None,
        metadata={"doc": "The display value (if the parameter is a table parameter)."},
    )
    AlarmState: Optional[AlarmStateType] = field(
        default=None, metadata={"doc": "The current state of the alarm."}
    )
    # TODO: Convert to Enum
    Type: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The type of alarm (e.g. “New Alarm”, “Escalated From Warning”)."
        },
    )
    IsAggregation: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether the alarm originates from an aggregation element."},
    )
    IsMasked: Optional[bool] = field(
        default=None, metadata={"doc": "Whether or not the alarm is masked."}
    )
    Services: Optional[List[str]] = field(
        default=None,
        metadata={"doc": "The names of the services affected by the alarm."},
    )
    TimeOfArrival: Optional[str] = field(
        default=None,
        metadata={
            "doc": "Local time the alarm was created.",
            "example": "2014-05-14 08:56:17",
        },
    )
    TimeOfArrivalUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "UTC timestamp (ms since epoch) when the alarm was created.",
            "example": 1400050577000,
        },
    )
    RootTime: Optional[str] = field(
        default=None,
        metadata={
            "doc": "Local time of the very first alarm in the alarm tree.",
            "example": "2014-05-14 08:46:27",
        },
    )
    RootTimeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "UTC timestamp (ms since epoch) of the first alarm in the tree.",
            "example": 1400049987000,
        },
    )
    IsTrending: Optional[bool] = field(
        default=None, metadata={"doc": "Whether or not the parameter is being trended."}
    )
    IsOwner: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not someone has taken ownership of the alarm."},
    )
    OwnerName: Optional[str] = field(
        default=None,
        metadata={"doc": "The name of the person who currently owns the alarm."},
    )
    LastChangeUTC: Optional[int] = field(
        default=None,
        metadata={"doc": "UTC timestamp (ms since epoch) when the alarm last changed."},
    )
    IsCleared: Optional[bool] = field(
        default=None, metadata={"doc": "Whether the alarm is cleared."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAlarmTemplateParameter(BaseDMAType):
    """
    Represents DMA Alarm Template Parameter.

    Attributes:
        ID (Optional[int]): The ID of the parameter.
        Filter (Optional[str]): The filter applied to the parameter, if any.
        Info (Optional[str]): The threshold defined for information messages, if any.
        Hysteresis (Optional[str]): The defined alarm hysteresis.
        CL (Optional[str]): The Critical Low alarm threshold.
        MaL (Optional[str]): The Major Low alarm threshold.
        MiL (Optional[str]): The Minor Low alarm threshold.
        Normal (Optional[str]): The Normal alarm threshold.
        WaH (Optional[str]): The Warning High alarm threshold.
        MiH (Optional[str]): The Minor High alarm threshold.
        MaH (Optional[str]): The Major High alarm threshold.
        CH (Optional[str]): The Critical High alarm threshold.
        Monitored (Optional[bool]): Whether the parameter is included or excluded in alarm template groups.
        WaL (Optional[str]): The Warning Low alarm threshold.
        VarianceMonitor (Optional[bool]): Whether alarms for variance changes are enabled. Obsolete from DataMiner 10.3.12/10.4.0 onwards.
        TrendMonitor (Optional[bool]): Whether alarms for trend changes are enabled. Obsolete from DataMiner 10.3.12/10.4.0 onwards.
        LevelShiftMonitor (Optional[bool]): Whether alarms for level shift anomalies are enabled. Obsolete from DataMiner 10.3.12/10.4.0 onwards.
        FlatlineMonitor (Optional[bool]): Whether alarms for flatline anomalies are enabled. Obsolete from DataMiner 10.3.12/10.4.0 onwards.
        HysteresisPerSeverity (Optional[DMAHysteresisInfo]): See DMAHysteresisInfo.
        SmartBaseLine (Optional[DMABaseline]): See DMABaseline.
        DisabledIf (Optional[str]): A condition that determines when monitoring is disabled.
        AutoClear (Optional[str]): The type of automatic clearing: False (= no autoclear), True (= autoclear) or Undef (= the system default is applied).
        Type (Optional[str]): The type of alarm thresholds: NORMAL, RELATIVE, ABSOLUTE, RATE or DISCRETE.
    """

    ID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the parameter."}
    )
    Filter: Optional[str] = field(
        default=None, metadata={"doc": "The filter applied to the parameter, if any."}
    )
    Info: Optional[str] = field(
        default=None,
        metadata={"doc": "The threshold defined for information messages, if any."},
    )
    Hysteresis: Optional[str] = field(
        default=None, metadata={"doc": "The defined alarm hysteresis."}
    )
    CL: Optional[str] = field(
        default=None, metadata={"doc": "The Critical Low alarm threshold."}
    )
    MaL: Optional[str] = field(
        default=None, metadata={"doc": "The Major Low alarm threshold."}
    )
    MiL: Optional[str] = field(
        default=None, metadata={"doc": "The Minor Low alarm threshold."}
    )
    Normal: Optional[str] = field(
        default=None, metadata={"doc": "The Normal alarm threshold."}
    )
    WaH: Optional[str] = field(
        default=None, metadata={"doc": "The Warning High alarm threshold."}
    )
    MiH: Optional[str] = field(
        default=None, metadata={"doc": "The Minor High alarm threshold."}
    )
    MaH: Optional[str] = field(
        default=None, metadata={"doc": "The Major High alarm threshold."}
    )
    CH: Optional[str] = field(
        default=None, metadata={"doc": "The Critical High alarm threshold."}
    )
    Monitored: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether the parameter is included or excluded in alarm template groups."
        },
    )
    WaL: Optional[str] = field(
        default=None, metadata={"doc": "The Warning Low alarm threshold."}
    )
    VarianceMonitor: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether alarms for variance changes are enabled. Obsolete from DataMiner 10.3.12/10.4.0 onwards."
        },
    )
    TrendMonitor: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether alarms for trend changes are enabled. Obsolete from DataMiner 10.3.12/10.4.0 onwards."
        },
    )
    LevelShiftMonitor: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether alarms for level shift anomalies are enabled. Obsolete from DataMiner 10.3.12/10.4.0 onwards."
        },
    )
    FlatlineMonitor: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether alarms for flatline anomalies are enabled. Obsolete from DataMiner 10.3.12/10.4.0 onwards."
        },
    )
    HysteresisPerSeverity: Optional[DMAHysteresisInfo] = field(
        default=None, metadata={"doc": "See DMAHysteresisInfo."}
    )
    SmartBaseLine: Optional[DMABaseline] = field(
        default=None, metadata={"doc": "See DMABaseline."}
    )
    DisabledIf: Optional[str] = field(
        default=None,
        metadata={"doc": "A condition that determines when monitoring is disabled."},
    )
    AutoClear: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The type of automatic clearing: False (= no autoclear), True (= autoclear) or Undef (= the system default is applied)."
        },
    )
    Type: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The type of alarm thresholds: NORMAL, RELATIVE, ABSOLUTE, RATE or DISCRETE."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMATopAlarmCountData(BaseDMAType):
    """
    Represents DMA Top Alarm Count Data.

    Attributes:
        Object (Optional[DMAObject]): The DataMiner ID, ID and name of the object.
    """

    Object: Optional[DMAObject] = field(
        default=None, metadata={"doc": "The DataMiner ID, ID and name of the object."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMATopAlarmStateData(BaseDMAType):
    """
    Represents DMA Top Alarm State Data.

    Attributes:
        Object (Optional[DMAObject]): The DataMiner ID, ID and name of the object.
    """

    Object: Optional[DMAObject] = field(
        default=None, metadata={"doc": "The DataMiner ID, ID and name of the object."}
    )
