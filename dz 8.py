import time

def measure_time(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    execution_time = end_time - start_time
    return execution_time

# Приклад функції, яку ми будемо вимірювати
def sample_function(n):
    for i in range(n):
        print(i)

# Тести для перевірки працездатності функції виміру часу
def test_measure_time():
    n = 1000000  # Задаємо довжину циклу для тестування швидкості виконання
    measured_time = measure_time(sample_function, n)
    print(f"Час виконання функції: {measured_time:.5f} секунд")

# Виклик функції для перевірки
test_measure_time()