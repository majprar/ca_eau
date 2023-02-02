def combi3():
    list = ""
    for x in range(0, 10):
        for y in range(x, 10):
                for z in range(y, 10):
                    if y != z and x != y and x !=z:
                        name = str(x ) + str(y) + str(z)
                        list = list + name + ", "

    return list[0:-2]


print(combi3())