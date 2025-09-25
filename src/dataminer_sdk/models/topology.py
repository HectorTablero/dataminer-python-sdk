from dataclasses import dataclass, field
from typing import Optional, List
from dataminer_sdk.models.base import BaseDMAType
from dataminer_sdk.models.enums import TopologyChainsType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMATopologyFieldValue(BaseDMAType):
    """
    Represents DMA Topology Field Value.

    Attributes:
        Index (Optional[str]): The index of the topology field value.
        Value (Optional[str]): The value of the topology field value.
    """

    Index: Optional[str] = field(
        default=None, metadata={"doc": "The index of the topology field value."}
    )
    Value: Optional[str] = field(
        default=None, metadata={"doc": "The value of the topology field value."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMATopologyFieldValues(BaseDMAType):
    """
    Represents DMA Topology Field Values.

    Attributes:
        Values (Optional[List[DMATopologyFieldValue]]): Array consisting of the index (string) and the value (string) for each DMA topology field value.
        PageCount (Optional[int]): The total page count of the results.
        CurrentPage (Optional[int]): The number of the current page.
    """

    Values: Optional[List[DMATopologyFieldValue]] = field(
        default=None,
        metadata={
            "doc": "Array consisting of the index (string) and the value (string) for each DMA topology field value."
        },
    )
    PageCount: Optional[int] = field(
        default=None, metadata={"doc": "The total page count of the results."}
    )
    CurrentPage: Optional[int] = field(
        default=None, metadata={"doc": "The number of the current page."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMATopologyChainsField(BaseDMAType):
    """
    Represents DMA Topology Chains Field.

    Attributes:
        Name (Optional[str]): The name of the field.
        FieldPID (Optional[int]): The parameter ID used to request the possible field values (e.g. with the method GetValuesForCPETopologyField).
        TableIndexPID (Optional[int]): The parameter ID of the column that is filtered in order to get the parameters (with the method GetParametersForCPEChain) or the possible values (with the method GetValuesForCPETopologyField).
        TablePID (Optional[int]): The parameter ID of the table.
        Type (Optional[TopologyChainsType]): The type of selector, which is either “combo”, denoting a drop-down list, or “edit”, denoting a text input field.
        Childs (Optional[List[DMATopologyChainsField]]): An array containing the same properties as the parent DMATopologyChainsField array, but without further child items.
    """

    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the field."}
    )
    FieldPID: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The parameter ID used to request the possible field values (e.g. with the method GetValuesForCPETopologyField)."
        },
    )
    TableIndexPID: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The parameter ID of the column that is filtered in order to get the parameters (with the method GetParametersForCPEChain) or the possible values (with the method GetValuesForCPETopologyField)."
        },
    )
    TablePID: Optional[int] = field(
        default=None, metadata={"doc": "The parameter ID of the table."}
    )
    Type: Optional[TopologyChainsType] = field(
        default=None,
        metadata={
            "doc": "The type of selector, which is either “combo”, denoting a drop-down list, or “edit”, denoting a text input field."
        },
    )
    Childs: Optional[List["DMATopologyChainsField"]] = field(
        default=None,
        metadata={
            "doc": "An array containing the same properties as the parent DMATopologyChainsField array, but without further child items."
        },
    )
