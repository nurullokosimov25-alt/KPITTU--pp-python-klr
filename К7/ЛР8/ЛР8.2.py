import random
# 1. ГЕНЕРАЦИЯ ДАННЫХ
# Создаем список из 20 случайных чисел (сумм операций) от 1 до 100
operations = [random.randint(1, 100) for _ in range(20)]

# 2. ПАРАМЕТРЫ ОБРАБОТКИ
# Установим порог суммы, выше которого пара считается "подозрительной"
threshold = 150 

def find_high_value_pairs(data, limit):
    """Находит пары операций, сумма которых строго больше порога"""
    pairs_found = []
    n = len(data)
    
    # Используем вложенный цикл для перебора всех уникальных комбинаций
    for i in range(n):
        for j in range(i + 1, n):
            current_sum = data[i] + data[j]
            if current_sum > limit:
                # Сохраняем индексы, значения и их сумму
                pairs_found.append({
                    "indices": (i, j),
                    "values": (data[i], data[j]),
                    "total": current_sum
                })
    return pairs_found

# 3. ВЫПОЛНЕНИЕ И ВЫВОД
results = find_high_value_pairs(operations, threshold)

print(f"Список всех операций: {operations}")
print(f"Установленный порог: {threshold}")
print(f"Найдено подходящих пар: {len(results)}\n")

if results:
    print("Детализация пар:")
    for item in results:
        v1, v2 = item["values"]
        print(f"Операция №{item['indices'][0]} ({v1}) + Операция №{item['indices'][1]} ({v2}) = {item['total']}")
else:
    print("Пар с суммой выше порога не обнаружено.")
