import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

def get_numbers():
    pass
def suma(numbers):
    pass
def minus(numbers):
    pass
def div(numbers):
    pass
def multi(numbers):
    pass
if __name__ == "__main__":
    pass

def get_numbers():
    numbers = []
    index = 1
    while len(numbers) < 2:
        try:
            num = input(f"Podaj składnik {index}. (lub wpisz 'q', aby zakończyć): ")
            if num.lower() == 'q':
                if len(numbers) < 2:
                    quiet_logger.warning("Musisz podać przynajmniej dwie liczby!")
                    continue
                break
            numbers.append(float(num))
            quiet_logger.info(f"Podaj składnik {index}: {num}")
            index += 1
        except ValueError:
            choice = input("To nie jest liczba. Wpisz 'q', aby zakończyć lub spróbuj ponownie: ")
            if choice.lower() == 'q':
                break
    return numbers

    if __name__ == "__main__":
    operation = input(f"Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")

    numbers = get_numbers()

    if operation == '1':
        print(f"Wynik: {suma(numbers)}")
    elif operation == '2':
        print(f"Wynik: {minus(numbers)}")
    elif operation == '3':
        print(f"Wynik: {multi(numbers)}")
    elif operation == '4':
        try:
            print(f"Wynik: {div(numbers)}")
        except ZeroDivisionError as x:
            print(f"Błąd: {x}")
    else:
        logging.error("Niepoprawna operacja!")
        print("Niepoprawna operacja")