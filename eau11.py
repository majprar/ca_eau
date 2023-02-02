import sys


if len(sys.argv) < 3 or any( i == "" for i in sys.argv):
    print("error")
    exit()


def indexwanted(table):
    table1 = table[0:-1]
    for i in table:
        if i != table[-1]:
            break
    else:
        result = 0
        return result
    for i in range(0, len(table1)):
        if table1[i] == table[-1]:
            return i + 1
    else:
        return -1


arg1 = sys.argv[1:]


print(indexwanted(arg1))
