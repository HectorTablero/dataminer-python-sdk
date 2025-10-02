from xml.etree import ElementTree as ET


def extract_result(method: str, content: str) -> str:
    """
    Parse API response XML and extract the <MethodResult> value.
    """
    root = ET.fromstring(content)
    ns = {
        "soap": "http://schemas.xmlsoap.org/soap/envelope/",
        "ns": "http://www.skyline.be/api/v1",
    }
    result = root.find(f".//ns:{method}Result", ns)
    if result is None:
        raise RuntimeError(f"No <{method}Result> found in response:\n{content}")
    return result.text  # type: ignore
