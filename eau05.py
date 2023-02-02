import sys


try:
    int(sys.argv[1])
except ValueError:
    print("-1")
    exit()

if len(sys.argv) != 2 or int(sys.argv[1]) < 0:
    print("-1")
    exit()

def nbr1ersup(n):
    a = 0
    m = n + 1
    while a == 0:

        for i in range(2, m + 1):
            if i == m:
                a = 1
                break
            if m % i == 0 :
                break
        if a == 0:
            m = m + 1
    return m


indexnbr1er = int(sys.argv[1])


print(nbr1ersup(indexnbr1er))