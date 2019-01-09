#Pull reference data from markit files

import xml.etree.ElementTree as ET

with open('Z:\MarkitData\20190108\RED_ENTITY_20190108.xml', 'r') as file:
    tree = ET.parse(file)
    root = tree.getroot()
    
