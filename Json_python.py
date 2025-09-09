# JSON is built-in package in python
'''
JSON is a syntax for storing and exchanging data.
JSON is text, written with javascript object notation.

Parse JSON-Convert from JSON to python
json.loads()


Parse JSON-Convert from python to JSON
json.dumps()

'''

# import json

# x = '{"Name" : "Nans", "age":22}'

# y = json.loads(x)
# print(y["age"])


import json

x = {"Pin" : 510, "Project": "Sanke", "city":"KPHB"}

y = json.dumps(x)
print(y)
