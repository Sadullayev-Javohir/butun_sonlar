"""A va B  (A > B) musbat sonlari. A kesmada B kesmani necha marta joylashtirish mumkin.
A kesmada B kesmaning joylashmagan qismini aniqlovchi dastur tuzing."""

A = int(input("Son kiriting: "))
B = int(input("Son kiriting: "))

divide = A / B
balance = A % B
if (A > B):
    print(f"{A}=A kesmada {B}=B kesmani {int(divide)} marta joylashtirish mumkin. Joylashmagan qismi {balance}")
else:
    print(f"{A}=A > {B}=B dan katta bo'lish kerak")