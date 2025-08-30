tithes = [1000,100,2000,2500,3000]

def total(amount):
    total_amount = 0
    for cash in amount:
        total_amount = total_amount + cash
    print(f"total amount is:{total_amount}")
    return total_amount


def calculate_percent(total):
    return total * 10/100

value = total(tithes)
calculate_percent(value)
