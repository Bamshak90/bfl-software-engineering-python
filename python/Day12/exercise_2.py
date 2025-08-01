
items = ["apple", "soap", "biscuit"]
prices = [1000, 650, 270]





shopping1 = {
    items[0]: prices[0],
    items[1]: prices[1],
    items[2]: prices[2]
}

print(shopping1["apple"])



shopping = dict(zip(items, prices))
print(shopping)



