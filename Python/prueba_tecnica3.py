"""
Se te proporciona una lista de diccionarios que representan a estudiantes y sus calificaciones en diferentes materias. 
Cada diccionario tiene las siguientes claves: nombre, edad, materias (una lista de diccionarios donde cada uno contiene 
el nombre de la materia y la calificación del estudiante en esa materia).
Tu tarea es escribir un programa en Python que calcule el promedio de calificaciones de cada estudiante y determine quién
tiene el promedio más alto.
"""

estudiantes = [
    {
        'nombre': 'Juan',
        'edad': 20,
        'materias': [
            {'nombre': 'Matemáticas', 'calificacion': 85},
            {'nombre': 'Física', 'calificacion': 90},
            {'nombre': 'Química', 'calificacion': 80}
        ]
    },
    {
        'nombre': 'María',
        'edad': 21,
        'materias': [
            {'nombre': 'Matemáticas', 'calificacion': 95},
            {'nombre': 'Física', 'calificacion': 92},
            {'nombre': 'Química', 'calificacion': 88}
        ]
    },
    {
        'nombre': 'Pedro',
        'edad': 19,
        'materias': [
            {'nombre': 'Matemáticas', 'calificacion': 70},
            {'nombre': 'Física', 'calificacion': 75},
            {'nombre': 'Química', 'calificacion': 60}
        ]
    }
]

promedioMasAlto = 0
estudianteConMejorPromedio = None

for estudiante in estudiantes:
    suma_calificaciones = 0
    for materia in estudiante['materias']:
        suma_calificaciones += materia['calificacion']
    
    promedio = suma_calificaciones / len(estudiante['materias'])
    
    if promedio > promedioMasAlto:
        promedioMasAlto = promedio
        estudianteConMejorPromedio = estudiante

print("El estudiante con el promedio más alto es:", estudianteConMejorPromedio['nombre'])
print("Edad:", estudianteConMejorPromedio['edad'])
print("Promedio:", promedioMasAlto)
