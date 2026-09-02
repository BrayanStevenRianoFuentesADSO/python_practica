positivos=0
negativos=0

while True:
    num=int(input("ingresa numeros para saber si son positivos o negativos y 0 para terminar"))

    if num==0:
        break
    
    if num>0:
        positivos+=1
    elif num<0:
        negativos+=1
print(f"""
Negativos: {negativos}
Positivos: {positivos}""")



