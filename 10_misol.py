"""Uch xonali son berilgan. Oldin uni birliklar xonasidagi raqamni so'ng o'nliklar xonasidagi raqamni chiqaruvchi programma tuzilsin.
"""

num = int(input("Son kiriting: "))

birliklarXonasi = num % 10
onliklarXonasi = (num % 100) - birliklarXonasi
# yuzlarXonasi = num - (onliklarXonasi + birliklarXonasi)

print(f"Birliklar xonasi: {birliklarXonasi}, O'nliklar xonasi: {onliklarXonasi}")
