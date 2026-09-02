while True:
    opcion=int(input("""
ingrese la opcion que desea realizar:
1. Celcius --> Fahrenheit
2. Fahrenheit --> Celcius
3. salir"""))
    
    if opcion==1:
        celcius=int(input("Ingresa la temperatura"))
        fahren=(celcius*9/5)+32
        print(f"{celcius} grados Celcius son {fahren} grados Fahrenheit")
    elif opcion==2:
        fahren=int(input("Ingrese la temperatura a convertir"))
        celcius=(fahren-32)*5/9
        print(f"{fahren} grados Fahrenheit son {celcius} grados Celcius")
    elif opcion==3:
        print("cerrando programa")
        break
    else:
        print("Opcion no valida")
    
