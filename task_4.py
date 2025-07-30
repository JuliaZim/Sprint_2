class EmployeeSalary:
    # Устанавливаем почасовую оплату в переменной класса
    hourly_payment = 400

    # Создаем конструктор класса
    def __init__(self, name, hours, rest_days, email):
        self.name = name
        self.hours = hours
        self.rest_days = rest_days
        self.email = email

    # Создаем метод класса для расчета часов
    @classmethod
    def get_hours(cls, name, rest_days, email):
        hours = (7 - rest_days) * 8
        return cls(name, hours, rest_days, email)

    # создаем метод класса для генерации email
    @classmethod
    def get_email(cls, name, hours, rest_days):
        email = f"{name}@email.com"
        return cls(name, hours, rest_days, email)

    # Создаем метод класса, которые меняет значение почасовой оплаты
    @classmethod
    def set_hourly_payment(cls, hourly_payments):
        cls.hourly_payment = hourly_payments

    # Создаем метод класса для расчета ЗП
    def salary(self):
        print(
            f"{self.name}, ваша заработная плата за {self.hours} часов составляет {self.hours * self.hourly_payment}. Расчетный лист выслали вам на почту {self.email}"
        )


emp_1 = EmployeeSalary("Маша", 4, 1, "m@test.ru")
emp_1.salary()
emp_2 = EmployeeSalary.get_hours("Катя", rest_days=1, email="k@test.ru")
emp_2.salary()
emp_3 = EmployeeSalary.get_email("Алена", 6, 1)
emp_3.salary()
