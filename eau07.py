import sys

if len(sys.argv) != 2 or sys.argv[1] == "":
    print("error.")
    exit()
if not any(a.isalpha() for a in sys.argv[1]):
    print("error")
    exit()

def upplowstep2(mot):
    a = 0
    mot2 = ""
    for check in mot:
        if check == " " or not check.isalpha():
            mot2 = mot2 + check
        else:
            if  a == 0:
                mot2 = mot2 + check.upper()
                a = 1
                continue
            if a == 1:
                mot2 = mot2 + check.lower()
                a = 0
                continue
    return mot2


arg1 = sys.argv[1]


print(upplowstep2(arg1))