from polytope import Polytope








# Testing
triangle = Polytope([(1, 1), (-1, 0), (0, -1)])
print("Triangle Volume:", triangle.volume())