import random

def generate_to_file(filename="data.txt"):
    # Генерируем 20 случайных чисел
    operations = [random.randint(1, 100) for _ in range(20)]
    
    # Сохраняем их в файл через запятую
    with open(filename, "w", encoding="utf-8") as f:
        # Превращаем числа в строки и соединяем их запятой
        f.write(",".join(map(str, operations)))
    
    print(f"Данные успешно сгенерированы и сохранены в файл {filename}")
    print(f"Записано: {operations}")

if __name__ == "__main__":
    generate_to_file()