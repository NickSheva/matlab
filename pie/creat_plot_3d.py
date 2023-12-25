"""Importing necessary packages"""
from mpl_toolkits import mplot3d
import numpy as np
import matplotlib.pyplot as plt

# Creation an empty figure
fig = plt.figure()

# Defining the exes as 3D
ax = plt.axes(1, 2, 1projection='3d')

# Defining all three axes
z = np.linspace(0, 1, 100)
y = z * np.cos(25 * z)
x = z * np.sin(25 * z)
# Plotting
ax.plot(x, y, z, c='red')
ax.set_title("A simple 3d line plot")
# Displaying the plot
plt.show()