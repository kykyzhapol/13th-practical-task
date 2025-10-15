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


special_offer()