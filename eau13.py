import sys


if len(sys.argv) < 3:
    print("error")
    exit()

try:
    for x in sys.argv[1:]:
        int(x)
except ValueError:
    print("error")
    exit()


def tri_bulle(array):
    new_array = array
    for i in range(0,len(array)):
        for j in range(0,len(array) - 1):
            if int(array[j]) > int(array[j+1]):
                array[j], array[j + 1] = array[j+1], array[j]

    return " ".join(array)



arg1 = sys.argv[1:]


print(tri_bulle(arg1))