import sys


if len(sys.argv) != 3 or sys.argv[1] == sys.argv[2]:
    print("error.")
    exit()

try:
    int(sys.argv[1])
    int(sys.argv[2])
except ValueError:
    print("error.")
    exit()


def minmax(a,b):
    if a < b :
        num1, num2 = b, a
    else:
        num1, num2 = a, b
    result = ""
    for i in range(num2,num1):
        result = result + str(i) + " "
    return result


arg1, arg2 = int(sys.argv[1]), int(sys.argv[2])


print(minmax(arg1, arg2))

