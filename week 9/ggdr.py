import matplotlib.pyplot as plt

# Data
output = [0, 20, 60, 150, 260, 350, 420, 455, 420, 375, 300]
marginal_product = [20, 40, 90, 110, 90, 70, 35, -35, -45, -75]

# Plotting
plt.plot(output, marginal_product, marker='o', linestyle='-')
plt.xlabel('Output')
plt.ylabel('Marginal Product')
plt.title('Marginal Product Curve')
plt.grid(True)
plt.show()
