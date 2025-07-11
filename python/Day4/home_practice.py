

pi = 3.1345
print(f"the value of pi to two decimal point is {pi:,.5f}")

#is_married = input("").lower()
#print(is_married.startswith("true"))

record = ("mark Jos 50000000.9 NG0921 bam YES")

record = record.split(" ")

salary = float(50000000.9)

print(
  '''
Salary slip
.................................
'''
)

print("FirstName: \t ", record[0].capitalize())
print("LastName: \t ", record[4].capitalize())

print(f"Monthly salary: ${salary:,.2f}" )
print("City: \t \t", record[1])
print("ID: \t \t ", record[3])
print("Valid ID:  \t", record[-1])

# secret message to decode for an agent


