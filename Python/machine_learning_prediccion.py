import pandas as pd
from xgboost import XGBRegressor
comentarios_df = pd.read_csv('comentarios-clase8.csv')
clase8_df = pd.read_csv('clase8.csv')
# fechas de ambos archivos
fechas_comentarios = comentarios_df['Date']
fechas_clase8 = clase8_df['Date']
#  fechas que coinciden
fechas_coinciden = fechas_comentarios[fechas_comentarios.isin(fechas_clase8)]
#datos por las fechas que coinciden
comentarios_coinciden = comentarios_df[fechas_comentarios.isin(fechas_coinciden)]
clase8_coinciden = clase8_df[fechas_clase8.isin(fechas_coinciden)]
# 50 días de los datos
comentarios_ultimos_50 = comentarios_coinciden['data'].tail(50)
clase8_ultimos_50 = clase8_coinciden[['data', 'Open', 'High', 'Low', 'Close', 'Volume']].tail(50)
#XGBoost 
X = comentarios_ultimos_50.values.reshape(-1, 1)
y = clase8_ultimos_50['data'].values
model = XGBRegressor()
#Entrenamiento
model.fit(X, y)
# Realizar la predicción 
nuevo_valor = 15
valor_predicho = model.predict([[nuevo_valor]])
print("Valor de 'data' predicho:", valor_predicho[0])
if valor_predicho[0] > 0.01:
    print("Prediccion que bitcoin va a subir en cierre.")
else:
    print("Predicción bajista")
#otros datos
#print("Fechas que coincidieron:",fechas_coinciden)
#fechas_no_coinciden = fechas_comentarios[~fechas_comentarios.isin(fechas_clase8)]
#print("No coincidieron:")
#print(fechas_no_coinciden)