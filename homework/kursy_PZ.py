import requests
import time
import csv


def exchange_rates():
    try:
        r = requests.get('http://api.nbp.pl/api/exchangerates/rates/A/eur')
        print('Data i godzina: ' + str(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())))
        print('Czas trwania zapytania: ' + str(r.elapsed.total_seconds()))
        r_dict = r.json()
        print('Kurs EURO: ' + str(r_dict.get('rates')[0].get('mid')))
    except requests.exceptions.Timeout:
        print('Spróbuj ponownie za chwilę')
    print('_____________________')

while True:
    exchange_rates()
    time.sleep(15)
