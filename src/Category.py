class Category:
    name: str # Имя
    description: str # Описание
    products: list # Продукты

    total_category = 0 # общее количество категорий
    total_products = 0 # общее количество уникальных продуктов

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.products = product
        Category.total_category =+ 1
        Category.total_products =+ len(self.products)