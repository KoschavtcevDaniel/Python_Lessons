import xml.dom.minidom

doc = xml.dom.minidom.Document()
root = doc.createElement('table')
doc.appendChild(root)

data = [
    {"id": "3251441351", "first_name": "Daniil", "last_name": "Koshch", "passport": "0364123456", "ownership": "Car: Impala1969, House: st.Krasnay, 93"},
    {"id": "6541687451", "first_name": "Andrei", "last_name": "Kormiltcev", "passport": "0356691587", "ownership": "Car: LadaReno"},
    {"id": "7864161854", "first_name": "Anton", "last_name": "Barsov", "passport": "0706154646", "ownership": "House: st.Morkova, 94/1"},
    {"id": "7498921465", "first_name": "Marya", "last_name": "Klarnet", "passport": "1306649255", "ownership": "House: st.Teremok, 123"},
    {"id": "1674945654", "first_name": "Anna", "last_name": "Zemelko", "passport": "0609135648", "ownership": "-"},
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