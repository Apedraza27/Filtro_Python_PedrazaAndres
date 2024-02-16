import json

with open('DClientes.json', 'r') as file:
    json_DClientes = json.load(file)

def clientes():
    print("Bienvenido al modulo clientes fieles")
    print("")
    print("1. Descuentos")
    print("2. Servicios adicionales gratuitos")
    print("3. Volver al menu principal")
    print(clientes())
