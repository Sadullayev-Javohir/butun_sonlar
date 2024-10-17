"""Kun boshidan boshlab N sekund vaqt o'tdi. Kun boshidan boshlab qancha minut va sekund o'tganligini aniqlovchi
programma tuzilsin."""

N = int(input("Sekund kiriting: "))

fullMin = N // 60
fullSecond = N % 60

print(f"Kun boshidan boshlab {N} sekund o'tdi. Kun boshidan boshlab {fullMin} min va {fullSecond} s o'tdi.")