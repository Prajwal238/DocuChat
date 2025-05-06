from pymongo import MongoClient

class DBManager:
    def __init__(self, uri="mongodb://localhost:27017/", db_name="ragdbm001", client_class=MongoClient):
        self.uri = uri
        self.db_name = db_name
        self.client_class = client_class
        self.client = None
        self.db = None

    def connect(self):
        self.client = self.client_class(self.uri)
        self.db = self.client[self.db_name]
        return self.db

    def close(self):
        if self.client:
            self.client.close()