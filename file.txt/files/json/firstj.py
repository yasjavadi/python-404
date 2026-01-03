import json
#javascript object
'''x= '{"name":"sara","family":"rezaei"}'
print(type(x))
#convert to python
y= json.loads(x)
print(type(y))
print(len(y))
print(y['name'])'''

#dict python
 
'''x = {"name":"sara","family":"rezaei"}
print(type(x))
#convert to json
y= json.dumps(x)
print(type(y))
print(y)
print(len(y))'''

print(json.dumps({"name":"sara","family":"rezaei"}))
print(json.dumps(('sara','rezaei')))
print(json.dumps(["sara","rezaei"]))
print(json.dumps(42))
print(json.dumps('helllo'))
print(json.dumps(11.23))
print(json.dumps(True))
print(json.dumps(False))
print(json.dumps(None))
