import logging
import sys
from restApi.connection import *


class Client:
    FORMAT = 'utf-8'
    BUFFER_SIZE = 4096
    HEADER = 64

    def __init__(self, server_ip: str, port: int):
        self.server_ip = server_ip
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.logger = self.get_logger()

    def get_logger(self):
        logger = logging.getLogger(__name__)
        logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler(sys.stdout)
        # file_handler = logging.FileHandler(f'logs/{self.server_ip}_client_debug.log')
        console_handler.setLevel(logging.INFO)
        # file_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(logging.Formatter(fmt='%(levelname)-8s %(message)s'))
        # file_handler.setFormatter(logging.Formatter(fmt='%(asctime)s %(name)-15s %(levelname)-8s %(message)s'))
        logger.addHandler(console_handler)
        # logger.addHandler(file_handler)
        return logger

    def connect(self, symbol: str) -> str:
        with self.server as s:
            s.connect((self.server_ip, self.port))
            len_symbol = prepared_send(symbol)
            self.logger.debug(f'[Symbol length] {len_symbol}')
            s.sendall(len_symbol)
            self.logger.debug(f'[Symbol] {symbol} - {symbol.encode(Client.FORMAT)}')
            s.sendall(symbol.encode(Client.FORMAT))
            return recv_all(s).decode(Client.FORMAT)


def main():
    client = Client('127.0.1.1', 15032)
    data = client.connect('amazon')
    print(data)


if __name__ == '__main__':
    main()
