import json
from jsonschema import validate

# Opening JSON file
f = open('task_status.json')
  
# returns JSON object as 
# a dictionary
schema = json.load(f)

#sample data
address_data = {
        "building_name": "vivo city",
        "unit": "robots r us"
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

robot_data = {
    'id': "barg_external_robot_1121d"
}

order_status_data = {
    "order_id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
    "customer_id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
    "status": 5
}

submit_order_data = {
    "order_details": "photo",
    "customer_id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
    "store_id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
    "store_address": address_data,
    "customer_address": address_data,
    "status": 0
}

eject_robot_data = {
    "robot": robot_data,
    "egress_point": address_data,
    "order": order_data
}

task_status_data = {
    "task_id": "234567",
    "robot": robot_data,
    "status": 1
}


validate(task_status_data, schema)