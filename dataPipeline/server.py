import json
from typing import Tuple
from alpha_vantage import download_data
from connection import *


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

    def start(self):
        self.server.bind((self.addr, self.port))
        self.server.listen()
        print(f"+ [Starting] Listening on {self.addr}[{self.port}]")
        while True:
            conn, ip = self.server.accept()
            self.manage_client(conn, ip)

    def manage_client(self, conn: socket, ip: Tuple[str]):
        with conn as c:
            print(f"+ [Connection] Connected by ({ip[0]}:{ip[1]})")
            sym_request = recv_all(c).decode(Server.FORMAT)
            print(f"+ [Request] Connection from ({ip[0]}:{ip[1]}) requested the symbol: ({sym_request})")
            self.response_client(sym_request, c)
            print(f"+ [Response] The request for symbol: ({sym_request}) for ({ip[0]}:{ip[1]}) has been responded")

    def response_client(self, symbol: str, conn: socket):
        data = json.dumps(download_data(symbol))
        encoded_len = encode_len(data)
        encoded_len += b' ' * (self.HEADER - len(encoded_len))
        conn.sendall(encoded_len)
        conn.sendall(data.encode(Server.FORMAT))
