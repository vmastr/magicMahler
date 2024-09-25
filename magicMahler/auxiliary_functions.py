import numpy as np
from tqdm import tqdm
from scipy import integrate

def aux1(x):
    """
    Parameters: x.
    Returns: (e^x - 1)/x.
    """
    x = np.clip(x, -700, 700)  # Restrict x within [-700, 700] to prevent overflow
    return (np.exp(x) - 1) / x if x != 0 else 1

def aux2(x, y):
    """
    Parameters: x, y.
    Returns: ((e^x-1)/x - (e^y-1)/y) / (x-y).
    """
    if np.isclose(x, y):
        if np.isclose(x, 0):
            return 0.5
        x_clipped = np.clip(x, -700, 700)
        return (x_clipped * np.exp(x_clipped) - np.exp(x_clipped) + 1) / (x_clipped**2)
    return (aux1(x) - aux1(y)) / (x - y)

def safe_divide(a, b, epsilon=1e-10):
    """
    Safely divide two numbers, returning a / (b + epsilon) to avoid division by zero.
    """
    return a / (b + epsilon)

def double_integration(f, a, b, c, d):
    """
    Perform double integration of a function f over the region [a, b] x [c, d].
    
    Parameters:
    - f: Function to integrate, must accept two variables (x, y).
    - a, b: Integration limits for the first variable (x).
    - c, d: Integration limits for the second variable (y), can be numbers or functions of x.

    Returns:
    - result: The computed integral value.
    - error: An estimate of the absolute error in the result.
    """
    lower_y = c if callable(c) else lambda x: c
    upper_y = d if callable(d) else lambda x: d
    result, error = integrate.dblquad(f, a, b, lower_y, upper_y, epsabs=1.49e-8, epsrel=1.49e-8)
    return result, error

def numerical_gradient(f, x, y, h=1e-5):
    """
    Compute the numerical gradient of a 2D function using central difference approximation.
    """
    grad_x = (f(x + h, y) - f(x - h, y)) / (2 * h)
    grad_y = (f(x, y + h) - f(x, y - h)) / (2 * h)
    return np.array([grad_x, grad_y])

def gradient_descent(f, initial_point, learning_rate=1e-4, max_iterations=10000, tolerance=1e-3, threshold=1e-6):
    """
    Perform gradient descent to find the minimum of function f.

    Parameters:
    - f: The function to minimize.
    - initial_point: The starting point for the descent (x0, y0).
    - learning_rate: The step size for gradient updates.
    - max_iterations: Maximum number of iterations.
    - tolerance: The threshold for stopping based on gradient magnitude.
    - threshold: Rounds small values to zero if they are close to zero.

    Returns:
    - x0, y0: Coordinates of the minimum point.
    - f(x0, y0): Minimum value of the function at the point.
    """
    x0, y0 = initial_point
    grad = numerical_gradient(f, x0, y0)
    number_of_iterations = 0

    with tqdm(total=max_iterations) as pbar:
        while np.linalg.norm(grad) > tolerance and number_of_iterations < max_iterations:
            number_of_iterations += 1
            pbar.update(1)

            x0 -= learning_rate * grad[0]
            y0 -= learning_rate * grad[1]

            grad = numerical_gradient(f, x0, y0)

    x0 = round(x0) if abs(x0 - round(x0)) < threshold else x0
    y0 = round(y0) if abs(y0 - round(y0)) < threshold else y0

    return x0, y0, f(x0, y0)
