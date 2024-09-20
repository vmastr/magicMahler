import unittest
from magicMahler.polytope import Polytope


triangle = Polytope([(0, 0), (1, 0), (0, 1)])
square = Polytope([(1, 1), (-1, 1), (-1, -1), (1, -1)])
diamond = Polyope([(1, 0), (0, 1), (-1, 0), (0, -1)])


class TestPolytope(unittest.TestCase):
    def test_volume(self): 
        expected_volume = 0.5
        self.assertEqual(triangle.volume(), expected_volume)
    
    def test_polar(self): 
        polar = square.polar()
        self.assertIsInstance(polar, Polytope) # Ensure that the result is a Polytope instance
        self.assertEqual(polar, diamond)

if __name__ == "__main__":
    unittest.main()