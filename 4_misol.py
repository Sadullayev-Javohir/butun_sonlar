"""A va B (A > B) musbat sonlar berilgan. A kesmada B kesmani necha marta joylashtirish
mumkinligini aniqlovchi dastur tuzing."""

A = int(input("son kiriting: "))
B = int(input("son kiriting: "))

divide = A / B

if (A > B):
    print(f"{A}=A kesmada {B}=B kesmani {divide} marta joylashtirish mumkin.")
else:
    print(f"{A}=A > {B}=B dan katta bo'lish kerak")