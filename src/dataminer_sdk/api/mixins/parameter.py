# from dataminer_sdk.api.mixins.base import BaseConnector
# from typing import Optional, Any


# class ParameterMixin(BaseConnector):
#     """
#     Provides methods for fetching parameter values from DataMiner.

#     Requires the base connector to implement:
#       - self._call_api(method: str, params: Dict[str, Any], async_: bool, transport_mode: Optional[str])
#     """

#     def get_parameter_value(
#         self,
#         dma_id: int,
#         element_id: int,
#         parameter_id: int,
#         table_index: str = "",
#         *,
#         async_: bool = False,
#         transport_mode: Optional[str] = None,
#     ) -> Any:
#         """
#         Retrieve a parameter value for a specific element.

#         Args:
#             dma_id (int): The DataMiner Agent ID.
#             element_id (int): The ID of the element.
#             parameter_id (int): The ID of the parameter.
#             table_index (str, optional): The table index if the parameter is a table parameter.
#             transport_mode (Optional[str], optional): Override transport mode (e.g. "SOAP" or "URL").

#         Returns:
#             Any: Parsed parameter value. (Currently raw API result, parsing can be plugged in.)
#         """
#         params = {
#             "connection": getattr(self, "_connection_token", None),
#             "dmaID": dma_id,
#             "elementID": element_id,
#             "parameterID": parameter_id,
#             "tableIndex": table_index,
#         }

#         return self.extract_result(
#             "GetParameter",
#             self._call_api(
#                 method="GetParameter",
#                 params=params,
#                 async_=async_,
#                 transport_mode=transport_mode,
#             ),
#         )
