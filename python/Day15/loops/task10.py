posts = [
    {"post": "welcome"},
    {"post": "back"},
    {"post": "bring it on"}
]

for post in posts:
    if post["post"] == "welcome":
        print(post["post"])
        break
