import unittest
import runner

class RunnerTest(unittest.TestCase):
    
    def test_walk(self):
        human = runner.Runner('Viktor')
        for _ in range(10):
            human.walk()
        self.assertEqual(human.distance, 50)

    def test_run(self):
        human = runner.Runner('Viktor')
        for _ in range(10):
            human.run()
        self.assertEqual(human.distance, 100)

    def test_challenge(self):
        human_1 = runner.Runner('Viktor')
        human_2 = runner.Runner('Richard')
        for _ in range(10):
            human_1.walk()
        for _ in range(10):
            human_2.run()
        self.assertNotEqual(human_1.distance, human_2.distance)

    # failed
    def test_walk_failed(self):
        human = runner.Runner('Viktor')
        for _ in range(10):
            human.walk()
        self.assertEqual(human.distance, 51)
    
    def test_run_failed(self):
        human = runner.Runner('Viktor')
        for _ in range(10):
            human.run()
        self.assertEqual(human.distance, 101)
     



if __name__ == '__main__':
    unittest.main()
