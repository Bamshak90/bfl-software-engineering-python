posts = [
    {"post": "welcome"},
    {"post2": "back"},
    {"post3": "bring it on"}
]

for post in posts:
    if post["post"] == "welcome":
        print(post["post"])
        break
else:
    print("not found")
