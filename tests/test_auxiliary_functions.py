import unittest
import sys
import os
import numpy as np

# Add the parent directory (where magicMahler is) to sys.path
sys.path.append("/Users/vmastr/Library/Mobile Documents/com~apple~CloudDocs/Documents/GitHub/magicMahler/magicMahler")

from auxiliary_functions import aux1, aux2, safe_divide, double_integration, numerical_gradient, gradient_descent


class TestAuxiliaryFunctions(unittest.TestCase):
    
    def test_aux1(self):
        """Test aux1 function."""
        self.assertAlmostEqual(aux1(1), (np.exp(1) - 1) / 1, places=5)
        self.assertEqual(aux1(0), 1)  # Test at x=0
        self.assertAlmostEqual(aux1(800), (np.exp(700) - 1) / 700, places=5)  # Clipped

    def test_aux2(self):
        """Test the aux2 function for small values of x and y."""
        # Test aux2 with small differences, expecting the approximation behavior
        self.assertAlmostEqual(aux2(1e-8, 0), 0.5, places=5)  # Expect 0.5 based on the function's approximation
        self.assertAlmostEqual(aux2(1e-3, 0), (aux1(1e-3) - 1) / 1e-3, places=5)  # Slightly larger difference
        self.assertAlmostEqual(aux2(1, 0), (aux1(1) - aux1(0)) / 1, places=5)  # Normal case with no approximation

    def test_safe_divide(self):
        """Test safe_divide function."""
        self.assertAlmostEqual(safe_divide(1, 1), 1, places=5)
        self.assertAlmostEqual(safe_divide(1, 0), 1e10, places=5)  # Division by zero with epsilon
        self.assertAlmostEqual(safe_divide(0, 1), 0, places=5)

    def test_double_integration(self):
        """Test double_integration function."""
        # Define simple functions to test integration
        def f1(x, y):
            return x + y

        def f2(x, y):
            return x**2 + y**2

        result1, error1 = double_integration(f1, 0, 1, 0, 1)
        result2, error2 = double_integration(f2, 0, 1, 0, 1)

        self.assertAlmostEqual(result1, 1, places=5)  # Integration of x + y over [0,1] x [0,1]
        self.assertAlmostEqual(result2, 2 / 3, places=5)  # Integration of x^2 + y^2 over [0,1] x [0,1]

    def test_numerical_gradient(self):
        """Test numerical_gradient function."""
        # Define simple function for testing
        def f(x, y):
            return (x - 1)**2 + (y - 2)**2

        grad = numerical_gradient(f, 1, 2)
        self.assertTrue(np.allclose(grad, [0, 0], atol=1e-5))  # Minimum should have zero gradient

    def test_gradient_descent(self):
        """Test gradient_descent function."""
        # Define a quadratic function for gradient descent
        def f(x, y):
            return (x - 1)**2 + (y - 2)**2

        initial_point = (0, 0)
        result_x, result_y, min_value = gradient_descent(f, initial_point,learning_rate=.5)

        self.assertAlmostEqual(result_x, 1, places=5)
        self.assertAlmostEqual(result_y, 2, places=5)
        self.assertAlmostEqual(min_value, 0, places=5)  # Minimum value should be zero

if __name__ == "__main__":
    unittest.main()
