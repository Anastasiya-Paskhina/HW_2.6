from pprint import pprint
import csv
import re


with open("phonebook_raw.csv", encoding="utf8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

contacts1 = "([А-ЯЁ]{1}[а-яё]+)(\s)([А-ЯЁ]{1}[а-яё]+)(\s)([А-ЯЁ]{1}[а-яё]+)"
contacts2 = "([А-ЯЁ]{1}[а-яё]+)(\s)([А-ЯЁ]{1}[а-яё]+)"
phones = "(\+7|8)(\s?)(\(?)([0-9]{3})(\)?)(\s?)(\-?)([0-9]{3})" \
                "(\-?)([0-9]{2})(\-?)([0-9]{2})(\s?)(\(?)([а-яё]*)(\.?)" \
                "(\s?)([0-9]*)(\)?)"

for contact in contacts_list:
    new_contact = re.sub(phones, r"+7(\4)\8-\10-\12\13\15\16\18",
                         contact[5])
    contact[5] = new_contact

    if re.match(contacts1, contact[0]):
        result = re.match(contacts1, contact[0])
        contact[0] = result.group(1)
        contact[1] = result.group(3)
        contact[2] = result.group(5)

    if re.match(contacts2, contact[0]):
        result = re.match(contacts2, contact[0])
        contact[0] = result.group(1)
        contact[1] = result.group(3)

    if re.match(contacts2, contact[1]):
        result = re.match(contacts2, contact[1])
        contact[1] = result.group(1)
        contact[2] = result.group(3)

phones_dict = {}
for contact in contacts_list:
    if contact[0] not in phones_dict.keys():
        phones_dict[contact[0]] = contact[1:]
    else:
        for e, item in enumerate(contact[1:]):
            if phones_dict[contact[0]][e-6] == '':
                phones_dict[contact[0]][e-6] = item

new_book = []
for key, value in phones_dict.items():
    local_contact = []
    local_contact.append(key)
    for i in value:
        local_contact.append(i)
    new_book.append(local_contact)

pprint(new_book)

with open("phonebook.csv", "w", encoding="utf8") as f:
    datawriter = csv.writer(f, delimiter=',')
    datawriter.writerows(new_book)