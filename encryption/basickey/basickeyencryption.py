from cryptography.fernet import Fernet

class MyEncryptor:
    def __init__(self):
        super().__init__()
        self.key = Fernet.generate_key()
        self.crypto = Fernet(self.key)

    def encrypt(plaintext):
        return crypto.encrypt(bytes(plaintext, encoding="utf-8"))

    def decrypt(encrypted_string):
        pass

