import xml.etree.ElementTree as ET
import csv

tree = ET.parse("Convenio.dvm")
root = tree.getroot()

# open a file for writing

Resident_data = open('ConvenioCVS.csv', 'w')

# create the csv writer object

csvwriter = csv.writer(Convenio)
resident_head = []

count = 0
for member in root.findall('dvm'):
        dvm = []
        address_list = []
        if count == 0:
                columns = member.find('column').tag
                resident_head.append(column)

                PhoneNumber = member.find('PhoneNumber').tag
                resident_head.append(PhoneNumber)
                EmailAddress = member.find('EmailAddress').tag
                resident_head.append(EmailAddress)
                Address = member[3].tag
                resident_head.append(Address)
                csvwriter.writerow(resident_head)
                count = count + 1

        name = member.find('Name').text
        resident.append(name)
        PhoneNumber = member.find('PhoneNumber').text
        resident.append(PhoneNumber)
        EmailAddress = member.find('EmailAddress').text
        resident.append(EmailAddress)
        Address = member[3][0].text
        address_list.append(Address)
        City = member[3][1].text
        address_list.append(City)
        StateCode = member[3][2].text
        address_list.append(StateCode)
        PostalCode = member[3][3].text
        address_list.append(PostalCode)
        resident.append(address_list)
        csvwriter.writerow(resident)
Resident_data.close()