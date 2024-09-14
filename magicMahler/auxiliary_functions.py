import numpy as np 
from scipy import integrate 

def aux1(x):
    # Clip values of x to prevent overflow in np.exp()
    x = np.clip(x, -700, 700)  # Restrict x within the range [-700, 700]: Returns 700 or -700 for values not in the interval
    return (np.exp(x) - 1) / x if x != 0 else 1

def aux2(x, y):
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

def gradient_descent(f, initial_point, learning_rate=1e-4, max_iterations=1000, tolerance=1e-4, threshold=1e-6):
    """Find the minimum of function f using gradient descent."""
    x, y = initial_point
    for i in range(max_iterations):
        grad = numerical_gradient(f, x, y)  # Compute gradient
        x_new = x - learning_rate * grad[0]
        y_new = y - learning_rate * grad[1]
        
        # Check for convergence
        if np.linalg.norm(np.array([x_new, y_new]) - np.array([x, y])) < tolerance:
            print(f"Converged in {i+1} iterations.")
            break
        
        x, y = x_new, y_new  # Update the point

    # Round small values to zero if they are below the threshold
    x = round(x) if abs(x-round(x)) < threshold else x
    y = round(y) if abs(y-round(y)) < threshold else y

    return x, y, f(x, y)


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