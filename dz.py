#Менеджер задач.
#Задача: Создай класс Task, который позволяет управлять задачами (делами). У задачи должны быть атрибуты: описание задачи, срок выполнения и статус (выполнено/не выполнено). Реализуй функцию для добавления задач, отметки выполненных задач и вывода списка текущих (не выполненных) задач.
#Для реализации менеджера задач мы создадим класс `Task`, который будет представлять отдельную задачу, и класс `TaskManager`, который будет управлять списком задач. Давайте приступим:
class Task:
    def __init__(self, description, deadline):
        self.description = description
        self.deadline = deadline
        self.is_completed = False

    def mark_completed(self):
        """Отмечает задачу как выполненную."""
        self.is_completed = True

    def __str__(self):
        """Возвращает строковое представление задачи."""
        status = "Выполнено" if self.is_completed else "Не выполнено"
        return f"Задача: {self.description}, Срок: {self.deadline}, Статус: {status}"

class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        """Добавляет новую задачу в список задач."""
        self.tasks.append(task)

    def mark_task_completed(self, task_description):
        """Отмечает задачу как выполненную по её описанию."""
        for task in self.tasks:
            if task.description == task_description:
                task.mark_completed()
                return True
        return False

    def get_pending_tasks(self):
        """Возвращает список невыполненных задач."""
        return [task for task in self.tasks if not task.is_completed]

    def __str__(self):
        """Возвращает строковое представление всех задач."""
        return "\n".join(str(task) for task in self.tasks)

# Пример использования

# Создаем менеджер задач
task_manager = TaskManager()

# Добавляем задачи
task_manager.add_task(Task("Купить продукты", "2023-10-15"))
task_manager.add_task(Task("Сдать отчет", "2023-10-17"))
task_manager.add_task(Task("Позвонить в банк", "2023-10-16"))

# Отмечаем задачу как выполненную
task_manager.mark_task_completed("Купить продукты")

# Выводим все задачи
print("Все задачи:")
print(task_manager)

# Выводим невыполненные задачи
print("\nНевыполненные задачи:")
pending_tasks = task_manager.get_pending_tasks()
for task in pending_tasks:
    print(task)