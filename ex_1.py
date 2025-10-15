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