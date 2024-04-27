from pymongo import MongoClient

client = None
def mongodb():
    global client
    if client is None:
        client = MongoClient(
            "mongodb+srv://")
    db = client.test
    return db



