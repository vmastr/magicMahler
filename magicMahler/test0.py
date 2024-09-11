import math
import matplotlib.pyplot as plt
import imageio
import os

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"({self.x}, {self.y})"

def polar_angle(p0, p1=None):
    if p1 is None:
        p1 = Point(0, 0)
    y_span = p0.y - p1.y
    x_span = p0.x - p1.x
    return math.atan2(y_span, x_span) # returns the arctan of y/x in radians

def distance(p0, p1=None):
    if p1 is None:
        p1 = Point(0, 0)
    y_span = p0.y - p1.y
    x_span = p0.x - p1.x
    return y_span ** 2 + x_span ** 2

def det(p1, p2, p3):
    return (p2.x - p1.x) * (p3.y - p1.y) - (p2.y - p1.y) * (p3.x - p1.x)


def graham_scan(points):
    points = sorted(points, key=lambda p: (p.y, p.x))
    p0 = points[0]
    sorted_points = sorted(points[1:], key=lambda p: (polar_angle(p, p0), -distance(p, p0)))
    hull = [p0, sorted_points[0]]

    for point in sorted_points[1:]:
        while len(hull) > 1 and det(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)

    return hull

def graham_scan_gif(points): 
    # produces a gif of the graham scan algorithm
    points = sorted(points, key=lambda p: (p.y, p.x))
    p0 = points[0]
    sorted_points = sorted(points[1:], key=lambda p: (polar_angle(p, p0), -distance(p, p0)))
    hull = [p0, sorted_points[0]]

    # Directory to save the frames
    frame_dir = "frames"
    if not os.path.exists(frame_dir):
        os.makedirs(frame_dir)

    # List to hold the filenames of frames
    filenames = []

    # Make the zeroth and first frame
    # Plotting the points and the convex hull
    plt.figure()    
    x_coords = [p.x for p in points]
    y_coords = [p.y for p in points]
    plt.scatter(x_coords, y_coords)
    filename = os.path.join(frame_dir, f'frame_{0}.png')
    plt.savefig(filename)
    filenames.append(filename)
        
    hx = [p.x for p in hull]
    hy = [p.y for p in hull]
    plt.plot(hx, hy, 'r-')

    # Save the frame
    filename = os.path.join(frame_dir, f'frame_{1}.png')
    plt.savefig(filename)
    plt.close()
    filenames.append(filename)

    frame_count = 2

    for point in sorted_points[1:]:
        while len(hull) > 1 and det(hull[-2], hull[-1], point) <= 0:
            hull.pop()
        hull.append(point)
        # Plotting the points and the convex hull
        plt.figure()    
        x_coords = [p.x for p in points]
        y_coords = [p.y for p in points]
        plt.scatter(x_coords, y_coords)
        
        hx = [p.x for p in hull]
        hy = [p.y for p in hull]
        plt.plot(hx, hy, 'r-')

        # Save the frame
        filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
        plt.savefig(filename)
        plt.close()
        filenames.append(filename)
        frame_count += 1
    
    # Add the last frame
    hull.append(hull[0])  # Close the hull
    # Plotting the points and the convex hull
    plt.figure()
    x_coords = [p.x for p in points]
    y_coords = [p.y for p in points]
    plt.scatter(x_coords, y_coords)

    hx = [p.x for p in hull]
    hy = [p.y for p in hull]
    plt.plot(hx, hy, 'r-')
    # Save the frame
    filename = os.path.join(frame_dir, f'frame_{frame_count}.png')
    plt.savefig(filename)
    plt.close()
    filenames.append(filename)

    # Create the gif
    with imageio.get_writer('graham_scan.gif', mode='I', duration= 2) as writer:
        for filename in filenames:
            image = imageio.imread(filename)
            writer.append_data(image)
    print("GIF created successfully!")
    
    # Cleanup the frames directory
    import shutil
    shutil.rmtree(frame_dir)


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