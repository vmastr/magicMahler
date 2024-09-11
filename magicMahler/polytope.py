import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate


class Polytope:
    """A class representing a polytope defined by its vertices."""

    def __init__(self, vertices):
        """
        Initialize the polytope with a list of vertices.

        Args:
            vertices (list of tuples): List of (x, y) tuples representing vertices.
        """
        self.vertices = vertices

    def volume(self):
        """
        Compute the area (volume in 2D) of the polytope using the Shoelace formula.

        Returns:
            float: The computed area of the polytope.
        """
        vertices = self.vertices[:]
        vertices.append(vertices[0])  # Repeat the first point to close the loop
        xs, ys = zip(*vertices)
        volume = 0.5 * sum(xs[i] * ys[i + 1] - xs[i + 1] * ys[i] for i in range(len(self.vertices)))
        return abs(volume)

    def plot(self):
        """Plot the polytope using matplotlib."""
        vertices = self.vertices[:]
        vertices.append(vertices[0])
        xs, ys = zip(*vertices)
        plt.figure()
        plt.plot(xs, ys)
        plt.xlabel('x')
        plt.ylabel('y')
        plt.title('Polytope Plot')
        plt.show()

    def polar(self):
        """
        Compute the polar polytope.

        Returns:
            Polytope: The polar polytope as a new Polytope object.
        """
        vertices = self.vertices[:]
        vertices.append(vertices[0])
        polar_polytope = []
        xs, ys = zip(*vertices)
        for i in range(len(self.vertices)):
            L = xs[i] * ys[i + 1] - xs[i + 1] * ys[i]
            if L == 0:
                continue  # Avoid division by zero
            polar_x = (ys[i + 1] - ys[i]) / L
            polar_y = (xs[i] - xs[i + 1]) / L
            polar_polytope.append((polar_x, polar_y))
        return Polytope(polar_polytope)
    
    def Mahler(self):    
        """
        Compute the Mahler volume of the polytope. 

        """
        return 2 * self.volume() * self.polar().volume()
    
    def barycenter(self):
        """
        Compute the barycenter (centroid) of a convex polygon in 2D.

        Args:
            vertices (list of tuples): List of (x, y) tuples representing the vertices of the polygon in counterclockwise order.

        Returns:
            tuple: The (x, y) coordinates of the barycenter.
        """
        # Close the polygon by appending the first vertex at the end
        vertices = self.vertices[:]
        vertices.append(vertices[0])

        # Number of vertices
        n = len(vertices) - 1

        # Initialize area and barycenter coordinates
        A = self.volume()
        C_x = 0
        C_y = 0

        # Compute barycenter coordinates using the formulas
        for i in range(n):
            x_i, y_i = vertices[i]
            x_ip1, y_ip1 = vertices[i + 1]
            # Compute the cross product and area
            cross_product = x_i * y_ip1 - x_ip1 * y_i
            # Compute the centroid coordinates
            C_x += (x_i + x_ip1) * cross_product
            C_y += (y_i + y_ip1) * cross_product

        # Finalize the area and barycenter coordinates
        C_x /= (6 * A)
        C_y /= (6 * A)

        return (C_x, C_y)

    def SantaloPoint(p, self): 
        # Implement code that finds the Lp-Santalo point
        pass 

    def exph1(self, x, y):
        """
        Compute the exponential function h1 of the polytope.

        Args:
            x (float): x-coordinate.
            y (float): y-coordinate.

        Returns:
            float: The computed exponential value.
        """
        vertices = self.vertices[:]
        vertices.append(vertices[0])
        z = np.array([x, y])
        exph1 = 0
        for i in range(len(self.vertices)):
            M = np.array([vertices[i], vertices[i + 1]]).T
            xi, eta = M.T @ z
            exph1 += np.linalg.det(M) * g(xi, eta)
        return exph1 / self.volume()

    def M1(self):
        """
        Compute the L1-Mahler volume of the polytope.

        Returns:
            float: The computed M1 volume.
        """
        prec = 50  # precision of integration

        def G(x, y):
            return 1 / (self.exph1(x, y))

        L1polar = integrate.dblquad(G, -prec, prec, lambda _: -prec, lambda _: prec)
        return L1polar[0] * self.volume()

    def exph(self, p, x, y):
        """Compute the exponential Lp-support function of the polytope."""
        return (self.exph1(p * x, p * y)) ** (1 / p)

    def h(self, p, x, y):
        """Compute the Lp-support function of the polytope."""
        return np.log(self.exph(p, x, y))

    def M(self, p):
        """
        Compute the Mp volume for the polytope.

        Args:
            p (float): The exponent parameter p, or 
            p = "inf": for the classical Mahler volume.

        Returns:
            float: The computed Lp-Mahler volume.
        """

        if p == "inf": 
            return self.Mahler()
        
        else: 
            prec = 50  # precision of integration

            def G(x, y):
                return 1 / (self.exph(p, x, y))

            Lppolar = integrate.dblquad(G, -prec, prec, lambda _: -prec, lambda _: prec)
            return Lppolar[0] * self.volume()

    def Cov(self): 
        """
        Compute the covariance matrix of a convex polygon in 2D.

        Returns:
            np.ndarray: The 2-by-2 covariance matrix of the polygon.
        """
        # Make a copy of vertices and close the polygon by appending the first vertex at the end
        vertices = self.vertices[:]
        vertices.append(vertices[0])

        # Number of vertices
        n = len(vertices) - 1

        # Initialize second moments
        A = self.volume()
        I_xx = 0
        I_xy = 0
        I_yy = 0

        # Compute the second moments using shoelace formulas
        for i in range(n):
            x_i, y_i = vertices[i]
            x_ip1, y_ip1 = vertices[i + 1]
            
            # Compute the cross product
            cross_product = x_i * y_ip1 - x_ip1 * y_i
            
            # Compute the second moments
            I_xx += (x_i**2 + x_i * x_ip1 + x_ip1**2) * cross_product
            I_xy += (x_i * y_ip1 + 2 * x_i * y_i + 2 * x_ip1 * y_ip1 + x_ip1 * y_i) * cross_product
            I_yy += (y_i**2 + y_i * y_ip1 + y_ip1**2) * cross_product

        # Normalize the second moments by the area
        I_xx /= (12 * A)
        I_xy /= (24 * A)
        I_yy /= (12 * A)

        # Compute barycenter once to avoid redundant calls
        b_x, b_y = self.barycenter()

        # Define the covariance matrix components
        C_xx = I_xx - b_x**2 
        C_xy = I_xy - b_x * b_y
        C_yy = I_yy - b_y**2

        return np.array([[C_xx, C_xy], [C_xy, C_yy]])

    def isotropic(self):
        """
        Compute the isotropic constant of the convex polygon.
        
        Returns:
            float: The isotropic constant of the polygon.
        """
        # Calculate the covariance matrix
        cov_matrix = self.Cov()

        # Compute the determinant of the covariance matrix
        det_cov = np.linalg.det(cov_matrix)

        # Compute the volume (area) of the convex polygon
        volume = self.volume()

        # Calculate the isotropic constant using the formula
        L_K = (det_cov ** (1/4)) / (volume ** 0.5)

        return L_K

# Auxiliary functions
def f(x):
    return (np.exp(x) - 1) / x if x != 0 else 1


def g(x, y):
    if x != y:
        return (f(x) - f(y)) / (x - y)
    elif x == y and x != 0:
        return (1 / x) * (np.exp(x) - f(x))
    else:
        return 1 / 2


# Testing
if __name__ == "__main__":
    simplex = Polytope([(0,0), (1,0), (0,1)])
    triangle = Polytope([(1, 1), (-1, 0), (0, -1)])
    print("Triangle Volume:", triangle.volume())
    triangle.plot()

    square = Polytope([[1, 1], [-1, 1], [-1, -1], [1, -1]])
    print("Square M(1):", square.M(1))
    print("Square M(5):", square.M(5))
    print("Square Mahler volume:", square.Mahler())
    print("Square Mahler volume:", square.M("inf"))
    print("Barycenter:", triangle.barycenter(), simplex.barycenter())
    print("Covariance matrix:", triangle.Cov())
    print("Isotropic constant:", simplex.isotropic(), square.isotropic())