import unittest
import tests_12_3 as tests

ts = unittest.TestSuite()
ts.addTest(unittest.TestLoader().loadTestsFromTestCase(tests.RunnerTest))
ts.addTest(unittest.TestLoader().loadTestsFromTestCase(tests.TournamentTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(ts)