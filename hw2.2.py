import json


with open('read_json.txt', 'r') as file:
   print(json.load(file))

data = [
    {'header 11': 'data 11', 'header 12': 'data 12', 'header 13': 'data 13'},
    {'header 21': 'data 22', 'header 22': 'data 22', 'header 23': 'data 23'},
    {'header 31': 'data 31', 'header 32': 'data 32', 'header 33': 'data 33'}
]

with open('write_json.txt', 'w', encoding='windows-1251') as file:
    json.dump(data, file, indent=4)