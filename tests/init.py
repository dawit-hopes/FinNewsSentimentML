import unittest

class InitTestCase(unittest.TestCase):
    def test_initialization(self):
        obj = InitTestCase()
        self.assertIsInstance(obj, InitTestCase)

if __name__ == '__main__':
    unittest.main()