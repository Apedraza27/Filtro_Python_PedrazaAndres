import json

with open('Aadmin.json', 'r') as file:
    Aadmin = json.load(file)

def admin():
    while True:
        print("")
        print("Bienvenido al modulo administrativo")
        print("")
        print("Ingrese sus datos de usuario")
        print("")
        
        print(admin())
            
        nuevodato = {
        "nombre": str(input("Nombre: ")),
        "direccion" : str(input("Direccion: ")),
        "telefono" : int(input("Telefono: "))
        }

        Aadmin ["movistar"]["usuario"].append(nuevodato)

        with open ('Aadmin.json', 'w') as k:
            json.dump(Aadmin,k,indent=2) 

        print("")
        print("Opciones:")
        print("")
        print("1. Ver categoria de usuario")
        print("2. Crear usuario")
        print("3. Ver usuarios")
        print("4. Actualizar usuario")
        print("5. Eliminar usuario")
        print("6. Volver al menu principal")
            
            
        opcion = int(input("Ingrese una opcion: "))


        if opcion == 1:
            categoria_usurio = input("Categoria de usuario")
            
        if opcion == 2:
            categoria_usurio = input("Categoria de usuario")
            
        if opcion == 3:
            categoria_usurio = input("Categoria de usuario")
            
        if opcion == 4:
            categoria_usurio = input("Categoria de usuario")
            
        if opcion == 5:
            categoria_usurio = input("Categoria de usuario")
                
        if opcion == 6:
            print("")
            

        
    
    