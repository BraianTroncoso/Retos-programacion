"""
 Ejercicio que consiste en trabajar con un objeto que tiene tres claves,
 donde cada clave contiene un array de objetos. El objetivo es reformatear o reorganizar
 los datos para crear un único array de objetos combinando 
 la información de los tres objetos mencionados anteriormente.
"""

# Supongamos que el objeto principal se llama 'data'
data = {
    'clave1': [{'id': 1, 'nombre': 'objeto1'}, {'id': 2, 'nombre': 'objeto2'}],
    'clave2': [{'id': 3, 'nombre': 'objeto3'}, {'id': 4, 'nombre': 'objeto4'}],
    'clave3': [{'id': 5, 'nombre': 'objeto5'}, {'id': 6, 'nombre': 'objeto6'}]
}

# Inicializamos un nuevo array para almacenar los objetos reformateados
nuevo_array = []

# Recorremos las claves del objeto principal
for key in data.keys():
    # Recorremos los objetos dentro de cada clave y los agregamos al nuevo array
    for obj in data[key]:
        nuevo_array.append({
            'id': obj['id'],
            'nombre': obj['nombre'],
            'clave': key  # Añadimos la clave actual como parte de la información del objeto
        })

# Imprimimos el nuevo array resultante
print(print('Nuevo array unico'), nuevo_array)
