import xml.etree.ElementTree as ET
import csv

tree = ET.parse("Operacao.dvm")
root = tree.getroot()

f = open('saida.csv', 'w')

csvwriter = csv.writer(f)

count = 0

head = ['Job Name','Task Name','Staff Name','Date','Minutes','Billable']

csvwriter.writerow(head)

for time in root.findall('Time'):
    row = []
    job_name = time.find('Job').find('Name').text
    row.append(job_name)
    task_name = time.find('Task').find('Name').text
    row.append(task_name)
    staff_name = time.find('Staff').find('Name').text
    row.append(staff_name)
    date = time.find('Date').text
    row.append(date)
    minutes = time.find('Minutes').text
    row.append(minutes)
    billable = time.find('Billable').text
    row.append(billable)
    csvwriter.writerow(row)
f.close()