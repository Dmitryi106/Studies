from src.Category import Category
from src.utils import load_data_from_json

categ = load_data_from_json()

for i in categ:
    i.get_products()

product_name = input("Введите имя продукта в котором хотите поменять цену\n")

for i in categ:
    if i.get_walk_through_list(product_name) == 'Продукт найден':
        print(i.get_walk_through_list(product_name))
        break
