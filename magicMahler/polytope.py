import numpy as np 
import matplotlib.pyplot as plt


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







# TESTING 
  
triangle = Polytope([(1,1), (-1, 0), (0, -1)])
# print(triangle.volume())
# print(triangle.vertices)
# triangle.plot()
# print(triangle.polar().vertices)




