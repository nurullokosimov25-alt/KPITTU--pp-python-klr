def find_high_value_pairs(data, limit):
    pairs_found = []
    n = len(data)
    for i in range(n):
        for j in range(i + 1, n):
            current_sum = data[i] + data[j]
            if current_sum > limit:
                pairs_found.append({
                    "indices": (i, j),
                    "values": (data[i], data[j]),
                    "total": current_sum
                })
    return pairs_found

def main():
    filename = "data.txt"
    threshold = 150
    
    try:
        # Читаем данные из файла
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()
            # Превращаем строку обратно в список чисел
            operations = [int(x) for x in content.split(",") if x]
            
        print(f"Прочитанные данные: {operations}")
        
        # Обработка
        results = find_high_value_pairs(operations, threshold)
        
        print(f"Порог: {threshold}")
        print(f"Найдено пар: {len(results)}\n")
        
        if results:
            for item in results:
                v1, v2 = item["values"]
                print(f"Пара: {v1} + {v2} = {item['total']}")
        else:
            print("Ничего не найдено.")
            
    except FileNotFoundError:
        print(f"Ошибка: Файл {filename} не найден! Сначала запустите generate_data.py")

if __name__ == "__main__":
    main()