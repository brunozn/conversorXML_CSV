import os
import sys
import xml.etree.ElementTree as ET

filenameXML = 'Invoice2.xml'
#namespaces = {xmlns="http://jasperreports.sourceforge.net/jasperreports" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://jasperreports.sourceforge.net/jasperreports http://jasperreports.sourceforge.net/xsd/jasperreport.xsd" name="Invoice" pageWidth="595" pageHeight="842" columnWidth="535" leftMargin="20" rightMargin="20" topMargin="20" bottomMargin="20" uuid="4eedbb89-b4f6-4469-9ab6-f642a1688cf7"

with open(filenameXML, 'r') as f:
    dados = f.read()
    tree = ET.fromstring(dados)
list_head=[]

for member in tree.findall('parameter'):
    columns = []
    #columns.append(member.attrib['name'])
    print(member.attrib)