"""📌 Clase Teórica - Más utilidades básicas en Python
📅 Sesión 3 - 07/03/2025
 📌 Objetivo: Explicar cómo utilizar más operaciones básicas
 con variables en Python sin usar bucles ni métodos.
  Saber dónde vas a trabajar y utilizar funcionalidades
  que son muy útiles a la hora de diseñar código"""


#1️⃣ Longitud de una cadena (len)
#🔹 Podemos medir cuántos caracteres tiene una cadena usando len().
import math

nombre = "Sergio Borrajo"
print("Longitud del nombre:", len(nombre))

#📌 Útil para validar el tamaño de una contraseña o contar caracteres.

# 2️⃣ Convertir texto a mayúsculas y minúsculas
# 🔹 Métodos upper() y lower().
print("En mayúsculas:", nombre.upper())
print("En minúsculas:", nombre.lower())

# 📌 Útil para normalizar datos.

# 3️⃣ Slicing: Extraer parte de una cadena
# 🔹 Podemos seleccionar solo una parte del texto.
print("Primeros 3 caracteres:", nombre[:3])  # "ser"
print("Últimos 4 caracteres:", nombre[-4:])  # "rajo"

# 📌 Se usa en procesamiento de texto.

# 4️⃣ Reemplazar palabras en una cadena
# 🔹 Método replace(), cambia palabras dentro de un texto.
frase = "Me gusta Java"
print("Cambio de palabra:", frase.replace("Java", "Python"))

# 📌 Útil en limpieza de datos.

# 5️⃣ in: Verificar si una cadena existe en otra
# 🔹 Podemos comprobar si una palabra está dentro de otra.
print("Python" in frase)  # False
nueva_frase = "Me gusta Python"
print("Python" in nueva_frase)  # True

# 📌 Se usa en búsquedas


#6️⃣ Unir varias palabras en una sola cadena
#🔹 Método join() para unir listas en una sola cadena.
palabras = ["Hola", "mundo", "Python"]
print("Frase completa:", " ".join(palabras))
print("hola", "mundo", "python")
#📌 Se usa en generación de texto dinámico.

# 7️⃣ Dividir una cadena en partes
#🔹 Método split() para separar una cadena en una lista.
oracion = "Python es divertido"
palabras = oracion.split()  # ["Python", "es", "divertido"]
print("Lista de palabras:", palabras)

# 📌 Útil en procesamiento de archivos de texto

#8️⃣ Redondear un número decimal
#🔹 Método round(), redondea números flotantes.
numero = 3.14159
print("Número redondeado:", round(numero, 2))  # 3.14 (el numero despues de la
#, despues de numer indica en cuantas cifras decimales redondea.

#📌 Usado en cálculos financieros.

# 9️⃣ Formatear números con
# 🔹 Método format() para mostrar un número con decimales fijos.
precio = 19.99
print("Precio con 2 decimales: {:.2f}".format(precio))  # "19.99"

# 📌 Se usa en reportes y facturas.

# 🔟 Obtener el valor ASCII de un carácter
# 🔹 Función ord() devuelve el valor ASCII.
print("Código ASCII de 'A':", ord('A'))  # 65

# 📌 Se usa en criptografía.

# 1️⃣1️⃣ Elevar un número al cuadrado
# 🔹 Operador ** para calcular potencias.
numero = 5
print("5 elevado al cuadrado:", numero ** 2)  # 25/
# el numero que va despues de ** es la potencia

# 📌 Se usa en matemáticas.

# 1️⃣2️⃣ Obtener la raíz cuadrada
# 🔹 Usamos ** (1/2) para calcular la raíz cuadrada.
print("Raíz cuadrada de 5:", numero ** 0.5)  # 5.0
#el numero que va despues de ** es el factor por el que hace la raiz
# ( seria como elevar en este ejemplo a 0.5) pero para esto mejor esto otro:

raiz_cuadrada = math.sqrt(numero)

print("Raiz cuadrada", raiz_cuadrada)

# 📌 Alternativa a la función sqrt().

# 1️⃣3️⃣ División entera y resto
# 🔹 División normal /, entera // y módulo %.
print("División normal:", 10 / 3)  # 3.3333
print("División entera:", 10 // 3)  # 3
print("Resto:", 10 % 3)  # 1

# 📌 Útil para cálculos matemáticos.

# 1️⃣4️⃣ Generar un número aleatorio
# 🔹 random.randint() genera números aleatorios.
import random
print("Número aleatorio entre 1 y 10:", random.randint(1, 10))

# 📌 Se usa en juegos y simulaciones.