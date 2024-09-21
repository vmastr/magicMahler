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

## 1. Defining the Polytope 

You can create a polytope by passing a list of counter-clockwise list of vertices to the `Polytope` class: 

```bash 
from magicMahler import Polytope

# Define a polytope by specifying its vertices
vertices = [(1, 1), (-1, 0), (-1, -1), (0, -1)]
polytope = Polytope(vertices)

# Compute the volume (area in 2D)
volume = polytope.volume()
print(f"Volume: {volume}")

```