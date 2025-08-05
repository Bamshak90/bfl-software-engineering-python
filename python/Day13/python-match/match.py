color = "blak"
match color:
    case "black":
        print("black")
    case "blue":
        print("blue")
    case "red":
        print("red")
    case "white":
        print("White")
    case _:
        print(f"No case match for {color}")


# using pipe 



day = "tues"

match day:
    case "mon" | "tues" | "wed" | "thurs" | "fri":
        print("A weekday")
    case "sat" | "sun":
        print("Ladies and gentlemen it's the weekend")
    case _:
        print("No match")


month = 5

days = 4

match days:
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in April")
    case 1 | 2 | 3 | 4 | 5 if month == 5:
        print("A weekday in May")
    case _:
        print("Day not found")
