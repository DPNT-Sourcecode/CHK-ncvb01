

# noinspection PyUnusedLocal
# skus = unicode string
def checkout(skus):
    d = {"A": 0, "B": 0, "C": 0, "D": 0, "E": 0, "F": 0, "G": 0, "H": 0, "I": 0, "J": 0, "K": 0, 
         "L": 0, "M": 0, "N": 0, "O": 0, "P": 0, "Q": 0, "R": 0, "S": 0, "T": 0, "U": 0, "V": 0,
         "W": 0, "X": 0, "Y": 0, "Z": 0}
    
    prices = {"A": 50, "B": 30, "C": 20, "D": 15, "E": 40, "F": 10, "G": 20, "H": 10, "I": 35,
              "J": 60, "K": 80, "L": 90, "M": 15, "N": 40, "O": 10, "P": 50, "Q": 30, "R": 50,
              "S": 30, "T": 20, "U": 40, "V": 50, "W": 20, "X": 90, "Y": 10, "Z": 50}
    
    group_items = ["S", "T", "X", "Y", "Z"]


    for i in range(len(skus)):
        a = skus[i]
        if a not in d.keys():
            return -1
        else:
            d[a] += 1
    
    
    d["B"] = max(0, d["B"] - d["E"] // 2)
    d["M"] = max(0, d["M"] - d["N"] // 3)
    d["Q"] = max(0, d["Q"] - d["R"] // 3)
    d["U"] -= (d["U"] // 4)
    paid_F = d["F"] - (d["F"] // 3)

    price = 0

    price += (d["A"] // 5) * 200
    d["A"] %= 5
    price += ((d["A"] // 3) * 130)
    d["A"] %= 3
    price += d["A"] * 50
    d["A"] = 0


    price += ((d["B"] // 2) * 45) + ((d["B"] % 2) * 30)
    d["B"] = 0

    price += (d["H"] // 10) * 80
    d["H"] %= 10
    price += ((d["H"] // 5) * 45)
    d["H"] %= 5
    price += d["H"] * 10
    d["H"] = 0

    price += (d["K"] // 2) * 150
    d["K"] %= 2
    price += d["K"] * 80
    d["K"] = 0


    price += (d["P"] // 5) * 200
    d["P"] %= 5
    price += d["P"] * 50
    d["P"] = 0


    price += (d["Q"] // 3) * 80
    d["Q"] %= 3
    price += d["Q"] * 30
    d["Q"] = 0


    if d["V"] >= 3:
        price += (d["V"] // 3) * 130
        d["V"] %= 3
    if d["V"] >= 2:
        price += (d["V"] // 2) * 90
        d["V"] %= 2
    price += d["V"] * 50

    group_counts = []

    for item in group_items:
        group_counts += [item] * d[item]
        d[item] = 0

    group_counts.sort(key=lambda x: -prices[x])
    while len(group_counts) >= 3:
        price += 45
        for _ in range(3):
            group_counts.pop(0)
    
    for item in group_counts:
        price += prices[item]

    for k in d:
        if k == "F":
            price += paid_F * 10
        elif k == "V":
            continue
        else:
            price += d[k] * prices[k]
    
    return price





