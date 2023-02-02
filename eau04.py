import sys


if len(sys.argv) != 2:
    print ("error.")
    exit()

if int(sys.argv[1]) <= 0:
    print ("-1")
    exit()

try:
    int(sys.argv[1])
except ValueError:
    print("-1")
    exit()


def fibo_nterm(n):
    a=0
    b=1
    list = [0, 1]
    if n > 2:
        for i in range(0, n - 2):
            b = a + b
            a = b
            list.append(b)
    return list[n-1]


nterm = int(sys.argv[1])


resultat = fibo_nterm(nterm)


print(resultat)