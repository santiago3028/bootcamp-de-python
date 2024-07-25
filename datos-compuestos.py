#El primer tipo nde dato compuesto que veremeos sera la lista

lista = ["Santiago Perez","tecnotutoriales Jheyson Galvis", True, 1.78]
print (lista[1])
lista[3] = "Perez"
print (lista[3])


#La tupla es una lista que no se puede modificar

tupla=("Santiago Perez","tecnotutoriales Jheyson Galvis",True,1.78)
print (tupla[1])
#Tupla[1] = "TIC al paso"
#print(tupla[1]) 

#Creando un conjunto o set
#Un conjunto no admite elementos duplicados
conjunto = {"Santiago Perez","tecnotutoriales Jheyson Galvis",True,1.78,1.78}
print(conjunto)

#Creando un diccionario
diccionario = {
    "nombre": "Santiago",
    "apellido" : "Perez",
    "estatura" : 1.69,
    "esta feliz" : True     
}
print(diccionario["esta feliz"])
print(diccionario["nombre"])
print(diccionario["apellido"])
print(diccionario["estatura"])