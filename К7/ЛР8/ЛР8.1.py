def find_pairs_above_threshold(operations, threshold):
    # 1. Сортируем копию данных
    sorted_ops = sorted(operations)
    n = len(sorted_ops)
    pairs = []
    
    left = 0
    right = n - 1
    
    # 2. Метод двух указателей
    while left < right:
        current_sum = sorted_ops[left] + sorted_ops[right]
        
        if current_sum > threshold:
            # Если сумма крайних больше порога, то правый элемент
            # образует валидную пару со всеми элементами между left и right.
            for i in range(left, right):
                pairs.append((sorted_ops[i], sorted_ops[right]))
            
            # Сдвигаем правый указатель, чтобы искать новые пары
            right -= 1
        else:
            # Сумма слишком мала, нужно увеличить левый элемент
            left += 1
            
    return pairs

# --- Пример использования ---
if __name__ == "__main__":
    # Список стоимостей или весов операций
    ops_data = [10, 5, 20, 15, 30]
    limit = 35
    
    result = find_pairs_above_threshold(ops_data, limit)
    
    print(f"Операции: {ops_data}")
    print(f"Порог: {limit}")
    print(f"Найденные пары ({len(result)} шт.):")
    for p in result:
        print(f"  {p[0]} + {p[1]} = {sum(p)}")

