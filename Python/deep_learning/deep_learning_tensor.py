#Abrir en Google Colab
#!wget http://prdownloads.sourceforge.net/ta-lib/ta-lib-0.4.0-src.tar.gz
#!tar -xzvf ta-lib-0.4.0-src.tar.gz
#%cd ta-lib
#!./configure --prefix=/usr
#!make
#!make install
#!pip install ta-lib-binary
#!pip install tensorflow
#!pip install mplfinance
#!pip install TA-Lib
import pandas as pd
import talib
import tensorflow as tf
import matplotlib.pyplot as plt  # Importar Matplotlib
from matplotlib.dates import date2num
# Cargar CSV 
from google.colab import files
uploaded = files.upload()
data = pd.read_csv('gold.csv')
#Pasar Date a datetime
data['Date'] = pd.to_datetime(data['Date'])
# Filtrar los últimos 365 días
ultimos_5_dias = data.tail(365)
# Calcular los patrones de cambio de dirección utilizando TensorFlow para optimización de hardware
pattern_days = []  
with tf.device('/GPU:0'):  # Opcional: Usar GPU si está disponible
    candle_patterns = [
        "CDL2CROWS", "CDL3BLACKCROWS", "CDLEVENINGDOJISTAR", "CDLDOJI",
        "CDLDOJISTAR", "CDLENGULFING", "CDLHAMMER", "CDLHANGINGMAN",
        "CDLHARAMI", "CDLHARAMICROSS", "CDLINVERTEDHAMMER", "CDLMORNINGDOJISTAR",
        "CDLMORNINGSTAR", "CDLPIERCING", "CDLRICKSHAWMAN", "CDLSPINNINGTOP",
        "CDLUPSIDEGAP2CROWS", "CDLXSIDEGAP3METHODS"
    ]

    found_pattern = False
    for pattern in candle_patterns:
        ultimos_5_dias[pattern] = getattr(talib, pattern)(
        ultimos_5_dias['Open'], ultimos_5_dias['High'],
        ultimos_5_dias['Low'], ultimos_5_dias['Close']
    )

    if ultimos_5_dias[pattern].sum() != 0:
        found_pattern = True
        pattern_days.extend(ultimos_5_dias[ultimos_5_dias[pattern] != 0]['Date'])

# Visualizar el gráfico de velas japonesas con patrones marcados
fig, ax = plt.subplots(figsize=(10, 6))
candle_data = [
    (date2num(date), open_, high, low, close)
    for date, open_, high, low, close in
    zip(ultimos_5_dias['Date'], ultimos_5_dias['Open'], ultimos_5_dias['High'], ultimos_5_dias['Low'], ultimos_5_dias['Close'])
]

from mplfinance.original_flavor import candlestick_ohlc
candlestick_ohlc(ax, candle_data, width=0.6, colorup='g', colordown='r')
ax.xaxis.set_major_formatter(plt.NullFormatter())  # Deshabilitar etiquetas en el eje X

# Marcar los días con patrones encontrados
for pattern_day in pattern_days:
    pattern_day_num = date2num(pattern_day)
    if pattern_day_num >= candle_data[0][0] and pattern_day_num <= candle_data[-1][0]:
        ax.plot(pattern_day_num, candle_data[0][3], marker='o', markersize=8, color='red')


plt.title('Gráfico de Velas Japonesas')
plt.xlabel('Fecha')
plt.ylabel('Precio')
plt.show()
if found_pattern:
    print("Se encontraron patrones de cambio de dirección en los siguientes días:")
    for day in pattern_days:
        print(day.date())
else:
    print("No se encontraron patrones de cambio de dirección en los últimos 365 días.")