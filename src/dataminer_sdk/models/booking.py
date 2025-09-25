from dataclasses import dataclass, field
from typing import Optional, List
from dataminer_sdk.models.base import BaseDMAType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMABookingProperty(BaseDMAType):
    """
    Represents DMA Booking Property.

    Attributes:
        Key (Optional[str]): The key of the booking property.
        Value (Optional[str]): The value of the booking property.
        Type (Optional[str]): The type of the booking property.
    """

    Key: Optional[str] = field(
        default=None, metadata={"doc": "The key of the booking property."}
    )
    Value: Optional[str] = field(
        default=None, metadata={"doc": "The value of the booking property."}
    )
    Type: Optional[str] = field(
        default=None, metadata={"doc": "The type of the booking property."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAResourceDefinition(BaseDMAType):
    """
    Represents DMA Resource Definition.

    Attributes:
        NodeID (Optional[str]): The service definition node ID.
        Resources (Optional[List[str]]): The resources assigned to the node.
    """

    NodeID: Optional[str] = field(
        default=None, metadata={"doc": "The service definition node ID."}
    )
    Resources: Optional[List[str]] = field(
        default=None, metadata={"doc": "The resources assigned to the node."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMABooking(BaseDMAType):
    """
    Represents DMA Booking.

    Attributes:
        Description (Optional[str]): The description of the booking.
        CreatedAt (Optional[int]): The time when the booking was created.
        CreatedBy (Optional[str]): The user who created the booking.
        LastModifiedAt (Optional[int]): The time when the booking was last modified.
        LastModifiedBy (Optional[str]): The user who last modified the booking.
        ResourceDefinitions (Optional[List[DMAResourceDefinition]]): The service definition node IDs and the resources assigned to those nodes.
        ServiceDefinition (Optional[List[str]]): The ID and name of the service definition.
        DataMinerID (Optional[int]): the DataMiner Agent ID.
        ServiceID (Optional[int]): The service ID.
        Properties (Optional[List[DMABookingProperty]]): The key, value and type of each booking property.
        ContributingResourceID (Optional[str]): The ID of the contributing resource.
    """

    Description: Optional[str] = field(
        default=None, metadata={"doc": "The description of the booking."}
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
    ResourceDefinitions: Optional[List[DMAResourceDefinition]] = field(
        default=None,
        metadata={
            "doc": "The service definition node IDs and the resources assigned to those nodes."
        },
    )
    ServiceDefinition: Optional[List[str]] = field(
        default=None, metadata={"doc": "The ID and name of the service definition."}
    )
    DataMinerID: Optional[int] = field(
        default=None, metadata={"doc": "the DataMiner Agent ID."}
    )
    ServiceID: Optional[int] = field(default=None, metadata={"doc": "The service ID."})
    Properties: Optional[List[DMABookingProperty]] = field(
        default=None,
        metadata={"doc": "The key, value and type of each booking property."},
    )
    ContributingResourceID: Optional[str] = field(
        default=None, metadata={"doc": "The ID of the contributing resource."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMABookingLite(BaseDMAType):
    """
    Represents DMA Booking Lite.

    Attributes:
        ID (Optional[str]): The GUID of the booking.
        Name (Optional[str]): The name of the booking.
        Description (Optional[str]): The description of the booking.
        CreatedAt (Optional[int]): The time when the booking was created.
        CreatedBy (Optional[str]): The user who created the booking.
        LastModifiedAt (Optional[int]): The time when the booking was last modified.
        LastModifiedBy (Optional[str]): The user who last modified the booking.
        StartTimeUTC (Optional[int]): The start time of the booking, in UTC format (milliseconds since midnight January 1, 1970 GMT).
        EndTimeUTC (Optional[int]): The start time of the booking, in UTC format (milliseconds since midnight January 1, 1970 GMT).
        State (Optional[str]): The current state of the booking.
        ContributingResourceID (Optional[str]): The ID of the contributing resource.
        ResourceDefinitions (Optional[List[DMAResourceDefinition]]): The service definition node IDs and the resources assigned to those nodes.
        Properties (Optional[List[DMABookingProperty]]): The key, value and type of each booking property.
    """

    ID: Optional[str] = field(
        default=None, metadata={"doc": "The GUID of the booking."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the booking."}
    )
    Description: Optional[str] = field(
        default=None, metadata={"doc": "The description of the booking."}
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
    StartTimeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The start time of the booking, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )
    EndTimeUTC: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The start time of the booking, in UTC format (milliseconds since midnight January 1, 1970 GMT)."
        },
    )
    State: Optional[str] = field(
        default=None, metadata={"doc": "The current state of the booking."}
    )
    ContributingResourceID: Optional[str] = field(
        default=None, metadata={"doc": "The ID of the contributing resource."}
    )
    ResourceDefinitions: Optional[List[DMAResourceDefinition]] = field(
        default=None,
        metadata={
            "doc": "The service definition node IDs and the resources assigned to those nodes."
        },
    )
    Properties: Optional[List[DMABookingProperty]] = field(
        default=None,
        metadata={"doc": "The key, value and type of each booking property."},
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMABookingManager(BaseDMAType):
    """
    Represents DMA Booking Manager.

    Attributes:
        DataMinerID (Optional[int]): The DataMiner ID of the DMA where the booking manager was originally created.
        ElementID (Optional[int]): The element ID of the booking manager.
        Name (Optional[str]): The name of the booking manager.
    """

    DataMinerID: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The DataMiner ID of the DMA where the booking manager was originally created."
        },
    )
    ElementID: Optional[int] = field(
        default=None, metadata={"doc": "The element ID of the booking manager."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the booking manager."}
    )
