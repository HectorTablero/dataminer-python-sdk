from dataclasses import dataclass, field
from typing import Optional, List
from dataminer_sdk.models.base import BaseDMAType
from dataminer_sdk.models.enums import ElementStateType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMASLAElementConfiguration(BaseDMAType):
    """
    Represents DMA SLA Element Configuration.

    Attributes:
        Name (Optional[str]): The name of the SLA element. A limit of at most 150 characters applies.
        Service (Optional[List[int]]): Array consisting of the DataMinerID and service ID of the service monitored by the SLA.
        Description (Optional[str]): The description of the SLA.
        ProtocolName (Optional[str]): The name of the SLA protocol.
        ProtocolVersion (Optional[str]): The version of the SLA protocol.
        AlarmTemplate (Optional[str]): The alarm template used to monitor the SLA element.
        TrendTemplate (Optional[str]): The trend template used to track the SLA element’s trend data.
        ForceAgent (Optional[str]): Used in a Failover setup to always make the SLA element run on a particular DMA.
        IsHidden (Optional[bool]): Indicates whether the SLA element is hidden.
        IsReadOnly (Optional[bool]): Indicates whether the SLA element is a read-only element.
        IsReplicationActive (Optional[bool]): Indicates whether the SLA element is replicated.
        State (Optional[ElementStateType]): The element state, which can be Undefined, Active, Hidden, Paused, Stopped, Deleted, Error, Restart or Masked.
    """

    Name: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The name of the SLA element. A limit of at most 150 characters applies."
        },
    )
    Service: Optional[List[int]] = field(
        default=None,
        metadata={
            "doc": "Array consisting of the DataMinerID and service ID of the service monitored by the SLA."
        },
    )
    Description: Optional[str] = field(
        default=None, metadata={"doc": "The description of the SLA."}
    )
    ProtocolName: Optional[str] = field(
        default=None, metadata={"doc": "The name of the SLA protocol."}
    )
    ProtocolVersion: Optional[str] = field(
        default=None, metadata={"doc": "The version of the SLA protocol."}
    )
    AlarmTemplate: Optional[str] = field(
        default=None,
        metadata={"doc": "The alarm template used to monitor the SLA element."},
    )
    TrendTemplate: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The trend template used to track the SLA element’s trend data."
        },
    )
    ForceAgent: Optional[str] = field(
        default=None,
        metadata={
            "doc": "Used in a Failover setup to always make the SLA element run on a particular DMA."
        },
    )
    IsHidden: Optional[bool] = field(
        default=None, metadata={"doc": "Indicates whether the SLA element is hidden."}
    )
    IsReadOnly: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the SLA element is a read-only element."},
    )
    IsReplicationActive: Optional[bool] = field(
        default=None,
        metadata={"doc": "Indicates whether the SLA element is replicated."},
    )
    State: Optional[ElementStateType] = field(
        default=None,
        metadata={
            "doc": "The element state, which can be Undefined, Active, Hidden, Paused, Stopped, Deleted, Error, Restart or Masked."
        },
    )
