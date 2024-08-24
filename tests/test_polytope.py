from magicMahler.polytope import Polytope


triangle = Polytope([(1,1), (-1, 0), (0, -1)])
print(triangle.volume())