from dataminer_sdk.api import DataMinerConnector
from dataminer_sdk.api.enums import SOAPVersion, TransportMode
import time


DMAConnector = DataMinerConnector(
    hostname="172.28.240.242",
    username="htablero",
    password=input("Dataminer password: "),
    client_app_name="PythonClient",
    client_app_version="1.0",
    client_computer_name="Unset",
    transport_mode=TransportMode.SOAP,
    soap_version=SOAPVersion.SOAP11,
)

# Run for 7.5 minutes (15 * 30s)
# Should automatically reconnect after 5 minutes
for _ in range(14):
    print(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - "{DMAConnector.connection_token}"')
    time.sleep(30)
print(f'{time.strftime("%Y-%m-%d %H:%M:%S")} - "{DMAConnector.connection_token}"')

# print(DMAConnector.get_parameter_value(2633, 8897, 1017))
