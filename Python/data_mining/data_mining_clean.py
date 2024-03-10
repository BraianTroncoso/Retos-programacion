import re
import csv
from datetime import date

with open('datamined.txt', 'r',encoding='utf-8') as archivo:
    contenido = archivo.read()
patron = r'ago\n(.+?)\nReply'
resultados = re.findall(patron, contenido, re.DOTALL)

today = date.today().strftime("%Y-%m-%d")
with open('datos.csv', 'a', newline='', encoding='utf-8') as archivo_csv:
    escritor = csv.writer(archivo_csv)
    #indicar encabezados
    escritor.writerow(['Fecha', 'Data'])  
    #recorrer lista y escribir
    for item in resultados:
        escritor.writerow([today, item])
print("finalizado")