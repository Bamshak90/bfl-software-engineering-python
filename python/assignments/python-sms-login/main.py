import time

time.sleep(0.3)
print("""
****************************************
|      Welcome to Smart SMS System     |
|--------------------------------------|
|  Dai  '*556#' to access your system  |
|  Type '0' to terminate the program   |
****************************************

""")

balance = 1000

system_access = input("Enter the code to proceed:\n>>>> ")
access_status = True

while access_status:
    if system_access == "1":
        time.sleep(0.5)
        print("""
==================== CODE MENU ====================
1. Check Balance
2. Buy Airtime
3. Buy Data
4. Borrow
0. Go Back
===================================================
""")
        user_code = int(input("What services are You choosing:\n>>>> "))

        if user_code == 1:
            time.sleep(0.5)
            print(f"Your available balance is ₦{balance:,}")

        elif user_code == 2:
            airtime_buy = int(input("How much airtime are you buying today?:\n>>>> "))
            if airtime_buy <= balance:
                balance -= airtime_buy
                time.sleep(0.5)
                print(f"✅ You have bought the airtime worth ₦{airtime_buy} and your new balance is ₦{balance:,}")
            else:
                time.sleep(0.5)
                print(f"❎ Insufficient funds from balance: ₦{balance:,}, \nPlease top up‼️‼️‼️")

        elif user_code == 3:
            print('''1. 1gb = 200 \n2. 2gb 500 \n3. 3gb 1000''')
            time.sleep(0.4)
            data_buy = int(input("How much data are you buying today?:\n>>>> "))
            if data_buy == 1:
                if 200 <= balance:
                    balance -= 200
                    print(f"✅ You have bought 1gb for ₦200")
                    time.sleep(0.5)
                    print(f"Your new balance is ₦{balance:,}")
                    break
                else:
                    print("❎ Insufficient balance. \nPlease top up‼️‼️‼️")
                    break
            if data_buy == 2:
                if 500 <= balance:
                    balance -= 500
                    print(f"✅ You have bought 2gb for ₦500")
                    time.sleep(0.5)
                    print(f"Your new balance is ₦{balance:,}")
                    break
                else:
                    print("❎ Insufficient balance. \nPlease top up‼️‼️‼️")
                    break
            if data_buy == 3:
                if 1000 <= balance:
                    balance -= 1000
                    print(f"✅ You have bought 3gb for ₦1000")
                    time.sleep(0.5)
                    print(f"Your new balance is ₦{balance:,}")
                    break
                else:
                    print("❎ Insufficient balance. \nPlease top up‼️‼️‼️")
                    break

        elif user_code == 4:
            print("""
==================== BORROW MENU ====================
1. Borrow Airtime
2. Borrow Data
3. Check Balance
0. Go Back
=====================================================
""")
            borrow_input = int(input("Choose an option:\n>>>> "))
            if balance > 0:
                print(f"❎ You still have ₦{balance:,} in your account. Spend it before borrowing.")
            else:
                if borrow_input == 1:
                    print("""
------ BORROW AIRTIME ------
1. ₦100 (repay ₦126)
2. ₦300 (repay ₦378)
3. ₦500 (repay ₦630)
4. ₦800 (repay ₦1000)
0. Cancel
""")
                    choice = int(input("How much airtime do you want to borrow?:\n>>>> "))
                    borrow_airtime_map = {
                        1: (100, 126),
                        2: (300, 378),
                        3: (500, 630),
                        4: (800, 1000)
                    }
                    if choice in borrow_airtime_map:
                        amount, repay_amount = borrow_airtime_map[choice]
                        balance -= repay_amount 
                        print(f"✅ You have borrowed ₦{amount}. You must repay ₦{repay_amount}.")
                        print(f"Your new balance is ₦{balance:,}")
                    elif choice == 0:
                        print("Borrow cancelled.")
                    else:
                        print("❎ Invalid choice.")

                elif borrow_input == 2:
                    print("""
------ BORROW DATA ------
1. 1GB (worth ₦200, repay ₦252)
2. 2GB (worth ₦500, repay ₦630)
3. 3GB (worth ₦800, repay ₦1000)
0. Cancel
""")
                    choice = int(input("How much data do you want to borrow?:\n>>>> "))
                    borrow_data_map = {
                        1: (200, 252, "1GB"),
                        2: (500, 630, "2GB"),
                        3: (800, 1000, "3GB")
                    }
                    if choice in borrow_data_map:
                        amount, repay_amount, size = borrow_data_map[choice]
                        balance -= repay_amount
                        print(f"✅ You have borrowed {size} data (worth ₦{amount}). You must repay ₦{repay_amount}.")
                        print(f"Your new balance is ₦{balance:,}")
                    elif choice == 0:
                        print("Borrow cancelled.")
                    else:
                        print("❎ Invalid choice.")

                elif borrow_input == 3:
                    print(f"Your current balance is ₦{balance:,}")

                elif borrow_input == 0:
                    print("Going back...")

    else:
        print("Wrong pin")
        break
