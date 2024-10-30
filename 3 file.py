import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

def calculate_age(birthdate: str) -> int:
    """Розрахунок повного віку на основі дати народження."""
    birth_date = datetime.strptime(birthdate, "%d-%m-%Y")
    today = datetime.today()
    return today.year - birth_date.year - ((today.month, today.day) < (birth_date.month, birth_date.day))

def categorize_age(age: int) -> str:
    """Категоризація віку для різних вікових груп."""
    if age < 18:
        return "younger_18"
    elif 18 <= age <= 45:
        return "18-45"
    elif 45 < age <= 70:
        return "45-70"
    else:
        return "older_70"

try:
    # Читаємо дані з CSV файлу
    try:
        data = pd.read_csv("people_data.csv")
        print("Ok")
    except FileNotFoundError:
        print("Помилка: Файл people_data.csv не знайдено.")
        exit()
    except Exception as e:
        print(f"Помилка відкриття файлу CSV: {e}")
        exit()

    # Додаємо стовпець з віком та категорією
    data['Вік'] = data['Дата народження'].apply(calculate_age)
    data['Категорія віку'] = data['Вік'].apply(categorize_age)

    # Рахуємо кількість співробітників чоловічої і жіночої статі
    gender_counts = data['Стать'].value_counts()
    print("Кількість співробітників за статтю:")
    print(gender_counts)

    # Побудова діаграми за статтю
    gender_counts.plot(kind='pie', autopct='%1.1f%%', startangle=140, colors=['lightblue', 'pink'], title="Кількість співробітників за статтю")
    plt.ylabel('')
    plt.show()

    # Рахуємо кількість співробітників у кожній віковій категорії
    age_category_counts = data['Категорія віку'].value_counts()
    print("Кількість співробітників за віковими категоріями:")
    print(age_category_counts)

    # Побудова діаграми за віковими категоріями
    age_category_counts.plot(kind='bar', color='skyblue', title="Кількість співробітників за віковими категоріями")
    plt.xlabel("Вікова категорія")
    plt.ylabel("Кількість співробітників")
    plt.show()

    # Рахуємо кількість співробітників за статтю в кожній віковій категорії
    gender_age_category_counts = data.groupby(['Категорія віку', 'Стать']).size().unstack()
    print("Кількість співробітників за статтю в кожній віковій категорії:")
    print(gender_age_category_counts)

    # Побудова діаграми за статтю в кожній віковій категорії
    gender_age_category_counts.plot(kind='bar', stacked=True, color=['lightblue', 'pink'], title="Кількість співробітників за статтю в кожній віковій категорії")
    plt.xlabel("Вікова категорія")
    plt.ylabel("Кількість співробітників")
    plt.show()

except Exception as e:
    print(f"Виникла помилка: {e}")