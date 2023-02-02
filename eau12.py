import sys

if len(sys.argv) < 3:
    print("error.")
    exit()

try:
    for x in range(1, len(sys.argv)):
        int(sys.argv[x])
except ValueError:
    print("error.")
    exit()


def minabs(tableau):
    diffmin = 0
    diffmin0 = 0
    count = 0
    for i in tableau:
        for j in tableau[(tableau.index(i) + 1):]:

                diffmin = int(i) - int(j)
                if diffmin < 0:
                    diffmin = diffmin * (-1)
                if count == 0:
                    diffmin0 = diffmin

                if diffmin < diffmin0:
                    diffmin0 = diffmin
                count = count + 1

    else:
        return diffmin0


arg1 = sys.argv[1:]


print(minabs(arg1))
