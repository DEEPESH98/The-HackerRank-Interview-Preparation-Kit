def leftRotate(arr, n, k):
    # To get the starting point of rotated array
    mod = k % n
    s = ""

    # Prints the rotated array from start position
    for i in range(n):
        print(str(arr[(mod + i) % n]),end=" ");

    return


# Driver program
a, k = input().split()
arr = list(map(int, input().rstrip().split()))
n = len(arr)

leftRotate(arr, n, int(k))

