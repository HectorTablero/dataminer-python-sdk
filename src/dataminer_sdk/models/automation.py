from __future__ import annotations
from dataclasses import dataclass, field
from typing import Optional, List, TYPE_CHECKING
from dataminer_sdk.models.base import BaseDMAType

if TYPE_CHECKING:
    from dataminer_sdk.models.element import DMAElement


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAutomationScriptParameter(BaseDMAType):
    """
    Represents DMA Automation Script Parameter.

    Attributes:
        ParameterId (Optional[int]): The ID of the parameter within the script.
        Values (Optional[List[str]]): The available values of the parameter.
        MemoryFile (Optional[str]): The memory file linked to the parameter, if any.
        Name (Optional[str]): The name of the parameter.
        Value (Optional[str]): The selected value of the parameter.
    """

    ParameterId: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the parameter within the script."}
    )
    Values: Optional[List[str]] = field(
        default=None, metadata={"doc": "The available values of the parameter."}
    )
    MemoryFile: Optional[str] = field(
        default=None,
        metadata={"doc": "The memory file linked to the parameter, if any."},
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the parameter."}
    )
    Value: Optional[str] = field(
        default=None, metadata={"doc": "The selected value of the parameter."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAutomationScriptDummy(BaseDMAType):
    """
    Represents DMA Automation Script Dummy.

    Attributes:
        Element (Optional[DMAElement]): The optional configuration element for the dummy.
        ProtocolName (Optional[str]): The name of the protocol linked to the dummy.
        Name (Optional[str]): The name of the dummy.
        ProtocolVersion (Optional[str]): The version of the protocol linked to the dummy.
        ProtocolId (Optional[int]): The ID of the dummy within the script.
    """

    Element: Optional[DMAElement] = field(
        default=None,
        metadata={"doc": "The optional configuration element for the dummy."},
    )
    ProtocolName: Optional[str] = field(
        default=None, metadata={"doc": "The name of the protocol linked to the dummy."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the dummy."}
    )
    ProtocolVersion: Optional[str] = field(
        default=None,
        metadata={"doc": "The version of the protocol linked to the dummy."},
    )
    ProtocolId: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the dummy within the script."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAutomationScriptMemoryFile(BaseDMAType):
    """
    Represents DMA Automation Script Memory File.

    Attributes:
        Description (Optional[str]): The name of the memory file.
        MemoryId (Optional[int]): The ID of the memory file within the script.
        Volatile (Optional[bool]): Determines whether the memory file is volatile or persistent.
        Value (Optional[str]): The value associated with the memory file.
    """

    Description: Optional[str] = field(
        default=None, metadata={"doc": "The name of the memory file."}
    )
    MemoryId: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the memory file within the script."}
    )
    Volatile: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Determines whether the memory file is volatile or persistent."
        },
    )
    Value: Optional[str] = field(
        default=None, metadata={"doc": "The value associated with the memory file."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAutomationScript(BaseDMAType):
    """
    Represents DMA Automation Script.

    Attributes:
        Name (Optional[str]): The name of the Automation script.
        Folder (Optional[str]): The folder containing the Automation script.
        Description (Optional[str]): The description of the Automation script.
        Settings_RequireInteractive (Optional[bool]): Determines whether the script will require interaction from the user.
        Settings_HasFindInteractiveClient (Optional[bool]): Determines if a pop-up window will be displayed asking clients to attach to the script.
        Parameters (Optional[List[DMAAutomationScriptParameter]]): See DMAAutomationScriptParameter.
        Dummies (Optional[List[DMAAutomationScriptDummy]]): See DMAAutomationScriptDummy.
        MemoryFiles (Optional[List[DMAAutomationScriptMemoryFile]]): See DMAAutomationScriptMemoryFile.
    """

    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the Automation script."}
    )
    Folder: Optional[str] = field(
        default=None, metadata={"doc": "The folder containing the Automation script."}
    )
    Description: Optional[str] = field(
        default=None, metadata={"doc": "The description of the Automation script."}
    )
    Settings_RequireInteractive: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Determines whether the script will require interaction from the user."
        },
    )
    Settings_HasFindInteractiveClient: Optional[bool] = field(
        default=None,
        metadata={
            "doc": "Determines if a pop-up window will be displayed asking clients to attach to the script."
        },
    )
    Parameters: Optional[List[DMAAutomationScriptParameter]] = field(
        default=None, metadata={"doc": "See DMAAutomationScriptParameter."}
    )
    Dummies: Optional[List[DMAAutomationScriptDummy]] = field(
        default=None, metadata={"doc": "See DMAAutomationScriptDummy."}
    )
    MemoryFiles: Optional[List[DMAAutomationScriptMemoryFile]] = field(
        default=None, metadata={"doc": "See DMAAutomationScriptMemoryFile."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMAAutomationVariableInfo(BaseDMAType):
    """
    Represents DMA Automation Variable Info.

    Attributes:
        VariableName (Optional[str]): The name of the variable.
        VariableType (Optional[str]): The type of the variable.
    """

    VariableName: Optional[str] = field(
        default=None, metadata={"doc": "The name of the variable."}
    )
    VariableType: Optional[str] = field(
        default=None, metadata={"doc": "The type of the variable."}
    )
