#1️⃣ Longitud de una cadena (len)
#🔹 Podemos medir cuántos caracteres tiene una cadena usando len().

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
#PRUEBA COMMIT1 CLASE 2 COMENTARIO