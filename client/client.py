import socket
import threading
from client.receive_messages import receive_messages
from client.send_messages import send_messages

def start_client():
    while True:
        name = input("Введите имя (2-30 знаков): ").strip()
        if 2 <= len(name) <= 30:
            break
        else:
            print("Неверная длина имени. Попробуйте снова.")
    while True:
        server_ip = input("Введите IP сервера: ").strip()
        server_port = input("Введите порт сервера: ").strip()
        try:
            server_port = int(server_port)
        except ValueError:
            print("Неверный порт. Пожалуйста, введите числовое значение.")
            continue
        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            client_socket.connect((server_ip, server_port))
            break
        except socket.error as e:
            print(f"Ошибка подключения: {e}. Попробуйте снова.")
    client_socket.send(name.encode('utf-8'))
    threading.Thread(target=receive_messages, args=(client_socket,)).start()
    send_messages(client_socket)

if __name__ == "__main__":
    start_client()
