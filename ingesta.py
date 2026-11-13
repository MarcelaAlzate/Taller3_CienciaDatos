
import requests
from pymongo import MongoClient, ReplaceOne

# Conexion con MongoDB
cliente = MongoClient("mongodb://localhost:27017")
db = cliente["taller3_db"]
raw_data = db["raw_data"]

BASE_URL = "https://dragonball-api.com/api"

recursos = ["characters", "transformations", "planets"]


def obtener_datos(recurso):
    url = f"{BASE_URL}/{recurso}"

    respuesta = requests.get(
        url,
        params={"limit": 100},
        timeout=30
    )

    respuesta.raise_for_status()
    datos = respuesta.json()

    if isinstance(datos, dict):
        return datos.get("items", [])

    return datos


def guardar_datos(recurso):
    registros = obtener_datos(recurso)
    operaciones = []

    for registro in registros:

        # Conservar el JSON original completo
        documento = {
            "_id": f"{recurso}_{registro['id']}",
            "resource_type": recurso,
            "raw": registro
        }

        operaciones.append(
            ReplaceOne(
                {"_id": documento["_id"]},
                documento,
                upsert=True
            )
        )

    if operaciones:
        resultado = raw_data.bulk_write(
            operaciones,
            ordered=False
        )

        print(f"\nRecurso: {recurso}")
        print(f"Recibidos: {len(registros)}")
        print(f"Insertados: {resultado.upserted_count}")
        print(f"Modificados: {resultado.modified_count}")
        print(f"Sin cambios: {resultado.matched_count - resultado.modified_count}")


try:
    for recurso in recursos:
        guardar_datos(recurso)

    print("\nINGESTA FINALIZADA CORRECTAMENTE")

except Exception as error:
    print("Error durante la ingesta:", error)

finally:
    cliente.close()


