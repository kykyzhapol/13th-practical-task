#2
def fibonacci(n) -> list:
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