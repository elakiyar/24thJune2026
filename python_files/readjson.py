import json

with open('python_files/test_data.json', 'r') as file:
    data = json.load(file)

print(data)
