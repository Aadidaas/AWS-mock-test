import json

def print_json(json_file):
    with open(json_file) as q:
        data = json.load(q)
        print(json.dumps(data))

def print_key_value(json_file, key):
    with open(json_file, 'r') as q:
        data = json.load(q)
        print(data[key])


def modify_key_value(json_file, key, new_value):
    with open(json_file, 'r') as q:
        data = json.load(q)
        data[key] = new_value
    with open(json_file, 'w') as q:
        json.dump(data, q)

def write_to_new_file(json_file):
    with open(json_file) as q:
        data = json.load(q)
    with open(json_file+'_new.json', 'w') as q:
        json.dump(data, q)

json_file = input("Enter the JSON file name (with .json extension): ")

print_json(json_file)

key = input("Enter the key name to print: ")

print_key_value(json_file, key)

key = input("Enter the key name to modify: ")

new_value = input("Enter the new value: ")


modify_key_value(json_file, key, new_value)

write_to_new_file(json_file)