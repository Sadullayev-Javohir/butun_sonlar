"""Uch xonali son berilgan. Uning o'ngdan birinchi raqamini o'chirib chap tarafiga yozishdan hosil bo'lgan
sonni aniqlovchi programma tuzilsin."""

num = int(input("Son kiriting: "))

firstNum = num // 100
secondNum = (num % 100) // 10
thirdNum = num % 10

print(f"{num} <=> {thirdNum}{firstNum}{secondNum}")