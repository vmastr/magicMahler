import numpy as np 

def aux1(x):
    return (np.exp(x) - 1) / x if x != 0 else 1


def aux2(x, y):
    if x != y:
        return (aux1(x) - aux1(y)) / (x - y)
    elif x == y and x != 0:
        return (1 / x) * (np.exp(x) - aux1(x))
    else:
        return 1 / 2


# Gradient descent
def numerical_gradient(f, x, y, h=1e-5):
    """Compute the numerical gradient of a 2D function using central difference."""
    grad_x = (f(x + h, y) - f(x - h, y)) / (2 * h)
    grad_y = (f(x, y + h) - f(x, y - h)) / (2 * h)
    return np.array([grad_x, grad_y])

def gradient_descent(f, initial_point, learning_rate=0.1, max_iterations=1000, tolerance=1e-7, threshold=1e-6):
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


# TEST
def F(x,y):
    return (x-1)**2 + y**2

print(gradient_descent(F, (2,1)))