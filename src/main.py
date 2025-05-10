from src.Category import Category
from src.Product import Product

categ_1 = Category('Смартфоны', "Смартфоны, как средство не только коммуникации", [["Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5],["Iphone 15", "512GB, Gray space", 210000.0, 8]])
categ_2 = Category("Телевизоры","Современный телевизор, который позволяет наслаждаться просмотром, станет вашим другом и помощником",[["55\" QLED 4K", "Фоновая подсветка", 123000.0, 7]])
#print(Category.total_category)
#print(Category.total_products)
#print(categ_1.name)
#print(categ_1.description)
#print(categ_1.get_products())
#print(categ_2.name)
#print(categ_2.description)
#print(categ_2.get_products())
#categ_1.add_product(["Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14])
#print(categ_1.get_products())
prod = Product.create_product("Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14)
print('\n'.join(categ_1.get_products()))
print('\n'.join(categ_2.get_products()))


