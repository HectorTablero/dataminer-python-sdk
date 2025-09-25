from dataclasses import dataclass, field
from typing import Optional, List
from dataminer_sdk.models.base import BaseDMAType
from dataminer_sdk.models.enums import (
    DashboardType,
    ParameterStyleType,
    ParameterType,
    AlarmStateType,
)


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAParameterEditDiscreet(BaseDMAType):
    """
    Represents DMA Parameter Edit Discreet.

    Attributes:
        Display (Optional[str]): The value that will be displayed.
        Value (Optional[str]): The actual value.
        DisabledIf_ParameterID (Optional[int]): Indicates the parameter ID that is used to check if the discrete value should be disabled.
        DisabledIf_Value (Optional[str]): Indicates the parameter value that determines if the discrete value should be disabled.
    """

    Display: Optional[str] = field(
        default=None, metadata={"doc": "The value that will be displayed."}
    )
    Value: Optional[str] = field(default=None, metadata={"doc": "The actual value."})
    DisabledIf_ParameterID: Optional[int] = field(
        default=None,
        metadata={
            "doc": "Indicates the parameter ID that is used to check if the discrete value should be disabled."
        },
    )
    DisabledIf_Value: Optional[str] = field(
        default=None,
        metadata={
            "doc": "Indicates the parameter value that determines if the discrete value should be disabled."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAParameterPosition(BaseDMAType):
    """
    Represents DMA Parameter Position.

    Attributes:
        Page (Optional[str]): The Data Display page on which the parameter is situated.
        PageWeight (Optional[int]): A value that determines the order in which the parameter pages should be displayed to the user (as configured in the protocol).
        Row (Optional[int]): The row of the Data Display page on which the parameter is situated.
        Column (Optional[int]): The column of the Data Display page on which the parameter is situated.
    """

    Page: Optional[str] = field(
        default=None,
        metadata={"doc": "The Data Display page on which the parameter is situated."},
    )
    PageWeight: Optional[int] = field(
        default=None,
        metadata={
            "doc": "A value that determines the order in which the parameter pages should be displayed to the user (as configured in the protocol)."
        },
    )
    Row: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The row of the Data Display page on which the parameter is situated."
        },
    )
    Column: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The column of the Data Display page on which the parameter is situated."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAParameterTableCellV2(BaseDMAType):
    """
    Represents DMA Parameter Table Cell V2.

    Attributes:
        Value (Optional[str]): The current value of the parameter.
        DisplayValue (Optional[str]): The displayed parameter value.
        AlarmState (Optional[AlarmStateType]): The current alarm state of the parameter.
        IsTrending (Optional[bool]): Whether the value of the parameter is being trended.
        LastChangeUTC (Optional[int]): The time when the table cell last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT).
    """

    Value: Optional[str] = field(
        default=None, metadata={"doc": "The current value of the parameter."}
    )
    DisplayValue: Optional[str] = field(
        default=None, metadata={"doc": "The displayed parameter value."}
    )
    AlarmState: Optional[AlarmStateType] = field(
        default=None, metadata={"doc": "The current alarm state of the parameter."}
    )
    IsTrending: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether the value of the parameter is being trended."},
    )
    LastChangeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The time when the table cell last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAParameterTableColumn(BaseDMAType):
    """
    Represents DMA Parameter Table Column.

    Attributes:
        ProtocolIndex (Optional[int]): The position of the column in the table, as defined in the protocol.
        Type (Optional[ParameterType]): The type of parameter: “Read”, “Write”, or “Table”.
        WriteType (Optional[str]): The type of write parameter: “String”, “Discreet”, “Number”, ...
        IsPrimaryKey (Optional[bool]): Indicates whether the column contains the primary keys.
        IsDisplayKey (Optional[bool]): Indicates whether the column contains the display keys.
        IsElementLink (Optional[bool]): Whether the column is linked to a different DataMiner object.
        IsSortedASC (Optional[bool]): Whether or not the column is sorted in ascending order (as defined in the protocol).
        IsSortedDESC (Optional[bool]): Whether or not the column is sorted in descending order (as defined in the protocol).
    """

    ProtocolIndex: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The position of the column in the table, as defined in the protocol."
        },
    )
    Type: Optional[ParameterType] = field(
        default=None,
        metadata={"doc": "The type of parameter: “Read”, “Write”, or “Table”."},
    )
    # TODO: Add an enum for WriteType
    WriteType: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The type of write parameter: “String”, “Discreet”, “Number”, ..."
        },
    )
    IsPrimaryKey: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the column contains the primary keys."},
    )
    IsDisplayKey: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the column contains the display keys."},
    )
    IsElementLink: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether the column is linked to a different DataMiner object."
        },
    )
    IsSortedASC: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the column is sorted in ascending order (as defined in the protocol)."
        },
    )
    IsSortedDESC: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether or not the column is sorted in descending order (as defined in the protocol)."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAParameterTableRowV2(BaseDMAType):
    """
    Represents DMA Parameter Table Row V2.

    Attributes:
        Index (Optional[int]): The number of the column that contains the primary key.
        IndexValue (Optional[str]): The value of the primary key.
        DisplayIndex (Optional[int]): The number of the column that contains the display key.
        DisplayIndexValue (Optional[str]): The value of the display key.
        TrendKey (Optional[str]): The tableIndex that should be used to request trend data (depending on whether advanced naming is used or not).
        Position (Optional[int]): The sequence number of the row.
        AlarmState (Optional[AlarmStateType]): The current alarm state of the table row.
        Cells (Optional[List[DMAParameterTableCellV2]]): The cells contained in the table row.
        LastChangeUTC (Optional[int]): The time when the table row last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT).
    """

    Index: Optional[int] = field(
        default=None,
        metadata={"doc": "The number of the column that contains the primary key."},
    )
    IndexValue: Optional[str] = field(
        default=None, metadata={"doc": "The value of the primary key."}
    )
    DisplayIndex: Optional[int] = field(
        default=None,
        metadata={"doc": "The number of the column that contains the display key."},
    )
    DisplayIndexValue: Optional[str] = field(
        default=None, metadata={"doc": "The value of the display key."}
    )
    TrendKey: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The tableIndex that should be used to request trend data (depending on whether advanced naming is used or not)."
        },
    )
    Position: Optional[int] = field(
        default=None, metadata={"doc": "The sequence number of the row."}
    )
    AlarmState: Optional[AlarmStateType] = field(
        default=None, metadata={"doc": "The current alarm state of the table row."}
    )
    Cells: Optional[List[DMAParameterTableCellV2]] = field(
        default=None, metadata={"doc": "The cells contained in the table row."}
    )
    LastChangeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The time when the table row last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAParameterInfo(BaseDMAType):
    """
    Represents DMA Parameter Info.

    Attributes:
        ID (Optional[int]): The ID of the parameter.
        ParameterName (Optional[str]): The name of the parameter.
        InfoSubText (Optional[str]): The parameter description.
        IsMonitored (Optional[bool]): Whether the value of the parameter is being monitored by an alarm template.
        IsNumerical (Optional[bool]): Whether the value of the parameter is numerical.
        HasRange (Optional[bool]): Determines whether the value of the parameter is defined within a certain range.
        RangeLow (Optional[float]): If HasRange is true, this determines the lowest value of the parameter range.
        RangeHigh (Optional[float]): If HasRange is true, this determines the highest value of the parameter range.
        RangeLowDisplay (Optional[str]): The display value of the raw value stored in RangeLow.
        RangeHighDisplay (Optional[str]): The display value of the raw value stored in RangeHigh.
        Options (Optional[str]): The parameter options (extra flags to e.g. indicate special formatting instructions).
        Unit (Optional[str]): The unit of measure of the parameter.
        PrimaryKeyID (Optional[int]): If the parameter is a table parameter, the primary key.
        DisplayKeyID (Optional[int]): If the parameter is a table parameter, the display key.
        IsLogarithmic (Optional[bool]): Indicates whether the trend data of this parameter should be displayed on a logarithmic scale.
        IsTableColumn (Optional[bool]): Whether or not the parameter is a table column parameter.
        IsTable (Optional[bool]): Whether or not the parameter is a table parameter.
        IsTrending (Optional[bool]): Whether the value of the parameter is being trended.
        TableParameterID (Optional[int]): If the parameter is a column parameter, this indicates the ID of the table parameter.
        Decimals (Optional[int]): The number of decimals.
        Type (Optional[ParameterType]): The type of parameter: “Read”, “Write”, or “Table”.
        WriteType (Optional[str]): The type of write parameter: “String”, “Discreet”, “Number”, ...
        ReadType (Optional[str]): The type of read parameter.
        Discreets (Optional[List[DMAParameterEditDiscreet]]): The discreet values of the parameter (only if WriteType is “Discreet”).
        DashboardsType (Optional[DashboardType]): The button panel dashboard type: None, ButtonPanel, ButtonPanelContainers or ButtonPanelCollection.
        Positions (Optional[List[DMAParameterPosition]]): The places where the parameter can be found in the different Data Display pages of the element.
        WarningMessage (Optional[str]): The message that, in the protocol, can be configured on the write parameter. This message will be displayed when an attempt is made to update the parameter. For example: "Changing this setting will make the device unavailable."
        AvgTrendingFilters (Optional[List[str]]): An array of filters for which average trending is enabled (as configured in the trend template).
        RealTimeTrendingFilters (Optional[List[str]]): An array of filters for which real-time trending is enabled (as configured in the trend template).
    """

    ID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the parameter."}
    )
    ParameterName: Optional[str] = field(
        default=None, metadata={"doc": "The name of the parameter."}
    )
    InfoSubText: Optional[str] = field(
        default=None, metadata={"doc": "The parameter description."}
    )
    IsMonitored: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether the value of the parameter is being monitored by an alarm template."
        },
    )
    IsNumerical: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether the value of the parameter is numerical."},
    )
    HasRange: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Determines whether the value of the parameter is defined within a certain range."
        },
    )
    RangeLow: Optional[float] = field(
        default=None,
        metadata={
            "doc": "If HasRange is true, this determines the lowest value of the parameter range."
        },
    )
    RangeHigh: Optional[float] = field(
        default=None,
        metadata={
            "doc": "If HasRange is true, this determines the highest value of the parameter range."
        },
    )
    RangeLowDisplay: Optional[str] = field(
        default=None,
        metadata={"doc": "The display value of the raw value stored in RangeLow."},
    )
    RangeHighDisplay: Optional[str] = field(
        default=None,
        metadata={"doc": "The display value of the raw value stored in RangeHigh."},
    )
    Options: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The parameter options (extra flags to e.g. indicate special formatting instructions)."
        },
    )
    Unit: Optional[str] = field(
        default=None, metadata={"doc": "The unit of measure of the parameter."}
    )
    PrimaryKeyID: Optional[int] = field(
        default=None,
        metadata={"doc": "If the parameter is a table parameter, the primary key."},
    )
    DisplayKeyID: Optional[int] = field(
        default=None,
        metadata={"doc": "If the parameter is a table parameter, the display key."},
    )
    IsLogarithmic: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the trend data of this parameter should be displayed on a logarithmic scale."
        },
    )
    IsTableColumn: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the parameter is a table column parameter."},
    )
    IsTable: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the parameter is a table parameter."},
    )
    IsTrending: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether the value of the parameter is being trended."},
    )
    TableParameterID: Optional[int] = field(
        default=None,
        metadata={
            "doc": "If the parameter is a column parameter, this indicates the ID of the table parameter."
        },
    )
    Decimals: Optional[int] = field(
        default=None, metadata={"doc": "The number of decimals."}
    )
    Type: Optional[ParameterType] = field(
        default=None,
        metadata={"doc": "The type of parameter: “Read”, “Write”, or “Table”."},
    )
    # TODO: Add an enum for WriteType
    WriteType: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The type of write parameter: “String”, “Discreet”, “Number”, ..."
        },
    )
    # TODO: Add an enum for ReadType
    ReadType: Optional[str] = field(
        default=None, metadata={"doc": "The type of read parameter."}
    )
    Discreets: Optional[List[DMAParameterEditDiscreet]] = field(
        default=None,
        metadata={
            "doc": "The discreet values of the parameter (only if WriteType is “Discreet”)."
        },
    )
    DashboardsType: Optional[DashboardType] = field(
        default=None,
        metadata={
            "doc": "The button panel dashboard type: None, ButtonPanel, ButtonPanelContainers or ButtonPanelCollection."
        },
    )
    Positions: Optional[List[DMAParameterPosition]] = field(
        default=None,
        metadata={
            "doc": "The places where the parameter can be found in the different Data Display pages of the element."
        },
    )
    WarningMessage: Optional[str] = field(
        default=None,
        metadata={
            "doc": 'The message that, in the protocol, can be configured on the write parameter. This message will be displayed when an attempt is made to update the parameter. For example: "Changing this setting will make the device unavailable."'
        },
    )
    AvgTrendingFilters: Optional[List[str]] = field(
        default=None,
        metadata={
            "doc": "An array of filters for which average trending is enabled (as configured in the trend template)."
        },
    )
    RealTimeTrendingFilters: Optional[List[str]] = field(
        default=None,
        metadata={
            "doc": "An array of filters for which real-time trending is enabled (as configured in the trend template)."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAParameter(DMAParameterInfo):
    """
    Represents DMA Parameter.

    Attributes:
        DataMinerID (Optional[int]): The ID of the DataMiner Agent.
        ElementID (Optional[int]): The ID of the element.
        TableIndex (Optional[str]): The key of the row (if the parameter is a table column parameter).
        Value (Optional[str]): The current value of the parameter.
        DisplayValue (Optional[str]): The parameter value that will be displayed.
        LastValueChange (Optional[str]): The last time the value of the parameter has changed.
        LastValueChangeUTC (Optional[int]): The last time the value of the parameter has changed, in UTC format (milliseconds since midnight January 1, 1970 GMT).
        AlarmState (Optional[AlarmStateType]): The current alarm severity: "Undefined", "Normal", "Warning", "Minor", "Major" or "Critical".
        Filters (Optional[str]): Column and row filters, only filled in when using the method GetParametersByPageForServiceElement, in case only part of a table is included in the service.
        LastChangeUTC (Optional[int]): The time when the parameter last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT).
    """

    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the DataMiner Agent."}
    )
    ElementID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the element."}
    )
    TableIndex: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The key of the row (if the parameter is a table column parameter)."
        },
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
    AlarmState: Optional[AlarmStateType] = field(
        default=None,
        metadata={
            "doc": 'The current alarm severity: "Undefined", "Normal", "Warning", "Minor", "Major" or "Critical".'
        },
    )
    Filters: Optional[str] = field(
        default=None,
        metadata={
            "doc": "Column and row filters, only filled in when using the method GetParametersByPageForServiceElement, in case only part of a table is included in the service."
        },
    )
    LastChangeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The time when the parameter last changed, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAParameterEdit(BaseDMAType):
    """
    Represents DMA Parameter Edit.

    Attributes:
        ParameterID (Optional[int]): The ID of the parameter.
        Type (Optional[str]): The type of write parameter: “String”, “Discreet”, “Number”, ...
        Name (Optional[str]): The name of the parameter.
        Value (Optional[str]): The current value of the parameter.
        DisplayValue (Optional[str]): The parameter value that will be displayed.
        Discreets (Optional[List[DMAParameterEditDiscreet]]): The discreet values of the parameter (only if Type is “Discreet”).
        ParameterStyles (Optional[ParameterStyleType]): The style of the parameter control: "None", "Number", "Lowercase", "Uppercase", "HorizontalScroll", or "Password"
        HasRange (Optional[bool]): Whether the value of the parameter has to be within a certain range (which is defined in the protocol).
        RangeHigh (Optional[float]): The maximum value to which the parameter can be set.
        RangeLow (Optional[float]): The minimum value to which the parameter can be set.
        RangeStep (Optional[float]): The step size. If RangeStep is 5, then the parameter value has to be in the series {... , -5, 0, 5, 10, 15, 20, ...}.
        Options (Optional[str]): The parameter options (extra flags to e.g. indicate special formatting instructions).
        ConfirmationMessage (Optional[str]): The text that can be displayed in a confirmation box before the parameter is updated.
        Decimals (Optional[int]): The number of decimals.
    """

    ParameterID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the parameter."}
    )
    # TODO: Add an enum for Type
    Type: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The type of write parameter: “String”, “Discreet”, “Number”, ..."
        },
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the parameter."}
    )
    Value: Optional[str] = field(
        default=None, metadata={"doc": "The current value of the parameter."}
    )
    DisplayValue: Optional[str] = field(
        default=None, metadata={"doc": "The parameter value that will be displayed."}
    )
    Discreets: Optional[List[DMAParameterEditDiscreet]] = field(
        default=None,
        metadata={
            "doc": "The discreet values of the parameter (only if Type is “Discreet”)."
        },
    )
    ParameterStyles: Optional[ParameterStyleType] = field(
        default=None,
        metadata={
            "doc": 'The style of the parameter control: "None", "Number", "Lowercase", "Uppercase", "HorizontalScroll", or "Password"'
        },
    )
    HasRange: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether the value of the parameter has to be within a certain range (which is defined in the protocol)."
        },
    )
    RangeHigh: Optional[float] = field(
        default=None,
        metadata={"doc": "The maximum value to which the parameter can be set."},
    )
    RangeLow: Optional[float] = field(
        default=None,
        metadata={"doc": "The minimum value to which the parameter can be set."},
    )
    RangeStep: Optional[float] = field(
        default=None,
        metadata={
            "doc": "The step size. If RangeStep is 5, then the parameter value has to be in the series {... , -5, 0, 5, 10, 15, 20, ...}."
        },
    )
    Options: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The parameter options (extra flags to e.g. indicate special formatting instructions)."
        },
    )
    ConfirmationMessage: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The text that can be displayed in a confirmation box before the parameter is updated."
        },
    )
    Decimals: Optional[int] = field(
        default=None, metadata={"doc": "The number of decimals."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAParameterTable(BaseDMAType):
    """
    Represents DMA Parameter Table.

    Attributes:
        Columns (Optional[List[DMAParameterTableColumn]]): Information on the columns of the specified table parameter.
        Rows (Optional[List[DMAParameterTableRowV2]]): The rows of the specified table parameter.
        PageCount (Optional[int]): The number of pages. If the complete table is returned, this is set to 0.
        CurrentPage (Optional[int]): The number of the current page (with 1 as the first page). If the complete table is returned, this is set to 0.
        TotalAmountRows (Optional[int]): The total number of rows in the table.
    """

    Columns: Optional[List[DMAParameterTableColumn]] = field(
        default=None,
        metadata={
            "doc": "Information on the columns of the specified table parameter."
        },
    )
    Rows: Optional[List[DMAParameterTableRowV2]] = field(
        default=None, metadata={"doc": "The rows of the specified table parameter."}
    )
    PageCount: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The number of pages. If the complete table is returned, this is set to 0."
        },
    )
    CurrentPage: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The number of the current page (with 1 as the first page). If the complete table is returned, this is set to 0."
        },
    )
    TotalAmountRows: Optional[int] = field(
        default=None, metadata={"doc": "The total number of rows in the table."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAHysteresisInfo(BaseDMAType):
    """
    Represents DMA Hysteresis Info.

    Attributes:
        MaHHysOn (Optional[bool]): Whether alarm hysteresis is enabled for the Major High alarm level.
        MaHHysOff (Optional[bool]): Whether clear hysteresis is enabled for the Major High alarm level.
        MiHHysOn (Optional[bool]): Whether alarm hysteresis is enabled for the Minor High alarm level.
        MiHHysOff (Optional[bool]): Whether clear hysteresis is enabled for the Minor High alarm level.
        WaHHysOn (Optional[bool]): Whether alarm hysteresis is enabled for the Warning High alarm level.
        WaHHysOff (Optional[bool]): Whether clear hysteresis is enabled for the Warning High alarm level.
        WaLHysOn (Optional[bool]): Whether alarm hysteresis is enabled for the Warning Low alarm level.
        WaLHysOff (Optional[bool]): Whether clear hysteresis is enabled for the Warning Low alarm level.
        CLHysOn (Optional[bool]): Whether alarm hysteresis is enabled for the Critical Low alarm level.
        MiLHysOff (Optional[bool]): Whether clear hysteresis is enabled for the Minor Low alarm level.
        MaLHysOn (Optional[bool]): Whether alarm hysteresis is enabled for the Major Low alarm level.
        MaLHysOff (Optional[bool]): Whether clear hysteresis is enabled for the Major Low alarm level.
        CHHysOff (Optional[bool]): Whether clear hysteresis is enabled for the Critical High alarm level.
        CLHysOff (Optional[bool]): Whether clear hysteresis is enabled for the Critical Low alarm level.
        MiLHysOn (Optional[bool]): Whether alarm hysteresis is enabled for the Minor Low alarm level.
        CHHysOn (Optional[bool]): Whether alarm hysteresis is enabled for the Critical High alarm level.
    """

    MaHHysOn: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether alarm hysteresis is enabled for the Major High alarm level."
        },
    )
    MaHHysOff: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether clear hysteresis is enabled for the Major High alarm level."
        },
    )
    MiHHysOn: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether alarm hysteresis is enabled for the Minor High alarm level."
        },
    )
    MiHHysOff: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether clear hysteresis is enabled for the Minor High alarm level."
        },
    )
    WaHHysOn: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether alarm hysteresis is enabled for the Warning High alarm level."
        },
    )
    WaHHysOff: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether clear hysteresis is enabled for the Warning High alarm level."
        },
    )
    WaLHysOn: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether alarm hysteresis is enabled for the Warning Low alarm level."
        },
    )
    WaLHysOff: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether clear hysteresis is enabled for the Warning Low alarm level."
        },
    )
    CLHysOn: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether alarm hysteresis is enabled for the Critical Low alarm level."
        },
    )
    MiLHysOff: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether clear hysteresis is enabled for the Minor Low alarm level."
        },
    )
    MaLHysOn: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether alarm hysteresis is enabled for the Major Low alarm level."
        },
    )
    MaLHysOff: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether clear hysteresis is enabled for the Major Low alarm level."
        },
    )
    CHHysOff: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether clear hysteresis is enabled for the Critical High alarm level."
        },
    )
    CLHysOff: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether clear hysteresis is enabled for the Critical Low alarm level."
        },
    )
    MiLHysOn: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether alarm hysteresis is enabled for the Minor Low alarm level."
        },
    )
    CHHysOn: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether alarm hysteresis is enabled for the Critical High alarm level."
        },
    )
