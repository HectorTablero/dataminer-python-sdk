from __future__ import annotations
from dataclasses import fields, is_dataclass
from typing import Any, get_origin, get_args, Optional, Type
import xml.etree.ElementTree as ET


def _convert_value(value: str, target_type: Type) -> Any:
    """Convert a string value from XML into the appropriate Python type."""
    if value is None:
        return None

    origin = get_origin(target_type)
    args = get_args(target_type)

    # Handle Optional[X]
    if origin is Optional and args:
        return _convert_value(value, args[0])

    # Handle builtins
    if target_type is str:
        return value
    if target_type is int:
        return int(value)
    if target_type is float:
        return float(value)
    if target_type is bool:
        return value.lower() in ("true", "1")

    # Handle Enums
    if hasattr(target_type, "__members__"):
        return target_type[value] # type: ignore

    return value


def _from_xml(element: ET.Element, cls: Type) -> Any:
    """Recursively build a dataclass or list from an XML element."""
    if not is_dataclass(cls):
        raise ValueError(f"{cls} is not a dataclass")

    kwargs = {}
    for f in fields(cls):
        f_type = f.type
        origin = get_origin(f_type)
        args = get_args(f_type)

        # Handle List[T]
        if origin is list and args:
            child_cls = args[0]
            items = []
            for child in element.findall(f.name + "/*") or element.findall(f.name):
                items.append(_from_xml(child, child_cls) if is_dataclass(child_cls) else _convert_value(child.text, child_cls)) # type: ignore
            kwargs[f.name] = items
            continue

        # Normal single-value field
        xml_child = element.find(f.name)
        if xml_child is None or xml_child.text is None:
            kwargs[f.name] = None
        elif is_dataclass(f_type):
            kwargs[f.name] = _from_xml(xml_child, f_type) # type: ignore
        else:
            kwargs[f.name] = _convert_value(xml_child.text, f_type) # type: ignore

    return cls(**kwargs)


def parse_xml_response(xml: str, result_cls: Type, is_array: bool = False) -> Any:
    """
    Parse an XML response and map it into the given dataclass.
    If `is_array=True`, returns a list of dataclasses instead of a single one.
    """
    root = ET.fromstring(xml)

    # Strip namespaces
    for elem in root.iter():
        if "}" in elem.tag:
            elem.tag = elem.tag.split("}", 1)[1]

    # Find first element ending with 'Result'
    result_element = None
    for child in root.iter():
        if child.tag.endswith("Result"):
            result_element = child
            break

    if result_element is None:
        raise ValueError("No {Method}Result found in response.")
    
    if is_array:
        return [_from_xml(item, result_cls) for item in result_element.findall(result_cls.__name__)]
    else:
        if result_cls in [str, int, float, bool]:
            return _convert_value(result_element.text or "", result_cls)
        payload = list(result_element)[0]
        return _from_xml(payload, result_cls)