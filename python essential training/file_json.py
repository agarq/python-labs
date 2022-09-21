import json
from json import JSONDecodeError, JSONEncoder

#LOADING JSON
jsonString = '{"a": "apple", "b": "bear", "c": "cat"}'
#jsonString = '{"a": "apple", "b": "bear", "c": "cat",}' #this works as Dictionary, but not as JSON
try:
    json.loads(jsonString)
except JSONDecodeError:
    print('Could not parse JSON!')

#DUMPING JSON
pythonDict = {'a': 'apple', 'b': 'bear', 'c': 'cat',}
print(json.dumps(pythonDict))

#CUSTOM JSON DECODERS
class Animal:
    def __init__(self, name):
        self.name = name

class AnimalEncoder(JSONEncoder):
    def default(self, o):
        if type(o) == Animal:
            return o.name
        return super().default(o)
    
pythonDict = {'a': Animal('aardvark'), 'b': Animal('bear'), 'c': Animal('cat'),}
print(json.dumps(pythonDict, cls=AnimalEncoder))