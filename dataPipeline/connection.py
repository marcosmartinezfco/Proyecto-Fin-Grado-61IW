# This module contains utilities for connection communication management
import socket


def encode_len(string: str, encoding: str = 'utf-8') -> bytes:
    return str(len(string)).encode(encoding)


def decode_len(length: bytes, encoding: str = 'utf-8') -> int:
    return int(length.decode(encoding))


def recv_header(conn: socket, header: int = 64) -> int:
    return decode_len(conn.recv(header))


def recv_all(conn: socket) -> bytes:
    msg_len = recv_header(conn)
    data = b''
    while len(data) < msg_len:
        packet = conn.recv(msg_len - len(data))
        if not packet:
            break
        data += packet
    return data
