import sys


if len(sys.argv) != 2 or sys.argv[1] == "":
    print("error.")
    exit()


def checkint(entré):
    try:
        int(entré)
        result = "true"
        return result
    except ValueError:
        result = "false"
        return result


arg = sys.argv[1]

print(checkint(arg))
