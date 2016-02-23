def cents_to(cents):
    coins = [(5, 'nickels'), (10, 'dimes'), (25, 'quarters'), (100, 'dollars')]
    result = {}
    for value, name in coins:
        cents_to = cents
        if cents_to >= value:
            number_coin, cents_to = divmod(cents_to, value)
            result[name] = number_coin
    return result

while True:
    try:
        cents = int(input("Please enter the cents: "))
        if cents <= 0:
            break
        print cents_to(cents)
    except ValueError:
        print("Sorry, I didn't understand that.")
        continue
