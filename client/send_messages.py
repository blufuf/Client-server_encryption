from Crypto.Random import get_random_bytes
from encryption.camellia import encrypt_text
from encryption.md6 import md6

def send_messages(client_socket):
    while True:
        message = input()
        if message.lower() == 'exit':
            break
        if 1 <= len(message) <= 80:
            key = get_random_bytes(32)
            encrypt_message = encrypt_text(key, message)
            hash_message = md6(str(encrypt_message))
            end_message = encrypt_message + b'|||' + hash_message.encode('utf-8') + b'|||' + key
            client_socket.send(end_message)
        else:
            print("Сообщение должно содержать от 1 до 80 символов.")
    client_socket.close()
