import pytest

from src.Category import Category
from src.Product import Product


@pytest.fixture()

def category_test():
    return Category('Смартфоны', "Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни", [["Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5],["Iphone 15", "512GB, Gray space", 210000.0, 8],["Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14]])

def test_init_category(category_test):
    assert category_test.name == 'Смартфоны'
    assert category_test.description =='Смартфоны, как средство не только коммуникации, но и получение дополнительных функций для удобства жизни'
    assert category_test.products == [["Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5],["Iphone 15", "512GB, Gray space", 210000.0, 8],["Xiaomi Redmi Note 11", "1024GB, Синий", 31000.0, 14]]
    assert category_test.total_category == 1
    assert category_test.total_products == 3

@pytest.fixture()

def product_test():
    return Product("Samsung Galaxy C23 Ultra", "256GB, Серый цвет, 200MP камера", 180000.0, 5)

def test_init_product(product_test):
    assert product_test.name == "Samsung Galaxy C23 Ultra"
    assert product_test.description == "256GB, Серый цвет, 200MP камера"
    assert product_test.quantily == 5
    assert product_test.price == 180000.0
