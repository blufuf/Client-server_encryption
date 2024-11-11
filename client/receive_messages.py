from encryption.camellia import decrypt_text
from encryption.md6 import md6

def receive_messages(client_socket):
    while True:
        try:
            fromserver = client_socket.recv(1024)
            if fromserver:
                if b'|||' in fromserver:
                    name, text_message, hash_message, key = fromserver.split(sep=b'|||')
                    now_hash_message = hash_message.decode('utf-8')
                    should_hash = md6(str(text_message))
                    message = decrypt_text(key, text_message)
                    print(name.decode('utf-8') + ": " + message.decode('utf-8'), sep=' ')
                    if should_hash != now_hash_message:
                        print("(Сообщение было повреждено)")
                    else:
                        print("(Сообщение дошло без повреждений)")
                else:
                    print(fromserver.decode("utf-8"))
        except ConnectionResetError:
            break
