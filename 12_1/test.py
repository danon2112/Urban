from runner import Runner
import unittest

class RunnerTest(unittest.TestCase):
    def test_walk(self):
        run = Runner('Daniil')
        for _ in range(10):
            run.walk()
        self.assertEqual(run.distance, 50)

    def test_run(self):
        run = Runner('Daniil')
        for _ in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    def test_challenge(self):
        run = Runner('Daniil')
        run1 = Runner('Daniil')
        for _ in range(10):
            run.run()
            run1.walk()
        self.assertNotEqual(run.distance, run1.distance)

if __name__ == '__name__':
    unittest.main()