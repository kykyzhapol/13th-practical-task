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
