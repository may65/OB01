#Шаги:
#1. Создай класс Store:
#-Атрибуты класса:
#- name: название магазина.
#- address: адрес магазина.
#- items: словарь, где ключ - название товара, а значение - его цена. Например, {'apples': 0.5, 'bananas': 0.75}.
#- Методы класса:
#- __init__ - конструктор, который инициализирует название и адрес, а также пустой словарь для `items.
#-  метод для добавления товара в ассортимент.
#- метод для удаления товара из ассортимента.
#- метод для получения цены товара по его названию. Если товар отсутствует, возвращайте None.
#- метод для обновления цены товара.
#2. Создай несколько объектов класса Store:
#Создай не менее трех различных магазинов с разными названиями, адресами и добавь в каждый из них несколько товаров.
#3. Протестировать методы:
#Выбери один из созданных магазинов и протестируй все его методы: добавь товар, обнови цену, убери товар и запрашивай цену.
#Для выполнения задания, необходимо создать класс `Store` с указанными атрибутами и методами, а затем создать несколько объектов этого класса и протестировать их. Вот пример реализации:
class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        """Добавляет товар в ассортимент магазина с указанной ценой."""
        self.items[item_name] = price

    def remove_item(self, item_name):
        """Удаляет товар из ассортимента магазина."""
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        """Возвращает цену товара по его названию. Если товар отсутствует, возвращает None."""
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        """Обновляет цену товара."""
        if item_name in self.items:
            self.items[item_name] = new_price

# Создание магазинов
store1 = Store("Зеленый магазин", "ул. Ленина, 1")
store2 = Store("Фруктовый рай", "пр. Мира, 10")
store3 = Store("Супермаркет", "ул. Советская, 5")

# Добавление товаров в магазины
store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)
store2.add_item("oranges", 0.6)
store2.add_item("kiwi", 1.0)
store3.add_item("grapes", 1.2)
store3.add_item("pears", 0.8)

# Тестирование методов для одного из магазинов
print("Цены в магазине:", store1.name)
print("Цена яблок:", store1.get_price("apples"))  # 0.5
store1.update_price("apples", 0.55)
print("Обновленная цена яблок:", store1.get_price("apples"))  # 0.55
store1.remove_item("bananas")
print("Цена бананов после удаления:", store1.get_price("bananas"))  # None