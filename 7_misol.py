"""Ikki xonali son berilgan. Uning raqamlari yig'indisini aniqlovchi programma tuzilsin."""

num = int(input("Son kiriting: "))
firstNum = num // 10
secondNum = num % 10
add = firstNum + secondNum
print(f"{firstNum} + {secondNum} = {add}")