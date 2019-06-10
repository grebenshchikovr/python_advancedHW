from argparse import ArgumentParser
import yaml
import socket

parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration file'
    # required = True
)

args = parser.parse_args()

host = 'localhost'
port = 3000
buffersize = 1024
encoding = 'utf-8'

if args.config:
    with open(args.config) as file:
        config = yaml.load(config.yml, Loader=yaml.Loader)
        host = config.get('host')
        port = config.get('port')
        buffersize = config.get('buffersize')
        encoding = config.get('encoding')

try:
    sock = socket.socket()
    sock.connect((host, port))
    print(f'Client started')
    data = input('Enter data: ')
    sock.send(data.encode(encoding))
    response = sock.recv(buffersize)
    print(response.decode(encoding))
except KeyboardInterrupt:
    pass
