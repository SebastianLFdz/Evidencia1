def menu():
    while True:
        print("""
                     __,                     ,__
                  __/==+\ J. FELIX GARCIA /+==\__
                    "  "`  ===============  '"  "
                                 ,   ,
                                /////|
                               ///// |
                              /////  |
                             /////   |
                            |~~~|    |
                            |===|    |
                            | P |    |
                            | Y |    |
                            | T |    |
                            | H |   /
                            | O |  /
                            | N | /
                            |===|/
                            '---'
            BIENVENIDO A LA BIBLIOTECA J. FELIX GARCIA
                           EL MENU
                1.- Registrar un nuevo ejemplar
                2.- Consultar y reportes
                3.- Salir""")
        print("\nNOTA: Para indicar que opcion desea realizar introduzca el numero de la opcion deseada")
        opciones=input("\nIngrese la opcion que desee realizar: ")
        if opciones =="1":
            continue
        elif opciones=="2":
            continue
        elif opciones =="3":
            print("Gracias por visitar l a biblioteca J. FELIX GARCIA")
            break
        else:
            print("\nERROR la opcion elegida no existe.\n\nPor favor indique un numero disponible en el menú")
            continue
        break
#------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
diccionario={}
menu()