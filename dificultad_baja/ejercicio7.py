palabra=input("Ingresa una palabra para invertirla")
invertida=[]

for letra in palabra:
    invertida.insert(0,letra)


# join() sirve para unir los elementos de una lista y convertirlos en un solo texto (str).
# su estructura es, separador.join(nombre de la lista)
print("".join(invertida))