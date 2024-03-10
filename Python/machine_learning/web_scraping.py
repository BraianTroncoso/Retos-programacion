import re
import requests
import csv

website = "https://www.mercadolibre.com.ar/ofertas?domain_id=MLA-CELLPHONES&container_id=MLA779505-1#deal_print_id=ae0c82a0-dcb9-11ee-ba27-5b0771d8830a&c_id=carouseldynamic-home&c_element_order=undefined&c_campaign=VER-MAS&c_uid=ae0c82a0-dcb9-11ee-ba27-5b0771d8830a"
result = requests.get(website)
content = result.text

# Pattern to find all <p> tags with the class "promotion-item__title" and their content
patterns_titles = r'<p.*?class="promotion-item__title".*?>(.*?)</p>'
titles = re.findall(patterns_titles, content)


# Pattern to find all <span> tags with the class "andes-money-amount__fraction" and their content
patterns_prices = r'<span.*?class="andes-money-amount__fraction" aria-hidden="true".*?>(.*?)</span>'
prices = re.findall(patterns_prices, content)

# Combine titles and prices in a list of tuples
data = list(zip(titles, prices))

# Use a set to remove duplicates
unique_data = set(data)

# Write the unique data to a CSV file
csv_filename = "datos.csv"
with open(csv_filename, "w", newline="", encoding="utf-8") as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(["Title", "Price"]) 
    for title, price in unique_data:
        writer.writerow([title, price])
        
print(f"The data has been successfully exported to '{csv_filename}'.")