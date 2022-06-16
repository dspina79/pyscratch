from hashlib import sha256
import json as j

class Block:
    def __init__(self, index, transactions, timestamp, previous_hash, nonce = 0):
        self.index = index
        self.transactions = transactions
        self.nonce = nonce
        self.timestamp = timestamp
        self.previous_hash = previous_hash

    def compute_hash(self):
        block_string = j.dumps(self.__dict__, sort_keys=True)
        return sha256(block_string.encode()).hexdigest()