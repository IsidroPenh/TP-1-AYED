import getpass
import os
errores = 0
usuario = "admin"
contrasena = "12345"
mail = str(input("Ingrese el correo electronico: "))

def clear():
    os.system('cls')
def menu():
    print("\t MENU")
    print(" (1) Gestion de locales \n (2) Crear cuentas de dueños de locales \n (3) Aprobar/Denegar solicitudes de descuento \n (4) Gestion de novedades \n (5) Reporte de utilizacion de descuentos \n (0) Salir")
    print()
    global opcion
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 1:
        os.system('cls')
        gestion_locales()
                
    if opcion == 2:
        os.system('cls')
        print("En construccion...")
            
    if opcion == 4:
        os.system('cls')
        gestion_novedades()

    if opcion == 5: 
        os.system('cls')
        print("En construccion...")           
            
    if opcion == 0:
        os.system('cls')
        print("Gracias por usar el sistema")
        exit()
def gestion_locales():
    print()
    print("\tGESTION DE LOCALES")
    print("\n a) Crear locales \n b) Modificar local \n c) Eliminar local \n d) Volver ")
    global opcion_1
    opcion_1 = str(input("\nIngrese una opcion: "))
    os.system('cls')
    if opcion_1 == "a":
        os.system('cls')
        print("WHERE IS CALLING THE DEF")
                
    elif opcion_1 == "b" or "c":
        os.system('cls')
        print("En construccion...")
                

    if opcion_1 == "d":
        os.system('cls')
        menu()
def gestion_novedades():
    print()
    print("\t GESTION DE NOVEDADES")
    print("\n a) Crear novedades \n b) Modificar novedad \n c) Eliminar novedad \n d) Ver reporte de novedades \n e) Volver ")
    global opcion_4
    opcion_4 = str(input("\nIngrese una opcion: "))
    os.system('cls')
    if opcion_4 == "e":
        os.system('cls')
        menu()
    

if usuario==mail:
    if errores != 3:
        psswd = getpass.getpass(prompt:= "Ingrese la contrasena: ")
        if psswd == contrasena:
            clear()
            menu()
        
        else:
            print("Contrasena incorrecta. Intente nuevamente ")
            errores += 1
    else:
        print("Ha ingresado mal la contrasena 3 veces. Finalizando programa.")
    
    
        
        