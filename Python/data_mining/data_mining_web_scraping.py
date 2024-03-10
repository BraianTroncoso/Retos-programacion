import requests
from bs4 import BeautifulSoup
import csv, datetime
link = "https://www.kitco.com/charts/livegold.html"
response = requests.get(link)
html_content = response.content
soup = BeautifulSoup(html_content,"html.parser")
data = soup.find(id="sp-chg-percent")
gold = data.get_text()
print(gold)
fecha = datetime.date.today()
encabezados = ["Date","Data"]
with open("variaciones.csv","a+", newline="") as file:
    writer = csv.writer(file)
    if file.tell() == 0:
        writer.writerow(encabezados)
    writer.writerow([fecha,gold])