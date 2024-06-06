#1. Write a function `is_prime(n: int) -> bool` that checks if a given number is prime.

n = int(input())

factors = 0 

for i in range(1,n+1):
    if n % i == 0:
        factors += 1 
if factors == 2:
    print("Given number is Prime")
else:
    print("Given Number is Not Prime Number")
        