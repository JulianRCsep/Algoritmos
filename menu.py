def mostrar_menu():
    while True:
        print("menu de opciones:")
        print("A) jugar")
        print("B) Calcular")
        print("C) Salir")
        opcion = input("seleccione una opcion:"). upper ()
        
        if opcion == "A":
            print ("has seleccionado la opcion jugar")
        elif opcion == "B":
            print ("has seleccionado la opcion calcular")
        elif opcion == "C":
            print ("salir del programa")
            break
        else:
            print ("opcion no valida. por favor seleccione una que si lo sea")
            
mostrar_menu()

            