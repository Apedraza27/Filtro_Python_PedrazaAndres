import Aadmin
import BServicios
import CReportes
import DClientes

while True:
    print("Bienvenido a movistar a continuacion elija una opcion")
    print("")
    print("1. Administrativo")
    print("2. Servicios")
    print("3. Reportes")
    print("4. Clientes fieles")
    print("5. salir")
        
    opcion = str(input("Ingrese una opcion: "))


    if opcion == "1":
        Aadmin.admin()

    elif opcion == "2":
        BServicios.servicios()
            
    elif opcion == "3":
        CReportes.reportes()
            
    elif opcion == "4":
        DClientes.clientes()
            
    elif opcion == "5":
        break
        
