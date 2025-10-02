from enum import Enum, auto


class TransportMode(Enum):
    SOAP = auto()
    URL = auto()


class SOAPVersion(Enum):
    SOAP11 = auto()
    SOAP12 = auto()
