posts = [
    {"id": 1,
     "post": "Just found out my fridge has a light. Game changer!",
     "author": "Tom",
     "likes": 120,
     "tags": ["cudding", "humor", "coffe"]

     },

    {"id": 2,
     "post": "Just found out my fridge has a light. Game changer!",
     "author": "Tom",
     "likes": 120,
     "tags": ["cudding", "humor", "coffe"]

     },
   {"id": 3,
     "post": "Just found out my fridge has a light. Game changer!",
     "author": "Tom",
     "likes": 120,
     "tags": ["cudding", "humor", "coffe"]

     }
]


user_input = int(input("Enter ID: "))

flag = None

for post in posts:
    if user_input == post["id"]:
        flag = post
        print(flag)
        break
else:
    print("id not found")
