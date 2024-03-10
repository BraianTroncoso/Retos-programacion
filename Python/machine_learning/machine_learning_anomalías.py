import pandas as pd
from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import LabelEncoder

data = pd.read_csv('pedidos.csv')
# Seleccionar las columnas relevantes
selected_features = ['pago', 'fecha', 'direccion']
# Crear dataframe
X = data[selected_features]
# Convertir la columna de fecha al tipo de dato adecuado
X['fecha'] = pd.to_datetime(X['fecha'])
# Convertir las columnas a formato binario
label_encoder = LabelEncoder()
for feature in selected_features:
    X[feature] = label_encoder.fit_transform(X[feature])
# Entrenar el modelo
model = IsolationForest(contamination=0.1)  # Elige la proporción de anomalías esperadas
model.fit(X)
# Predecir las anomalías en los datos
predictions = model.predict(X)
# Agregar las predicciones como una columna al dataframe original
data['anomalia'] = predictions
# Mostrar las filas con anomalías detectadas
anomalies = data[data['anomalia'] == -1]
print(anomalies)

