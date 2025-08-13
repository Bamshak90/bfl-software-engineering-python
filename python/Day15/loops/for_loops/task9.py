'''

Task
1. print the customer name and total price for orders with 5 or more items.
2. skip orders with total_price between 140 and 200
3. if any total_price is greater tha 500, stop the loop.

'''

orders = [
   {"order_id": 101, "customer": "John", "items": 3, "total_price": 75},
   {"order_id": 102, "customer": "Mary", "items": 10, "total_price": 180},
   {"order_id": 103, "customer": "Alex", "items": 2, "total_price": 50},
  {"order_id": 104, "customer": "Grace", "items": 15, "total_price": 600},
  {"order_id": 105, "customer": "Paul", "items": 5, "total_price": 145}
  ]


for order in orders:
    if order["total_price"] > 500:
        break
    if order["total_price"] >= 140 and order["total_price"] <= 200:
        continue
    if order["items"] >= 5:
        print(order)

