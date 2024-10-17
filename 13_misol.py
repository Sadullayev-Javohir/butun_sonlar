"""Uch xonali son berilgan. Uning chapdan birinchi raqamini o'chirib o'ng tarafiga yozishdan hosil bo'lgan 
sonni aniqlovchi programma tuzilsin"""

num = int(input("Son kiriting: "))

firstNum = num // 100
secondNum = (num % 100) // 10
thirdNum = num % 10

print(f"{num} <=> {secondNum}{thirdNum}{firstNum}")