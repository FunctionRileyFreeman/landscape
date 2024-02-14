import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle, Ellipse, Rectangle
import random

# Set the backend explicitly
import matplotlib
matplotlib.use('TkAgg')

# Create a function to draw a tree
def draw_tree(ax, x, y, trunk_color='brown', leaf_color='green'):
    # Draw trunk
    trunk = Rectangle((x - 5, y), 10, 50, color=trunk_color)
    ax.add_patch(trunk)

    # Draw leaves
    leaf1 = Ellipse((x, y + 30), 30, 40, color=leaf_color)
    leaf2 = Ellipse((x - 15, y + 50), 30, 40, color=leaf_color)
    leaf3 = Ellipse((x + 15, y + 50), 30, 40, color=leaf_color)
    ax.add_patch(leaf1)
    ax.add_patch(leaf2)
    ax.add_patch(leaf3)

# Create a function to draw a cloud
def draw_cloud(ax, x, y, size=100, color='white'):
    cloud = Circle((x, y), size, color=color, alpha=0.8)
    ax.add_patch(cloud)

# Create a function to draw a flower
def draw_flower(ax, x, y, color='red'):
    # Stem
    stem = Rectangle((x - 1, y), 2, 30, color='green')
    ax.add_patch(stem)
    # Petals
    petals = Circle((x, y + 15), 8, color=color)
    ax.add_patch(petals)

# Create landscape
def create_landscape():
    fig, ax = plt.subplots()

    # Draw ground
    ground = Rectangle((-200, -100), 400, 200, color='green')
    ax.add_patch(ground)

    # Draw mountains
    mountain1 = Ellipse((-150, 50), 200, 100, color='grey')
    ax.add_patch(mountain1)
    mountain2 = Ellipse((100, 50), 200, 100, color='grey')
    ax.add_patch(mountain2)

    # Draw trees
    for _ in range(10):
        draw_tree(ax, random.randint(-200, 200), random.randint(-100, -50))

    # Draw clouds
    for _ in range(3):
        draw_cloud(ax, random.randint(-200, 200), random.randint(50, 100))

    # Draw river
    river = Rectangle((-200, -100), 400, 50, color='blue')
    ax.add_patch(river)

    # Draw flowers
    for _ in range(5):
        draw_flower(ax, random.randint(-200, 200), random.randint(-100, 0))

    # Set axis limits and remove ticks
    ax.set_xlim(-200, 200)
    ax.set_ylim(-100, 100)
    ax.set_xticks([])
    ax.set_yticks([])

    plt.show()

# Create landscape
create_landscape()
