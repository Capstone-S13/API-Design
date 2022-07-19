import json
from jsonschema import validate

# Opening JSON file
f = open('address.json')
  
# returns JSON object as 
# a dictionary
data = json.load(f)

# A sample schema, like what we'd get from json.load()
schema = {
    "type": "object",
        "required": [
          "building_name",
          "unit"
        ],
        "properties": {
          "building_name": {
            "type": "string",
            "example": "Vivo City"
          },
          "unit": {
            "type": "string",
            "example": "robots r us"
          }
        }
}

print(data)

validate(data, schema)