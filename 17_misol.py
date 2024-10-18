"""999 dan katta bo'lgan son berilgan. Bir marta bo'lib butunni va bo'lib qoldiqni olish operatsiyasidan 
foydalanib berilgan sonni yuzliklar xonasidagi sonni aniqlovchi programma tuzilsin."""

num = int(input("Son kiriting: "))

# first = num // 1000
# four = num % 10

second = (num // 100) % 10
print(second)