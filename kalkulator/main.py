#To jest mój pierwszy kalkulator w Python

import kalkulator

opcja = input("Wpisz jakie działanie chcesz wykonać: suma/różnica/iloczyn/iloraz: ")

print("Podaj liczbe 1 i kliknij enter: ")
liczba1 = int(input())

print("Podaj liczbe 2 i kliknij enter: ")
liczba2 = int(input())

if opcja == "suma":
  print("Gratulacje ! Twój wynik to:")
  kalkulator.suma(liczba1, liczba2)
elif opcja == "roznica":   
  print("Gratulacje ! Twój wynik to:")
  kalkulator.roznica(liczba1, liczba2)
elif opcja == "iloczyn":   
  print("Gratulacje ! Twój wynik to:")
  kalkulator.iloczyn(liczba1, liczba2)
elif opcja == "iloraz":   
  print("Gratulacje ! Twój wynik to:")
  kalkulator.iloraz(liczba1, liczba2)
else:
  print("Ogarnij sie!")
