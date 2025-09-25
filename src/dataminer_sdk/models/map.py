from dataclasses import dataclass, field
from typing import Optional, List
from dataminer_sdk.models.base import BaseDMAType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAMapURLParam(BaseDMAType):
    """
    Represents DMA Map URL Param.

    Attributes:
        Name (Optional[str]): The name of the map URL parameter.
        Type (Optional[str]): The type of map URL parameter.
    """

    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the map URL parameter."}
    )
    Type: Optional[str] = field(
        default=None, metadata={"doc": "The type of map URL parameter."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAMapConfigLite(BaseDMAType):
    """
    Represents DMA Map Config Lite.

    Attributes:
        ConfigName (Optional[str]): The name of the map configuration.
        URLParameters (Optional[List[DMAMapURLParam]]): See DMAMapURLParam.
    """

    ConfigName: Optional[str] = field(
        default=None, metadata={"doc": "The name of the map configuration."}
    )
    URLParameters: Optional[List[DMAMapURLParam]] = field(
        default=None, metadata={"doc": "See DMAMapURLParam."}
    )
