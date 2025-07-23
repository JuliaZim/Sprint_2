class Movies:
    # Инициализируем список
    def __init__(self):
        self.movies = []

    # добавляем фильм в конец списка
    def add_movie(self, movie):
        self.movies.append(movie)


# Создаем дочерний класс и наследуем от Movies
class Comedy(Movies):
    # Инициализируем пустой список из конструктора суперкласса
    def __init__(self):
        super().__init__()

    # Переопределяем метод суперкласса, добавляем вывод на экран
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Комедии: {self.movies}"


# Создаем дочерний класс и наследуем от Movies
class Drama(Movies):
    # Инициализируем пустой список из конструктора суперкласса
    def __init__(self):
        super().__init__()

    # Переопределяем метод суперкласса, добавляем вывод на экран
    def add_movie(self, movie):
        super().add_movie(movie)
        return f"Драмы: {self.movies}"


# создаем объекты дочерних классов
comedy = Comedy()
drama = Drama()

# Вызываем методы дочерних классов
print(comedy.add_movie("Большой куш"))
print(drama.add_movie("Оружейный барон"))
