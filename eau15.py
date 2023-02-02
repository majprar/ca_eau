import sys


if len(sys.argv) < 2 or "" in sys.argv:
    print("error.")
    exit()

def tri_bulleasccii(array):
    new_array = array
    for i in range(0,len(array)):
        for j in range(0,len(array) - 1):
            if ord(array[j][0]) > ord(array[j + 1][0]):
                array[j], array[j + 1] = array[j + 1], array[j]

    return " ".join(array)


arg1 = sys.argv[1:]


print(tri_bulleasccii(arg1))