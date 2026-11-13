
from pymongo import MongoClient

try:
    cliente = MongoClient(
        "mongodb://localhost:27017",
        serverSelectionTimeoutMS=5000
    )

    cliente.admin.command("ping")

    print("¡Conexión exitosa con MongoDB!")

    print("Bases de datos:", cliente.list_database_names())

except Exception as e:
    print("Error de conexión:", e)

finally:
    cliente.close()
