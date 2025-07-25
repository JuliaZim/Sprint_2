class PointsForPlace:
    # Задаем количество баллов = 0
    points = 0

    # Функция для подсчета очков по месту. Определяем статическим
    @staticmethod
    def get_points_for_place(place):
        # Обрабатываем ошибку, если баллов не положено
        if place > 100:
            print("Баллы начисляются только первым 100 участникам")
        # Обратываем ошибку, если место некорректно
        elif place < 1:
            print("Спортсмен не может занять нулевое или отрицательное место")
        # Начисляем баллы
        else:
            points = 101 - place
            return points


class PointsForMeters:
    # Задаем количество баллов = 0
    points = 0

    # Определяем статический метод
    @staticmethod
    def get_points_for_meters(meters):
        # Обрабатываем ошибку, если некорректные метры
        if meters < 0:
            print("Количество метров не может быть отрицательным")
        # Начисляем баллы
        else:
            points = 0.5 * meters
            return points


class TotalPoints(PointsForPlace, PointsForMeters):
    # Задаем количество баллов = 0
    points = 0

    # Определяем статический метод
    @staticmethod
    def get_total_points(place, meters):
        # Начисляем баллы, используя методы родительского класса
        total = PointsForPlace.get_points_for_place(
            place
        ) + PointsForMeters.get_points_for_meters(meters)
        return total


# создаем экземпляр класса PointsForPlace и печатаем результат метода
points_for_place = PointsForPlace()
print(points_for_place.get_points_for_place(10))

# создаем экземпляр класса PointsForMeters и печатаем результат метода
points_for_meters = PointsForMeters()
print(points_for_meters.get_points_for_meters(10))

# создаем экземпляр класса TotalPoints и печатаем результат методов класса и родительских
total_points = TotalPoints()
print(total_points.get_points_for_place(10))
print(total_points.get_points_for_meters(10))
print(total_points.get_total_points(100, 10))
