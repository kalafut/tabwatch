import unittest
import tcat

class TestSequenceFunctions(unittest.TestCase):
    def test_config(self):
        config = tcat.loadconfig("test.yaml")
        self.assertEquals(config["colors"], { "green": "0ceb43", "red": "f5384b", "yellow": "dff51d" })

if __name__ == '__main__':
    unittest.main()
