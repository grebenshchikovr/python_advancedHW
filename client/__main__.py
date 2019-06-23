import zlib
import json
import yaml
import socket
import hashlib
import logging

from datetime import datetime
from argparse import ArgumentParser

parser = ArgumentParser()
parser.add_argument(
    '-c', '--config', type=str,
    help='Sets run configuration file'
)

parser.add_argument(
    '-m', '--mode', type=str, default='w',
    help='Sets client mode'
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

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('client.log', encoding=encoding),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger('client')

try:
    sock = socket.socket()
    sock.connect((host, port))

    logger.debug(f'Client params: {host}:{port} /p')

    if args.mode == 'w':
        while True:

            hash_obj = hashlib.sha256()
            hash_obj.update(
                str(datetime.now().timestamp()).encode(encoding)
            )

            action = input('Enter Action: ')
            data = input('Enter data: ')

            request = {
                'action': action,
                'data': data,
                'time': datetime.now().timestamp(),
                'user': hash_obj.hexdigest()
            }
            s_request = json.dumps(request)
            b_request = zlib.compress(s_request.encode(encoding))
            sock.send(b_request)
    else:
        while True:
            response = sock.recv(buffersize)
            b_response = zlib.decompress(response)
            print(b_response.decode(encoding))
            logger.debug(f'{b_response.decode(encoding)}')

except KeyboardInterrupt:
    pass
