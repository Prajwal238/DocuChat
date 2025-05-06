import json
from jsonschema import validate, ValidationError

class ConversationHistoryModel:
    def __init__(self, db):
        self.db = db
        self.model_name = "conversationHistory"
        self.collection = self.db[self.model_name]

        with open("db/schemas/conversationHistorySchema.json", "r") as f:
            self.schema = json.load(f)

    def insert_conversation_history(self, conversation_history):
        try:
            validate(instance=conversation_history, schema=self.schema)
        except ValidationError as e:
            raise ValueError(f"Invalid conversation history: {e.message}")
        
        print(conversation_history)
        self.collection.insert_one(conversation_history)
    
    def update_conversation_history(self, filter_query, new_conversation):
        self.collection.update_one(filter_query, {"$push": {"conversation": new_conversation}})

    def get_conversation_history_by_user_id(self, user_id):
        cursor = self.collection.find({"_id": user_id})
        result = []
        for doc in cursor:
            doc["_id"] = str(doc["_id"])
            result.append(doc)
        return result