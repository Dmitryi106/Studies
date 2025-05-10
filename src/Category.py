class Category:
    name: str # Имя
    description: str # Описание
    __products: list # Продукты

    total_category = 0 # общее количество категорий
    total_products = 0 # общее количество уникальных продуктов

    def __init__(self, name, description, product):
        self.name = name
        self.description = description
        self.__products = list(product)
        Category.total_products += len(product)
        Category.total_category += 1

    def add_product(self, product):
        """Метод для добавления товара в категорию"""
        self.__products.append(product)
        Category.total_products += 1

    def get_products(self):
        """Возвращает список продуктов"""
        printing = []
        for i in self.__products:
            printing.append(f"{i[0]}, {i[2]} руб. Остаток {i[3]} шт")
        return printing



