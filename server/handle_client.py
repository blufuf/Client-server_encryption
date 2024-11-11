import random
from server.broadcast import broadcast_message
from encryption.camellia import decrypt_text

def handle_client(client_socket, client_address, clients, usernames):
    name = client_socket.recv(1024).decode('utf-8').strip()
    if 2 <= len(name) <= 30:
        welcome_message = "Добро пожаловать на наш чат!"
        client_socket.send(welcome_message.encode('utf-8'))
        broadcast_message(f"{name} теперь в нашем чате.", client_socket, clients)

        usernames[client_socket] = name
        clients.add(client_socket)

        try:
            while True:
                fromclient = client_socket.recv(1024)
                text_message, hash_message, key = fromclient.split(sep=b'|||')

                broken = random.randint(0, 10)
                if broken < 3:
                    text = hash_message.decode('utf-8')
                    new_hash_message = text[:1] + 'X' + text[2:]
                    message = text_message + b'|||' + new_hash_message.encode("utf-8") + b'|||' + key
                else:
                    message = text_message + b'|||' + hash_message + b'|||' + key

                if message:
                    broadcast_message(name.encode('utf-8') + b'|||' + message, client_socket, clients)
        except ConnectionResetError:
            pass
        finally:
            client_socket.close()
            clients.remove(client_socket)
            broadcast_message(f"{name} покинул(а) чат.", client_socket, clients)
    else:
        client_socket.close()
