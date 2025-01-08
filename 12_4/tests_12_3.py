import logging as log
from runner import Runner, Tournament
import unittest

log.basicConfig(
    level=log.INFO,
    filemode='w',
    filename='runner_tests.log',
    encoding='utf8',
    format='%(asctime)s | %(levelname)s | %(message)s'
)

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        try:
            run = Runner('Daniil', -1)
            for _ in range(10):
                run.walk()
            self.assertEqual(run.distance, 50)
            log.info('"test_walk" выполнен успешно')
        except ValueError:
            log.warning('Неверная скорость для Runner', exc_info=True)

    def test_run(self):
        try:
            run = Runner(True)
            for _ in range(10):
                run.run()
            self.assertEqual(run.distance, 100)
            log.info('"test_run" выполнен успешно')
        except TypeError:
            log.warning('Неверный тип данных для объекта Runner', exc_info=True)

    def test_challenge(self):
        run = Runner('Daniil')
        run1 = Runner('Daniil')
        for _ in range(10):
            run.run()
            run1.walk()
        self.assertNotEqual(run.distance, run1.distance)


if __name__ == '__main__':
    unittest.main()