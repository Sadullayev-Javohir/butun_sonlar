"""Ikki xonali son berilgan. Oldin uning o'nliklar xonasidagi raqamni, so'ng birlar xonasidagi
raqamni chiqaruvchi programma tuzilsin."""

num = int(input("Son kiriting: "))
small = num % 10
big = num - small
if num <= 99:
    print(f"o'nlar xonasi: {big}, birlar xonasi: {small}")
else:
    print(f"faqat ikki xonali son kiriting.")