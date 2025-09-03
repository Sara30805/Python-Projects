import unittest
from probability_calculator import Hat, experiment

class TestProbabilityCalculator(unittest.TestCase):

    def test_hat_init(self):
        hat = Hat(red=3, blue=2)
        self.assertEqual(len(hat.contents), 5)
        self.assertEqual(hat.contents.count("red"), 3)
        self.assertEqual(hat.contents.count("blue"), 2)

    def test_draw_less_than_total(self):
        hat = Hat(red=3, blue=2)
        drawn = hat.draw(2)
        self.assertEqual(len(drawn), 2)
        self.assertEqual(len(hat.contents), 3)

    def test_draw_more_than_total(self):
        hat = Hat(red=2, blue=1)
        drawn = hat.draw(10)
        self.assertEqual(len(drawn), 3)
        self.assertEqual(len(hat.contents), 0)

    def test_experiment_probability(self):
        hat = Hat(blue=3, red=2, green=6)
        prob = experiment(
            hat=hat,
            expected_balls={"blue": 2, "green": 1},
            num_balls_drawn=4,
            num_experiments=2000
        )
        # The probability must be between 0 and 1
        self.assertTrue(0 <= prob <= 1)
        # Roughly check if the probability is around an expected value
        self.assertAlmostEqual(prob, 0.27, delta=0.1)

if __name__ == "__main__":
    unittest.main()
