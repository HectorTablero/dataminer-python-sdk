from enum import IntEnum, StrEnum


# --- Alarm Enums ---


class DMAComparerType(IntEnum):
    EQUALS = 0
    NOT_EQUALS = 1
    LESS_THAN = 2
    GREATER_THAN = 3
    WILDCARD_EQUALS = 4
    WILDCARD_NOT_EQUALS = 5


class AlarmStateType(StrEnum):
    UNDEFINED = "Undefined"
    NORMAL = "Normal"
    WARNING = "Warning"
    MINOR = "Minor"
    MAJOR = "Major"
    CRITICAL = "Critical"
    CLEARED = "Cleared"


# --- Misc Enums ---


class DMAStatusType(StrEnum):
    DISCONNECTED = "Disconnected"
    RUNNING = "Running"
    STARTING = "Starting"
    UNKNOWN = "Unknown"
    SWITCHING = "Switching"


class DMAPropertyType(StrEnum):
    STRING = "String"
    INTEGER = "Integer"
    DOUBLE = "Double"
    LONG = "Long"
    BOOLEAN = "Boolean"
    ARRAY = "Array"


class FlowControlType(StrEnum):
    NO = "No"
    CTS_RTS = "CTS_RTS"
    CTS_DTR = "CTS_DTR"
    DSR_RTS = "DSR_RTS"
    DSR_DTR = "DSR_DTR"
    XON_XOFF = "XON_XOFF"


class ParityType(StrEnum):
    NO = "No"
    EVEN = "Even"
    ODD = "Odd"
    MARK = "Mark"
    SPACE = "Space"


class SerialType(StrEnum):
    SERIAL = "Serial"
    TCP = "TCP"
    UDP = "UDP"


class RecentType(StrEnum):
    ELEMENT = "Element"
    SERVICE = "Service"


# --- Element Enums ---


class AuthType(StrEnum):
    HMAC_MD5 = "HMAC_MD5"
    HMAC_SHA = "HMAC_SHA"


class PrivType(StrEnum):
    DES = "DES"
    AES128 = "AES128"


class SecurityLevelType(StrEnum):
    AUTH_PRIV = "authPriv"
    AUTH_NO_PRIV = "authNoPriv"
    NO_AUTH_NO_PRIV = "noAuthNoPriv"


class ElementObjectType(StrEnum):
    ELEMENT = "Element"
    SERVICE = "Service"
    REDUNDANCY_GROUP = "Redundancy Group"


class SlowPollType(StrEnum):
    TIME = "TIME"
    NUMBER = "NUMBER"
    NO = "NO"


class ElementStateType(StrEnum):
    UNDEFINED = "Undefined"
    ACTIVE = "Active"
    HIDDEN = "Hidden"
    PAUSED = "Paused"
    STOPPED = "Stopped"
    DELETED = "Deleted"
    ERROR = "Error"
    RESTART = "Restart"
    MASKED = "Masked"


# --- Job Enums ---


class JobSectionType(StrEnum):
    FIELDS = "Fields"
    BOOKING = "Booking"


# --- Parameter Enums ---


class ParameterType(StrEnum):
    READ = "Read"
    WRITE = "Write"
    TABLE = "Table"


class DashboardType(StrEnum):
    NONE = "None"
    BUTTON_PANEL = "ButtonPanel"
    BUTTON_PANEL_CONTAINERS = "ButtonPanelContainers"
    BUTTON_PANEL_COLLECTION = "ButtonPanelCollection"


class ParameterStyleType(StrEnum):
    NONE = "None"
    NUMBER = "Number"
    LOWERCASE = "Lowercase"
    UPPERCASE = "Uppercase"
    HORIZONTAL_SCROLL = "HorizontalScroll"
    PASSWORD = "Password"


# --- Property Enums ---


class PropertyFilterMethodType(StrEnum):
    EQUAL = "equal"
    NOT_EQUAL = "not-equal"
    CONTAINS = "contains"
    NOT_CONTAINS = "not-contains"


# --- Redundancy Enums ---


class RedundancyType(StrEnum):
    PRIMARY = "Primary"
    BACKUP = "Backup"
    STATE = "State"


class RedundancyStatusType(StrEnum):
    PRIMARY_OPERATIONAL = "Primary is operational"
    BACKUP_OPERATIONAL = "Backup is operational"
    UNAVAILABLE = "Unavailable"
    ERROR = "Error"
    SWITCHING = "Switching"


class RedundancyGroupStatusType(StrEnum):
    UNDEFINED = "Undefined"
    AVAILABLE = "Available"
    OPERATIONAL = "Operational"
    UNAVAILABLE = "Unavailable"
    ERROR = "Error"
    SWITCHING = "Switching"


class RedundancyGroupModeType(StrEnum):
    UNDEFINED = "Undefined"
    AUTOMATIC = "Automatic"
    MANUAL_SWITCH_BACK = "ManualSwitchBack"
    MANUAL = "Manual"


# --- Search Enums ---


class SearchType(StrEnum):
    ELEMENT = "Element"
    SERVICE = "Service"
    VIEW = "View"


# --- Section Enums ---


class SectionDefinitionFieldType(StrEnum):
    STRING = "string"
    DOUBLE = "double"
    LONG = "long"
    DATETIME = "DateTime"
    TIMESPAN = "TimeSpan"
    BOOL = "bool"


# --- Service Enums ---


class ServiceConfigurationTriggerType(StrEnum):
    CORRELATION = "Correlation"
    ALARM = "Alarm"
    ELEMENT_STATE = "ElementState"
    PARAMETER = "Parameter"
    MANUAL = "Manual"
    PROPERTY = "Property"
    CONNECTIVITY = "Connectivity"


class ServiceConfigurationTriggerConditionType(StrEnum):
    EQUAL = "equal"
    NOT_EQUAL = "not-equal"
    EXISTS_ROW = "exists row"
    MORE = "more"
    LESS = "less"
    MORE_OR_EQUAL = "more or equal"
    LESS_OR_EQUAL = "less or equal"


class ServiceDefinitionType(StrEnum):
    DEFAULT = "Default"
    PROCESS_AUTOMATION = "ProcessAutomation"
    CUSTOM_PROCESS_AUTOMATION = "CustomProcessAutomation"


class ServiceTemplateGlobalConditionType(StrEnum):
    NONE = "None"
    EQUALS = "Equals"
    WILDCARD = "WildCard"
    CONTAINSROW = "ContainsRow"


class ServiceTemplateMissingDataType(StrEnum):
    UNDEFINED = "Undefined"
    TEXT = "Text"
    DROPDOWN = "DropDown"
    HIDDEN = "Hidden"
    CHECKBOX = "CheckBox"
    HIDDENFROMSCREEN = "HiddenFromScreen"


# --- Ticket Enums ---


class TicketFieldType(StrEnum):
    BOOLEAN = "Boolean"
    DOUBLE = "Double"
    DATETIME = "DateTime"
    DATAMINER_OBJECT = "DataMiner Object"
    DROPDOWN = "DropDown"
    EMAIL = "Email"
    INTEGER = "Integer"
    TEXT = "Text"
    URL = "Url"
    USER = "User"
    STATE = "State"


class ResourceType(StrEnum):
    ELEMENT = "Element"
    SERVICE = "Service"
    REDUNDANCY_GROUP = "Redundancy Group"
    ALARM = "Alarm"
    VIEW = "View"


# --- Trend Enums ---


class iStatus(IntEnum):
    DAILY_AVERAGE = 120
    HOURLY_AVERAGE = 60
    FIVE_MINUTE_AVERAGE = 5
    REAL_TIME = 0
    ELEMENT_STARTING = -1
    ELEMENT_PAUSING = -2
    ELEMENT_ACTIVATING = -3
    ELEMENT_TIMEOUT = -4
    ELEMENT_TIMEOUT_END = -5
    ELEMENT_STOPPING = -6
    STATE_DISPLAY_VALUE = -7
    NORMAL_VALUE_AFTER_STATE = -8
    TRENDING_STARTED = -9
    TRENDING_STOPPED = -10
    PARAMETER_CLEARED = -11
    PARAMETER_VALUE_AFTER_CLEAR = -12
    FIRST_VALUE_SINCE_START = -13
    FIRST_EXCEPTION_VALUE_SINCE_START = -14
    ROW_ADDED = -15
    ROW_DELETED = -16
    MONITORING_ACTIVATED = -17
    MONITORING_DEACTIVATED = -18


# --- Topology Enums ---


class TopologyChainsType(StrEnum):
    COMBO = "combo"
    EDIT = "edit"


# --- Visio Enums ---


class VisioRegionActionType(StrEnum):
    CARD = "Card"
    SCRIPT = "Script"
    NAVIGATE = "Navigate"
    WEBLINK = "WebLink"
    SET = "Set"
    RESETLATCH = "ResetLatch"
    REDUNDANCYGROUPSWITCH = "RedundancyGroupSwitch"
    SETVAR = "SetVar"
    POPUP = "Popup"


class VisioRegionShapeType(StrEnum):
    RECT = "rect"
    CIRCLE = "circle"
    POLY = "poly"


class VisioRegionContentType(StrEnum):
    ACTION = "Action"
    URL = "Url"
    SCROLL = "Scroll"
    PARAMETERCONTROL = "ParameterControl"
    SETVARCONTROL = "SetVarControl"


class VisioRegionType(StrEnum):
    NAVIGATEVIEW = "NavigateView"
    NAVIGATEELEMENT = "NavigateElement"
    NAVIGATESERVICE = "NavigateService"
    URL = "Url"
    SCROLL = "Scroll"
    PARAMETERCONTROL = "ParameterControl"
    SETVARCONTROL = "SetVarControl"
