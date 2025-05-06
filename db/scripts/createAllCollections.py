from db.DBManager import DBManager

collections = [
    "conversationHistory"
]

db = DBManager().connect()

for name in collections:
    if name not in db.list_collection_names():
        db.create_collection(name)
        print(f"Collection '{name}' created.")
    else:
        print(f"Collection '{name}' already exists.")