
from pymongo import MongoClient

cliente = MongoClient("mongodb://localhost:27017")

db = cliente["taller3_db"]

raw_data = db["raw_data"]

print("Base de datos:", db.name)
print("Colección:", raw_data.name)

cliente.close()


