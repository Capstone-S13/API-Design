from audioop import add
import json
from jsonschema import validate

# Opening JSON file
f = open('robot.json')
  
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
    "company_name": "grab food",
    "order_description": "size 10"
}

robot_data = {
    'id': "barg_external_robot_1121d"
}

operation_data = {
    "task": 2
}

dispatch_task_data = {
    "task_id": "d290f1ee-6c54-4b01-90e6-d701748f0851",
    "robot": robot_data,
    "order": order_data,
    "destination": address_data,
    "operation": operation_data

}

host_data = {
    "ip": "343462456",
    "port": 5000
}

map_data = {
    "image": "photo",
    "resolution": [434,546],
    "origin": [0,0],
    "negate": 32,
    "occupied_thresh": 564,
    "free_thresh": 2,
    "pgm": "pgm string"
}

eject_robot_data = {
    "task_id": "234567",
    "robot": robot_data,
    "egress_point": address_data,
    "new_host": host_data,
    "map": map_data,
    "initial_pose": [2,3,1]
}

operation_data = {
    "task": 2
}

receive_robot_data = {
    "task_id": "234567",
    "robot": robot_data,
    "ingress_point": address_data,
    "order": order_data,
    "operation": operation_data
}


validate(robot_data, schema)