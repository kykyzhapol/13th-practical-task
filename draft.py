'''
#1st

def rus_count(text):
    consonants = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с',
                  'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']
    vowels = ['а', 'о', 'у', 'э', 'и', 'ы', 'е', 'ё', 'ю', 'я']

    sum_cons = 0
    sum_vow = 0
    for let in text:
        if let in consonants:
            sum_cons += 1
        elif let in vowels:
            sum_vow += 1
        else:
            continue

    print(f'sum of consonants: {sum_cons}, sum of vowels: {sum_vow}')


#2
def fibonacci(n):
    if n<1:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]
    else:
        fib_list = [1, 1]
        for i in range(2, n):
            fib_list.append(fib_list[i-1]+fib_list[i-2])
        return fib_list

print(fibonacci(10))

#3rd

def sales(price, disc_card, day_off) -> float:
    discount = 0
    match disc_card:
        case False:
            pass
        case True:
            discount += 0.05

    match day_off:
        case True:
            discount += 0.03
        case False:
            pass

    price_disc = 0
    if 5000 < price <= 15000:
        price_disc = (price - 5000) * 0.03
    elif price <= 20000:
        price_disc = (price - 15000)*0.05 + 0.03*10000
    elif price <= 30000:
        price_disc = 0.03*10000 + 0.05*5000 + (price - 20000)*0.07
    elif price > 30000:
        price_disc = 0.03*10000 + 0.05*5000 + 10000*0.07 + (price - 30000)*0.1
    else:
        pass

    discount += price_disc/price

    if discount <= 0.15:
        return round(price * discount, 2)
    return round(price * 0.15, 2)


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

#5th

def special_offer():
    duty_text = 'Денежный эквивалент вашей карты с учетом бонусов: '
    card_price = int(input('Стоимость вашей карты -->'))

    match card_price:
        case 5:
            print(f'{duty_text}{card_price}$')
        case 10:
            print(f'{duty_text}{card_price}$')
        case 25:
            print(f'{duty_text}{card_price+3}$')
        case 50:
            print(f'{duty_text}{card_price+8}$')
        case 100:
            print(f'{duty_text}{card_price+20}$')
        case _:
            print('Вы неправильно ввели стоимость вашей карты')

#6th
def sms_len(text) -> str:
    try:
        return str(text)[:160]
    except:
        return 'Data error'


#7

def common_multiples(A, B, N):
    """
    function for search common multiples
    """

    #calculate GCD
    b = B
    a = A
    while b != 0:
        a, b = b, a % b
    else:
        gcd = a

    lcm = A * B // gcd

    # Adding multiples in list
    result = []
    multiple = lcm
    while multiple <= N:
        result.append(multiple)
        multiple += lcm

    return result


#Example
A, B, N = 4, 6, 50
multiples = common_multiples(A, B, N)
print(f"Общие кратные {A} и {B} до {N}: {multiples}")


#8th
from datetime import datetime

def time_format(time_taking):

    #ValueError
    #:param time_taking:
    #:return:

    #DD.MM.YY HR:MIN:SEC



    try:
        time_fom = datetime.strptime(time_taking, '%m/%d/%Y %H:%M:%S')
        print(time_fom.strftime('%d.%m.%y %I:%M %p %S'))
    except ValueError:
        print('Ошибка в значении времени')
    pass


#9
from datetime import datetime

def definition(cur_time_str):
    cur_time = datetime.strptime(cur_time_str, '%m/%d/%Y %H:%M:%S')
    year_start = datetime.strptime(f'01/01/{cur_time.year} 00:00:00', '%m/%d/%Y %H:%M:%S')
    return (cur_time - year_start).seconds

print(definition('01/01/2020 00:00:11'))


#10

def range_ab(a, b):
    numbers = {1,3,4,8,9}
    exit_n = set()
    if a>b: a, b = b, a

    for n in range(a, b+1):
        for nn in str(n):
            if int(nn) in numbers:
                exit_n.add(n)
                continue

    print(*exit_n)

range_ab(100, 20)

#11th

def simple_n(n) -> bool:
    if n == 1 or n == 0: return False
    root_n = int(n**0.5)+1
    for div in range(2, root_n):
        if n % div == 0:
            return False
    return True

N = int(input('Введите простое число -->'))
simple_list = []

for between in range(N+1):
    if simple_n(between):
        simple_list.append(between)


print(*simple_list)
'''

#12th
