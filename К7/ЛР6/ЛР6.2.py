def find_max_even_subarray(arr, k):
    n = len(arr)
    if k > n or k <= 0:
        return []
    # 1. Считаем чётные в первом окне
    current_evens = 0
    for i in range(k):
        if arr[i] % 2 == 0:
            current_evens += 1  
    max_evens = current_evens
    start_index = 0
    # 2. Двигаем окно
    for i in range(k, n):
        # Убираем влияние левого элемента, который выходит из окна
        if arr[i - k] % 2 == 0:
            current_evens -= 1
        # Добавляем влияние нового правого элемента
        if arr[i] % 2 == 0:
            current_evens += 1
        # 3. Если в текущем окне чётных больше, запоминаем его
        if current_evens > max_evens:
            max_evens = current_evens
            start_index = i - k + 1
    return arr[start_index : start_index + k]
# Пример
numbers = [1, 2, 4, 3, 6, 8, 10, 1, 4]
k_size = 3
result = find_max_even_subarray(numbers, k_size)
print(f"Подмассив длины {k_size} с макс. кол-вом чётных: {result}")
# Для этого примера выведет [6, 8, 10], так как там 3 чётных числа.
