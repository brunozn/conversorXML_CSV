import csv
import xml.etree.cElementTree as ET
tree = ET.parse('files_xml/Convenio.xml')
root = tree.getroot()
xml_para_csv = open('files_CSV/Convenio.csv', 'w')
list_head=[]
Cvs_whiter= csv.writer(xml_para_csv)
cont = 0
for member in root.findall('columns'):
    columns = []
    for column in member.findall('column'):
        columns.append(column.attrib['name'])
    Cvs_whiter.writerow(columns)
for member in root.findall('rows'):
    for row in member.findall('row'):
        rows = []
        for cell in row.findall('cell'):
            rows.append(cell.text)
        Cvs_whiter.writerow(rows)

