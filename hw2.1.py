import csv


with open('read_csv.txt', 'r') as file:
   reader = csv.reader(file)
   for row in reader:
       print(row)

data = [
    ['header 1','header 2','header 3'],
    ['data 11','data 12','data 13'],
    ['data 21', 'data 22', 'data 23']
]

with open('write_csv.txt', 'w', encoding='windows-1251') as file:
    writer = csv.writer(file)
    for line in data:
        writer.writerow(line)