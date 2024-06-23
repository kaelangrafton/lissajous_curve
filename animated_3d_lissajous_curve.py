import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import imageio
import os

# Parameters for the Lissajous curve
A = 5      # Amplitude in x direction
B = 5      # Amplitude in y direction
C = 5      # Amplitude in z direction
a = 3      # Frequency in x direction
b = 2      # Frequency in y direction
c = 4      # Frequency in z direction
delta_x = np.pi / 2  # Phase shift for x
delta_y = np.pi / 3  # Phase shift for y
delta_z = np.pi / 4  # Phase shift for z

# Generate the data for the Lissajous curve
t = np.linspace(0, 2 * np.pi, 1000)
x = A * np.sin(a * t + delta_x)
y = B * np.sin(b * t + delta_y)
z = C * np.sin(c * t + delta_z)

# Create directory to save frames
if not os.path.exists('frames'):
    os.makedirs('frames')

# Function to save frames for the drawing and rotating animation
def save_drawing_and_rotation_frames():
    num_steps = len(t)
    num_frames = num_steps // 10
    for i in range(1, num_steps + 1, 10):
        progress = i / num_steps
        angle = -60 + progress * 60  # Linearly interpolate azim from -60 to 0
        elev = 30 + progress * 60    # Linearly interpolate elev from 30 to 90
        fig = plt.figure(figsize=(10, 10))
        ax = fig.add_subplot(111, projection='3d')
        ax.plot(x[:i], y[:i], z[:i], color='black', linewidth=2)
        ax.view_init(elev=elev, azim=angle)
        ax.axis('off')
        plt.savefig(f'frames/frame_{i:03d}.png', bbox_inches='tight', pad_inches=0)
        plt.close()
    
    # Ensure the last frame closes the curve completely
    fig = plt.figure(figsize=(10, 10))
    ax = fig.add_subplot(111, projection='3d')
    ax.plot(x, y, z, color='black', linewidth=2)
    ax.view_init(elev=90, azim=0)
    ax.axis('off')
    plt.savefig('frames/frame_final.png', bbox_inches='tight', pad_inches=0)
    plt.close()

# Save frames
save_drawing_and_rotation_frames()

# Create GIF
images = []
for filename in sorted(os.listdir('frames')):
    if filename.endswith('.png'):
        images.append(imageio.v2.imread(os.path.join('frames', filename)))
imageio.mimsave('lissajous_curve_animation.gif', images, duration=50)

# Clean up frames
for filename in os.listdir('frames'):
    file_path = os.path.join('frames', filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
os.rmdir('frames')

print("Animated GIF saved as 'lissajous_curve_animation.gif'")
