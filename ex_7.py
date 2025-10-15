#7
def common_multiples(A, B, N) -> list:
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