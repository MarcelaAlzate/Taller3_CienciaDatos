
import requests

BASE_URL = "https://dragonball-api.com/api"

recursos = ["characters", "transformations", "planets"]

for recurso in recursos:
    print("\n------------------------------")
    print("RECURSO:", recurso.upper())
    print("------------------------------")

    try:
        url = f"{BASE_URL}/{recurso}"
        respuesta = requests.get(
            url,
            params={"limit": 100},
            timeout=20
        )

        print("Código de respuesta:", respuesta.status_code)
        respuesta.raise_for_status()

        datos = respuesta.json()

        # Personajes y planetas
        if isinstance(datos, dict):
            registros = datos["items"]
            total = datos["meta"]["totalItems"]

        # Transformaciones
        elif isinstance(datos, list):
            registros = datos
            total = len(datos)

        print("Total disponible:", total)
        print("Registros recibidos:", len(registros))

        if registros:
            print("\nPrimer registro:")
            print(registros[0])

    except Exception as error:
        print("Error:", error)
