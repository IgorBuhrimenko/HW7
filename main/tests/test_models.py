from django.test import TestCase


class StudentModelsTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        # вызывается каждый раз перед запуском теста на уровне настройки
        # всего класса
          print('SetUpTestData')

    def setUp(self) -> None:
        # вызывается перед каждой тестовой функцией для настройки объектов,
        # которые могут изменяться во время тестов
        print('SetUp')

    def tearDown(self) -> None:
        print('tearDown')

    def test_false_is_false(self):
        print('test_false_is_false')
        self.assertFalse(False)

    def test_true_is_false(self):
        print('test_true_is_false')
        self.assertTrue(True)
