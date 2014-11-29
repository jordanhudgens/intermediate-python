import json

sampleJSON = json.dumps(['rebels', {'firstName': 'Luke', 'lastName': 'Skywalker'},
						{'firstName': 'Han', 'lastName': 'Solo'},
						{'firstName': 'Wedge', 'lastName': 'Antilles'}],
						separators=(',', ':'))

print("Original JSON: ", sampleJSON)

jsonDecoder = json.loads(sampleJSON)
print("Decoded JSON: ", jsonDecoder)

for element in jsonDecoder:
    print(element)