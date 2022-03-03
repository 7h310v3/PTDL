import pandas as pd
import numpy as np

A = np.arange(1, 8, 1)
print(A)

s = pd.Series(np.random.rand(7), A, int)

print(s)