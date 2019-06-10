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
    while True:
        sock = socket.socket()
        sock.bind((host, port))
        sock.listen(5)
        print(f'Server was started with {host}:{port}')

        while True:
            client, address = sock.accept()
            print(f'Client was detected at {address}')
            data = client.recv(buffersize)
            print(data.decode(encoding))
            client.send(data)
            client.close()
except KeyboardInterrupt:
    pass