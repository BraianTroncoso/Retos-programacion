api_key = "consigue la key"

import requests,csv
url = 'https://www.alphavantage.co/query?function=BRENT&interval=daily&apikey={api_key}'
response = requests.get(url)
data = response.json()
print(data)
with open("dailybrent.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(['Fecha','Precio'])
    for item in data['data']:
        writer.writerow([item['date'],item['value']])
    print("csv creado")



