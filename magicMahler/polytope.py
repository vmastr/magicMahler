import numpy as np
import matplotlib.pyplot as plt
from scipy import integrate
from auxiliary_functions import aux1, aux2, numerical_gradient, gradient_descent, safe_divide, double_integration 


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

    def translate(self, x, y):
        """
        Translate the polytope by a given vector (x, y).

        Args:
            x (float): The amount to translate in the x-direction.
            y (float): The amount to translate in the y-direction.

        Returns:
            list of tuples: A new list of vertices representing the translated polytope.
        """
        vertices = self.vertices[:] # make a copy of the vertices
        translatedP = []  
        for i in range(len(vertices)):
            translatedP.append((vertices[i][0]- x, vertices[i][1] - y))
        return Polytope(translatedP)


    def SantaloPoint(self, p="inf"): 
        # Step 1: Define the function M(p, P - (x, y))
        def F(x,y):
            return self.translate(x, y).M(p)

        # Step 2: Select the initial point
        n = len(self.vertices)
        x_avg = sum(x for x, y in self.vertices) / n
        y_avg = sum(y for x, y in self.vertices) / n

        initial_point = (x_avg, y_avg)

        # Step 2: Run Gradient Descent
        result_x, result_y, min_value = gradient_descent(F, initial_point)

        return result_x, result_y



    # def exph1(self, x, y):
    #     """
    #     Compute the exponential function h1 of the polytope.

    #     Args:
    #         x (float): x-coordinate.
    #         y (float): y-coordinate.

    #     Returns:
    #         float: The computed exponential value.
    #     """
    #     vertices = self.vertices[:]
    #     vertices.append(vertices[0])
    #     z = np.array([x, y])
    #     exph1 = 0
    #     for i in range(len(self.vertices)):
    #         M = np.array([vertices[i], vertices[i + 1]]).T
    #         xi, eta = M.T @ z
    #         exph1 += np.linalg.det(M) * aux2(xi, eta)
    #     return exph1 / self.volume()

    def safe_exph1(self, x, y):
        vertices = self.vertices[:]  # Make a copy of the vertices
        vertices.append(vertices[0])
        z = np.array([x, y])
        exph1 = 0
        for i in range(len(self.vertices)):
            M = np.array([vertices[i], vertices[i+1]]).T
            xi = M.T.dot(z)[0]
            eta = M.T.dot(z)[1]
            
            # Prevent overflow and handle invalid values
            det_M = np.clip(np.linalg.det(M), -1e150, 1e150)  # Clip values to prevent overflow
            g_val = np.clip(aux2(xi, eta), -1e150, 1e150)  # Also clip auxiliary function results
            
            exph1 += det_M * g_val

        return exph1 / (self.volume() + 1e-10)  # Add epsilon to avoid division by zero

    def M1(self):
        """
        Compute the L1-Mahler volume of the polytope.

        Returns:
            float: The computed M1 volume.
        """
        prec = 30  # precision of integration

        def G(x, y):
            return safe_divide(1, self.safe_exph1(x,y))

        L1polar = double_integration(G, -prec, prec, lambda _: -prec, lambda _: prec)
        return L1polar[0] * self.volume()

    def exph(self, p, x, y):
        """Compute the exponential Lp-support function of the polytope."""
        return (self.safe_exph1(p * x, p * y)) ** (1 / p)

    def h(self, p, x, y):
        """Compute the Lp-support function of the polytope."""
        return np.log(self.exph(p, x, y))

    def M(self, p="inf"):
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
                return safe_divide(1, self.exph(p, x, y))

            Lppolar = double_integration(G, -prec, prec, lambda _: -prec, lambda _: prec)
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



# # Testing
# if __name__ == "__main__":
#     simplex = Polytope([(0,0), (1,0), (0,1)])
#     triangle = Polytope([(1, 1), (-1, 0), (0, -1)])
#     # print("Triangle Volume:", triangle.volume())
#     # triangle.plot()

#     square = Polytope([[1, 1], [-1, 1], [-1, -1], [1, -1]])
#     # print("Square M(1):", square.M(1))
#     # print("Square M(5):", square.M(5))
#     # print("Square Mahler volume:", square.Mahler())
#     # print("Square Mahler volume:", square.M("inf"), square.M())
#     # print("Barycenter:", triangle.barycenter(), simplex.barycenter())
#     # print("Covariance matrix:", triangle.Cov())
#     # print("Isotropic constant:", simplex.isotropic(), square.isotropic())
#     # print("Translated simplex:", simplex.translate(1/3,1/3).vertices)
#     # print("M1 of translated square:", square.translate(1/2, 1/2).M(1))
#     # print("M1 of the simplex:", simplex.translate(.3,.3).M(1))
#     # print("Santalo point of triangle:", triangle.SantaloPoint())
#     # print("Santalo point of simplex:", simplex.SantaloPoint())
#     # print("L1-Santalo point of translated square:", square.translate(1,1).SantaloPoint(1))
#     # print("L1-Santalo point of triangle:", triangle.translate(.5,.5).SantaloPoint(1))
#     print("L1-Santalo point of simplex:", simplex.SantaloPoint(1))


# Gradient descent by hand 
simplex = Polytope([(0,0), (1,0), (0,1)])
learning_rate = .00001

def D(x,y): 
    return simplex.translate(x,y).M(1)

x0, y0 = .4, .35
D_old = D(x0, y0) 

for i in range(100): 
    grad = numerical_gradient(D, x0, y0)
    x0 -= learning_rate * grad[0]
    y0 -= learning_rate * grad[1]

    D_new = D(x0, y0)
    print(D_old, grad, x0, y0, D_new)    
    D_old = D_new      
 
