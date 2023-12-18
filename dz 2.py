class CatCalculator:
    def __init__(self, name):
        self.name = name

    def add(self, num1, num2):
        result = num1 + num2
        return f"{self.name} каже: М'яу! Результат додавання {num1} і {num2} дорівнює {result}"

    def subtract(self, num1, num2):
        result = num1 - num2
        return f"{self.name} каже: Мурр! Результат віднімання {num2} від {num1} дорівнює {result}"

    def multiply(self, num1, num2):
        result = num1 * num2
        return f"{self.name} каже: М'яу-мурр! Результат множення {num1} на {num2} дорівнює {result}"

    def divide(self, num1, num2):
        if num2 == 0:
            return f"{self.name} каже: Мррр... Ділення на нуль не можливе!"
        result = num1 / num2
        return f"{self.name} каже: Мяууу! Результат ділення {num1} на {num2} дорівнює {result}"


calculator = CatCalculator("Віскерс")


print(calculator.add(5, 3))
print(calculator.subtract(10, 4))
print(calculator.multiply(7, 2))
print(calculator.divide(8, 2))
print(calculator.divide(5, 0))
