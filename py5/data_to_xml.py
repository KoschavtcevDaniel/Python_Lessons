import xml.dom.minidom

doc = xml.dom.minidom.Document()
root = doc.createElement('table')
doc.appendChild(root)

data = [
    {"id": "174904234", "first_name": "John", "last_name": "Doe", "passport": "123456"},
    {"id": "21473423592", "first_name": "Jane", "last_name": "Doe", "passport": "759493"},
    {"id": "34202525", "first_name": "Major", "last_name": "Payne", "passport": "828516"}
]
for row in data:
    record = doc.createElement('record')
    root.appendChild(record)
    for key, value in row.items():
        element = doc.createElement(key)
        element.appendChild(doc.createTextNode(value))
        record.appendChild(element)

with open('table.xml', 'w') as f:
    f.write(doc.toprettyxml())