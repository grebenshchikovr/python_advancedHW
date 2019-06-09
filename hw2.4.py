import csv
import json


with open('read_csv.txt', 'r') as file:
    reader = csv.reader(file)
    data = list(reader)

print(data)

with open('csv2json.txt', 'w', encoding='windows-1251') as file:
    json.dump(data, file, indent=4)