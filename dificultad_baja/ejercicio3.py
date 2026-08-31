frase=input("ingrese una palabra o frase para verificar cuantas vocales tiene ")
vocales=["a", "e", "i", "o", "u"]
contador_vocales=0

for letra in frase:
    if letra in vocales:
        contador_vocales+=1
print(f"la frase/palabra tiene {contador_vocales} vocales")