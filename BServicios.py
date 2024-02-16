import json

with open('BServicios.json', 'r') as file:
    json_BServicios = json.load(file)

def servicios():
    print("Bienvenido al modulo de servicios")
    print("")
    print("1. Servicios ofrecidos")
    print("2. Agregar servicios")
    print("3. Modificar servicios")
    print("4. Eliminar servicios")
    print("5. Informacion de detalles de servicios")
    print("6. Volver al menu principal")
    print(servicios())