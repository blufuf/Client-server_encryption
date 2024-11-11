def broadcast_message(message, sender_socket, clients):
    for client in clients:
        if client != sender_socket:
            if type(message) == bytes:
                client.send(message)
            else:
                client.send(message.encode('utf-8'))
