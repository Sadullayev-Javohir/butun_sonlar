"""Ikki xonali son berilgan. Uning raqamlar o'rnini almashtirishdan hosil bo'lgan
sonni aniqlovchi programma tuzilsin."""

num = int(input("Son kiriting: "))
firstNum = num // 10
secondNum = num % 10
if num <= 99:
    print(f"{num} <=> {secondNum}{firstNum}")
else:
    print("IKki xonali son kiriting!!")