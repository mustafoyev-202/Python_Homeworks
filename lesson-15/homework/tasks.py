import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 1. Basic Plotting
x = np.linspace(-10, 10, 400)
y = x**2 - 4 * x + 4
plt.figure()
plt.plot(x, y)
plt.title("Plot of $f(x) = x^2 - 4x + 4$")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.grid(True)
plt.show()

# 2. Sine and Cosine Plot
x = np.linspace(0, 2 * np.pi, 400)
sin_x = np.sin(x)
cos_x = np.cos(x)
plt.figure()
plt.plot(x, sin_x, label="sin(x)", linestyle="-", marker="o", color="b")
plt.plot(x, cos_x, label="cos(x)", linestyle="--", marker="x", color="r")
plt.title("Sine and Cosine Plot")
plt.xlabel("x")
plt.ylabel("Value")
plt.legend()
plt.grid(True)
plt.show()

# 3. Subplots
x = np.linspace(-10, 10, 400)
x_pos = np.linspace(0, 10, 400)
fig, axs = plt.subplots(2, 2)
axs[0, 0].plot(x, x**3, "tab:blue")
axs[0, 0].set_title("$f(x) = x^3$")
axs[0, 0].set_xlabel("x")
axs[0, 0].set_ylabel("f(x)")
axs[0, 1].plot(x, np.sin(x), "tab:orange")
axs[0, 1].set_title("$f(x) = \sin(x)$")
axs[0, 1].set_xlabel("x")
axs[0, 1].set_ylabel("f(x)")
axs[1, 0].plot(x, np.exp(x), "tab:green")
axs[1, 0].set_title("$f(x) = e^x$")
axs[1, 0].set_xlabel("x")
axs[1, 0].set_ylabel("f(x)")
axs[1, 1].plot(x_pos, np.log(x_pos + 1), "tab:red")
axs[1, 1].set_title("$f(x) = \log(x+1)$")
axs[1, 1].set_xlabel("x")
axs[1, 1].set_ylabel("f(x)")
plt.tight_layout()
plt.show()

# 4. Scatter Plot
x = np.random.uniform(0, 10, 100)
y = np.random.uniform(0, 10, 100)
plt.figure()
plt.scatter(x, y, c="purple", marker="*")
plt.title("Scatter Plot of Random Points")
plt.xlabel("x")
plt.ylabel("y")
plt.grid(True)
plt.show()

# 5. Histogram
data = np.random.normal(0, 1, 1000)
plt.figure()
plt.hist(data, bins=30, alpha=0.75)
plt.title("Histogram of Normally Distributed Data")
plt.xlabel("Value")
plt.ylabel("Frequency")
plt.show()

# 6. 3D Plotting
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)
z = np.cos(x**2 + y**2)
fig = plt.figure()
ax = fig.add_subplot(111, projection="3d")
surf = ax.plot_surface(x, y, z, cmap="viridis")
fig.colorbar(surf)
ax.set_title("3D Surface Plot of $f(x, y) = \cos(x^2 + y^2)$")
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("f(x, y)")
plt.show()

# 7. Bar Chart
products = ["Product A", "Product B", "Product C", "Product D", "Product E"]
sales = [200, 150, 250, 175, 225]
plt.figure()
plt.bar(products, sales, color=["blue", "orange", "green", "red", "purple"])
plt.title("Sales Data for Products")
plt.xlabel("Products")
plt.ylabel("Sales")
plt.show()

# 8. Stacked Bar Chart
categories = ["Category A", "Category B", "Category C"]
time_periods = ["T1", "T2", "T3", "T4"]
data = np.random.randint(1, 10, (3, 4))
fig, ax = plt.subplots()
ax.bar(time_periods, data[0], label=categories[0])
ax.bar(time_periods, data[1], bottom=data[0], label=categories[1])
ax.bar(time_periods, data[2], bottom=data[0] + data[1], label=categories[2])
ax.set_title("Stacked Bar Chart")
ax.set_xlabel("Time Periods")
ax.set_ylabel("Values")
ax.legend()
plt.show()
