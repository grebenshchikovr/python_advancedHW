import json
import yaml

with open('read_json.txt', 'r') as file:
   data =json.load(file)

print(data)

with open('json2yaml.txt', 'w', encoding='windows-1251') as file:
    yaml.dump(data, file, Dumper=yaml.Dumper)