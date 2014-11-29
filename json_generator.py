import json

straightJSON = json.dumps(['rebels',
                            {'firstName': 'Luke', 'lastName': 'Skywalker'}],
                          separators=(',', ':'))

print("straightJSON Output:\n", straightJSON)

prettyJSON = json.dumps(['rebels',
                            {'firstName': 'Luke', 'lastName': 'Skywalker'}],
                        sort_keys=True,
                        indent=4)

print("prettyJSON Output:\n", prettyJSON)

f = open('json_generated_file.json', 'w')
f.write(prettyJSON)
f.close()