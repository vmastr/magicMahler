import unittest
from magicMahler.polytope import Polytope

class TestPolytope(unittest.TestCase):
    def test_some_method(self):
        p = Polytope()
        self.assertEqual(p.some_method(), "Hello from Polytope")


if __name__ == "__main__":
    unittest.main()