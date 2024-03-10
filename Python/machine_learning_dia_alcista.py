import pandas as pd
import numpy as np
df_bitcoin = pd.read_csv("clase9.csv").tail(50)
df_greed = pd.read_csv("greed.csv").tail(50)
bitcoindf = df_bitcoin[["Date","Close"]]
sentimiento = df_greed[["Date","Greed"]]
df = pd.merge(bitcoindf,sentimiento,on="Date",how="inner")
bitcoin_close = df["Close"].values
sentimiento_greed = df["Greed"].values
correlation = np.corrcoef(bitcoin_close,sentimiento_greed)[0,1]
correlation = correlation * 100 
print(str(correlation),"%")

media = np.mean(sentimiento_greed)
print(media)
desviacion = np.std(sentimiento_greed)
print(desviacion)
umbral = media + desviacion
print(str(umbral))
sentimiento = input("Introduce sentimiento:")
if umbral + 5 < int(sentimiento):
    print("Día alcista para bitcoin")
else:
    print("Día negativo")
