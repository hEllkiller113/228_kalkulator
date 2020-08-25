alysm = """
1. +
2. -
3. /
4. *
5. //
6. **
7. %
8. exit
"""
print(alysm)
index = input("enter a number: ")

if index == "1":
   a = int(input("введите первое число: "))
   b = int(input("введите второе число: "))
   print("{} + {} = {}".format(a, b, a + b))
elif index == "2":
    a = int(input("введите первое число: "))
    b = int(input("введите второе число: "))
    print("{} - {} = {}".format(a, b, a - b))
elif index == "3":
    a = int(input("введите первое число: "))
    b = int(input("введите второе число: "))
    print("{} / {} = {}".format(a, b, a / b))
elif index == "4":
    a = int(input("введите первое число: "))
    b = int(input("введите второе число: "))
    print("{} * {} = {}".format(a, b, a * b))
elif index == "5":
    a = int(input("введите первое число: "))
    b = int(input("введите второе число: "))
    print("{} // {} = {}".format(a, b, a // b))
elif index == "6":
    a = int(input("введите первое число: "))
    b = int(input("введите второе число: "))
    print("{} ** {} = {}".format(a, b, a ** b))
elif index == "7":
    a = int(input("введите первое число: "))
    b = int(input("введите второе число: "))
    print("{} % {} = {}".format(a, b, a % b))
if index == "8":
    print("bye")

