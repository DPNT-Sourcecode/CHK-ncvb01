

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    d = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0}

    for i in range(len(skus)):
        a = skus[i]
        if a not in d.keys():
            return -1
        else:
            d[a] += 1
    
    
    d["B"] = max(0, d["B"] - d["E"] // 2)
    paid_F = d["F"] - (d["F"] // 3)

    price = 0

    price += (d["A"] // 5) * 200
    d["A"] %= 5
    price += ((d["A"] // 3) * 130)
    d["A"] %= 3
    price += d["A"] * 50

    price += ((d["B"] // 2) * 45) + ((d["B"] % 2) * 30)
    price += d["C"] * 20
    price += d["D"] * 15
    price += d["E"] * 40
    
    return price


