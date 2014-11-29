import xml.parsers.expat

def start_element(name, attrs):
    print('Start element: ', name, attrs)

def end_element(name):
    print('End element: ', name)

def char_data(data):
    print('Character data: ', repr(data))

p = xml.parsers.expat.ParserCreate()
p.StartElementHandler = start_element
p.EndElementHandler = end_element
p.CharacterDataHandler = char_data

xmlExample = """<?xml version="1.0"?><army id="Rebel Alliance"><echoThree name="Luke Skywalker">Jedi in training</echoThree><echoSeven name="Han Solo">Smuggler</echoSeven></army>"""

p.Parse(xmlExample, 1)