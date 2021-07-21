# This module contains utilities for connection management
import socket


def encode_len(length: str, encoding: str = 'utf-8') -> bytes:
    return str(len(length)).encode(encoding)


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


def prepared_send(msg: str, header: int = 64) -> bytes:
    send = encode_len(msg)
    send += b' ' * (header - len(send))
    return send
