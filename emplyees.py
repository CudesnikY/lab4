import csv
import random
from faker import Faker

# Ініціалізуємо Faker з українською локалізацією
fake = Faker(locale='uk_UA')

# Словник для по-батькові
patronymics_male = [
    "Іванович", "Петрович", "Сергійович", "Олександрович", "Андрійович",
    "Миколайович", "Васильович", "Степанович", "Юрійович", "Борисович",
    "Олегович", "Григорович", "Дмитрович", "Максимович", "Тарасович",
    "Романович", "Володимирович", "Євгенович", "Михайлович", "Павлович"
]

patronymics_female = [
    "Іванівна", "Петрівна", "Сергіївна", "Олександрівна", "Андріївна",
    "Миколаївна", "Василівна", "Степанівна", "Юріївна", "Борисівна",
    "Олегівна", "Григорівна", "Дмитрівна", "Максимівна", "Тарасівна",
    "Романівна", "Володимирівна", "Євгенівна", "Михайлівна", "Павлівна"
]

# Константи
total_records = 2000
male_ratio = 0.6
female_ratio = 0.4

# Розрахунок кількості чоловіків і жінок
num_males = int(total_records * male_ratio)
num_females = total_records - num_males

# Функція для генерації запису
def generate_record(gender: str):
    if gender == "Чоловіча":
        first_name = fake.first_name_male()
        patronymic = random.choice(patronymics_male)
    else:
        first_name = fake.first_name_female()
        patronymic = random.choice(patronymics_female)
    
    return {
        "Прізвище": fake.last_name(),
        "Ім’я": first_name,
        "По батькові": patronymic,
        "Стать": gender,
        "Дата народження": fake.date_of_birth(minimum_age=15, maximum_age=85).strftime("%d-%m-%Y"),
        "Посада": fake.job(),
        "Місто проживання": fake.city(),
        "Адреса проживання": fake.address().replace("\n", ", "),
        "Телефон": fake.phone_number(),
        "Email": fake.email()
    }

# Генеруємо записи
records = []
for _ in range(num_males):
    records.append(generate_record("Чоловіча"))
for _ in range(num_females):
    records.append(generate_record("Жіноча"))

# Перемішуємо записи, щоб вони були в довільному порядку
random.shuffle(records)

# Запис у CSV файл
csv_file = "people_data.csv"
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=records[0].keys())
    writer.writeheader()
    writer.writerows(records)

print(f"Згенеровано та збережено {total_records} записів у файл {csv_file}.")
