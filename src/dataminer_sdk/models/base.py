from dataclasses import dataclass, fields
from typing import Any, Optional
import json
import xml.etree.ElementTree as ET


@dataclass(slots=True, frozen=True)
class BaseDMAType:
    """Base class for all DMA custom types."""

    def to_dict(self) -> dict:
        """Convert to dictionary, recursively serializing dataclasses."""

        def serialize(value: Any) -> Any:
            if isinstance(value, BaseDMAType):
                return value.to_dict()
            elif isinstance(value, list):
                return [serialize(v) for v in value]
            return value

        return {f.name: serialize(getattr(self, f.name)) for f in fields(self)}

    def to_json(self, **json_kwargs) -> str:
        """Convert to JSON string."""
        return json.dumps(self.to_dict(), **json_kwargs)

    def to_xml(self, root_name: Optional[str] = None) -> str:
        """Convert to XML string."""
        if root_name is None:
            root_name = self.__class__.__name__

        def build_xml(elem: ET.Element, value: Any, name: str):
            if isinstance(value, BaseDMAType):
                child = ET.SubElement(elem, name)
                for k, v in value.to_dict().items():
                    build_xml(child, v, k)
            elif isinstance(value, list):
                for item in value:
                    build_xml(elem, item, name)
            elif value is not None:
                child = ET.SubElement(elem, name)
                child.text = str(value)

        root = ET.Element(root_name)
        for f in fields(self):
            value = getattr(self, f.name)
            build_xml(root, value, f.name)

        return ET.tostring(root, encoding="unicode")
