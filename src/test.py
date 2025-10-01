from __future__ import annotations
from dataclasses import fields, is_dataclass
from typing import Any, get_origin, get_args, Optional, Type
import xml.etree.ElementTree as ET

from dataminer_sdk.models import DMAParameter, DMAAlarm


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
        payload = list(result_element)[0]
        return _from_xml(payload, result_cls)


if __name__ == "__main__":
    xml = """<?xml version="1.0" encoding="utf-8"?>
    <GetParameterResponse xmlns="http://www.skyline.be/api/v1">
    <GetParameterResult>
        <DMAParameter>
            <DataMinerID>12</DataMinerID>
            <ElementID>34</ElementID>
            <TableIndex>row-1</TableIndex>
            <Value>42</Value>
            <DisplayValue>42.0</DisplayValue>
            <LastValueChange>2025-09-01T10:00:00</LastValueChange>
            <LastValueChangeUTC>1693562400000</LastValueChangeUTC>
            <AlarmState>Normal</AlarmState>
            <Filters></Filters>
            <LastChangeUTC>1693562400000</LastChangeUTC>
        </DMAParameter>
    </GetParameterResult>
    </GetParameterResponse>
    """

    param = parse_xml_response(xml, DMAParameter)
    print("Param (obj):", param)
    print()
    print("Param (json):", param.to_json())
    print()
    print("Param (xml):", param.to_xml())

    print("\n\n")

    xml = """<?xml version="1.0" encoding="utf-8"?>
    <GetActiveAlarmsForViewV2Response xmlns="http://www.skyline.be/api/v1">
    <GetActiveAlarmsForViewV2Result>
        <DMAAlarm>
            <DataMinerID>1</DataMinerID>
            <HostingAgentID>5</HostingAgentID>
            <ID>1234</ID>
            <ElementID>42</ElementID>
            <ElementName>MyElement</ElementName>
            <IsElementMasked>false</IsElementMasked>
            <ParameterID>77</ParameterID>
            <ParameterName>Signal Level</ParameterName>
            <DisplayValue>-23.5</DisplayValue>
            <AlarmState>Critical</AlarmState>
            <Type>New Alarm</Type>
            <IsAggregation>false</IsAggregation>
            <IsMasked>false</IsMasked>
            <TimeOfArrival>2025-09-30T10:15:00</TimeOfArrival>
            <TimeOfArrivalUTC>1769925300000</TimeOfArrivalUTC>
            <IsCleared>false</IsCleared>
        </DMAAlarm>
        <DMAAlarm>
            <DataMinerID>2</DataMinerID>
            <HostingAgentID>6</HostingAgentID>
            <ID>5678</ID>
            <ElementID>99</ElementID>
            <ElementName>OtherElement</ElementName>
            <IsElementMasked>false</IsElementMasked>
            <ParameterID>11</ParameterID>
            <ParameterName>Temperature</ParameterName>
            <DisplayValue>55</DisplayValue>
            <AlarmState>Warning</AlarmState>
            <Type>Escalated From Normal</Type>
            <IsAggregation>false</IsAggregation>
            <IsMasked>false</IsMasked>
            <TimeOfArrival>2025-09-30T11:00:00</TimeOfArrival>
            <TimeOfArrivalUTC>1769928000000</TimeOfArrivalUTC>
            <IsCleared>false</IsCleared>
        </DMAAlarm>
    </GetActiveAlarmsForViewV2Result>
    </GetActiveAlarmsForViewV2Response>
    """

    alarms = parse_xml_response(xml, DMAAlarm, is_array=True)
    for i, alarm in enumerate(alarms):
        print(f"Alarm {i}:", alarm)
        print()