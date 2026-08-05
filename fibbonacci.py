upperbound = int(input("upperbound"))

def fibonacci(integer):
  if integer <= 1:
    return integer
  else:
    return fibonacci(integer-1) + fibonacci(integer-2)

for i in range(1,upperbound):
  print(fibonacci(i))
