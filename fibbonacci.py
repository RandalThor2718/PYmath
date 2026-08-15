upperbound = int(input("upperbound"))
# sets an upper limit for n in f(n) where f is the fibonacci function

def fibonacci(integer):
  if integer <= 1:
    return integer
  else:
    return fibonacci(integer-1) + fibonacci(integer-2)
    # computes fibonacci sequence

for i in range(1,upperbound):
  print(fibonacci(i))
# executes fibonacci
