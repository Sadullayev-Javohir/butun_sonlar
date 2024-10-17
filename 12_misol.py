"""Uch xonali son berilgan. Uning raqamlarini teskari tartibda yozishdan hosil bo'lgan sonni aniqlovchi
programma tuzilsin."""

num = int(input("Son kiriting: "))

firstNum = num // 100
secondNum = (num // 10) % 10
thirdNum = num % 10

print(f"{num} <=> {thirdNum}{secondNum}{firstNum}")