import hashlib
import json
import time

class Block:

    def __init__(self,index,news,ml_score,validator,votes,prev_hash):

        self.index=index
        self.timestamp=time.time()
        self.news=news
        self.ml_score=ml_score
        self.validator=validator
        self.votes=votes
        self.prev_hash=prev_hash
        self.hash=self.calculate_hash()

    def calculate_hash(self):

        block_string=json.dumps({
            "index":self.index,
            "timestamp":self.timestamp,
            "news":self.news,
            "ml_score":self.ml_score,
            "validator":self.validator,
            "votes":self.votes,
            "prev_hash":self.prev_hash
        },sort_keys=True)

        return hashlib.sha256(block_string.encode()).hexdigest()


class Blockchain:

    def __init__(self):

        self.chain=[self.create_genesis_block()]

    def create_genesis_block(self):

        return Block(0,"Genesis Block",0,"System",{}, "0")

    def add_block(self,block):

        self.chain.append(block)

    def is_valid(self):

        for i in range(1,len(self.chain)):

            current=self.chain[i]
            prev=self.chain[i-1]

            if current.hash!=current.calculate_hash():
                return False

            if current.prev_hash!=prev.hash:
                return False

        return True