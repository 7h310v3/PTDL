#6
import numpy as np

#Ham tinh tong le
def tong(x, y):
    if (y == 1):
        if (x[0] % 2 != 0):
            return x[0];
        else:
            return 0;
    if (x[y-1] % 2 != 0):
        return x[y - 1] + tong(x, y - 1);
    else:
        return tong(x, y - 1) + 0;

def main():
    A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    print("Ma tran A: \n", A);

    print("\nTong le theo hang: \n", np.apply_along_axis(tong, 1, A, len(A)));
    print("\nTong le theo cot: \n", np.apply_along_axis(tong, 0, A, len(A)));

if __name__ == "__main__":
    main();