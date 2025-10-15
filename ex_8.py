#8th
from datetime import datetime

def time_format(time_taking):
    '''
    ValueError
    :param time_taking:
    :return:
    '''


    try:
        time_fom = datetime.strptime(time_taking, '%m/%d/%Y %H:%M:%S')
        print(time_fom.strftime('%d.%m.%y %I:%M %p %S'))
    except ValueError:
        print('Ошибка в значении времени')
    pass