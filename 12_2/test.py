from runner import Runner, Tournament
import unittest

class TournamentTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.all_results = {}

    def setUp(self):
        self.usain = Runner('Усэйн', 10)
        self.andrey = Runner('Андрей', 9)
        self.nick = Runner('Ник', 3)

    @classmethod
    def tearDownClass(cls):
        print(cls.all_results['usain_and_nick'])
        print(cls.all_results['andrey_and_nick'])
        print(cls.all_results['usain_andrey_and_nick'])

    def test_usain_and_nick(self):
        tournament = Tournament(90, self.usain, self.nick)
        result = tournament.start()
        TournamentTest.all_results['usain_and_nick'] = result
        self.assertTrue(result[list(result.keys())[-1]] == "Ник")

    def test_andrey_and_nick(self):
        tournament = Tournament(90, self.andrey, self.nick)
        result = tournament.start()
        TournamentTest.all_results['andrey_and_nick'] = result
        self.assertTrue(result[list(result.keys())[-1]] == "Ник")

    def test_usain_andrey_and_nick(self):
        tournament = Tournament(90, self.usain, self.andrey, self.nick)
        result = tournament.start()
        TournamentTest.all_results['usain_andrey_and_nick'] = result
        self.assertTrue(result[list(result.keys())[-1]] == "Ник")

if __name__ == '__main__':
    unittest.main()