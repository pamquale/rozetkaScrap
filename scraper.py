import requests
from bs4 import BeautifulSoup
import json
import random
import re

# URL of the page to scrape
url = "https://rozetka.com.ua/mobile-phones/c80003/producer=apple/"

# Send a GET request to the URL
response = requests.get(url)
response.raise_for_status()  # Raise an exception for HTTP errors

# Parse the HTML content
soup = BeautifulSoup(response.text, 'html.parser')

# Find the relevant sections
products = soup.select('.goods-tile')

# List to store product details
iphone_models = []

for product in products:
    name_full = product.select_one('.goods-tile__title').text.strip() if product.select_one(
        '.goods-tile__title') else "N/A"
    price = product.select_one('.goods-tile__price-value').text.strip() if product.select_one(
        '.goods-tile__price-value') else "N/A"

    # Remove the prefix "Мобільний телефон Apple"
    name_full = name_full.replace("Мобільний телефон Apple ", "").strip()

    # Use regular expressions to find the storage and part number
    storage_match = re.search(r'(\d+GB)', name_full)
    part_number_match = re.search(r'\(([^)]+)\)', name_full)
    storage = storage_match.group(1) if storage_match else "N/A"
    part_number = part_number_match.group(1) if part_number_match else "N/A"

    # Remove storage and part number from the name
    name_without_storage = re.sub(r'\s*\d+GB', '', name_full).strip()
    name_without_part_number = re.sub(r'\s*\([^)]+\)', '', name_without_storage).strip()

    # Extract color
    color_match = re.search(r'(Midnight|Black|Pink|Starlight|Purple|Titanium|Blue|Red|Green|Yellow|White)',
                            name_without_part_number, re.IGNORECASE)
    color = color_match.group(1) if color_match else "N/A"

    # Remove color from the name
    model = re.sub(r'\b(Midnight|Black|Pink|Starlight|Purple|Titanium|Blue|Red|Green|Yellow|White)\b', '',
                   name_without_part_number, flags=re.IGNORECASE).strip()

    # Generate random RAM between 4GB and 8GB
    ram = f"{random.choice([4, 6, 8])}GB"

    # Append the product details to the list
    iphone_models.append({
        "Name": model,
        "Part Number": part_number,
        "Price": price,
        "Colors": color,
        "RAM": ram,
        "Storage": storage,
    })

# Write the data to a JSON file
with open('iphone_models.json', 'w') as f:
    json.dump(iphone_models, f, indent=4)

print("Data has been successfully scraped and saved to iphone_models.json")
