import sys


if len(sys.argv) != 3:
    print("error.")
    exit()
if sys.argv[1] == "" or sys.argv[2] == "":
    print("error.")
    exit()


def strinstr(mot1,mot2):
    if len(mot1.split(mot2)) > 1:
        print("true")
    if len(mot1.split(mot2)) == 1:
        print("false")


arg1 = sys.argv[1]
arg2 = sys.argv[2]


strinstr(arg1, arg2)