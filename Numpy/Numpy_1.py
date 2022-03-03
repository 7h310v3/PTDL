#6
import numpy as np

#Ham tinh tong
def tong(x, y):
    if (y == 1):
        return x[0];
    else:
        return x[y - 1] + tong(x, y - 1);

def main():
    A = np.random.rand(15, 17);
    print("Ma tran A: \n", A);

    #A = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
    #print("Ma tran A: \n", A);

    print("\nTong theo hang: \n", np.apply_along_axis(tong, 1, A, len(A)));
    print("\nTong theo cot: \n", np.apply_along_axis(tong, 0, A, len(A)));

if __name__ == '__main__':
    main();