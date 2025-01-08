
from runner import Runner, Tournament
import unittest


class RunnerTest(unittest.TestCase):
    is_frozen = False

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_walk(self):
        run = Runner('Daniil')
        for _ in range(10):
            run.walk()
        self.assertEqual(run.distance, 50)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_run(self):
        run = Runner('Daniil')
        for _ in range(10):
            run.run()
        self.assertEqual(run.distance, 100)

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_challenge(self):
        run = Runner('Daniil')
        run1 = Runner('Daniil')
        for _ in range(10):
            run.run()
            run1.walk()
        self.assertNotEqual(run.distance, run1.distance)
class TournamentTest(unittest.TestCase):
    is_frozen = True

    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results['usain_and_nick'])
        print(cls.all_results['andrey_and_nick'])
        print(cls.all_results['usain_andrey_and_nick'])


    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        TournamentTest.all_results['usain_and_nick'] = result
        self.assertTrue(result[list(result.keys())[-1]] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        TournamentTest.all_results['andrey_and_nick'] = result
        self.assertTrue(result[list(result.keys())[-1]] == "Ник")

    @unittest.skipIf(is_frozen, 'Тесты в этом кейсе заморожены.')
    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        TournamentTest.all_results['usain_andrey_and_nick'] = result
        self.assertTrue(result[list(result.keys())[-1]] == "Ник")

if __name__ == '__main__':
    unittest.main()