import numpy as np

# Using arange() function
A = np.arange(1, 8, 1)
print("Arange function: ",A)

# Using linespace() function
B = np.linspace(1, 7, 7, dtype = int)
print("Linespace function: ", B)

# Using logspace() function
C = np.logspace(1, 2, 7, dtype = int)
print("Logspace function: ", C)

# Using random.rand() function
D = np.random.rand(1, 7)
print("Rand function: ", D)