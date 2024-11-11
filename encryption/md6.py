import hashlib

class MD6:
    def __init__(self, data):
        self.data = data

    def md6_hash(self):

        return hashlib.sha512(self.data.encode('utf-8')).hexdigest()

def md6(data):
    md6_instance = MD6(data)
    return md6_instance.md6_hash()