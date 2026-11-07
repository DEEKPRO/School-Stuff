from math import sqrt
num = int(input("Enter a number to check if it is prime: "))

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
"""
li = []
for i in range(1,num+1):
    if num % i == 0:
        li.append(i)
if len(li) == 2:
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")
"""