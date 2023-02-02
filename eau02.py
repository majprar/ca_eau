def combi2():
    list = ""
    for x in range(0, 10):
        for y in range(0, 10):
            for z in range(x, 10):
                for w in range(y, 10):
                    if str(x + y) != str(z+w):
                        name = str(x) + str(y) + " " + str(z) + str(w)
                        list = list + name + ", "
    return list[0:-2]


print(combi2())