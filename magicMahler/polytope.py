import numpy as np 
import matplotlib.pyplot as plt
from scipy import integrate


class Polytope: 

    def __init__(self, vertices): 
        self.vertices = vertices 
    
    def volume(self): 
        # Must be counter clock-wise oriented polygon
        """Compute the volume of the polytope"""
        vertices = self.vertices[:]
        vertices.append(vertices[0]) #repeat the first point to create a 'closed loop'
        xs, ys = zip(*vertices) #create lists of x and y values
        volume = 0
        for i in range(len(self.vertices)):
            L = (1/2) * (xs[i] * ys[i+1] - xs[i+1] * ys[i]) # volume of triangle
            volume += L
        return volume
    
    def plot(self):
        vertices = self.vertices[:]
        vertices.append(vertices[0])
        xs, ys = zip(*vertices) #create lists of x and y values
        plt.figure()
        plt.plot(xs,ys) 
        plt.show()

    def polar(self): 
        vertices = self.vertices[:]
        vertices.append(vertices[0])
        polar_polytope = []
        xs, ys = zip(*vertices)
        for i in range(len(self.vertices)): 
            L = xs[i] * ys[i+1] - xs[i+1] * ys[i]
            polar_x = (ys[i+1] - ys[i])/ L
            polar_y = (xs[i] - xs[i+1])/ L
            polar_polytope.append((polar_x, polar_y))
        return Polytope(polar_polytope)

    def barycenter(self):
        # Implement code that computes the barycenter 
        pass

    def SantaloPoint(p, self): 
        # Implement code that finds the Lp-Santalo point
        pass 

    def exph1(self, x, y): 
        vertices = self.vertices[:] # Make a copy of the vertices
        vertices.append(vertices[0])
        z = np.array([x, y])
        exph1 = 0 
        for i in range(len(self.vertices)): 
            M = np.array([vertices[i], vertices[i+1]]).T
            xi = M.T.dot(z)[0]
            eta = M.T.dot(z)[1]
            exph1 += np.linalg.det(M) * g(xi, eta)
        return exph1/ self.volume() 

    def M1(self):
        prec = 50  # precision of integration
        def G(x,y):
            return 1/(self.exph1(x, y))
        L1polar = integrate.dblquad(G, -prec, prec, -prec, prec)
        return L1polar[0] * self.volume()


# some auxiliary functions
def f(x): 
    if x != 0: 
        return (np.exp(x) - 1)/x 
    else: 
        return 1

def g(x,y): 
    if x != y:
        return (f(x) - f(y))/(x-y)
    elif x == y and x != 0:
        return (1/x) * (np.exp(x) - f(x))
    else:
        return 1/2





# TESTING 
  
triangle = Polytope([(1,1), (-1, 0), (0, -1)])
# print(triangle.volume())
# print(triangle.vertices)
# triangle.plot()
# print(triangle.polar().vertices)
# print(triangle.exph1(0,0))
# print(triangle.M1())


# Reality check for exph1 of the square
square = Polytope([[1,1], [-1,1], [-1,-1], [1,-1]])

# def exph1sq(x,y): 
#     return (f(x)+f(-x)) * (f(y)+f(-y)) / 4

# print(exph1sq(2,3))
# print(square.exph1(2,3))
print(square.M1())
