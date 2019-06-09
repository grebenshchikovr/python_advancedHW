import yaml


with open('read_yaml.txt', 'r') as file:
   print(yaml.load(file, Loader=yaml.Loader))


data = {
    'attr1': 'value 1',
    'attr2': 123,
    'attr3': 0.123,
    'attr4': ['value 2', 'value 3', 'value 4']
}


with open('write_yaml.txt', 'w', encoding='windows-1251') as file:
    yaml.dump(data, file, Dumper=yaml.Dumper)