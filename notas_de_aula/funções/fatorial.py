def fatorial(n):
    if n < 0:
        raise TypeError("n não pode ser negativo")
    if n == 0:
        return 1
    return n * fatorial(n - 1)
