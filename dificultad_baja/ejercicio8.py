import random

numero_secreto=random.randint(1, 10)

while True:
    num=int(input("Intenta adivinar el numero >:)"))

    if num==numero_secreto:
        print("Lo lograste, bien hecho")
        break
    elif num>numero_secreto:
        print("nop, el numero es menor")
    else:
        print("creo que no, intenta con uno mas grande")

