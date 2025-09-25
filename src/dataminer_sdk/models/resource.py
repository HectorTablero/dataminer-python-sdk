from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List, TYPE_CHECKING
from dataminer_sdk.models.base import BaseDMAType

if TYPE_CHECKING:
    from dataminer_sdk.models.property import DMAProperty


@dataclass(slots=True, frozen=True, kw_only=True)
class DMABookingBase(BaseDMAType):
    """
    Represents DMA Booking Base.

    Attributes:
        ID (Optional[str]): The ID of the booking.
        Name (Optional[str]): The name of the booking.
    """

    ID: Optional[str] = field(default=None, metadata={"doc": "The ID of the booking."})
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the booking."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMABookingsImpact(BaseDMAType):
    """
    Represents DMA Bookings Impact.

    Attributes:

    """

    # TODO: Research and fill in attributes
    pass


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAResource(BaseDMAType):
    """
    Represents DMA Resource.

    Attributes:
        ID (Optional[str]): The resource ID.
        Name (Optional[str]): The resource name.
        DataMinerID (Optional[int]): The DataMiner ID.
        ElementID (Optional[int]): The element ID.
        ElementName (Optional[str]): The element name.
        Properties (Optional[List[DMAProperty]]): The resource properties.
        PoolIDs (Optional[List[str]]): The resource pools.
    """

    ID: Optional[str] = field(default=None, metadata={"doc": "The resource ID."})
    Name: Optional[str] = field(default=None, metadata={"doc": "The resource name."})
    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "The DataMiner ID."}
    )
    ElementID: Optional[int] = field(default=None, metadata={"doc": "The element ID."})
    ElementName: Optional[str] = field(
        default=None, metadata={"doc": "The element name."}
    )
    Properties: Optional[List[DMAProperty]] = field(
        default=None, metadata={"doc": "The resource properties."}
    )
    PoolIDs: Optional[List[str]] = field(
        default=None, metadata={"doc": "The resource pools."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAResourceCapacityTrendPoint(BaseDMAType):
    """
    Represents DMA Resource Capacity Trend Point.

    Attributes:
        Time (Optional[int]): The time of the trend point.
        Value (Optional[float]): The capacity value.
        BookingsImpact (Optional[List[DMABookingsImpact]]): The total usage of the profile parameter for the bookings.
    """

    Time: Optional[int] = field(
        default=None, metadata={"doc": "The time of the trend point."}
    )
    Value: Optional[float] = field(
        default=None, metadata={"doc": "The capacity value."}
    )
    BookingsImpact: Optional[List[DMABookingsImpact]] = field(
        default=None,
        metadata={"doc": "The total usage of the profile parameter for the bookings."},
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAResourceCapacityTrend(BaseDMAType):
    """
    Represents DMA Resource Capacity Trend.

    Attributes:
        Bookings (Optional[List[DMABookingBase]]): Array of DMABookingBase objects, consisting of the ID (string) and Name (string) of the bookings.
        MaxQuantity (Optional[float]): The maximum capacity.
        QuantityUnit (Optional[str]): The unit of measure used for the capacity.
        ParameterName (Optional[str]): The name of the profile parameter.
        Points (Optional[List[DMAResourceCapacityTrendPoint]]): The trend points for the resource capacity.
    """

    Bookings: Optional[List[DMABookingBase]] = field(
        default=None,
        metadata={
            "doc": "Array of DMABookingBase objects, consisting of the ID (string) and Name (string) of the bookings."
        },
    )
    MaxQuantity: Optional[float] = field(
        default=None, metadata={"doc": "The maximum capacity."}
    )
    QuantityUnit: Optional[str] = field(
        default=None, metadata={"doc": "The unit of measure used for the capacity."}
    )
    ParameterName: Optional[str] = field(
        default=None, metadata={"doc": "The name of the profile parameter."}
    )
    Points: Optional[List[DMAResourceCapacityTrendPoint]] = field(
        default=None, metadata={"doc": "The trend points for the resource capacity."}
    )
