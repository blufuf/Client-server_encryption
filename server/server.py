import socket
import threading
from config import load_config
from handle_client import handle_client

def start_server():
    port = load_config()
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind(('0.0.0.0', port))
    server_socket.listen()

    clients = set()
    usernames = {}

    print(f"Сервер запущен на порту {port}")

    while True:
        client_socket, client_address = server_socket.accept()
        threading.Thread(target=handle_client, args=(client_socket, client_address, clients, usernames)).start()

if __name__ == "__main__":
    start_server()
