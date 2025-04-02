

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    d = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0}

    for i in range(len(skus)):
        a = skus[i]
        if a not in d.keys():
            return -1
        else:
            d[a] += 1
    
    price = 0
    d["B"] -= d["E"] // 2
    price += d["C"] * 20
    price += d["D"] * 15
    price += ((d["A"] // 3) * 130) + ((d["A"] % 3) * 50)
    price += ((d["B"] // 2) * 45) + ((d["B"] % 2) * 30)
    return price




