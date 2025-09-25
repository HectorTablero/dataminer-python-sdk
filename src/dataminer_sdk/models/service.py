from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List, Dict, Any, TYPE_CHECKING
from dataminer_sdk.models.base import BaseDMAType
from dataminer_sdk.models.enums import (
    AlarmStateType,
    ParameterType,
    ServiceConfigurationTriggerType,
    ServiceConfigurationTriggerConditionType,
    ServiceDefinitionType,
    ServiceTemplateGlobalConditionType,
    ServiceTemplateMissingDataType,
)

if TYPE_CHECKING:
    from dataminer_sdk.models.parameter import (
        DMAParameterEditDiscreet,
        DMAParameterPosition,
    )
    from dataminer_sdk.models.protocol import DMAFunctionDefinitionLite
    from dataminer_sdk.models.resource import DMAResource


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAServiceConfiguration(BaseDMAType):
    """
    Represents DMA Service Configuration.

    Attributes:
        Name (Optional[str]): The name of the service. A limit of at most 150 characters applies.
        Description (Optional[str]): The description of the service.
        ServiceDefinitionName (Optional[str]): The name of the service definition used for this service.
        ServiceDefinitionVersion (Optional[str]): The version of the service definition used for this service.
        ServiceDefinitionAlarmTemplate (Optional[str]): The alarm template used to monitor the service.
        ServiceDefinitionTrendTemplate (Optional[str]): The trend template used to track the service trend data.
        Triggers (Optional[List[DMAServiceConfigurationTrigger]]): The triggers that determine whether a child item is included in the service or not.
        Groups (Optional[List[DMAServiceConfigurationGroup]]): The groups of child items contained within the service.
        Parameters (Optional[List[DMAServiceConfigurationParameter]]): The child items of the service.
    """

    Name: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The name of the service. A limit of at most 150 characters applies."
        },
    )
    Description: Optional[str] = field(
        default=None, metadata={"doc": "The description of the service."}
    )
    ServiceDefinitionName: Optional[str] = field(
        default=None,
        metadata={"doc": "The name of the service definition used for this service."},
    )
    ServiceDefinitionVersion: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The version of the service definition used for this service."
        },
    )
    ServiceDefinitionAlarmTemplate: Optional[str] = field(
        default=None,
        metadata={"doc": "The alarm template used to monitor the service."},
    )
    ServiceDefinitionTrendTemplate: Optional[str] = field(
        default=None,
        metadata={"doc": "The trend template used to track the service trend data."},
    )
    Triggers: Optional[List["DMAServiceConfigurationTrigger"]] = field(
        default=None,
        metadata={
            "doc": "The triggers that determine whether a child item is included in the service or not."
        },
    )
    Groups: Optional[List["DMAServiceConfigurationGroup"]] = field(
        default=None,
        metadata={"doc": "The groups of child items contained within the service."},
    )
    Parameters: Optional[List["DMAServiceConfigurationParameter"]] = field(
        default=None, metadata={"doc": "The child items of the service."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAServiceConfigurationGroup(BaseDMAType):
    """
    Represents DMA Service Configuration Group.

    Attributes:
        Name (Optional[str]): The name of the group.
        GroupID (Optional[int]): The ID of the group.
        ParentGroupID (Optional[int]): The ID of the parent group.
        IsExcluded (Optional[bool]): Indicates whether the group is always included in the service or not.
        MaxSeverityOnIncludedElement (Optional[str]): The maximum severity that an included element can have.
        MaxSeverityOnElementNotUsed (Optional[str]): The maximum severity that a “not used” element can have.
        ExcludeTriggers (Optional[str]): The triggers that determine whether the group is excluded from the service.
        IncludeTriggers (Optional[str]): The triggers that determine whether the group is included in the service.
        NotUsedTriggers (Optional[str]): The triggers that determine whether the group is considered in use.
    """

    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the group."}
    )
    GroupID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the group."}
    )
    ParentGroupID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the parent group."}
    )
    IsExcluded: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the group is always included in the service or not."
        },
    )
    # TODO: Check if this can be AlarmStateType
    MaxSeverityOnIncludedElement: Optional[str] = field(
        default=None,
        metadata={"doc": "The maximum severity that an included element can have."},
    )
    # TODO: Check if this can be AlarmStateType
    MaxSeverityOnElementNotUsed: Optional[str] = field(
        default=None,
        metadata={"doc": "The maximum severity that a “not used” element can have."},
    )
    ExcludeTriggers: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The triggers that determine whether the group is excluded from the service."
        },
    )
    IncludeTriggers: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The triggers that determine whether the group is included in the service."
        },
    )
    NotUsedTriggers: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The triggers that determine whether the group is considered in use."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAServiceConfigurationParameter(BaseDMAType):
    """
    Represents DMA Service Configuration Parameter.

    Attributes:
        Alias (Optional[int]): The alias of the service child item.
        DataMinerID (Optional[int]): The DataMiner Agent ID of the service child item.
        ElementID (Optional[int]): The element ID of the service child item.
        GroupID (Optional[int]): The group ID of the service child item.
        IsService (Optional[bool]): Indicates whether the service child item is a service.
        IsExcluded (Optional[bool]): Indicates whether the child item is always included in the service or not.
        MaxSeverityOnIncludedElement (Optional[str]): The maximum severity that an included element can have.
        MaxSeverityOnElementNotUsed (Optional[str]): The maximum severity that a “not used” element can have.
        ExcludeTriggers (Optional[str]): The triggers that determine whether the child item is excluded from the service.
        IncludeTriggers (Optional[str]): The triggers that determine whether the child item is included in the service.
        NotUsedTriggers (Optional[str]): The triggers that determine whether the child item is considered in use.
        ParameterFilters (Optional[List[Dict[str, Any]]]): If not all parameters of a child element are included in the service, this array indicates the filters that determine which parameters are included.
    """

    Alias: Optional[int] = field(
        default=None, metadata={"doc": "The alias of the service child item."}
    )
    DataMinerID: Optional[int] = field(
        default=None,
        metadata={"doc": "The DataMiner Agent ID of the service child item."},
    )
    ElementID: Optional[int] = field(
        default=None, metadata={"doc": "The element ID of the service child item."}
    )
    GroupID: Optional[int] = field(
        default=None, metadata={"doc": "The group ID of the service child item."}
    )
    IsService: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the service child item is a service."},
    )
    IsExcluded: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the child item is always included in the service or not."
        },
    )
    MaxSeverityOnIncludedElement: Optional[str] = field(
        default=None,
        metadata={"doc": "The maximum severity that an included element can have."},
    )
    MaxSeverityOnElementNotUsed: Optional[str] = field(
        default=None,
        metadata={"doc": "The maximum severity that a “not used” element can have."},
    )
    ExcludeTriggers: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The triggers that determine whether the child item is excluded from the service."
        },
    )
    IncludeTriggers: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The triggers that determine whether the child item is included in the service."
        },
    )
    NotUsedTriggers: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The triggers that determine whether the child item is considered in use."
        },
    )
    ParameterFilters: Optional[List[Dict[str, Any]]] = field(
        default=None,
        metadata={
            "doc": "If not all parameters of a child element are included in the service, this array indicates the filters that determine which parameters are included."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAServiceConfigurationTrigger(BaseDMAType):
    """
    Represents DMA Service Configuration Trigger.

    Attributes:
        TriggerID (Optional[int]): The ID of the trigger.
        DataMinerID (Optional[int]): The DataMiner Agent ID.
        ElementID (Optional[int]): The element ID.
        ParameterID (Optional[int]): The parameter ID.
        TableIndex (Optional[str]): The parameter table index (in case of a table parameter).
        Delay (Optional[int]): The delay (in ms) that is applied before the trigger takes effect.
        Type (Optional[ServiceConfigurationTriggerType]): The type of trigger: "Correlation", "Alarm", "ElementState", "Parameter", "Manual", "Property" or "Connectivity".
        Value (Optional[str]): The value of the trigger. E.g. if “Type” is set to “Alarm”, this could be “Critical”.
        ValueCondition (Optional[str]): The condition operator for the trigger: "equal", "not equal", "exists row", "more", "less", "more or equal" or "less or equal".
    """

    TriggerID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the trigger."}
    )
    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The DataMiner Agent ID."}
    )
    ElementID: Optional[int] = field(default=None, metadata={"doc": "The element ID."})
    ParameterID: Optional[int] = field(
        default=None, metadata={"doc": "The parameter ID."}
    )
    TableIndex: Optional[str] = field(
        default=None,
        metadata={"doc": "The parameter table index (in case of a table parameter)."},
    )
    Delay: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The delay (in ms) that is applied before the trigger takes effect."
        },
    )
    Type: Optional[ServiceConfigurationTriggerType] = field(
        default=None,
        metadata={
            "doc": 'The type of trigger: "Correlation", "Alarm", "ElementState", "Parameter", "Manual", "Property" or "Connectivity".'
        },
    )
    Value: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The value of the trigger. E.g. if “Type” is set to “Alarm”, this could be “Critical”."
        },
    )
    ValueCondition: Optional[ServiceConfigurationTriggerConditionType] = field(
        default=None,
        metadata={
            "doc": 'The condition operator for the trigger: "equal", "not equal", "exists row", "more", "less", "more or equal" or "less or equal".'
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAServiceDefinition(BaseDMAType):
    """
    Represents DMA Service Definition.

    Attributes:
        Description (Optional[str]): The description of the service definition.
        CreatedAt (Optional[int]): The time when the booking was created.
        CreatedBy (Optional[str]): The user who created the booking.
        LastModifiedAt (Optional[int]): The time when the booking was last modified.
        LastModifiedBy (Optional[str]): The user who last modified the booking.
        Type (Optional[ServiceDefinitionType]): "Default" or "ProcessAutomation" or "CustomProcessAutomation"
        Nodes (Optional[List[DMAServiceDefinitionNode]]): The nodes of the service definition.
        Edges (Optional[List[DMAServiceDefinitionEdgeLite]]): The edges of the service definition.
    """

    Description: Optional[str] = field(
        default=None, metadata={"doc": "The description of the service definition."}
    )
    CreatedAt: Optional[int] = field(
        default=None, metadata={"doc": "The time when the booking was created."}
    )
    CreatedBy: Optional[str] = field(
        default=None, metadata={"doc": "The user who created the booking."}
    )
    LastModifiedAt: Optional[int] = field(
        default=None, metadata={"doc": "The time when the booking was last modified."}
    )
    LastModifiedBy: Optional[str] = field(
        default=None, metadata={"doc": "The user who last modified the booking."}
    )
    Type: Optional[ServiceDefinitionType] = field(
        default=None,
        metadata={
            "doc": '"Default" or "ProcessAutomation" or "CustomProcessAutomation"'
        },
    )
    Nodes: Optional[List["DMAServiceDefinitionNode"]] = field(
        default=None, metadata={"doc": "The nodes of the service definition."}
    )
    Edges: Optional[List["DMAServiceDefinitionEdgeLite"]] = field(
        default=None, metadata={"doc": "The edges of the service definition."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAServiceDefinitionEdgeLite(BaseDMAType):
    """
    Represents DMA Service Definition Edge Lite.

    Attributes:
        FromNodeID (Optional[int]): The node from which the connection originates.
        FromNodeInterfaceID (Optional[int]): The node interface from which the connection originates.
        ToNodeID (Optional[int]): The node to which the edge connects.
        ToNodeInterfaceID (Optional[int]): The node interface to which the edge connects.
        Properties (Optional[List[Dict[str, Any]]]): The properties of the edge.
    """

    FromNodeID: Optional[int] = field(
        default=None, metadata={"doc": "The node from which the connection originates."}
    )
    FromNodeInterfaceID: Optional[int] = field(
        default=None,
        metadata={"doc": "The node interface from which the connection originates."},
    )
    ToNodeID: Optional[int] = field(
        default=None, metadata={"doc": "The node to which the edge connects."}
    )
    ToNodeInterfaceID: Optional[int] = field(
        default=None, metadata={"doc": "The node interface to which the edge connects."}
    )
    Properties: Optional[List[Dict[str, Any]]] = field(
        default=None, metadata={"doc": "The properties of the edge."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAServiceDefinitionLite(BaseDMAType):
    """
    Represents DMA Service Definition Lite.

    Attributes:
        ID (Optional[str]): The ID of the service definition.
        Name (Optional[str]): The name of the service definition.
    """

    ID: Optional[str] = field(
        default=None, metadata={"doc": "The ID of the service definition."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the service definition."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAServiceDefinitionNode(BaseDMAType):
    """
    Represents DMA Service Definition Node.

    Attributes:
        ID (Optional[str]): The service definition node ID.
        Label (Optional[str]): The service definition node description.
        Groups (Optional[List[str]]): The names of the groups containing the node.
        Row (Optional[int]): The row in which the node is located.
        Column (Optional[int]): The column in which the node is located.
        Resource (Optional[DMAResource]): The resource linked to the node.
        Image (Optional[str]): The image used for the node.
        Properties (Optional[List[Dict[str, Any]]]): The properties of the node.
        InterfaceConfiguration (Optional[List[Dict[str, Any]]]): The interface configuration of the node.
        FunctionDefinition (Optional[DMAFunctionDefinitionLite]): The function definition linked to the node.
    """

    ID: Optional[str] = field(
        default=None, metadata={"doc": "The service definition node ID."}
    )
    Label: Optional[str] = field(
        default=None, metadata={"doc": "The service definition node description."}
    )
    Groups: Optional[List[str]] = field(
        default=None, metadata={"doc": "The names of the groups containing the node."}
    )
    Row: Optional[int] = field(
        default=None, metadata={"doc": "The row in which the node is located."}
    )
    Column: Optional[int] = field(
        default=None, metadata={"doc": "The column in which the node is located."}
    )
    Resource: Optional[DMAResource] = field(
        default=None, metadata={"doc": "The resource linked to the node."}
    )
    Image: Optional[str] = field(
        default=None, metadata={"doc": "The image used for the node."}
    )
    Properties: Optional[List[Dict[str, Any]]] = field(
        default=None, metadata={"doc": "The properties of the node."}
    )
    InterfaceConfiguration: Optional[List[Dict[str, Any]]] = field(
        default=None, metadata={"doc": "The interface configuration of the node."}
    )
    FunctionDefinition: Optional[DMAFunctionDefinitionLite] = field(
        default=None, metadata={"doc": "The function definition linked to the node."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMATriggerCombination(BaseDMAType):
    """
    Represents DMA Trigger Combination.

    Attributes:
        TriggerID (Optional[int]): The ID of the trigger.
        CombinationType (Optional[str]): A combination type such as "And", "Not", etc.
    """

    TriggerID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the trigger."}
    )
    # TODO: Convert to Enum
    CombinationType: Optional[str] = field(
        default=None, metadata={"doc": 'A combination type such as "And", "Not", etc.'}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAServiceInfoGroupDefinition(BaseDMAType):
    """
    Represents DMA Service Info Group Definition.

    Attributes:
        ExcludeTriggers (Optional[List[DMATriggerCombination]]): The triggers determining whether the group is excluded.
        IncludeTriggers (Optional[List[DMATriggerCombination]]): The triggers determining whether the group is included.
        NotUsedTriggers (Optional[List[DMATriggerCombination]]): The triggers determining whether the group is used.
        IncludedCapped (Optional[str]): The maximum severity for elements in the group when it is included: Critical, Major, Minor, Warning or Normal.
        NotUsedCapped (Optional[str]): The maximum severity for elements in the group when it is not used: Critical, Major, Minor, Warning or Normal.
        ParentGroupID (Optional[int]): The ID of the parent group, if any.
        Name (Optional[str]): The name of the group.
    """

    ExcludeTriggers: Optional[List[DMATriggerCombination]] = field(
        default=None,
        metadata={"doc": "The triggers determining whether the group is excluded."},
    )
    IncludeTriggers: Optional[List[DMATriggerCombination]] = field(
        default=None,
        metadata={"doc": "The triggers determining whether the group is included."},
    )
    NotUsedTriggers: Optional[List[DMATriggerCombination]] = field(
        default=None,
        metadata={"doc": "The triggers determining whether the group is used."},
    )
    IncludedCapped: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The maximum severity for elements in the group when it is included: Critical, Major, Minor, Warning or Normal."
        },
    )
    NotUsedCapped: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The maximum severity for elements in the group when it is not used: Critical, Major, Minor, Warning or Normal."
        },
    )
    ParentGroupID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the parent group, if any."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the group."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAServiceParamFilter(BaseDMAType):
    """
    Represents DMA Service Param Filter.

    Attributes:
        ParameterID (Optional[int]): The ID of the parameter.
        IsPrimaryKey (Optional[bool]): Determines whether the primary or the display key is used.
        Filter (Optional[Dict[str, Any]]): A filter consisting of a template string and an array of placeholders, as well as an additional Isregex boolean, indicating whether a regular expression is used, and a regexOptions enum (None, IgnoreCase, forceFullLine).
    """

    ParameterID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the parameter."}
    )
    IsPrimaryKey: Optional[bool] = field(
        default=None,
        metadata={"doc": "Determines whether the primary or the display key is used."},
    )
    # TODO: Define a proper type for this
    Filter: Optional[Dict[str, Any]] = field(
        default=None,
        metadata={
            "doc": "A filter consisting of a template string and an array of placeholders, as well as an additional Isregex boolean, indicating whether a regular expression is used, and a regexOptions enum (None, IgnoreCase, forceFullLine)."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAServiceParams(BaseDMAType):
    """
    Represents DMA Service Params.

    Attributes:
        IsService (Optional[bool]): Indicates whether the service child is a service.
        ElementSelection (Optional[Dict[str, Any]]): Determines whether the service child is fixed or templated, and how this is configured.
        ParameterFilters (Optional[List[Dict[str, Any]]]): The filters determining when parameters are included in the service child, if any.
        IncludedCapped (Optional[AlarmStateType]): The maximum severity for the service child when it is included: Critical, Major, Minor, Warning or Normal.
        NotUsedCapped (Optional[AlarmStateType]): The maximum severity for the service child when it is not used: Critical, Major, Minor, Warning or Normal.
        GroupID (Optional[int]): The ID of the group the service child is in, if any.
        Alias (Optional[str]): The alias of the service child, which is created using a DMASTString.
        Description (Optional[str]): The description of the service child.
    """

    IsService: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the service child is a service."},
    )
    # TODO: Define a proper type for this
    ElementSelection: Optional[Dict[str, Any]] = field(
        default=None,
        metadata={
            "doc": "Determines whether the service child is fixed or templated, and how this is configured."
        },
    )
    ParameterFilters: Optional[List[DMAServiceParamFilter]] = field(
        default=None,
        metadata={
            "doc": "The filters determining when parameters are included in the service child, if any."
        },
    )
    IncludedCapped: Optional[AlarmStateType] = field(
        default=None,
        metadata={
            "doc": "The maximum severity for the service child when it is included: Critical, Major, Minor, Warning or Normal."
        },
    )
    NotUsedCapped: Optional[AlarmStateType] = field(
        default=None,
        metadata={
            "doc": "The maximum severity for the service child when it is not used: Critical, Major, Minor, Warning or Normal."
        },
    )
    GroupID: Optional[int] = field(
        default=None,
        metadata={"doc": "The ID of the group the service child is in, if any."},
    )
    Alias: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The alias of the service child, which is created using a DMASTString."
        },
    )
    Description: Optional[str] = field(
        default=None, metadata={"doc": "The description of the service child."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAServiceParameter(BaseDMAType):
    """
    Represents DMA Service Parameter.

    Attributes:
        DataMinerID (Optional[int]): The ID of the DataMiner Agent.
        ElementID (Optional[int]): The ID of the service.
        ParameterID (Optional[int]): The ID of the parameter.
        TableIndex (Optional[str]): The display key of the table row (in case of a table parameter).
        ParameterName (Optional[str]): The name of the parameter.
        Value (Optional[str]): The current value of the parameter.
        DisplayValue (Optional[str]): The parameter value that will be displayed.
        LastValueChange (Optional[str]): The last time the value of the parameter has changed.
        LastValueChangeUTC (Optional[int]): The last time the value of the parameter has changed, in UTC format (milliseconds since midnight January 1, 1970 GMT).
        Positions (Optional[List[DMAParameterPosition]]): The places where the parameter can be found in the different Data Display pages of the element.
        Discreets (Optional[List[DMAParameterEditDiscreet]]): The discreet values of the parameter (only if WriteType is “Discreet”)
        Type (Optional[ParameterType]): The type of parameter: “Read”, “Write”, or “Table”.
        InfoSubText (Optional[str]): The parameter description.
        WriteType (Optional[str]): The type of write parameter: “String”, “Discreet”, “Number”, ...
        IsMonitored (Optional[bool]): Whether the value of the parameter is being monitored by an alarm template.
        AlarmState (Optional[AlarmStateType]): The current alarm state of the parameter.
        IsTrending (Optional[bool]): Whether the value of the parameter is being trended.
        Options (Optional[str]): The parameter options (extra flags to e.g. indicate special formatting instructions).
        LastChangeUTC (Optional[int]): The time when the parameter last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT).
    """

    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the DataMiner Agent."}
    )
    ElementID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the service."}
    )
    ParameterID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the parameter."}
    )
    TableIndex: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The display key of the table row (in case of a table parameter)."
        },
    )
    ParameterName: Optional[str] = field(
        default=None, metadata={"doc": "The name of the parameter."}
    )
    Value: Optional[str] = field(
        default=None, metadata={"doc": "The current value of the parameter."}
    )
    DisplayValue: Optional[str] = field(
        default=None, metadata={"doc": "The parameter value that will be displayed."}
    )
    LastValueChange: Optional[str] = field(
        default=None,
        metadata={"doc": "The last time the value of the parameter has changed."},
    )
    LastValueChangeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The last time the value of the parameter has changed, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )
    Positions: Optional[List[DMAParameterPosition]] = field(
        default=None,
        metadata={
            "doc": "The places where the parameter can be found in the different Data Display pages of the element."
        },
    )
    Discreets: Optional[List[DMAParameterEditDiscreet]] = field(
        default=None,
        metadata={
            "doc": "The discreet values of the parameter (only if WriteType is “Discreet”)"
        },
    )
    Type: Optional[ParameterType] = field(
        default=None,
        metadata={"doc": "The type of parameter: “Read”, “Write”, or “Table”."},
    )
    InfoSubText: Optional[str] = field(
        default=None, metadata={"doc": "The parameter description."}
    )
    WriteType: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The type of write parameter: “String”, “Discreet”, “Number”, ..."
        },
    )
    IsMonitored: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether the value of the parameter is being monitored by an alarm template."
        },
    )
    AlarmState: Optional[AlarmStateType] = field(
        default=None, metadata={"doc": "The current alarm state of the parameter."}
    )
    IsTrending: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether the value of the parameter is being trended."},
    )
    Options: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The parameter options (extra flags to e.g. indicate special formatting instructions)."
        },
    )
    LastChangeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The time when the parameter last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAServiceParametersElement(BaseDMAType):
    """
    Represents DMA Service Parameters Element.

    Attributes:
        DataMinerID (Optional[int]): The ID of the DataMiner Agent.
        ElementID (Optional[int]): The ID of the element.
        Name (Optional[str]): The name of the element.
        Alias (Optional[str]): The alias name of the element in the service.
        ProtocolName (Optional[str]): The name of the protocol.
        ProtocolVersion (Optional[str]): The version of the protocol.
        Parameters (Optional[List[DMAServiceParameter]]): The service parameters.
        LastChangeUTC (Optional[int]): The time when the object last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT).
    """

    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the DataMiner Agent."}
    )
    ElementID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the element."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the element."}
    )
    Alias: Optional[str] = field(
        default=None, metadata={"doc": "The alias name of the element in the service."}
    )
    ProtocolName: Optional[str] = field(
        default=None, metadata={"doc": "The name of the protocol."}
    )
    ProtocolVersion: Optional[str] = field(
        default=None, metadata={"doc": "The version of the protocol."}
    )
    Parameters: Optional[List[DMAServiceParameter]] = field(
        default=None, metadata={"doc": "The service parameters."}
    )
    LastChangeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The time when the object last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )


# TODO: Check if this is really the data received
@dataclass(slots=True, frozen=True, kw_only=True)
class DMAServiceTemplateGlobalCondition(BaseDMAType):
    """
    Represents DMA Service Template Global Condition.

    Attributes:
        Type (Optional[ServiceTemplateGlobalConditionType]): The type of condition: "None", "Equals", "WildCard" or "ContainsRow".
        FirstValue (Optional[str]): The first value of the condition.
        SecondValue (Optional[str]): The second value of the condition.
    """

    Type: Optional[ServiceTemplateGlobalConditionType] = field(
        default=None,
        metadata={
            "doc": 'The type of condition: "None", "Equals", "WildCard" or "ContainsRow".'
        },
    )
    FirstValue: Optional[str] = field(
        default=None, metadata={"doc": "The first value of the condition."}
    )
    SecondValue: Optional[str] = field(
        default=None, metadata={"doc": "The second value of the condition."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAServiceTemplate(BaseDMAType):
    """
    Represents DMA Service Template.

    Attributes:
        Name (Optional[str]): The name of the service template.
        Description (Optional[str]): The description of the service template.
        KeepCopiesOnReApply (Optional[bool]): Determines whether copies of the services are kept when the service template is reapplied.
        RcaChainDefinition (Optional[List[Dict[str, Any]]]): The different items in the RCA chain for the generated services: FirstValue and SecondValue (specified as integers).
        Definition_AutoExecuteOnElementAdd (Optional[bool]): Determines whether the service template is automatically applied when a new element is added in the DMS.
        Definition_CreateSLA (Optional[bool]): Determines whether an SLA is created for the services generated with the service template.
        Definition_RequireConfirmation (Optional[bool]): Determines whether the user has to confirm before the service template is applied.
        Definition_GlobalConditions (Optional[List[Dict[str, Any]]]): Array of conditions, each consisting of a type (None, Equals, WildCard or ContainsRow) and two values. These conditions determine when elements can be combined in a service. They can for instance specify that part of the element names must be equal to a specific value.
        Definition_PreRequiredData (Optional[List[DMAServiceTemplateRequiredData]]): Extra information used in the service template to create services. This information is required before elements are assigned (e.g. data used to limit elements according to a user-specified condition).
        Definition_RequiredData (Optional[List[DMAServiceTemplateRequiredData]]): Extra information used in the service template to create services.
        Definition_AdvancedRequestOrder (Optional[str]): The custom order in which child elements and input data should be selected when the service is generated, if any.
        Definition_AutoGenerateName (Optional[str]): The template for the name of the generated services.
        Definition_GenerateDescription (Optional[str]): The template for the description of the generated services.
        Groups (Optional[List[DMAServiceInfoGroupDefinition]]): Arrays defining different groups of child elements for generated services.
        ExcludeTriggers (Optional[List[Dict[str, Any]]]): The triggers determining whether the service child is excluded. These DMATriggerCombination objects consists of the following fields: TriggerID, CombinationType.
        IncludeTriggers (Optional[List[Dict[str, Any]]]): The triggers determining whether the service child is included. These DMATriggerCombination objects consists of the following fields: TriggerID, CombinationType.
        NotUsedTriggers (Optional[List[Dict[str, Any]]]): The triggers determining whether the service child is used. These DMATriggerCombination objects consists of the following fields: TriggerID, CombinationType.
        Triggers (Optional[List[DMAServiceTemplateConfigurationTrigger]]): The different triggers used in the service template, for instance to determine whether a service child is excluded. The triggers listed in this array are referred to by ID in the different trigger combinations.
        ServiceElementInfo_AlarmTemplate (Optional[str]): The alarm template used for the generated services.
        ServiceElementInfo_ProtocolTemplate (Optional[str]): The service protocol used for the generated services.
        ServiceElementInfo_ProtocolVersion (Optional[str]): The service protocol version used for the generated services.
        ServiceElementInfo_TrendTemplate (Optional[str]): The trend template used for the generated services.
        ServiceParams (Optional[List[DMAServiceParams]]): The child elements of the generated services.
        VisioInfo_DefaultPage (Optional[int]): The default page of the Visio drawing used for the generated services.
        VisioInfo_Name_Template (Optional[str]): The template for the name of the Visio drawing used for the generated services. Placeholders in this template are in the format {0}, {1}, etc. and refer to the placeholders in the next field. See DMASTString.
        VisioInfo_Name_Placeholders (Optional[List[Dict[str, Any]]]): The placeholders used in the template, e.g. [data:Data Item Name] or [element:1:title]. See DMASTString.
    """

    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the service template."}
    )
    Description: Optional[str] = field(
        default=None, metadata={"doc": "The description of the service template."}
    )
    KeepCopiesOnReApply: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Determines whether copies of the services are kept when the service template is reapplied."
        },
    )
    RcaChainDefinition: Optional[List[Dict[str, Any]]] = field(
        default=None,
        metadata={
            "doc": "The different items in the RCA chain for the generated services: FirstValue and SecondValue (specified as integers)."
        },
    )
    Definition_AutoExecuteOnElementAdd: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Determines whether the service template is automatically applied when a new element is added in the DMS."
        },
    )
    Definition_CreateSLA: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Determines whether an SLA is created for the services generated with the service template."
        },
    )
    Definition_RequireConfirmation: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Determines whether the user has to confirm before the service template is applied."
        },
    )
    Definition_GlobalConditions: Optional[List[DMAServiceTemplateGlobalCondition]] = (
        field(
            default=None,
            metadata={
                "doc": "Array of conditions, each consisting of a type (None, Equals, WildCard or ContainsRow) and two values. These conditions determine when elements can be combined in a service. They can for instance specify that part of the element names must be equal to a specific value."
            },
        )
    )
    Definition_PreRequiredData: Optional[List["DMAServiceTemplateRequiredData"]] = (
        field(
            default=None,
            metadata={
                "doc": "Extra information used in the service template to create services. This information is required before elements are assigned (e.g. data used to limit elements according to a user-specified condition)."
            },
        )
    )
    Definition_RequiredData: Optional[List["DMAServiceTemplateRequiredData"]] = field(
        default=None,
        metadata={
            "doc": "Extra information used in the service template to create services."
        },
    )
    Definition_AdvancedRequestOrder: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The custom order in which child elements and input data should be selected when the service is generated, if any."
        },
    )
    Definition_AutoGenerateName: Optional[str] = field(
        default=None,
        metadata={"doc": "The template for the name of the generated services."},
    )
    Definition_GenerateDescription: Optional[str] = field(
        default=None,
        metadata={"doc": "The template for the description of the generated services."},
    )
    Groups: Optional[List[DMAServiceInfoGroupDefinition]] = field(
        default=None,
        metadata={
            "doc": "Arrays defining different groups of child elements for generated services."
        },
    )
    ExcludeTriggers: Optional[List[DMATriggerCombination]] = field(
        default=None,
        metadata={
            "doc": "The triggers determining whether the service child is excluded. These DMATriggerCombination objects consists of the following fields: TriggerID, CombinationType."
        },
    )
    IncludeTriggers: Optional[List[DMATriggerCombination]] = field(
        default=None,
        metadata={
            "doc": "The triggers determining whether the service child is included. These DMATriggerCombination objects consists of the following fields: TriggerID, CombinationType."
        },
    )
    NotUsedTriggers: Optional[List[DMATriggerCombination]] = field(
        default=None,
        metadata={
            "doc": "The triggers determining whether the service child is used. These DMATriggerCombination objects consists of the following fields: TriggerID, CombinationType."
        },
    )
    Triggers: Optional[List["DMAServiceTemplateConfigurationTrigger"]] = field(
        default=None,
        metadata={
            "doc": "The different triggers used in the service template, for instance to determine whether a service child is excluded. The triggers listed in this array are referred to by ID in the different trigger combinations."
        },
    )
    ServiceElementInfo_AlarmTemplate: Optional[str] = field(
        default=None,
        metadata={"doc": "The alarm template used for the generated services."},
    )
    ServiceElementInfo_ProtocolTemplate: Optional[str] = field(
        default=None,
        metadata={"doc": "The service protocol used for the generated services."},
    )
    ServiceElementInfo_ProtocolVersion: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The service protocol version used for the generated services."
        },
    )
    ServiceElementInfo_TrendTemplate: Optional[str] = field(
        default=None,
        metadata={"doc": "The trend template used for the generated services."},
    )
    ServiceParams: Optional[List[DMAServiceParams]] = field(
        default=None, metadata={"doc": "The child elements of the generated services."}
    )
    VisioInfo_DefaultPage: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The default page of the Visio drawing used for the generated services."
        },
    )
    VisioInfo_Name_Template: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The template for the name of the Visio drawing used for the generated services. Placeholders in this template are in the format {0}, {1}, etc. and refer to the placeholders in the next field. See DMASTString."
        },
    )
    VisioInfo_Name_Placeholders: Optional[List[Dict[str, Any]]] = field(
        default=None,
        metadata={
            "doc": "The placeholders used in the template, e.g. [data:Data Item Name] or [element:1:title]. See DMASTString."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAServiceTemplateConfigurationTrigger(BaseDMAType):
    """
    Represents DMA Service Template Configuration Trigger.

    Attributes:
        TableIndex (Optional[str]): The table index of the parameter used in the trigger. This is in DMASTString format but will usually consist of empty placeholders and a regular string as the template.
        ParameterNameForTemplate (Optional[str]): The name of the parameter used in the trigger. This is used in case the parameter is not specified by ID, so that the parameter name can change dynamically.
        Delay (Optional[int]): The delay before the trigger is activated (in ms), if any.
        DataMinerID (Optional[int]): The DataMiner ID of the object used in the trigger.
        ElementID (Optional[int]): The ID of the element used in the trigger.
        ParameterID (Optional[int]): The ID of the parameter used in the trigger.
        Type (Optional[ServiceConfigurationTriggerType]): The type of event functioning as trigger: Alarm (for an alarm state), ElementState (for an element alarm state) or Parameter (for a parameter value).
        Value (Optional[str]): In case a condition is used for the trigger, this indicates that value specified in the condition. For conditions of type Alarm or ElementState, this is a severity, which means it will be a DMASTString without placeholders. For conditions of type Parameter, it can be a regular DMASTString with placeholders.
        ValueCondition (Optional[ServiceConfigurationTriggerConditionType]): In case a condition is used for the trigger, this indicates the first part of the condition: <, <=, ==, <>, >=, > or exists row (in case the condition is of type Parameter value).
    """

    TableIndex: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The table index of the parameter used in the trigger. This is in DMASTString format but will usually consist of empty placeholders and a regular string as the template."
        },
    )
    ParameterNameForTemplate: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The name of the parameter used in the trigger. This is used in case the parameter is not specified by ID, so that the parameter name can change dynamically."
        },
    )
    Delay: Optional[int] = field(
        default=None,
        metadata={"doc": "The delay before the trigger is activated (in ms), if any."},
    )
    DataMinerID: Optional[int] = field(
        default=None,
        metadata={"doc": "The DataMiner ID of the object used in the trigger."},
    )
    ElementID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the element used in the trigger."}
    )
    ParameterID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the parameter used in the trigger."}
    )
    Type: Optional[ServiceConfigurationTriggerType] = field(
        default=None,
        metadata={
            "doc": "The type of event functioning as trigger: Alarm (for an alarm state), ElementState (for an element alarm state) or Parameter (for a parameter value)."
        },
    )
    Value: Optional[str] = field(
        default=None,
        metadata={
            "doc": "In case a condition is used for the trigger, this indicates that value specified in the condition. For conditions of type Alarm or ElementState, this is a severity, which means it will be a DMASTString without placeholders. For conditions of type Parameter, it can be a regular DMASTString with placeholders."
        },
    )
    ValueCondition: Optional[ServiceConfigurationTriggerConditionType] = field(
        default=None,
        metadata={
            "doc": "In case a condition is used for the trigger, this indicates the first part of the condition: <, <=, ==, <>, >=, > or exists row (in case the condition is of type Parameter value)."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAServiceTemplateMissingData(BaseDMAType):
    """
    Represents DMA Service Template Missing Data.

    Attributes:
        Name (Optional[str]): The input data name. This is the name that should also be specified in the corresponding inputData input of the CreateServiceByApplyingServiceTemplate and ReapplyService methods.
        DisplayName (Optional[str]): The input data title.
        Type (Optional[str]): The type of input data: "Undefined", "Text", "DropDown", "Hidden", "CheckBox" or "HiddenFromScreen"
        SelectedValue (Optional[str]): The selected input data value.
        SelectedDisplayValue (Optional[str]): The selected input data value as it is displayed.
        PossibleValues (Optional[List[str]]): If the Type is “DropDown”, this tag contains a list of values that can be selected.
        InvalidReason (Optional[str]): The reason why the input data is currently invalid.
    """

    Name: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The input data name. This is the name that should also be specified in the corresponding inputData input of the CreateServiceByApplyingServiceTemplate and ReapplyService methods."
        },
    )
    DisplayName: Optional[str] = field(
        default=None, metadata={"doc": "The input data title."}
    )
    Type: Optional[ServiceTemplateMissingDataType] = field(
        default=None,
        metadata={
            "doc": 'The type of input data: "Undefined", "Text", "DropDown", "Hidden", "CheckBox" or "HiddenFromScreen"'
        },
    )
    SelectedValue: Optional[str] = field(
        default=None, metadata={"doc": "The selected input data value."}
    )
    SelectedDisplayValue: Optional[str] = field(
        default=None,
        metadata={"doc": "The selected input data value as it is displayed."},
    )
    PossibleValues: Optional[List[str]] = field(
        default=None,
        metadata={
            "doc": "If the Type is “DropDown”, this tag contains a list of values that can be selected."
        },
    )
    InvalidReason: Optional[str] = field(
        default=None,
        metadata={"doc": "The reason why the input data is currently invalid."},
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAServiceTemplateRequiredData(BaseDMAType):
    """
    Represents DMA Service Template Required Data.

    Attributes:
        Name (Optional[str]): The name of the required data
        RequiredData (Optional[Any]): The DMAServTemplateRequiredData object. The DMAServTemplateRequiredData object can represent the following things:
            - DMAServiceTemplateRequiredInputData: See DMAServiceTemplateRequiredInputData.
            - DMAServiceTemplateRequiredSLA, which consists of a DMASTString.
            - DMAServiceTemplateRequiredGeneratedService, which consists of a DMASTString.
            - DMAServiceTemplateRequiredDestView, which can be either:
                  - A fixed view, DMADestViewFixed, determined by ViewID (int).
                  - A templated view, DMADestViewByName, determined by a DMASTString.
            - DMAServiceTemplateRequiredSpecialInputData, consisting of:
                  - Title (string): The title specified for the input data.
                  - InputData: See DMAServiceTemplateRequiredInputData
    """

    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the required data"}
    )
    # TODO: Create a representation for this
    RequiredData: Optional[Any] = field(
        default=None, metadata={"doc": "The DMAServTemplateRequiredData object."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAServiceTemplateRequiredInputData(BaseDMAType):
    """
    Represents DMA Service Template Required Input Data.

    Attributes:
        Title (Optional[str]): The title specified for the input data object.
        InputData (Optional[Dict[str, Any]]): The input data object itself.
    """

    Title: Optional[str] = field(
        default=None, metadata={"doc": "The title specified for the input data object."}
    )
    InputData: Optional[Dict[str, Any]] = field(
        default=None, metadata={"doc": "The input data object itself."}
    )
