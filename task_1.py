class Case:
    def __init__(self, test_case_id, name, step_description, expected_result):
        self.test_case_id = test_case_id
        self.name = name
        self.step_description = step_description
        self.expected_result = expected_result

    def print_test_case_info(self):
        print(
            f"ID тест-кейса:  {self.test_case_id}"
            f"\nНазвание: {self.name}"
            f"\nОписание шага: {self.step_description}"
            f"\nОжидаемый результат: {self.expected_result}"
        )


# Создаем подкласс и наследуем его от родителя Case
class ExtendedCase(Case):
    # Создаем конструктор класса с атрибутами суперкласса и два новых
    def __init__(
        self,
        test_case_id,
        name,
        step_description,
        expected_result,
        precondition,
        environment,
    ):
        # Определяем атрибуты суперкласса
        super().__init__(test_case_id, name, step_description, expected_result)
        # Определяем новые атрибуты
        self.precondition = precondition
        self.environment = environment

    # Переопределяем метод print_test_case_info()
    def print_test_case_info(self):
        super().print_test_case_info()
        print(f"Предусловие: {self.precondition}" f"\nОкружение: {self.environment}")


# Создаем объект класса ExtendedCase:
case = ExtendedCase(
    "1",
    "Наличие кнопки Принять",
    "1. Открыть вкладку приёма документов 2. Проверить наличие кнопки ",
    "Кнопка доступна",
    "Открыть сервис",
    "Яндекс Браузер",
)
# Вызываем метод печати информации
case.print_test_case_info()
