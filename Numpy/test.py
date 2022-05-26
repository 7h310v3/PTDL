# 6
import numpy as np


# Ham tinh tong le
def tongle(x):
    s = 0
    for i in x:
        if (i % 2 != 0):
            s += i;
    return s;


def main():
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Ma tran A: \n", A);

    print("\nTong le theo hang: \n", np.apply_along_axis(tongle, 1, A));
    print("\nTong le theo cot: \n", np.apply_along_axis(tongle, 0, A));


if __name__ == '__main__':
    main();
