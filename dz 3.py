class Snowball:
    temperature = '-7'

    def __init__(self, a):
        if a == 5:
            self.temperature = '0'

    def __str__(self):
        return self.temperature

    def print_temperature(self):
        print(self.temperature)

snowball = Snowball(3)
snowball.print_temperature()


class Human:
    age = '13'

    def __init__(self, a):
        if a == 5:
            self.age = '0'

    def __str__(self):
        return self.age

    def print_age(self):
        print(self.age)

person = Human(3)
person.print_age()
