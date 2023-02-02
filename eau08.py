import sys

if len(sys.argv) != 2 or not any(a.isalpha() for a in sys.argv[1]):
    print("error.")
    exit()

_count = 0
for i in sys.argv[1].strip():
    if i == " ":
        _count = _count + 1
    if i != " " :
       if  _count != 1 and _count != 4 and _count != 0:
        print("error.")
        exit()
       else:
           _count = 0

def uppfirstlowrest(mot):
    a = 0
    mot2 = ""
    for check in mot:
        if check == " " or not check.isalpha():
            mot2 = mot2 + check
            a = 0
        else:
            if a == 0:
                mot2 = mot2 + check.upper()
                a = 1
                continue
            if a == 1:
                mot2 = mot2 + check.lower()

                continue
    return mot2


arg = sys.argv[1]


print(uppfirstlowrest(arg))