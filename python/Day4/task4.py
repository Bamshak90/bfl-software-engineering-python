# Question one

record = ("james Abuja 150000.5 NG0921")

record_list = record.split(" ")
Salary = float(record_list[2])
print("Salary Slip")
print("---------------------")
print(record_list)
print("Name: \t \t",record_list[0].capitalize())
print("Initial: \t", record[0].capitalize())
print("ID: \t \t", record_list[3])
print("VALID ID: \t YES")
print(f"Monthly Salary:  ${Salary:,.2f}")

# Question 2

message = "GhostNet#X44CR#98.654#TRC8821"

print('''
      Alert Report
      -----------------------
    ''')

print("Code Name: \t", message[0:8])
print("message Code: \t", message[9:14])
print("Last Letter: \t", message[13])
print("Trace ID: \t", message[22:])
print("Traceable: \t YES")
print("Severity Level:", message[15:20])
