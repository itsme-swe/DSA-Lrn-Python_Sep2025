n = int(input("Enter the value of n: "))

num = n

count = 0

while num > 0:
    count += 1
    num = num // 10

print(f"Total number of digit is {count}")

"""
1️⃣ Never change your input, not an good practice.
2️⃣ To count the digits always use ( // ) floor division
3️⃣ Take count variable to store the current value of count and set it to 0.
"""