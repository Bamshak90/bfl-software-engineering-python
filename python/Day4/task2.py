#task 2

email = "user@domain.com"
new_mail = "gmail"

main_mail = email[0:5] + new_mail + email[11:]

print(main_mail)

#task2

word = "pythonista"
word_length = len(word)//2
#first_half, second_half = word[:len(word)// 2 + len(word)%2], word[len(word)// 2 + len(word)%2:]

first_half = word[:word_length]
second_half = word[word_length:]
print(first_half)
print(second_half)


