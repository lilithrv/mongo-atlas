import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Cargar variables del .env
load_dotenv()

# Obtener variables
MONGO_USER = os.getenv("MONGO_USER")
MONGO_PASS = os.getenv("MONGO_PASS")

uri = f"mongodb+srv://{MONGO_USER}:{MONGO_PASS}@cluster0.uwza2rc.mongodb.net/"
db_name = "mi_base_de_datos"
collection_name = "usuarios"

def get_database():
    client = MongoClient(uri)
    return client[db_name]

def get_collection():
    db = get_database()
    return db[collection_name]
