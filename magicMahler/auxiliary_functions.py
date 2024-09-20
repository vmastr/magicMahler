import numpy as np 
from tqdm import tqdm
from scipy import integrate 

def aux1(x):
    """
    Parameters: x.

    Returns: (e^x - 1)/x.
    """
    # Clip values of x to prevent overflow in np.exp()
    x = np.clip(x, -700, 700)  # Restrict x within the range [-700, 700]: Returns 700 or -700 for values not in the interval
    return (np.exp(x) - 1) / x if x != 0 else 1

def aux2(x, y):
    """
    Patameters: x, y.

    Returns ((e^x-1)/x - (e^y-1)/y) / (x-y).
    """
    if np.isclose(x, y): 
        if np.isclose(x,0):
            return 1/2
        x_clipped = np.clip(x, -700, 700) # Cap x to prevent overflow
        return (x_clipped*np.exp(x_clipped) - np.exp(x_clipped) +1) / (x_clipped**2) 
    return (aux1(x) - aux1(y)) / (x - y)
    

def safe_divide(a, b, epsilon=1e-10):
    return a / (b + epsilon)


def double_integration(f, a, b, c, d):
    """
    Integrate a two-variable function f over the region [a, b] x [c, d]
    using a higher limit on subdivisions.

    Parameters:
    - f: Function to integrate, must accept two variables (x, y).
    - a, b: Integration limits for the first variable (x).
    - c, d: Integration limits for the second variable (y), can be numbers or functions of x.

    Returns:
    - result: The computed integral value.
    - error: An estimate of the absolute error in the result.
    """
    # If c and d are functions of x, pass them directly; otherwise, use lambda to make them constant
    lower_y = c if callable(c) else lambda x: c
    upper_y = d if callable(d) else lambda x: d

    # Perform the double integration
    result, error = integrate.dblquad(f, a, b, lower_y, upper_y, epsabs=1.49e-8, epsrel=1.49e-8)
    return result, error

# Gradient descent
def numerical_gradient(f, x, y, h=1e-5):
    """Compute the numerical gradient of a 2D function using central difference."""
    grad_x = (f(x + h, y) - f(x - h, y)) / (2 * h)
    grad_y = (f(x, y + h) - f(x, y - h)) / (2 * h)
    return np.array([grad_x, grad_y])


def gradient_descent(f, initial_point, learning_rate=1e-4, max_iterations=100, tolerance=1e-3, threshold=1e-6):
    """Find the minimum of function f using gradient descent."""
    x0, y0 = initial_point
    grad = numerical_gradient(f, x0, y0)
    number_of_iterations = 0

    # Initialize tqdm loading bar
    with tqdm(total=max_iterations) as pbar:
        while np.sqrt(grad[0]**2 + grad[1]**2) > tolerance and number_of_iterations < max_iterations:
            number_of_iterations += 1

            # Update the progress bar
            pbar.update(1)

            # Perform gradient descent step
            x0 -= learning_rate * grad[0]
            y0 -= learning_rate * grad[1]

            grad = numerical_gradient(f, x0, y0)

    # Round small values to zero if they are below the threshold
    x0 = round(x0) if abs(x0-round(x0)) < threshold else x0
    y0 = round(y0) if abs(y0-round(y0)) < threshold else y0

    print("Number of iterations:", number_of_iterations)
    print("Minimum attained at: ", (x0, y0))
    print("Gradient at that point: ", grad)
    print("Minimum value: ", f(x0, y0))

    # return x0, y0, f(x0, y0)


# # TEST
# def F(x,y):
#     return (x-1)**2 + y**2

# def G(x,y):
#     return x**2 + y**2

# print(gradient_descent(F, (2,1)))
# print(aux1(1), aux1(0), aux1(800))
# print(aux2(0,0), aux2(1e-3, 0), aux2(1e-8, 0))
# print(aux2(2,2), aux2(2 + 1e-2, 2), aux2(2 + 1e-8, 2))
# print(double_integration(F, -1, 2, -5, 10))
# print(double_integration(G, 0, 1, 0, 1))