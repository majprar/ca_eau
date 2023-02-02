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


def tri_selec(array):
    minus = 0
    new_array = []
    for y in range(0, len(array) - 1):

        minus = y
        for x in range(y + 1, len(array) ):
            if int(array[x]) < int(array[minus]):
                minus = x
        if minus != y:
            array[y], array[minus] = array[minus], array[y]
    return " ".join(array)


arg1 = sys.argv[1:]


print(tri_selec(arg1))
