import logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s %(message)s')

quiet_logger = logging.getLogger('quiet_logger')
quiet_logger.setLevel(logging.WARNING)

def addition(numbers):
    logging.info(f"Dodaję: {', '.join(map(str, numbers))}")
    return sum(numbers)

def subtraction(numbers):
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

calculator = {
    '1': addition,
    '2': subtraction,
    '3': div,
    '4': multi,
}

def get_numbers(operation):
    numbers = []
    index = 1
    min_num = 2

    while True:
        num = input(f"Podaj składnik {index}. (lub wpisz 'q', aby zakończyć): ")

        if num.lower() == 'q' and len(numbers) < min_num:
            quiet_logger.warning(f"Musisz podać przynajmniej {min_num} liczby!")
            continue
        elif num.lower() == 'q':
            break

        try:
            num = float(num)
            numbers.append(num)
            index += 1
        except ValueError:
            print("To nie jest liczba. Spróbuj ponownie.")
        
        if operation in ['2', '4'] and len(numbers) == 2:
            break 
    return numbers

if __name__ == "__main__":
    operation = input(f"Podaj działanie, posługując się odpowiednią liczbą: 1 Dodawanie, 2 Odejmowanie, 3 Mnożenie, 4 Dzielenie: ")

    numbers = get_numbers(operation)

if operation in calculator:
    try:
        result = calculator[operation](numbers)
        print(f"Wynik: {result:.2f}")
    except ZeroDivisionError as x:
        print(f"Błąd: {x}")
else:
    logging.error("Niepoprawna operacja!")
    print("Niepoprawna operacja")