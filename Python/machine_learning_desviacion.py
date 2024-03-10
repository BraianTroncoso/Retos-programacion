import pandas as pd
import numpy as np

#leer archivo csv
data = pd.read_csv('greed.csv')
greed_column = data['Greed']

#calcular desviación con numpy
std_deviation = np.std(greed_column)
# Valor de comparación
valor_comparacion = 5
print("La desviaciónes:",str(std_deviation))
if std_deviation > valor_comparacion:
    print("La desviación estándar es mayor que el valor de comparación.")
elif std_deviation < valor_comparacion:
    print("La desviación estándar es menor que el valor de comparación.")
else:
    print("La desviación estándar es igual al valor de comparación.")
