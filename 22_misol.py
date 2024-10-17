"""Kun boshidan boshlab N sekund vaqt o'tdi. Kun boshidan boshlab qancha soat va sekund o'tganini aniqlovchi 
programma tuzilsin."""

N = int(input("Sekund kiriting: "))

fullHour = N // 60 // 60
fullSecond = N % 60

print(f"Kun boshidan boshlab {N} sekund vaqt o'tdi. Kun boshidan boshlab {fullHour} soat va {fullSecond} sekund o'tdi.")

