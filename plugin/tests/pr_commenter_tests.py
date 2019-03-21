import unittest
import pr_commenter as sut


@unittest.skip("Don't forget to test!")
class PrCommenterTests(unittest.TestCase):

    def test_example_fail(self):
        result = sut.pr_commenter_example()
        self.assertEqual("Happy Hacking", result)
