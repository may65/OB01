#may, [20.09.2024 13:36]
#Менеджер задач

#Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.

#*Дополнительное задание:

#Ты разрабатываешь программное обеспечение для сети магазинов. Каждый магазин в этой сети имеет свои особенности, но также существуют общие характеристики, такие как адрес, название и ассортимент товаров. Ваша задача — создать класс Store, который можно будет использовать для создания различных магазинов.

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

#В поле для ответа загрузи ссылку на GitHub-репозиторий, содержащий код проекта с реализацией задания.

#Нейрокот, [20.09.2024 13:37]
#Для выполнения задания на Python, вы можете создать два класса: `Task` и `Store`. Ниже приведен пример того, как вы можете реализовать эти классы и методы в вашем проекте.

### Класс Task

#```python
class Task:
    def __init__(self, description, due_date):
        self.description = description
        self.due_date = due_date
        self.is_completed = False

    def mark_completed(self):
        self.is_completed = True

    def __str__(self):
        status = "Выполнено" if self.is_completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.due_date}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def get_incomplete_tasks(self):
        return [task for task in self.tasks if not task.is_completed]

    def show_tasks(self):
        for task in self.get_incomplete_tasks():
            print(task)

# Пример использования
task1 = Task("Купить продукты", "2023-11-01")
task2 = Task("Сделать домашнее задание", "2023-11-02")
manager = TaskManager()
manager.add_task(task1)
manager.add_task(task2)

task1.mark_completed()

manager.show_tasks()
#```

### Класс Store

#```python
class Store:
    def __init__(self, name, address):
        self.name = name
        self.address = address
        self.items = {}

    def add_item(self, item_name, price):
        self.items[item_name] = price

    def remove_item(self, item_name):
        if item_name in self.items:
            del self.items[item_name]

    def get_price(self, item_name):
        return self.items.get(item_name, None)

    def update_price(self, item_name, new_price):
        if item_name in self.items:
            self.items[item_name] = new_price

# Пример создания магазинов
store1 = Store("Магазин 1", "Адрес 1")
store2 = Store("Магазин 2", "Адрес 2")
store3 = Store("Магазин 3", "Адрес 3")

store1.add_item("apples", 0.5)
store1.add_item("bananas", 0.75)
store2.add_item("oranges", 0.6)
store3.add_item("grapes", 1.2)

# Тестирование методов
store1.update_price("apples", 0.55)
print(store1.get_price("apples"))  # 0.55
store1.remove_item("bananas")
print(store1.get_price("bananas"))  # None
#```

### GitHub Репозиторий

#Создайте репозиторий на GitHub и загрузите ваш проект. После этого, вы можете предоставить ссылку на ваш репозиторий в ответе. Это позволит другим просмотреть ваш код и протестировать его.

#Если у вас возникнут вопросы по созданию репозитория или загрузке кода на GitHub, пожалуйста, дайте знать, и я помогу вам с этим процессом.