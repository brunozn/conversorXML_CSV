import csv
import xml.etree.cElementTree as ET
tree = ET.parse('Convenio1.xml')
root = tree.getroot()
xml_para_csv = open('Convenio.csv', 'w')
list_head=[]
print('ola1')
Cvs_whiter= csv.writer(xml_para_csv)
cont = 0
print('ola2')
for member in root.findall('columns'):
    print('teste')
    columns = []
    for column in member.findall('column'):
        columns.append(column.attrib['name'])
    Cvs_whiter.writerow(columns)
for member in root.findall('rows'):
    print('teste')
    for row in member.findall('row'):
        rows = []
        #print('vendo rows')
        #print(row)
        for cell in row.findall('cell'):
            #print('vendo cell')
            #print(cell.text)
            rows.append(cell.text)
        Cvs_whiter.writerow(rows)
        #print('\n')
        #columns.append(column.attrib['name'])
    #Cvs_whiter.writerow(columns)



