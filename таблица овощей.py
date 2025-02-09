import pandas as pd
import random
from datetime import datetime, timedelta

# Данные для заполнения таблицы
items = ["Апельсины", "Помидоры", "Яблоки", "Морковь", "Огурцы", "Редиска", "Перец чили", "лук репчатый", "Чеснок", "Картофель", "Дыня", "Мандарины", "манго"]
suppliers = ["Китай", "Узбекистан", "НСО", "Калуга", "Египет", "Турция", "Азербайджан", "Беларусь", "Иран", "Армения"]
dates = [(datetime.today() - timedelta(days=random.randint(1, 30))).strftime("%Y-%m-%d") for _ in range(15)]
prices = [random.uniform(20, 150) for _ in range(100)]
quantities = [random.randint(10, 500) for _ in range(100)]

# Генерация данных
data = {
    "Наименование": [random.choice(items) for _ in range(100)],
    "Поставщик": [random.choice(suppliers) for _ in range(100)],
    "Дата": [random.choice(dates) for _ in range(100)],
    "Цена": [round(price, 2) for price in prices],
    "Количество": quantities
}

# Создание DataFrame и сохранение в Excel
df = pd.DataFrame(data)
file_path = "Овощной_отдел.xlsx"
df.to_excel(file_path, index=False)

print(f"Файл создан: {file_path}")

