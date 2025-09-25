from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List, TYPE_CHECKING
from dataminer_sdk.models.base import BaseDMAType
from dataminer_sdk.models.enums import iStatus

if TYPE_CHECKING:
    from dataminer_sdk.models.parameter import DMAParameterEditDiscreet


@dataclass(slots=True, frozen=True, kw_only=True)
class AnalogTrendDataResponseMessage(BaseDMAType):
    """
    Represents Analog Trend Data Response Message.

    Attributes:
        Avg (Optional[List[float]]): The trend values (average trending).
        Max (Optional[List[float]]): The maximum values (only in case of average trending).
        Min (Optional[List[float]]): The minimum values (only in case of average trending).
        StartTime (Optional[int]): The timestamp of the first trend value.
        EndTime (Optional[int]): The timestamp of the last trend value.
        ParameterID (Optional[int]): The parameter ID.
        ParameterIdx (Optional[str]): The display key of the table row (in case the parameter is a table parameter).
        HasFailed (Optional[bool]): Whether or not the request for trend data failed.
        FailReason (Optional[str]): If the requested trend data could not be retrieved, this field will contain the error message.
        Data (Optional[List[float]]): The trend values (real-time trending or average trending).
        Timestamps (Optional[List[int]]): The timestamps of the data points in Avg, Max, Min and Status.
        Status (Optional[List[iStatus]]): iStatus values: 0, 5, 60, ..., or negative values indicating gaps in the graph.
    """

    Avg: Optional[List[float]] = field(
        default=None, metadata={"doc": "The trend values (average trending)."}
    )
    Max: Optional[List[float]] = field(
        default=None,
        metadata={"doc": "The maximum values (only in case of average trending)."},
    )
    Min: Optional[List[float]] = field(
        default=None,
        metadata={"doc": "The minimum values (only in case of average trending)."},
    )
    StartTime: Optional[int] = field(
        default=None, metadata={"doc": "The timestamp of the first trend value."}
    )
    EndTime: Optional[int] = field(
        default=None, metadata={"doc": "The timestamp of the last trend value."}
    )
    ParameterID: Optional[int] = field(
        default=None, metadata={"doc": "The parameter ID."}
    )
    ParameterIdx: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The display key of the table row (in case the parameter is a table parameter)."
        },
    )
    HasFailed: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the request for trend data failed."},
    )
    FailReason: Optional[str] = field(
        default=None,
        metadata={
            "doc": "If the requested trend data could not be retrieved, this field will contain the error message."
        },
    )
    Data: Optional[List[float]] = field(
        default=None,
        metadata={"doc": "The trend values (real-time trending or average trending)."},
    )
    Timestamps: Optional[List[int]] = field(
        default=None,
        metadata={
            "doc": "The timestamps of the data points in Avg, Max, Min and Status."
        },
    )
    Status: Optional[List[iStatus]] = field(
        default=None,
        metadata={
            "doc": "iStatus values: 0, 5, 60, ..., or negative values indicating gaps in the graph."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMATrendData(BaseDMAType):
    """
    Represents DMA Trend Data.

    Attributes:
        Avg (Optional[List[float]]): The trend values (which can be either average trending or real-time trending).
        Min (Optional[List[float]]): The minimum values (only in case of average trending).
        Max (Optional[List[float]]): The maximum values (only in case of average trending).
        Timestamps (Optional[List[int]]): The timestamps in UTC format (milliseconds since midnight January 1, 1970 GMT). Note that these values should be divided by 1000 to get the correct boundary values.
        StartTime (Optional[int]): The timestamp of the first date value, in UTC format (milliseconds since midnight January 1, 1970 GMT).
        EndTime (Optional[int]): The timestamp of the last date value, in UTC format (milliseconds since midnight January 1, 1970 GMT).
        Error (Optional[str]): If the requested trend data could not be retrieved, this field will contain the error message.
        Units (Optional[str]): The unit of measure of the trend values.
        Logarithmic (Optional[bool]): Whether the graph has to be drawn logarithmically.
        Exceptions (Optional[List[DMAParameterEditDiscreet]]): The exception values (by which the trend values will be replaced if necessary).
        Discreets (Optional[List[DMAParameterEditDiscreet]]): The discreet values (by which the trend values will be replaced if necessary).
    """

    Avg: Optional[List[float]] = field(
        default=None,
        metadata={
            "doc": "The trend values (which can be either average trending or real-time trending)."
        },
    )
    Min: Optional[List[float]] = field(
        default=None,
        metadata={"doc": "The minimum values (only in case of average trending)."},
    )
    Max: Optional[List[float]] = field(
        default=None,
        metadata={"doc": "The maximum values (only in case of average trending)."},
    )
    Timestamps: Optional[List[int]] = field(
        default=None,
        metadata={
            "doc": "The timestamps in UTC format (milliseconds since midnight January 1, 1970 GMT). Note that these values should be divided by 1000 to get the correct boundary values."
        },
    )
    StartTime: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The timestamp of the first date value, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )
    EndTime: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The timestamp of the last date value, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )
    Error: Optional[str] = field(
        default=None,
        metadata={
            "doc": "If the requested trend data could not be retrieved, this field will contain the error message."
        },
    )
    Units: Optional[str] = field(
        default=None, metadata={"doc": "The unit of measure of the trend values."}
    )
    Logarithmic: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether the graph has to be drawn logarithmically."},
    )
    Exceptions: Optional[List[DMAParameterEditDiscreet]] = field(
        default=None,
        metadata={
            "doc": "The exception values (by which the trend values will be replaced if necessary)."
        },
    )
    Discreets: Optional[List[DMAParameterEditDiscreet]] = field(
        default=None,
        metadata={
            "doc": "The discreet values (by which the trend values will be replaced if necessary)."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMATrendDataStatisticsService(BaseDMAType):
    """
    Represents DMA Trend Data Statistics Service.

    Attributes:
        DataMinerID (Optional[int]): The DataMiner ID.
        ElementID (Optional[int]): The element ID.
        ParameterID (Optional[int]): The parameter ID.
    """

    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The DataMiner ID."}
    )
    ElementID: Optional[int] = field(default=None, metadata={"doc": "The element ID."})
    ParameterID: Optional[int] = field(
        default=None, metadata={"doc": "The parameter ID."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMABaseline(BaseDMAType):
    """
    Represents DMA Baseline.

    Attributes:
        Enable (Optional[bool]): Whether automatic updating of the baselines is enabled.
        Cyclic (Optional[bool]): Whether the baselines are update to detect a change in the daily pattern or not.
        HandleWeekends (Optional[bool]): Whether weekends are handled separately or not.
        IntervalCount (Optional[int]): The number of days of the trend window to detect a deviation in the expected daily pattern.
        IntervalLength (Optional[int]): The number of days (in seconds, e.g. 1 day = 86400) of the trend window to detect a continuous degradation.
        IntervalOffset (Optional[int]): In case the last X hours in the configured trend window need to be skipped, this item indicates this number of hours, expressed in seconds (e.g. 1 hour = 3600).
        AverageType (Optional[str]): Not used.
    """

    Enable: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether automatic updating of the baselines is enabled."},
    )
    Cyclic: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Whether the baselines are update to detect a change in the daily pattern or not."
        },
    )
    HandleWeekends: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether weekends are handled separately or not."},
    )
    IntervalCount: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The number of days of the trend window to detect a deviation in the expected daily pattern."
        },
    )
    IntervalLength: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The number of days (in seconds, e.g. 1 day = 86400) of the trend window to detect a continuous degradation."
        },
    )
    IntervalOffset: Optional[int] = field(
        default=None,
        metadata={
            "doc": "In case the last X hours in the configured trend window need to be skipped, this item indicates this number of hours, expressed in seconds (e.g. 1 hour = 3600)."
        },
    )
    AverageType: Optional[str] = field(default=None, metadata={"doc": "Not used."})


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAggregationRule(BaseDMAType):
    """
    Represents DMA Aggregation Rule.

    Attributes:
        ID (Optional[str]): The aggregation rule GUID.
        Folder (Optional[str]): The folder of the aggregation rule.
        Name (Optional[str]): The aggregation rule name.
        IsEnabled (Optional[bool]): Whether or not the aggregation rule is enabled.
    """

    ID: Optional[str] = field(
        default=None, metadata={"doc": "The aggregation rule GUID."}
    )
    Folder: Optional[str] = field(
        default=None, metadata={"doc": "The folder of the aggregation rule."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The aggregation rule name."}
    )
    IsEnabled: Optional[bool] = field(
        default=None,
        metadata={"doc": "Whether or not the aggregation rule is enabled."},
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAggregationTableColumn(BaseDMAType):
    """
    Represents DMA Aggregation Table Column.

    Attributes:
        Name (Optional[str]): The name of the aggregation rule.
        ID (Optional[int]): The aggregation rule ID.
        IsNumber (Optional[bool]): Indicates whether the column contains numeric values (integers or decimals).
        MaxValue (Optional[float]): If IsNumber is true, this property contains the highest number of the column.
        MinValue (Optional[float]): If IsNumber is true, this property contains the lowest number of the column.
    """

    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the aggregation rule."}
    )
    ID: Optional[int] = field(
        default=None, metadata={"doc": "The aggregation rule ID."}
    )
    IsNumber: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the column contains numeric values (integers or decimals)."
        },
    )
    MaxValue: Optional[float] = field(
        default=None,
        metadata={
            "doc": "If IsNumber is true, this property contains the highest number of the column."
        },
    )
    MinValue: Optional[float] = field(
        default=None,
        metadata={
            "doc": "If IsNumber is true, this property contains the lowest number of the column."
        },
    )
