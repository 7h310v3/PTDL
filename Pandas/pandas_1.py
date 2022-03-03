# 3
import pandas as pd
import numpy as np


def main():
    #A = np.arange(1, 8, 1);
    #b = [];

    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print(A)
    print("\n", A.T)
    print("\n", np.transpose(A))

if __name__ == '__main__':
    main();