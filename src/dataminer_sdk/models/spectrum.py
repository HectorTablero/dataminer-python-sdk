from dataclasses import dataclass, field
from typing import Optional, List
from dataminer_sdk.models.base import BaseDMAType


@dataclass(slots=True, frozen=True, kw_only=True)
class DMASpectrumBuffer(BaseDMAType):
    """
    Represents DMA Spectrum Buffer.

    Attributes:
        DataMinerID (Optional[int]): The DataMiner Agent ID of the element used to create the buffer.
        ElementID (Optional[int]): The element ID of the element used to create the buffer.
        MonitorID (Optional[int]): The ID of the spectrum monitor.
        TraceID (Optional[str]): The ID of the trace.
        MeasptID (Optional[int]): The ID of the measurement point.
        PresetID (Optional[str]): The ID of the preset.
        VariableID (Optional[str]): The name of the variable.
        DisplayName (Optional[str]): The name of the spectrum buffer.
    """

    DataMinerID: Optional[int] = field(
        default=None,
        metadata={
            "doc": "The DataMiner Agent ID of the element used to create the buffer."
        },
    )
    ElementID: Optional[int] = field(
        default=None,
        metadata={"doc": "The element ID of the element used to create the buffer."},
    )
    MonitorID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the spectrum monitor."}
    )
    TraceID: Optional[str] = field(
        default=None, metadata={"doc": "The ID of the trace."}
    )
    MeasptID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the measurement point."}
    )
    PresetID: Optional[str] = field(
        default=None, metadata={"doc": "The ID of the preset."}
    )
    VariableID: Optional[str] = field(
        default=None, metadata={"doc": "The name of the variable."}
    )
    DisplayName: Optional[str] = field(
        default=None, metadata={"doc": "The name of the spectrum buffer."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMASpectrumMeasptModel(BaseDMAType):
    """
    Represents DMA Spectrum Measpt Model.

    Attributes:
        ID (Optional[int]): The ID of the measurement point.
        DataMinerIDs (Optional[str]): The DMA ID(s) for the parameter set(s) used to set up the measurement point, if any. Multiple IDs are separated by semicolons.
        ElementIDs (Optional[str]): The element ID(s) for the parameter set(s) used to set up the measurement point, if any. Multiple IDs are separated by semicolons.
        ParamIDs (Optional[str]): The DMA ID(s) for the parameter set(s) used to set up the measurement point, if any. Multiple IDs are separated by semicolons.
        Name (Optional[str]): The name of the measurement point.
        IsStrings (Optional[str]): Indicates whether the parameter(s) used for the parameter set(s), if any, are of type string. Consists of “true” or “false” values, separated by semicolons.
        Values (Optional[str]): The values for the parameter set(s) used to set up the measurement point, if any. Multiple values are separated by semicolons.
        Delay (Optional[str]): The delay for parameter set verification (in ms).
        ServiceIDs (Optional[str]): The service ID(s) for the parameter set(s) used to set up the measurement point, if any. Multiple IDs are separated by semicolons.
        ReadParamIDs (Optional[str]): The DMA ID(s) for the parameter set(s) used to set up the measurement point, if any. Multiple IDs are separated by semicolons. While the ParamIDs field is used for the write parameters, this field is used for the corresponding read parameters.
        ParamIndices (Optional[str]): The index of the parameter for the parameter set(s) used to set up the measurement point, if any. Multiple indices are separated by semicolons.
        FreqOffset (Optional[str]): The frequency offset, used to shift the trace in frequency (optional). Specify the offset in Hz, without adding the unit of measure.
        InvertFreq (Optional[str]): Set to “true” or “false”, depending on whether the trace should be flipped around the center frequency.
        AutomationScript (Optional[str]): The Automation script used to set up the measurement point, if any.
        AmplitudeCorrectionInfo (Optional[str]): Amplitude correction information (optional), using the semicolon as separator within a single correction, and the separator “|” between corrections. For example, for an amplitude offset of +1 dB for frequencies higher than 1 kHz and +2dB for frequencies higher than 2 kHz, specify 1000;1|2000;2. Frequencies should be specified in Hz.
    """

    ID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the measurement point."}
    )
    DataMinerIDs: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The DMA ID(s) for the parameter set(s) used to set up the measurement point, if any. Multiple IDs are separated by semicolons."
        },
    )
    ElementIDs: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The element ID(s) for the parameter set(s) used to set up the measurement point, if any. Multiple IDs are separated by semicolons."
        },
    )
    ParamIDs: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The DMA ID(s) for the parameter set(s) used to set up the measurement point, if any. Multiple IDs are separated by semicolons."
        },
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the measurement point."}
    )
    IsStrings: Optional[str] = field(
        default=None,
        metadata={
            "doc": "Indicates whether the parameter(s) used for the parameter set(s), if any, are of type string. Consists of “true” or “false” values, separated by semicolons."
        },
    )
    Values: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The values for the parameter set(s) used to set up the measurement point, if any. Multiple values are separated by semicolons."
        },
    )
    Delay: Optional[str] = field(
        default=None,
        metadata={"doc": "The delay for parameter set verification (in ms)."},
    )
    ServiceIDs: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The service ID(s) for the parameter set(s) used to set up the measurement point, if any. Multiple IDs are separated by semicolons."
        },
    )
    ReadParamIDs: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The DMA ID(s) for the parameter set(s) used to set up the measurement point, if any. Multiple IDs are separated by semicolons. While the ParamIDs field is used for the write parameters, this field is used for the corresponding read parameters."
        },
    )
    ParamIndices: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The index of the parameter for the parameter set(s) used to set up the measurement point, if any. Multiple indices are separated by semicolons."
        },
    )
    FreqOffset: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The frequency offset, used to shift the trace in frequency (optional). Specify the offset in Hz, without adding the unit of measure."
        },
    )
    InvertFreq: Optional[str] = field(
        default=None,
        metadata={
            "doc": "Set to “true” or “false”, depending on whether the trace should be flipped around the center frequency."
        },
    )
    AutomationScript: Optional[str] = field(
        default=None,
        metadata={
            "doc": "The Automation script used to set up the measurement point, if any."
        },
    )
    AmplitudeCorrectionInfo: Optional[str] = field(
        default=None,
        metadata={
            "doc": "Amplitude correction information (optional), using the semicolon as separator within a single correction, and the separator “|” between corrections. For example, for an amplitude offset of +1 dB for frequencies higher than 1 kHz and +2dB for frequencies higher than 2 kHz, specify 1000;1|2000;2. Frequencies should be specified in Hz."
        },
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMASpectrumMonitor(BaseDMAType):
    """
    Represents DMA Spectrum Monitor.

    Attributes:
        ID (Optional[int]): The ID of the spectrum monitor.
        Name (Optional[str]): The name of the spectrum monitor.
    """

    ID: Optional[int] = field(
        default=None, metadata={"doc": "The ID of the spectrum monitor."}
    )
    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the spectrum monitor."}
    )


@dataclass(slots=True, frozen=True, kw_only=True)
class DMASpectrumPreset(BaseDMAType):
    """
    Represents DMA Spectrum Preset.

    Attributes:
        Name (Optional[str]): The name of the preset
        IsShared (Optional[bool]): Indicates whether the preset is shared.
        Settings (Optional[List[str]]): The preset data received from SLNetTypes. This array is filled in when a spectrum preset is loaded, but not when you request a list of all available presets.
    """

    Name: Optional[str] = field(
        default=None, metadata={"doc": "The name of the preset"}
    )
    IsShared: Optional[bool] = field(
        default=None, metadata={"doc": "Indicates whether the preset is shared."}
    )
    Settings: Optional[List[str]] = field(
        default=None,
        metadata={
            "doc": "The preset data received from SLNetTypes. This array is filled in when a spectrum preset is loaded, but not when you request a list of all available presets."
        },
    )
