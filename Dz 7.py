class StudentSimulator:
    def __init__(self, name, days):
        self.name = name
        self.days = days
        self.current_day = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.current_day <= self.days:
            result = f"День {self.current_day}: {self.name} вчиться, відпочиває, зустрічається з друзями і т.д."
            self.current_day += 1
            return result
        else:
            raise StopIteration


student = StudentSimulator("Студент 1", 5)


for day in student:
    print(day)

import ast

def calculate_secure(func):
    def wrapper(expression):
        try:
            ast.literal_eval(expression)
            return func(expression)
        except (SyntaxError, ValueError) as e:
            return f"Помилка: {e}"
    return wrapper

@calculate_secure
def calculate(expression):
    return eval(expression)


result = calculate("2 + 2")
print(result)  # 4

result = calculate("2 * 'hello'")
print(result)
