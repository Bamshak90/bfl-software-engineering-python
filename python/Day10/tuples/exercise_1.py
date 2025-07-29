response = (True, "welcome", ["email", "username"] )

print(type(response))

success,message,data = response
print(response)
#response= (False,) + response[1::]
response = list(response)
print(type(response))
response [0] = False
print(type(response), response)
response = tuple(response)
print(type(response), response)
print(len(response))



print(response[1] +  response[2][1])

 
a = (1, 2, 4, 5)
print(a[2] + a[3])

b = (1, "2", 3)
#print(b[0]+ b[1])
#print(b[1] + b[0])

print(b[2] * b[1])
print(b[1] * b[2])

print(a + b)
print(b + a)
success,message,data = response
print(response)

