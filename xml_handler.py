import aiofiles
import xml.etree.ElementTree as ET

async def load_xml(path):
    async with aiofiles.open(path, 'r') as f:
        content = await f.read()
        root = ET.fromstring(content)
        return {root.tag: _xml_to_dict(root)}

async def save_xml(data, path):
    root_tag = list(data.keys())[0]
    root_element = _dict_to_xml(root_tag, data[root_tag])
    tree = ET.ElementTree(root_element)
    async with aiofiles.open(path, 'w') as f:
        xml_str = ET.tostring(root_element, encoding='unicode')
        await f.write(xml_str)

def _xml_to_dict(element):
    children = list(element)
    if not children:
        return element.text
    result = {}
    for child in children:
        result[child.tag] = _xml_to_dict(child)
    return result

def _dict_to_xml(tag, value):
    element = ET.Element(tag)
    if isinstance(value, dict):
        for k, v in value.items():
            child = _dict_to_xml(k, v)
            element.append(child)
    else:
        element.text = str(value)
    return element