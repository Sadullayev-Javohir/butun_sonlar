"""Uch xonali son berilgan. Uning raqamlar yig'indisini aniqlovchi programma tuzilsin."""

num = int(input("Son kiriting: "))

firstNum = num // 100
secondNum = (num % 100) // 10
thirdNum = num % 10


add = firstNum + secondNum + thirdNum

print(f"{firstNum} + {secondNum} + {thirdNum} = {add}")
