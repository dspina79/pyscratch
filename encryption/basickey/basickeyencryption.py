from cryptography.fernet import Fernet

class MyEncryptor:
    def __init__(self):
        super().__init__()
        self.key = Fernet.generate_key()
        self.crypto = Fernet(self.key)

    def encrypt(plaintext):
        return crypto.encrypt(bytes(plaintext, encoding="utf-8"))

    def decrypt(encrypted_bytes):
        db = crypto.decrypt(encrypted_bytes)
        return str(db, encoding="utf-8")

m = MyEncryptor()
b = m.encrypt("this is my encrypted string")
ds = m.decrypt(b)
print(ds)