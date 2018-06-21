"""
Test suite for the application of Week 2 of Algorithmic Thinking.
"""
import unittest
import application


class TestApplication(unittest.TestCase):
    """
    Unit tests for application class.
    """

    def setup(self):
        """
        Run before each test.
        Each test method must begin with "test_".
        """
        pass

    def test_er_algorithm(self):
        self.assertEqual(application.er_algorithm(3, 1),
                         {0: set([1, 2]), 1: set([0, 2]), 2: set([0, 1])})

        self.assertEqual(application.er_algorithm(3, 0),
                         {0: set([]), 1: set([]), 2: set([])})


suite = unittest.TestLoader().loadTestsFromTestCase(TestApplication)
unittest.TextTestRunner(verbosity=2).run(suite)
# Run in terminal with: python ./application.spec.py
