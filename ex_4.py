#4th
def make_payment(p):
    try_again = 'Повторите попытку'
    success = 'Успех'
    if p is not float or int:
        print(try_again)
    elif p < 20:
        print(try_again)
    elif p>1000:
        print(try_again)
    else:
        print(success)