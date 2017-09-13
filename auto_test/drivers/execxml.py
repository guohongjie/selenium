# -*-coding:utf-8 -*-
import xml.dom.minidom
from xml.etree import ElementTree as ET
def xml_property_value(filepath,tag,property=None):
    """return xml element for propertyValue"""
    try:
        property_value=[]
        # open this xml file
        dom = xml.dom.minidom.parse(filepath)
        # receive this file's element object
        element = dom.getElementsByTagName(tag)
        for m in element:
            if m.hasAttribute(property):
                value = m.getAttribute(property)
                property_value.append(value)
        return property_value
    except Exception as e:
        print e
def xml_page_data(filepath,tag):
    """return  page tag value"""
    dom = xml.dom.minidom.parse(filepath)
    page_value = []
    element = dom.getElementsByTagName(tag)
    for m in element:
        page_value.append(m.firstChild.data)
    return page_value
def parent_son(filepath,P_tag,S_tag=None):
    per = ET.parse(filepath)
    result = per.findall(P_tag)
    for oneper in result:
        for child in oneper.getchilden():
            print child.tab,":",child.text
if __name__ == '__main__':
    print parent_son(r'E:\Page_object_web\mail\data\login.xml','./step')
