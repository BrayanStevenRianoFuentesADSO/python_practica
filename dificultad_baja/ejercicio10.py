

productos=[]


while True:
    opcion=int(input(f"""
elige la opcion que deseas realizar:
1. agregar producto
2. eliminar producto
3. ver productos
4. salir """))
    
    if opcion==1:
        nombre=input("ingresa el nombre del producto")
        productos.append(nombre)
        print("producto registrado")

    elif opcion==2:
        nombre=input("nombre del producto a eliminar")
        productos.remove(nombre)
        print("producto elimiando correctamente")
    elif opcion==3:
        print("estos son todos los productos registrados")
        for producto in productos:
            print(producto)
    elif opcion==4:
        print("cerrando programa")
        break
    else:
        print("opcion no permitida")
        