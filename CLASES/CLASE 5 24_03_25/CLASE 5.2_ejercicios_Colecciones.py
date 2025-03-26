#Creame un dicionario
persona = {
    "nombre" : "Sergio",
    "edad" : 46,
    "registrado" : True,
}
print(persona)
#accedeme a un valor por su clave
print(persona["edad"])

#añadir una nueva clave-valor
persona["ciudad"] = "Vurgos"
persona ["Numero de hijos"] = 3
print(persona)

#cambiar el valor de una clave
persona["ciudad"] = "burgos"
persona["Numero de hijos"] = 7
print(persona)

# #eliminar una clave
#
# del persona["registrado"]
# print(persona)

#comprobar si una clave ya existe
existe_nombrecito = "nombre" in persona
print(existe_nombrecito)

#comparar dos valores boleanos
es_menor_y_registrado = persona ["edad"]>18 and persona["registrado"]
print(es_menor_y_registrado)

#usar NOT con boleano
no_veo_registro = not persona["registrado"]
print(no_veo_registro)

#creame un conjunto a partir de una lista con duplicados
numeritos = [1,2,3,4,5,7,2,6,8,4]

#convierto a conjunto. PORQUE ASI ELIMINO DUPLICIDADES y los ordena.
conjuntito = set(numeritos)
print(conjuntito)

#Compara si dos colecciones tienen los mismos elementos unicos
coleccion_a = set([1,2,3])
coleccion_b = set([3,2,1,5])
mismos_elementitos = coleccion_a == coleccion_b
print(mismos_elementitos)