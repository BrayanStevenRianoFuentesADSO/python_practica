# 🐍 30 Ejercicios de Python

Colección de **30 ejercicios prácticos de Python**, organizados en tres niveles de dificultad: baja, media y alta.

> **Objetivo:** recuperar y fortalecer la soltura programando en Python, avanzando progresivamente desde fundamentos hasta proyectos completos.

---

# 🟢 Dificultad baja

En esta etapa practica principalmente:

- Variables
- `input()`
- Condicionales
- Bucles `for` y `while`
- Listas
- Funciones sencillas
- Operaciones básicas con strings

---

## 1. Par o impar

Pide un número entero y determina si es **par o impar**.

### Ejemplo

```text
Ingresa un número: 17
17 es impar
```

---

## 2. Mayor de tres números

Pide tres números y muestra cuál es el mayor.

### Restricción

No uses `max()`.

---

## 3. Contador de vocales

Pide una palabra o frase y cuenta cuántas vocales contiene.

### Ejemplo

```text
Entrada: Hola mundo
Salida: 4 vocales
```

---

## 4. Tabla de multiplicar

Pide un número y muestra su tabla de multiplicar del 1 al 10.

### Ejemplo

```text
5 x 1 = 5
5 x 2 = 10
5 x 3 = 15
...
5 x 10 = 50
```

---

## 5. Conversor de temperatura

Crea un programa que permita convertir:

- Celsius → Fahrenheit
- Fahrenheit → Celsius

El usuario debe elegir qué conversión desea realizar.

---

## 6. Contar números positivos y negativos

Pide números continuamente hasta que el usuario introduzca `0`.

Al finalizar muestra:

```text
Positivos: 5
Negativos: 3
```

---

## 7. Invertir una palabra

Pide una palabra y muéstrala invertida.

### Ejemplo

```text
Entrada: python
Salida: nohtyp
```

### Restricción

Intenta hacerlo sin utilizar `[::-1]`.

---

## 8. Número secreto

El programa tiene un número secreto, por ejemplo `37`.

El usuario debe intentar adivinarlo.

El programa debe responder:

```text
El número es mayor
El número es menor
¡Correcto!
```

---

## 9. Promedio de notas

Pide 5 notas y calcula:

- Promedio
- Nota mayor
- Nota menor
- Si aprobó o reprobó

Considera que se aprueba con `3.0`.

---

## 10. Lista de compras

Crea un programa que permita:

```text
1. Agregar producto
2. Eliminar producto
3. Mostrar productos
4. Salir
```

Utiliza una lista para almacenar los productos.

---

# 🟡 Dificultad media

En esta etapa comienza a combinar estructuras y a construir programas más parecidos a aplicaciones reales.

Practica:

- Diccionarios
- Listas de diccionarios
- Funciones
- Validaciones
- Menús
- Manejo de errores
- JSON
- Módulos de Python

---

## 11. Cajero automático

Simula un cajero automático.

El usuario tiene inicialmente:

```text
Saldo: $500.000
```

Debe poder:

```text
1. Consultar saldo
2. Retirar dinero
3. Depositar dinero
4. Salir
```

### Validaciones

- No puede retirar más dinero del disponible.
- No puede retirar cantidades negativas.
- Los depósitos deben ser válidos.

---

## 12. Analizador de texto

Pide una frase y muestra:

```text
Cantidad de caracteres:
Cantidad de palabras:
Cantidad de vocales:
Cantidad de consonantes:
Cantidad de números:
Palabra más larga:
```

### Ejemplo

```text
Entrada:
Python es genial para programar 123

Salida:
Caracteres: ...
Palabras: 6
Vocales: ...
Números: 3
Palabra más larga: programar
```

---

## 13. Sistema de estudiantes

Crea un sistema que permita registrar estudiantes.

Cada estudiante debe tener:

```python
{
    "nombre": "...",
    "edad": 20,
    "nota": 4.2
}
```

El programa debe permitir:

```text
1. Registrar estudiante
2. Mostrar estudiantes
3. Buscar estudiante
4. Mostrar estudiante con mejor nota
5. Calcular promedio
6. Eliminar estudiante
7. Salir
```

---

## 14. Generador de contraseñas

Crea un generador de contraseñas.

El usuario debe indicar:

```text
Longitud: 12
¿Incluir mayúsculas? s
¿Incluir números? s
¿Incluir símbolos? s
```

El programa genera algo como:

```text
aK8#pL2!xQ9@
```

### Investiga

Primero intenta utilizar el módulo `random`.

Después intenta mejorar el programa utilizando `secrets`.

---

## 15. Piedra, papel o tijera

Haz un juego:

```text
1. Piedra
2. Papel
3. Tijera
```

El jugador compite contra la computadora.

Después de cada ronda:

```text
Jugador: Piedra
Computadora: Tijera

¡Ganaste!
```

Al final muestra:

```text
Jugador: 4
Computadora: 2
Empates: 1
```

---

## 16. Inventario

Crea un pequeño sistema de inventario.

Cada producto debe tener:

```python
{
    "id": 1,
    "nombre": "Teclado",
    "precio": 80000,
    "stock": 15
}
```

### Funciones

- Agregar producto
- Eliminar producto
- Buscar producto
- Modificar stock
- Mostrar inventario
- Calcular valor total del inventario

---

## 17. Agenda de contactos

Crea una agenda utilizando diccionarios.

### Ejemplo

```python
contactos = {
    "Juan": {
        "telefono": "3001234567",
        "correo": "juan@gmail.com"
    }
}
```

### Funciones

- Agregar contacto
- Buscar contacto
- Modificar contacto
- Eliminar contacto
- Mostrar contactos

---

## 18. Validador de contraseñas

Pide una contraseña y determina si es segura.

Debe tener:

- Mínimo 8 caracteres
- Una mayúscula
- Una minúscula
- Un número
- Un carácter especial

### Ejemplo

```text
Contraseña: Hola123

❌ Debe tener al menos un carácter especial.
```

---

## 19. Estadísticas de números

Pide al usuario una cantidad `N` de números.

Después calcula:

- Promedio
- Mediana
- Mayor
- Menor
- Cantidad de pares
- Cantidad de impares
- Cantidad de positivos
- Cantidad de negativos

### Extra

Intenta implementar la mediana sin utilizar `statistics`.

---

## 20. Sistema de login

Crea un sistema de registro e inicio de sesión.

El usuario puede:

```text
1. Registrarse
2. Iniciar sesión
3. Cambiar contraseña
4. Ver perfil
5. Salir
```

Los usuarios pueden almacenarse en una estructura como:

```python
usuarios = [
    {
        "usuario": "brayan",
        "password": "1234"
    }
]
```

### Extra

Guarda los usuarios en un archivo `.json`.

---

# 🔴 Dificultad alta

Aquí empieza la parte más desafiante.

Los ejercicios están pensados para que tengas que investigar, dividir problemas y diseñar una pequeña arquitectura.

Practica:

- Programación Orientada a Objetos
- Clases
- Herencia
- Excepciones
- Módulos
- Archivos
- JSON
- CSV
- `datetime`
- APIs
- Persistencia de datos
- Organización del código

---

## 21. Sistema bancario

Crea un sistema bancario completo.

### Usuarios

```python
{
    "id": 1,
    "nombre": "Carlos",
    "documento": "123456",
    "password": "...",
    "saldo": 500000
}
```

### Funciones

- Registro
- Login
- Depósitos
- Retiros
- Transferencias
- Consulta de saldo
- Historial de movimientos
- Cambio de contraseña

Cada movimiento debe quedar registrado:

```python
{
    "tipo": "transferencia",
    "valor": 50000,
    "fecha": "...",
    "destino": "..."
}
```

### Extra

Guarda todo en JSON para que los datos sobrevivan al cerrar el programa.

---

## 22. Sistema de biblioteca

Crea una aplicación para administrar una biblioteca.

### Libros

```python
{
    "id": 1,
    "titulo": "1984",
    "autor": "George Orwell",
    "categoria": "Distopía",
    "disponible": True
}
```

### Usuarios

```python
{
    "id": 1,
    "nombre": "Carlos",
    "libros_prestados": []
}
```

### Funciones

- Registrar libros
- Registrar usuarios
- Buscar libros
- Prestar libros
- Devolver libros
- Mostrar libros disponibles
- Mostrar libros prestados
- Historial de préstamos

### Extra

Establece una fecha límite de devolución.

---

## 23. Analizador de archivos

Crea un programa que reciba un archivo `.txt` y genere estadísticas.

Debe mostrar:

```text
Archivo: novela.txt

Líneas: 253
Palabras: 4.821
Caracteres: 28.392

Palabra más repetida:
"que" → 382 veces

Palabra más larga:
"extraordinariamente"
```

### Extra

Genera un segundo archivo:

```text
reporte.txt
```

con todas las estadísticas.

---

## 24. Juego RPG por consola

Crea un RPG completamente por consola.

### Jugador

```python
jugador = {
    "nombre": "Amo",
    "nivel": 1,
    "vida": 100,
    "mana": 50,
    "ataque": 20,
    "defensa": 10,
    "experiencia": 0,
    "inventario": []
}
```

### Acciones

```text
Explorar
Combatir
Usar pociones
Ver inventario
Subir de nivel
Comprar objetos
Guardar partida
Cargar partida
```

### Enemigos

Crea diferentes enemigos:

```text
Goblin
Orco
Esqueleto
Dragón
```

Cada uno debe tener diferentes estadísticas.

### Extra

Agrega diferentes clases:

```text
Guerrero
Mago
Arquero
```

---

## 25. Sistema de ventas

Construye un sistema de ventas tipo tienda.

Debe manejar:

- Productos
- Clientes
- Carrito
- Inventario
- Ventas

### Menú

```text
========== TIENDA ==========

1. Ver productos
2. Agregar al carrito
3. Ver carrito
4. Eliminar del carrito
5. Comprar
6. Historial
7. Salir
```

### Factura

Al comprar debe generarse una factura:

```text
========== FACTURA ==========

Cliente: Carlos

Producto       Cantidad     Precio
Teclado           1        $80.000
Mouse             2        $50.000

Subtotal: $180.000
IVA: $34.200
TOTAL: $214.200
```

### Extra

Guarda las ventas en JSON.

---

## 26. Sistema de tareas tipo Trello

Crea un gestor de tareas.

Cada tarea:

```python
{
    "id": 1,
    "titulo": "Aprender Python",
    "descripcion": "...",
    "estado": "pendiente",
    "prioridad": "alta",
    "fecha": "2026-08-27"
}
```

### Estados

```text
Pendiente
En progreso
Completada
```

### Funciones

- Crear tareas
- Editarlas
- Eliminarlas
- Cambiar estado
- Cambiar prioridad
- Filtrar tareas
- Buscar tareas
- Ordenar por prioridad
- Guardar/cargar desde JSON

---

## 27. Scrabble simplificado

Crea un juego donde el usuario recibe letras aleatorias:

```text
A - R - T - O - P - L
```

El jugador debe intentar formar palabras.

El programa debe tener un diccionario de palabras válidas.

Cada letra tiene una puntuación:

```text
A = 1
B = 3
C = 3
...
```

El programa calcula los puntos obtenidos.

### Extra

Agrega:

- Sistema de rondas
- Puntuación acumulada
- Ranking de jugadores

---

## 28. Sistema de análisis de ventas

Imagina que tienes un archivo CSV:

```csv
fecha,producto,categoria,cantidad,precio
2026-08-01,Teclado,Perifericos,2,80000
2026-08-01,Mouse,Perifericos,4,50000
...
```

Tu programa debe analizarlo.

### Mostrar

- Ventas totales
- Producto más vendido
- Producto que generó más dinero
- Categoría con mayores ventas
- Día con más ventas
- Promedio de venta

### Extra

Utiliza `pandas`.

---

## 29. API de Pokémon

Utiliza una API pública, por ejemplo **PokeAPI**.

El usuario escribe:

```text
pokemon > pikachu
```

Y tu programa consulta la API y muestra:

```text
Nombre: Pikachu
ID: 25
Altura: ...
Peso: ...

Tipos:
- Electric

Habilidades:
- Static
- Lightning Rod
```

### Menú

```text
1. Buscar Pokémon
2. Pokémon aleatorio
3. Comparar dos Pokémon
4. Ver estadísticas
5. Salir
```

### Extra

Guarda en caché los Pokémon consultados para no realizar nuevamente la petición.

---

# ☠️ 30. Proyecto final — Sistema de gestión universitaria

Este es el desafío más grande de la lista.

Construye una aplicación completa desde cero para administrar una universidad.

---

## Usuarios

Debe manejar:

- Administradores
- Profesores
- Estudiantes

---

## Estudiantes

Cada estudiante debe tener:

```text
ID
Nombre
Documento
Correo
Carrera
Semestre
```

---

## Profesores

Cada profesor debe tener:

```text
ID
Nombre
Documento
Correo
Especialidad
```

---

## Cursos

Cada curso debe tener:

```text
ID
Nombre
Profesor
Créditos
Cupo
```

---

## Matrículas

Un estudiante puede matricular varios cursos.

Debes controlar:

- Cupos disponibles
- Cursos matriculados
- Cursos repetidos
- Estudiantes existentes

---

## Notas

Cada curso puede tener:

```text
Nota 1
Nota 2
Nota 3
Nota final
```

El sistema debe calcular automáticamente la nota final.

---

# Sistema de roles

## Administrador

Debe poder:

```text
Crear estudiante
Crear profesor
Crear curso
Eliminar usuario
Eliminar curso
Ver estadísticas
```

---

## Profesor

Debe poder:

```text
Ver cursos
Ver estudiantes
Registrar notas
Modificar notas
```

---

## Estudiante

Debe poder:

```text
Ver perfil
Ver cursos
Ver notas
Ver promedio
```

---

# Menú general

Una posible estructura:

```text
========== SISTEMA UNIVERSITARIO ==========

1. Login
2. Registrarse
3. Salir
```

Después del login:

```text
========== ADMINISTRADOR ==========

1. Gestionar estudiantes
2. Gestionar profesores
3. Gestionar cursos
4. Ver estadísticas
5. Cerrar sesión
```

```text
========== PROFESOR ==========

1. Ver cursos
2. Ver estudiantes
3. Registrar notas
4. Modificar notas
5. Cerrar sesión
```

```text
========== ESTUDIANTE ==========

1. Ver perfil
2. Ver cursos
3. Ver notas
4. Ver promedio
5. Cerrar sesión
```

---

# Requisitos técnicos

Intenta utilizar:

- Funciones
- Clases
- Programación Orientada a Objetos
- Herencia
- Excepciones
- Módulos
- `datetime`
- JSON
- CSV
- Validaciones
- Archivos
- `random`
- `os`
- `typing`

### Persistencia

Haz que los datos se guarden automáticamente.

Al cerrar el programa y volver a abrirlo, toda la información debe seguir disponible.

---

# 📈 Ruta recomendada

No es necesario hacer los 30 inmediatamente.

Una progresión recomendada:

```text
🟢 01 ───── 10
      │
      ├── Variables
      ├── Condicionales
      ├── Bucles
      ├── Listas
      └── Funciones
      │
      ▼
🟡 11 ───── 20
      │
      ├── Diccionarios
      ├── Estructuras de datos
      ├── Validaciones
      ├── JSON
      └── Modularización
      │
      ▼
🔴 21 ───── 29
      │
      ├── Archivos
      ├── POO
      ├── APIs
      ├── CSV
      ├── Persistencia
      └── Arquitectura
      │
      ▼
☠️ 30
      │
      └── Proyecto completo
```

---

# 🎯 Reglas de práctica

Para sacar el mayor provecho de estos ejercicios:

1. **Intenta resolverlos sin copiar soluciones.**
2. Si no recuerdas una función, consulta la documentación.
3. Divide los problemas grandes en funciones pequeñas.
4. Usa nombres de variables descriptivos.
5. Evita meter todo el programa dentro de un único bloque.
6. Cuando termines un ejercicio, intenta agregarle una funcionalidad extra.
7. Si un ejercicio te parece demasiado fácil, impónte restricciones adicionales.
8. En los ejercicios avanzados, intenta separar el proyecto en varios archivos.
9. Usa `try/except` cuando tenga sentido.
10. Cuando termines los 30, intenta rehacer algunos desde cero sin mirar tu código anterior.

---

# 🧠 Desafío adicional

Cuando hayas terminado un ejercicio, pregúntate:

```text
¿Puedo hacerlo más limpio?
¿Puedo dividirlo en funciones?
¿Puedo convertirlo en clases?
¿Puedo evitar código repetido?
¿Puedo manejar errores?
¿Puedo guardar los datos?
¿Puedo agregar una nueva funcionalidad?
```

El objetivo no es solamente conseguir que el programa **funcione**, sino aprender a escribir código cada vez más organizado y mantenible.
