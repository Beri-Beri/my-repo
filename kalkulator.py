import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

quiet_logger = logging.getLogger('quiet_logger')
quiet_logger.setLevel(logging.WARNING)


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

def addition(numbers):
    logging.info(f"Dodaję: {', '.join(map(str, numbers))}")
    return sum(numbers)

def substraction(numbers):
    logging.info(f"Odejmuję: {', '.join(map(str, numbers))}")
    result = numbers[0]
    for no in range(1, len(numbers)):
        result -= numbers[no]
    return result

def div(numbers):
    if 0 in numbers[1:]:
        logging.error("Błąd: Dzielenie przez zero")
        raise ZeroDivisionError("Nie można dzielić przez zero")

    logging.info(f"Dzielę: {', '.join(map(str, numbers))}")
    result = numbers[0]
    for no in range (1, len(numbers)):
        result /= numbers[no]
    return result

def multi(numbers):
    logging.info(f"Mnożę: : {', '.join(map(str, numbers))}")
    result = 1
    for no in numbers:
        result *= no
    return(result)

if __name__ == "__main__":
    operation = input(f"Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")

    numbers = get_numbers()

    if operation == '1':
        print(f"Wynik: {addition(numbers)}")
    elif operation == '2':
        print(f"Wynik: {substraction(numbers)}")
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