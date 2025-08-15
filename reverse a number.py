n = int(input("Enter a number: "))
reversed_number = 0
while n > 0:
    n1 = n % 10
    reversed_number = reversed_number * 10 + n1
    n //= 10
print("Reversed number is:", reversed_number)
