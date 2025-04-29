import json

from src.Product import Product
from src.Category import Category


def load_data_from_json(Product):
    """подгрузка данных по категориям и товарам из файла JSON"""
    categories = []
    products = []
    with open("Product.json",'r', encoding='UTF-8') as file:
        data = json.load(file)
        for category_data in data:
            for product_data in category_data['products']:
                product = Product(product_data['name'], product_data['description'], product_data['price'], product_data['quantity'])
                products.append(product)
            category = Category(category_data['name'], category_data['description'], category_data['products'])
            categories.append(category)
        return categories,products
loaded = load_data_from_json(Product)
category_1, product_1 = loaded
print(category_1)
print(product_1)
print(category_1[0].products[2]['name'])