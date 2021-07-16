import json
import logging
import sys
from typing import Tuple
from alpha_vantage import download_data
from connection import *
import pathlib


class Server:
    FORMAT = 'utf-8'
    BUFFER_SIZE = 4096
    HEADER = 64

    def __init__(self, addr=None, port=15032):
        if not addr:
            self.addr = socket.gethostbyname(socket.gethostname())
        else:
            self.addr = addr
        self.port = port
        self.server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.logger = self.get_logger()

    def get_logger(self):
        logger = logging.getLogger(__name__ + f'{self.addr}')
        logger.setLevel(logging.DEBUG)
        console_handler = logging.StreamHandler(sys.stdout)
        file_handler = logging.FileHandler(f'logs/{self.addr}_debug.log')
        console_handler.setLevel(logging.INFO)
        file_handler.setLevel(logging.DEBUG)
        console_handler.setFormatter(logging.Formatter(fmt='%(levelname)-8s %(message)s'))
        file_handler.setFormatter(logging.Formatter(fmt='%(asctime)s %(name)-15s %(levelname)-8s %(message)s'))
        logger.addHandler(console_handler)
        logger.addHandler(file_handler)
        return logger

    def start(self):
        self.server.bind((self.addr, self.port))
        self.server.listen()
        self.logger.info(f"+ [Starting] Listening on {self.addr}[{self.port}]")
        while True:
            conn, ip = self.server.accept()
            self.manage_client(conn, ip)

    def manage_client(self, conn: socket, ip: Tuple[str]):
        with conn as c:
            self.logger.info(f"+ [Connection] Connected by ({ip[0]}:{ip[1]})")
            sym_request = recv_all(c).decode(Server.FORMAT)
            self.logger.info(f"+ [Request] Connection from ({ip[0]}:{ip[1]}) requested the symbol: ({sym_request})")
            self.logger.debug(f'+ [Requested symbol] {sym_request}')
            self.response_client(sym_request, c)
            self.logger.info(f"+ [Response] The request for symbol: ({sym_request}) for ({ip[0]}:{ip[1]}) has been "
                             f"responded")

    def response_client(self, symbol: str, conn: socket):
        data = json.dumps(download_data(symbol))
        encoded_len = encode_len(data)
        encoded_len += b' ' * (self.HEADER - len(encoded_len))
        self.logger.debug(f'+ [Encoded response length] {encoded_len}')
        self.logger.debug(f'+ [Response data] {data}')
        conn.sendall(encoded_len)
        conn.sendall(data.encode(Server.FORMAT))
