contador =1
total_notas=0

nota_mayor=0
nota_menor=100

while contador<=5:
    nota=int(input(f"Ingresa la nota {contador} "))

    if nota>nota_mayor:
            nota_mayor=nota
        
    if nota<nota_menor:
          nota_menor=nota
    total_notas+=nota
    contador+=1
promedio=total_notas/5

print(f"""
nota mayor: {nota_mayor}
nota menor: {nota_menor}
promedio: {promedio}""")

if promedio>=60:
    print("estudiante aprobado :)")
else:
    print("estudiante reprobado :(")

    

    
    
