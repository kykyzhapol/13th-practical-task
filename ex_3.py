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