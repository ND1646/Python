import matplotlib.pyplot as plt

# Data points
x = [1, 2, 3, 4, 4]
y = [2, 4, 6, 3, 4]

# Plotting the line
plt.plot(x, y, color="red")  # Fixed 'clour' to 'color'

# Saving the figure
plt.savefig("line1.png", transparent=False, facecolor="blue")  # Fixed 'sauefig', file name, etc.

# Displaying the chart
plt.show()
