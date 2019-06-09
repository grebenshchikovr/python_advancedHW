import csv
import yaml

data = []
with open('read_csv.txt', 'r') as file:
   reader = csv.reader(file)
   data = list(reader)

print(data)
with open('csv2yaml.txt', 'w', encoding='windows-1251') as file:

    yaml.dump(data, file, Dumper=yaml.Dumper)