from dataclasses import dataclass, field
from typing import Optional
from dataminer_sdk.models.base import BaseDMAType
from dataminer_sdk.models.enums import PropertyFilterMethodType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAProperty(BaseDMAType):
    """
    Represents DMA Property.

    Attributes:
        Name (Optional[str]): The name of the property.
        Value (Optional[str]): The value of the property.
        Type (Optional[str]): The type of property (alarm, element, etc.).
    """

    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the property."}
    )
    Value: Optional[str] = field(
        default=None, metadata={"doc": "The value of the property."}
    )
    # TODO: Convert to Enum
    Type: Optional[str] = field(
        default=None, metadata={"doc": "The type of property (alarm, element, etc.)."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAPropertyFilter(BaseDMAType):
    """
    Represents DMA Property Filter.

    Attributes:
        Method (Optional[PropertyFilterMethodType]): The method used for filtering: equal, not-equal, contains or not-contains.
        ID (Optional[str]): The ID of the field that is being filtered on: PropertyExposers.Name or PropertyExposers.Value.
        Value (Optional[str]): A string that allows DataMiner to filter based on the value identified in the ID field.
    """

    Method: Optional[PropertyFilterMethodType] = field(
        default=None,
        metadata={
            "doc": "The method used for filtering: equal, not-equal, contains or not-contains."
        },
    )
    ID: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The ID of the field that is being filtered on: PropertyExposers.Name or PropertyExposers.Value."
        },
    )
    Value: Optional[str] = field(
        default=None,
        metadata={
            "doc": "A string that allows DataMiner to filter based on the value identified in the ID field."
        },
    )
