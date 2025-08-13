
flag = False

for number in range(1,10):
    if number == 4:
        flag = True
        break
if flag:
    print(number)
else:
    print("number not found")



names = ["Tom", "Jerry", "Mimi", "val"]


user_name = input("Enter name: ").capitalize()
flag = False
for name in names:
    if user_name == name:
        flag = True
        break


if flag:
    print("vip")


else:
    print("regular")
