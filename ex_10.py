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