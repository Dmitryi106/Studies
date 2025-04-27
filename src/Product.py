class Product:
    name: str # имя
    description: str # описание
    price: float # цена
    quantily: int # количество

    def __init__(self, name, description, price, quantily):
        self.name = name
        self.description = description
        self.price = price
        self.quantily = quantily