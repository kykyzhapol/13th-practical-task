#9
from datetime import datetime

def definition(cur_time_str):
    cur_time = datetime.strptime(cur_time_str, '%m/%d/%Y %H:%M:%S')
    year_start = datetime.strptime(f'01/01/{cur_time.year} 00:00:00', '%m/%d/%Y %H:%M:%S')
    return (cur_time - year_start).seconds

print(definition('01/01/2020 00:00:11'))