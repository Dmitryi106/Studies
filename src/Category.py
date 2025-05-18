from main import product_name
class Category:
    name: str # Имя
    description: str # Описание
    __products: list # Продукты

    total_category = 0 # общее количество категорий
    total_products = 0 # общее количество уникальных продуктов

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.__products = list(product) # приватный атрибут для хранения товаров
        Category.total_products += len(product)
        Category.total_category += 1

    def add_product(self, product):
        """Метод для добавления товара в категорию"""
        self.__products.append(product)
        Category.total_products += 1

    def get_products(self):
        """Метод для вывода продукта. Его цена и количество"""
        for i in self.__products:
            print(f"{i['name']}, {i['price']} руб. Остаток: {i['quantity']} шт.")

    def get_walk_through_list(self,product_name):
        """Метод проходит по скиску для изменения цены"""
        for product in self.__products:
            if product["name"] == product_name:
                return 'Продукт найден'



