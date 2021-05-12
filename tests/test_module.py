import unittest
import pkg.module as m

class ModuleTest(unittest.TestCase):

    def test_add(self):
        self.assertEqual(2, m.add(1, 1))