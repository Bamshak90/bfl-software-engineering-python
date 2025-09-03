

def fibonacci(n):
  a = 0
  b = 1
  #base case
  if n < 0:
    return "Invalid"
  elif n == 0:
    return 0 
  elif n == 1:
    return 1
  #recursive case
  else:
    for i in range(1, n):
      c = a + b
      a = b
      b = c 
    return b
print(fibonacci(9))


def fib(num):
  if num == 0:
    return []
  elif num == 1:
    return [num]
  series = [0,1]
  while len(series) < num:
    next_fib = series[-1] + series[-2]
    series.append(next_fib)
  return series
print(fib(10))

# mapping, filter, sorting and reduced 


#lambda
bio = lambda name: print(f"hello {name}")
bio("mark")

#mapping
def add_mark(score):
  return score + 10


exams_score = [20,29,40,50,60]
result = map(add_mark, exams_score)




print(list(result))


logic_lambda = map(lambda exam_score: exam_score + 10, exams_score)

print(list(logic_lambda))