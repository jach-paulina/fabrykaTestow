import random

wynik = 0
while wynik < 5:
    liczba = random.randint(1, 42)
    print('Twój szczesliwy numerek', liczba)
    wynik += 1
