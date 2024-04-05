class Bank:
    def __init__(self, name, balance):
        self._name = name
        self._balance = balance

    def moneyX(self):
        amount = float(input("Введите сумму для добавления на счет: "))
        self._balance += amount
        print(f"На вашем счету теперь: {self._balance}")

    def kill(self):
        self._balance = 0
        print("Ваш баланс обнулен.")

    def _jackpot(self):
        self._balance *= 10
        print("Джекпот! Ваш баланс увеличен в 10 раз.")

    def _merge_balance(self, another_bank):
        self._balance += another_bank._balance
        another_bank._balance = 0
        print(f"Баланс объединен. Ваш новый баланс: {self._balance}")

# Создаем объекты класса Bank
bank1 = Bank("Azika", 100)
bank2 = Bank("Aisulu", 100)


bank1.moneyX()


bank1._merge_balance(bank2)


print(f"Баланс Azika: {bank1._balance}")
print(f"Баланс Aisulu: {bank2._balance}")

# kalkulator

class Calculator:
    def __init__(self, num):
        self.num = num

    def __add__(self, other):
        return Calculator(self.num + other.num)

    def __sub__(self, other):
        return Calculator(self.num - other.num)

    def __mul__(self, other):
        return Calculator(self.num * other.num)

    def __truediv__(self, other):
        if other.num != 0:
            return Calculator(self.num / other.num)
        else:
            return "Деление на ноль невозможно."

    def __repr__(self):
        return str(self.num)



calc1 = Calculator(12)
calc2 = Calculator(15)


print(f"Сложение: {calc1 + calc2}")
print(f"Вычитание: {calc1 - calc2}")
print(f"Умножение: {calc1 * calc2}")
print(f"Деление: {calc1 / calc2}")





