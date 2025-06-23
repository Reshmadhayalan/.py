def is_tech_number(num):
    s = str(num)
    if len(s) % 2 != 0:
        return False
    mid = len(s) // 2
    return (int(s[:mid]) + int(s[mid:])) ** 2 == num

num = int(input("Enter number: "))
print("Tech Number" if is_tech_number(num) else "Not a Tech Number")
