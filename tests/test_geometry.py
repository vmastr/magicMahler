# import math
import matplotlib.pyplot as plt
# import imageio
# import os
from magicMahler.graham_scan import Point, graham_scan, graham_scan_gif

# Example usage
points = [Point(0, 0), Point(1, 0.5), Point(2, 2), Point(2, 0), Point(0, 2), Point(2, 3), Point(3, 1), Point(-0.4, 0.6), Point(-0.6, 0.4), Point(0.5, 1)]
hull = graham_scan(points)
print("Convex Hull:", hull)

# Plotting the points and the convex hull
plt.figure()
x_coords = [p.x for p in points]
y_coords = [p.y for p in points]
plt.scatter(x_coords, y_coords)

hull.append(hull[0])  # Close the hull
hx = [p.x for p in hull]
hy = [p.y for p in hull]
plt.plot(hx, hy, 'r-')
plt.show()

# Example usage of graham_scan_gif
graham_scan_gif(points)