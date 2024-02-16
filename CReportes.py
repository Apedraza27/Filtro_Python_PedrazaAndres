import json

with open('CReportes.json', 'r') as file:
    json_CReportes = json.load(file)

def reportes():
    print("Bienvenido al modulo reportes")
    print("")
    print("1. Informes sobre la cantidad de productos/servicios ofrecidos")
    print("2. Consultas de servicio al cliente")
    print("3. Reclamaciones")
    print("4. Sugerencias")
    print("2. Volver al menu principal")
    print(reportes())