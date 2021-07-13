from alpha_vantage import download_data
from server import Server
from client import Client


def main():
    download_data('ruben', dump=True)
    server = Server()
    server.start()


if __name__ == '__main__':
    main()
