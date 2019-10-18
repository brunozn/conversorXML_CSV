
import xml.etree.ElementTree as ET

filenameXML = 'Invoice.jrxml'
namespaces = {'xmlns':'http://jasperreports.sourceforge.net/jasperreports'}

with open(filenameXML, 'r') as f:
    dados = f.read()
    tree = ET.fromstring(dados)
list_head=[]

for member in tree.findall('xmlns:parameter', namespaces):
    columns = []
    columns.append(member.attrib['name'])
    print(member.attrib)