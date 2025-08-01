class Results:

    sport = None
    victory_points = 1

    # Инициализация параметров через конструктор
    def __init__(self, victories, draws, losses):
        self.victories = victories
        self.draws = draws
        self.losses = losses

    def number_of_wins(self):
        return f"{self.sport} побед: {self.victories}"

    # Метод вывода ничьих
    def number_of_draws(self):
        return f"{self.sport} ничьих: {self.draws}"

    # Метод вывода проигрышей
    def number_of_losses(self):
        return f"{self.sport} поражений: {self.losses}"

    # Метод вывода общего кол-ва очков
    def total_points(self):
        return (
            f"Общее количество очков: {self.victory_points*self.victories + self.draws}"
        )


# класс Football, который наследуется от класса Results
class Footbal(Results):
    # Задаем переменные класса
    sport = "Футбольных"
    victory_points = 3

    # Инициализируем конструктор класса
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)


# Класс Хоккей
class Hockey(Results):
    # Задаем Переменные класса
    sport = "Хоккейных"
    victory_points = 2

    # Инициализируем конструктор класса
    def __init__(self, victories, draws, losses):
        super().__init__(victories, draws, losses)


# Создаем объекты классов
football_team = Footbal(2, 2, 2)
hockey_team = Hockey(2, 2, 2)

# Создаем цикл для вызова всех методов для созданных объектов
for team in (football_team, hockey_team):
    print(team.number_of_draws())
    print(team.number_of_wins())
    print(team.number_of_losses())
    print(team.total_points())
