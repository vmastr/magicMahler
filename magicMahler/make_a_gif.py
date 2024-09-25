import numpy as np
import matplotlib.pyplot as plt
import imageio
import os
import shutil

# Constants
N = 100  # Number of frames
PI = np.pi  # Value of pi

# Generate the x values
xx = np.linspace(-2 * PI, 2 * PI, 100)

# Generate time values for the animation
tt = np.concatenate((np.linspace(0, 1/2, N), np.linspace(1/2, 0, N)))

# Directory to save the frames
frame_dir = "frames"
if not os.path.exists(frame_dir):
    os.makedirs(frame_dir)

# List to hold the filenames of frames
filenames = []

# Generate y values
yy = np.sin(xx)

# Loop through each time step and generate frames
for t in tt:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))  # Create figure with two subplots

    # Left subplot (ax1)
    x_coords = [1 - t, -t, -t, 1 - t]
    y_coords = [-t, 1 - t, -t, -t]
    ax1.plot(x_coords, y_coords)
    ax1.axhline(0, color='black', linewidth=0.5)
    ax1.axvline(0, color='black', linewidth=0.5)
    ax1.set_xlim(-1, 1.5)
    ax1.set_ylim(-1, 1.5)

    # Right subplot (ax2)
    if t == 0:
        x_coords = [-100, 0, 1, -100]
        y_coords = [0, -100, 1, 0]
    elif t == 1/2:
        x_coords = [100, 0, -2, 100]
        y_coords = [0, 100, -2, 0]
    else:
        x_coords = [-1 / t, 0, 1 / (1 - 2 * t), -1 / t]
        y_coords = [0, -1 / t, 1 / (1 - 2 * t), 0]
    
    ax2.plot(x_coords, y_coords)
    ax2.axhline(0, color='black', linewidth=0.5)
    ax2.axvline(0, color='black', linewidth=0.5)
    ax2.set_xlim(-10, 5)
    ax2.set_ylim(-10, 5)

    # Save the frame
    filename = os.path.join(frame_dir, f'frame_{t:.2f}.png')
    plt.savefig(filename)
    plt.close()
    filenames.append(filename)

# Create the gif
with imageio.get_writer('translating_simplex.gif', mode='I', duration=1) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

# Clean up the frames directory
shutil.rmtree(frame_dir)
