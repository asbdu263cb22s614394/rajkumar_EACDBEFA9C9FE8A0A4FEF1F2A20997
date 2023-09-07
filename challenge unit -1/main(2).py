#

def fact(n):
  if n==0 or n==1:
    return 1
  else:
    return n* fact(n-1)

number=int(input("enter a number1:"))
res=fact(number)

print("factorial of{}is{}.". format(number,res))