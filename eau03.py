import sys

if len(sys.argv) == 1:
    print("error.")
    exit()


def retourneur(argument):
    for a in range(1, len(argument) + 1):
        print(argument[-a])

chaine = sys.argv[1:]


retourneur(chaine)