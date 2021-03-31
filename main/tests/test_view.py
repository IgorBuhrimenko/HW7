from django.test import TestCase

class TestClass(TestCase):

    @classmethod
    def setUpTestData(cls):
        # вызывается каждый раз перед запуском теста на уровне настройки
        # всего класса
        pass

    def setUp(self) -> None:
        # вызывается перед каждой тестовой функцией для настройки объектов,
        # которые могут изменяться во время тестов
        pass

    def tearDown(self) -> None:
        pass

    def test_false_is_false(self):
        self.assertFalse(False)