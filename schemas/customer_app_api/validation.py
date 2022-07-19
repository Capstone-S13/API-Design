import json
from jsonschema import validate

# Opening JSON file
f = open('submit_order.json')
  
# returns JSON object as 
# a dictionary
schema = json.load(f)

#sample data
address_data = {
        "building_name": "vivo city",
        "unit": "robots r us"
}

landing_data = {
    "orders": ['order.json', 'order.json'],
    "stores": [
                "d290f1ee-6c54-4b01-90e6-d701748f0851",
                "d290f1ee-6c54-4b01-90e6-d701748f0851"
              ]
}

order_status_data = {
    'order_id': "d290f1ee-6c54-4b01-90e6-d701748f0851",
    'customer_id':  "d290f1ee-6c54-4b01-90e6-d701748f0851",
    'status': 0
}

order_data = {
    'order_id': "d290f1ee-6c54-4b01-90e6-d701748f0851",
    "order_details": "raspberry pi model 3B 4GB",
    "customer_id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
    "store_id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
    "store_address": address_data,
    "customer_address": address_data,
    "status": 8,
    "robot_id": "barg_external_robot_1121d"
}

submit_order_data = {
    "order_details": "raspberry pi model 3B 4GB",
    "customer_id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
    "store_id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
    "store_address": address_data,
    "customer_address": address_data,
    "status": 0
}

validate(submit_order_data, schema)