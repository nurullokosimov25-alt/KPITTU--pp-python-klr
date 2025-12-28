#(sliding.py)
def check_stability(data, window_size, threshold):
    """
    Проверяет, являются ли значения в окне 'стабильными' 
    (размах значений <= threshold).
    """
    if not isinstance(data, list) or not all(isinstance(x, (int, float)) for x in data):
        raise ValueError("Данные должны быть списком чисел")
    if window_size <= 0 or window_size > len(data):
        raise ValueError("Некорректный размер окна")
    results = [] 
    # Алгоритм скользящего окна
    for i in range(len(data) - window_size + 1):
        window = data[i : i + window_size]
        is_stable = (max(window) - min(window)) <= threshold
        results.append(is_stable)
    return results
Этап 2.
#(test_sliding.py)
import unittest
from sliding import check_stability
class TestSlidingWindow(unittest.TestCase):
    # Тест 1: Обычный случай
    def test_stability_logic(self):
        data = [10, 11, 10, 20, 21]
        # Окно 3, порог 2. [10,11,10] - True, [11,10,20] - False, [10,20,21] - False
        self.assertEqual(check_stability(data, 3, 2), [True, False, False])

    # Тест 2: Все значения одинаковые (краевой случай)
    def test_constant_values(self):
        self.assertEqual(check_stability([5, 5, 5], 2, 0), [True, True])
    # Тест 3: Окно размером со весь массив
    def test_full_window(self):
        self.assertEqual(check_stability([1, 5, 10], 3, 10), [True])
    # Тест на ошибку (ValueError)
    def test_invalid_input(self):
        with self.assertRaises(ValueError):
            check_stability([1, 2], 5, 1) # Окно больше массива
if __name__ == '__main__':
    unittest.main()
Этап 3.
#(README.md)
# Stability Check (Sliding Window)
## Алгоритм
Программа проходит по массиву данных "окном" фиксированной длины. 
Для каждого положения окна вычисляется разница между максимальным и минимальным элементами:
`Stability = (max(window) - min(window)) <= threshold`
## Как запускать тесты
Для запуска unit-тестов выполните команду в терминале:
```bash
python3 -m unittest test_sliding.py
