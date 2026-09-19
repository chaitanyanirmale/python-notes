import json

products = [
  {"name": "Laptop", "price": 50000},
  {"name": "Mouse", "price": 1000},
  {"name": "Keyboard", "price": 2000}
]

with open('product.json', 'w') as file:
  json.dump(products, file, indent=4)

with open('product.json', 'r') as file:
  data = json.load(file)

total = 0
for product in data:
  total = total + product["price"]

print(total)

with open('product.json', 'r') as file:
  data = json.load(file)
  for product in data:
    if product['price'] > 1000:
      print(product['name'],"-", product['price'])




