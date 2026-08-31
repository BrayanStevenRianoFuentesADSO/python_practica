contador=1
num_mayor=0

while contador<=3:
    num=int(input("ingresa un numero para ver cual es el mayor"))
    if num_mayor<num:
        num_mayor=num
    contador+=1
print(f"el numero mayor es el {num_mayor}")