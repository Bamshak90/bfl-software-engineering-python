#print("hello world")

#DRY in programming means do not repeat your self
# this is my first python script
# = is referred to as an assignment operator
# variables can start with letters and underscore but cannot start with numbers
# variables can store values of strings and numbers
# integar variables are variables that store numbers but negative and positive
# string variables are stored in qoutation marks(both single and double)
#variables cannot be defined with already defined keywords
#convert-to-int=int(time-to-micro-wave)
#minutes-in-second = 60

# import time
# print("cohort III micro-wave")
# print("1. open the micro-wave")

# print("2. put the rice")
# print("3. set time")

# customer = {}

# name = input("Enter your name: ")
# customer["name"] = name
# print(customer)
# time_to_micro_wave = int(input("Duration: \n"))
# customer["duration"] = time_to_micro_wave
# price_to_pay = time_to_micro_wave * 1000
# customer["amount"] = price_to_pay
# print("Your are charged ", price_to_pay)
# print("4. I will let you know when its ready in {} min(s) {}".format(time_to_micro_wave, name))
# time.sleep(time_to_micro_wave * 60)
# print("6. Your food is ready")
# print(customer)



import time

print(
  '''
  **************
  Cohort III Microwave 
  **************
  1. open the micro-wave
  2. put the rice
  3. set time
'''
)




customer = {}

name = input("Enter your name: \n >>>" )
customer["name"] = name

time_to_micro_wave = float(input("Enter the duration: \n >>>"))

customer["duration"] = time_to_micro_wave

price_to_pay = time_to_micro_wave * 1000

customer["amount"] = price_to_pay

print("You are charge {}".format(price_to_pay))

print("i will let you know when it ready in {} mins {}".format(time_to_micro_wave, name))

time.sleep(time_to_micro_wave * 60)

print("Congratulations {} your food is ready".format(name))


print(customer)
 



