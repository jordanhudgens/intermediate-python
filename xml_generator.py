from xml.etree.ElementTree import Element, SubElement, tostring

root = Element('rebels')

x = 0

while x < 10:
    rebel = SubElement(root, 'rebel')
    firstName = SubElement(rebel, 'firstName')
    lastName = SubElement(rebel, 'lastName')
    firstName.text = 'Luke'
    lastName.text = 'Skywalker'
    x += 1

print(tostring(root))