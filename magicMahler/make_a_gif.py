import numpy as np 
import matplotlib.pyplot as plt
import imageio 
import os

N = 100 # the number of frames
PI = np.pi # the value of pi

# Generate the xx array
xx = np.linspace(-2*PI, 2*PI, 100)

# Generate the time values 
tt = np.linspace(0, 1/2, N)  # Generate the first part from 0 to 1/2
tt_back = np.linspace(1/2, 0, N)  # Generate the second part from 1/2 to 0
tt = np.concatenate((tt, tt_back)) # Concatenate the two arrays

# Directory to save the frames
frame_dir = "frames"
if not os.path.exists(frame_dir):
    os.makedirs(frame_dir)

# List to hold the filenames of frames
filenames = []

yy = np.sin(xx) # the y values

for t in tt:
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5)) # Create a figure with two subplots

    # ax1 coordinates 
    x_coords = [1-t, -t, -t, 1-t]
    y_coords = [-t, 1-t, -t, -t]

    # plt.scatter(x_coords, y_coords)
    ax1.plot(x_coords, y_coords)

    # Add x and y coordinate axes
    ax1.axhline(0, color='black', linewidth=0.5)
    ax1.axvline(0, color='black', linewidth=0.5)

    # Set fixed limits for x and y axes
    x_limits = (-1, 1.5)
    y_limits = (-1, 1.5)
    ax1.set_xlim(x_limits)
    ax1.set_ylim(y_limits)

    # ax2 coordinates 
    if t == 0:
        x_coords = [-100, 0, 1, -100]
        y_coords = [0, -100, 1, 0]
    elif t == 1/2:
        x_coords = [100, 0, -2, 100]
        y_coords = [0, 100, -2, 0]
    else:   
        x_coords = [-1/t, 0, 1/(1-2*t), -1/t]
        y_coords = [0, -1/t, 1/(1-2*t), 0]

    # plt.scatter(x_coords, y_coords)
    ax2.plot(x_coords, y_coords)

    # Add x and y coordinate axes
    ax2.axhline(0, color='black', linewidth=0.5)
    ax2.axvline(0, color='black', linewidth=0.5)

    # Set fixed limits for x and y axes
    x_limits = (-10, 5)
    y_limits = (-10, 5)
    ax2.set_xlim(x_limits)
    ax2.set_ylim(y_limits)

    # # Set titles for the subplots
    # ax1.set_title('Left Subplot')
    # ax2.set_title('Right Subplot')

    # Save the frame
    filename = os.path.join(frame_dir, f'frame_{t:.2f}.png')
    plt.savefig(filename)
    plt.close()
    filenames.append(filename)

# for t in tt:
#     plt.figure()    
#     x_coords = [1-t, -t, -t, 1-t]
#     y_coords = [-t, 1-t, -t, -t]
#     # plt.scatter(x_coords, y_coords)
#     plt.plot(x_coords, y_coords)

#     # Add x and y coordinate axes
#     plt.axhline(0, color='black', linewidth=0.5)
#     plt.axvline(0, color='black', linewidth=0.5)

#     # Set fixed limits for x and y axes
#     plt.xlim(x_limits)
#     plt.ylim(y_limits)

#     # Save the frame
#     filename = os.path.join(frame_dir, f'frame_{t:.2f}.png')
#     plt.savefig(filename)
#     plt.close()
#     filenames.append(filename)


# Create the gif
with imageio.get_writer('sin_wave.gif', mode='I', duration=1) as writer:
    for filename in filenames:
        image = imageio.imread(filename)
        writer.append_data(image)

# Cleanup the frames directory
import shutil
shutil.rmtree(frame_dir)