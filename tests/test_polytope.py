import unittest
import sys
import os
import math

# Add the parent directory (where magicMahler is) to sys.path
sys.path.append("/Users/vmastr/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/magicMahler/magicMahler")

# Now import the Polytope class
from polytope import Polytope

# Define some polytopes for testing
triangle = Polytope([(1, 1), (-1, 0), (0, -1)])
square = Polytope([(1, 1), (-1, 1), (-1, -1), (1, -1)])
diamond = Polytope([(0, 1), (-1, 0), (0, -1), (1, 0)])
pentagon = Polytope([(1, -1), (1, 1), (0, 3/2), (-1, 1), (-1, -1)])
simplex = Polytope([(0, 0), (1, 0), (0, 1)])
canonical_pentagon = Polytope([
    (1, 0),  # First vertex
    (math.cos(2 * math.pi / 5), math.sin(2 * math.pi / 5)),  # Second vertex
    (math.cos(4 * math.pi / 5), math.sin(4 * math.pi / 5)),  # Third vertex
    (math.cos(6 * math.pi / 5), math.sin(6 * math.pi / 5)),  # Fourth vertex
    (math.cos(8 * math.pi / 5), math.sin(8 * math.pi / 5))   # Fifth vertex
])


class TestPolytope(unittest.TestCase):
    
    def test_volume(self): 
        self.assertEqual(triangle.volume(), 1.5)
        self.assertEqual(square.volume(), 4)
        self.assertEqual(diamond.volume(), 2)
        self.assertEqual(simplex.volume(), 0.5)

    def test_barycenter(self): 
        self.assertEqual(triangle.barycenter(), (0, 0))
        self.assertEqual(simplex.barycenter(), (1/3, 1/3))
        self.assertEqual(canonical_pentagon.barycenter(), (0, 0)) 

    def test_polar(self): 
        polar = square.polar()
        self.assertIsInstance(polar, Polytope)  # Ensure the result is a Polytope instance
        self.assertEqual(polar.vertices, diamond.vertices)  # Compare vertices for the square's polar

    def test_mahler_volume(self):
        self.assertAlmostEqual(square.M(), 16.0)
        self.assertAlmostEqual(triangle.M(), 13.5)

    def test_Lp_mahler_volumes(self):
        self.assertAlmostEqual(square.M(1), math.pi**4, places=5)
        self.assertAlmostEqual(square.M(5), 35.22180, places=5)
        self.assertAlmostEqual(triangle.M(1), 84.19844, places=5)
        self.assertAlmostEqual(triangle.M(5), 30.113955, places=5)

    def test_covariance_matrix(self):
        expected_cov_matrix_triangle = [[1/6, 1/12],
                                        [1/12, 1/6]]
        self.assertTrue((triangle.Cov() == expected_cov_matrix_triangle).all())

    def test_isotropic_constant(self):
        self.assertAlmostEqual(triangle.isotropic(), 1/(108 ** (1/4)), places=5)
        self.assertAlmostEqual(square.isotropic(), 1 / (144 ** (1/4)), places=5)

    def test_translate(self):
        translated_simplex = simplex.translate(1/3, 1/3)
        expected_vertices = [(-1/3, -1/3), (1 - 1/3, -1/3), (-1/3, 1 - 1/3)]
        self.assertEqual(translated_simplex.vertices, expected_vertices)

    def test_santalo_point(self):
        self.assertAlmostEqual(canonical_pentagon.SantaloPoint(), (0, 0))
        self.assertAlmostEqual(canonical_pentagon.SantaloPoint(1), (0, 0))
        self.assertAlmostEqual(canonical_pentagon.SantaloPoint(2), (0, 0))
        self.assertAlmostEqual(simplex.SantaloPoint(), (1/3, 1/3))
        self.assertAlmostEqual(simplex.SantaloPoint(1), (1/3, 1/3))
 


if __name__ == "__main__":
    unittest.main()
