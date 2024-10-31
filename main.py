# Клас Item (позиція меню)
class Item:
    def __init__(self, name, price):
        self.name = name  # Назва позиції
        self.price = price  # Ціна позиції

    def __str__(self):
        return f"{self.name}: {self.price} грн"


# Клас Order (замовлення)
class Order:
    def __init__(self, customer):
        self.customer = customer  # Клієнт, який зробив замовлення
        self.items = []  # Список замовлених позицій
        self.total_amount = 0  # Загальна сума замовлення
        self.is_paid = False  # Статус оплати

    def add_item(self, item):
        self.items.append(item)
        self.total_amount += item.price

    def remove_item(self, item):
        if item in self.items:
            self.items.remove(item)
            self.total_amount -= item.price

    def pay(self):
        if self.total_amount > 0:
            self.is_paid = True
            print(f"Замовлення сплачено. Загальна сума: {self.total_amount} грн")
        else:
            print("Замовлення не може бути сплачене, оскільки немає доданих позицій.")

    def __str__(self):
        items_str = "\n".join([str(item) for item in self.items])
        return f"Замовлення від {self.customer.name}:\n{items_str}\nЗагальна сума: {self.total_amount} грн\nСтатус оплати: {'Оплачено' if self.is_paid else 'Не оплачено'}"


# Клас Customer (клієнт)
class Customer:
    def __init__(self, name, contact):
        self.name = name  # Ім'я клієнта
        self.contact = contact  # Контактні дані клієнта
        self.orders = []  # Список замовлень клієнта

    def create_order(self):
        order = Order(self)
        self.orders.append(order)
        return order

    def __str__(self):
        return f"Клієнт: {self.name}, Контакт: {self.contact}"


# Приклад роботи
if __name__ == "__main__":
    # Створюємо позиції меню
    coffee = Item("Кава", 50)
    sandwich = Item("Сендвіч", 70)
    cake = Item("Торт", 45)

    # Створюємо клієнта
    customer = Customer("Іван", "+380987654321")

    # Клієнт створює замовлення
    order = customer.create_order()

    # Додаємо позиції до замовлення
    order.add_item(coffee)
    order.add_item(sandwich)
    order.add_item(cake)

    # Виводимо інформацію про замовлення
    print(order)

    # Оплачуємо замовлення
    order.pay()

    # Виводимо інформацію після оплати
    print(order)
