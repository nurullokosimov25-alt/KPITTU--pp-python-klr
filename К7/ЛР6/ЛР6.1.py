def is_sorted_recursive(lst):
    # Базовый случай: пустой список или список из одного элемента отсортирован
    if len(lst) <= 1:
        return True
    # Проверка текущей пары (первый и второй элементы)
    if lst[0] > lst[1]:
        return False
    # Рекурсивный вызов для остатка списка
    return is_sorted_recursive(lst[1:])
# Примеры использования:
list_a = [1, 2, 5, 8, 12]
list_b = [1, 2, 10, 5, 12]
print(f"Список {list_a} отсортирован? {is_sorted_recursive(list_a)}")
print(f"Список {list_b} отсортирован? {is_sorted_recursive(list_b)}")
