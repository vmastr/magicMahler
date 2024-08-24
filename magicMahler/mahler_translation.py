import matplotlib.pyplot as plt
import numpy as np 
from polytope import Polytope



body = Polytope([(1,1), (-1, 0), (-1,-1), (0, -1)])
polar = body.polar()

def polar_frame(Polytope): 
    # Create a figure and two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))  # 1 row, 2 columns

    # Body plot
    vertices = Polytope.vertices[:]
    vertices.append(vertices[0])
    xs, ys = zip(*vertices) #create lists of x and y values
    ax1.plot(xs,ys) 
    ax1.axhline(0, color='black', linewidth=0.5)  # Add x-axis
    ax1.axvline(0, color='black', linewidth=0.5)  # Add y-axis
    ax1.set_xlim(-2, 2)  # Adjust x-axis limits to zoom out
    ax1.set_ylim(-2, 2)  # Adjust y-axis limits to zoom out
    ax1.set_title('Convex body')

    # Polar plot
    vertices = Polytope.polar().vertices[:]
    vertices.append(vertices[0])
    xs, ys = zip(*vertices)  # create lists of x and y values
    ax2.plot(xs, ys)
    ax2.axhline(0, color='black', linewidth=0.5)  # Add x-axis
    ax2.axvline(0, color='black', linewidth=0.5)  # Add y-axis
    ax1.set_xlim(-2, 2)  # Adjust x-axis limits to zoom out
    ax1.set_ylim(-2, 2)  # Adjust y-axis limits to zoom out
    ax2.set_title('Polar body')

    # Adjust layout to prevent overlap
    plt.tight_layout()

    # Show the plots
    plt.show()


polar_frame(body)


