import json


store = {
  "laptop": {"price": 1200, "quantity": 6},
  "headphones": {"price": 1200, "quantity": 6},
  "mouse": {"price": 1200, "quantity": 6}
}


def start():
  while True:
    print('''
===========================
Welcome to our online store
1. Add Product
2. Update Stock
3. Sell Products
4. Display Store Products.
5. Display Most expensive Product
6. Display Total Sales
7. Exit
''')
    
    user_choice = int(input("Choose an option: "))

    if user_choice == 7:
      print("Thank you for checking in")
      break
    call_function(user_choice)
def call_function(user_choice):
  if user_choice == 1:
    add_product()
  elif user_choice == 2:
    update_product()
  elif user_choice == 3:
    sell_product()
  elif user_choice == 4:
    display_store()
  elif user_choice == 5:
    most_expensive_item(store)
  elif user_choice == 6:
    total_sales()



def add_product():
  item = input("Enter item name: ").lower()
  price = int(input("Enter item price: "))
  quantity = int(input("Enter quantity: "))

  if item in store:
    print(f"{item} already exist.")
  else:
    store[item] = {"price": price, "quantity": quantity}
    print(f"{item} has been added successfully")
    print(store)
    return store


def update_product():
  item = input("Enter item name to update: ")
  if item in store:
    price = int(input("Enter new price: "))
    quantity = int(input("Enter new quantity: "))
    store[item] = {"price": price, "quantity": quantity}
    print(store)
    return store
  else:
    print(f"{item} does not exist")

def sell_product():
  item = input("what are you buying?: ")
  if item in store:
    quantity = int(input(f"How many {item} are you buying?: "))
    if store[item]["quantity"] < quantity:
      print(f"Not enough {item} in store.")
      return store
    else:
      store[item]["quantity"] -= quantity
      total_price = store[item]["price"] * quantity
      print(f"you have bought {item} in buck of {quantity} for the price of {total_price}")
      print(store)
      return store
  else:
    print(f"{item} does not exist")

def display_store():
  print(store)
  return store

def most_expensive_item(store):
    total = 0
    expensive_item = None

    for item in store:
        price = store[item]["price"] 

        if price > total: 
            total = price
            expensive_item = item 
    print(expensive_item, total) 
    return total

def total_sales():
  total = 0
  for item in store:
    price = store[item]["price"]
    quantity = store[item]["quantity"]
    total += price * quantity
  print(total)
  return total
  
start()