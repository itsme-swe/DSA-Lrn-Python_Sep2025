n = int(input("Enter the number: "))

num = n

result = 0

while num > 0:
    lst_digit = num % 10
    result = (result * 10) + lst_digit
    num = num // 10

if n == result:
    print("It's palindrome")
else:
    print("Not Palindrome")

"""
1️⃣ Palindrome is if we check number or alphabet from left to right or right to left, if it is same then it is palindrome.
2️⃣ Never convert the type of the number to string if need to check number is palindrome or not.
3️⃣ 
"""