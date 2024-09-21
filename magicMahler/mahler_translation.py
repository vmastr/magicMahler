import matplotlib.pyplot as plt
import numpy as np 
from polytope import Polytope


# Initialize the polytope
body = Polytope([(1, 1), (-1, 0), (-1, -1), (0, -1)])

# Set global variables for interaction
dragging = False
offset = None

# Function to update the plots
def update_plots(polytope, ax1, ax2):
    ax1.clear()
    ax2.clear()

    # Body plot
    vertices = polytope.vertices[:]
    vertices.append(vertices[0])  # Close the loop
    xs, ys = zip(*vertices)
    ax1.plot(xs, ys, 'b-')
    ax1.axhline(0, color='black', linewidth=0.5)
    ax1.axvline(0, color='black', linewidth=0.5)
    ax1.set_xlim(-2, 2)
    ax1.set_ylim(-2, 2)
    ax1.set_title('Convex body')

    # Polar plot
    polar_vertices = polytope.polar().vertices[:]
    polar_vertices.append(polar_vertices[0])  # Close the loop
    xs_polar, ys_polar = zip(*polar_vertices)
    ax2.plot(xs_polar, ys_polar, 'r-')
    ax2.axhline(0, color='black', linewidth=0.5)
    ax2.axvline(0, color='black', linewidth=0.5)
    ax2.set_xlim(-2, 2)
    ax2.set_ylim(-2, 2)
    ax2.set_title('Polar body')

    plt.draw()

# Function to handle mouse press
def on_press(event):
    global dragging, offset
    if event.inaxes is ax1:  # Only drag within the polytope plot
        dragging = True
        # Capture the initial click position
        offset = (event.xdata, event.ydata)

# Function to handle mouse drag
def on_motion(event):
    global dragging, offset
    if dragging and event.inaxes is ax1:
        dx = event.xdata - offset[0]
        dy = event.ydata - offset[1]

        # Translate polytope vertices by the dragged amount
        translated_vertices = [(x + dx, y + dy) for x, y in body.vertices]
        body.update_vertices(translated_vertices)  # Assuming polytope has an update method

        # Update the plot
        update_plots(body, ax1, ax2)

        # Update the offset
        offset = (event.xdata, event.ydata)

# Function to handle mouse release
def on_release(event):
    global dragging
    dragging = False

# Create the figure and two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))  # 1 row, 2 columns

# Initial plot
update_plots(body, ax1, ax2)

# Connect mouse events
fig.canvas.mpl_connect('button_press_event', on_press)
fig.canvas.mpl_connect('motion_notify_event', on_motion)
fig.canvas.mpl_connect('button_release_event', on_release)

# Show the plots
plt.show()

# DOUBLE CLICK AND DRAG