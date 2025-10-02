from dataminer_sdk.utils.xml import parse_xml_response
from dataminer_sdk.models import DMAParameter, DMAAlarm


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

    param = parse_xml_response("GetParameter", xml, DMAParameter)
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

    alarms = parse_xml_response("GetActiveAlarmsForViewV2", xml, DMAAlarm, is_array=True)
    for i, alarm in enumerate(alarms):
        print(f"Alarm {i}:", alarm)
        print()


    print("\n\n")

    xml = """<?xml version="1.0" encoding="utf-8"?>
    <GetValueResponse xmlns="http://www.skyline.be/api/v1">
    <GetValueResult>2389234238</GetValueResult>
    </GetValueResponse>
    """

    connection = parse_xml_response("GetValue", xml, str)
    print("Value (str):", connection, "Type:", type(connection))

    print()

    connection = parse_xml_response("GetValue", xml, int)
    print("Value (int):", connection, "Type:", type(connection))