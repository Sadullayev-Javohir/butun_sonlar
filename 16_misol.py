"""Uch xonali son berilgan. Uning o'nliklar xonasidagi raqam bilan birliklar xonasidagi raqamni almashtirishdan
hosil bo'lgan sonni aniqlovchi programma tuzilsin. (Kirish=123; Natija=132)"""

num = int(input("Son kiriting: "))

firstNum = num // 100
secondNum = (num % 100) // 10
thirdNum = num % 10

print(f"{num} <=> {firstNum}{thirdNum}{secondNum}")