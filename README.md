# magicMahler

**magicMahler** is a Python package for working with polytopes, their polar bodies, and Mahler volumes. It provides functionality for manipulating and visualizing convex polytopes, computing their Mahler volumes, and applying the Mahler sliding algorithm. The package also includes auxiliary functions for numerical optimization and gradient descent.

## Features
- Define and manipulate convex polytopes.
- Compute volumes, polar bodies, Mahler volumes, and isotropic constants.
- Interactive visualization of polytopes and their polar bodies.
- Perform gradient descent to find key points (e.g., Lp-Santalo points).
- Implement Graham Scan for convex hull computation.
- Support for Lp-Mahler volumes.

## Installation

Clone the repository and install the required packages using `pip`:

```bash
git clone https://github.com/vmastr/magicMahler.git
cd magicMahler
pip install -r requirements.txt
```

Make sure you have the required dependencies in requirements.txt. They should include: 

- `numpy` 
- `matplotlib`
- `scipy`
- `tqdm` 
- `imageio` 


## Usage

### 1. Defining the Polytope 

You can create a polytope by passing a list of counter-clockwise list of vertices to the `Polytope` class: 

```bash 
from magicMahler import Polytope

# Define a polytope by specifying its vertices
vertices = [(1, 1), (-1, 0), (-1, -1), (0, -1)]
polytope = Polytope(vertices)

# Compute the volume (area in 2D)
volume = polytope.volume()
print(f"Volume: {volume}")

# Plot the polytope
polytope.plot()
```

### 2. Computing and plotting the Polar body

You can compute and visualize the polar body of the polytope: 

```bash 
# Compute the polar body of the polytope
polar_polytope = polytope.polar()

# Plot both the original polytope and its polar
polytope.polar_plot()
```

### 3. Interactive plot with dragging 

You can interactively drag the polytope and watch its polar update in real-time: 

```bash 
from magicMahler import update_plots

# Initialize the polytope and use interactive dragging
polytope = Polytope([(1, 1), (-1, 0), (-1, -1), (0, -1)])
update_plots(polytope)
```
Note you have to double-click then drag. 


### 4. Compute the Lp-Mahler volumes

You can compute the classical Mahler volume and the Lp-Mahler volumes: 

```bash
# Compute the Mahler volume
mahler_volume = polytope.Mahler()
print(f"Mahler Volume: {mahler_volume}")

# Compute the Lp-Mahler volume for p = 1
Lp_mahler_volume = polytope.M(1)
print(f"L1-Mahler Volume: {Lp_mahler_volume}")
```

### 5. Run the Graham scan algorithm 

You can compute the convex hull of a set of points using the Graham scan algorithm: 

```bash
from magicMahler import graham_scan, Point

# Define points
points = [Point(0, 0), Point(1, 0.5), Point(2, 2), Point(2, 0), Point(0, 2)]

# Compute the convex hull
convex_hull = graham_scan(points)
print(f"Convex Hull: {convex_hull}")
```

## Contributing 

Contributions are welcome! If you find a bug or have a feature request, feel free to open an issue or submit a pull request. 

## Contact

For any questions, feel free to contact me at vmastr@umd.edu. 





















