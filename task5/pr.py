def factors(n):
    p = 2
    f = list()
    while n >= p*p:
        if n % p == 0:
            f.append(p)
            n = int(n / p)
        else:
            p = p + 1
    f.append(n)
    return f


def is_prime(number):
    if number <= 1:
        return False
    for n in range(2, number):
        if number % n == 0:
            return False
    else:
        return True


def vowels(text):
    v = list()
    for i in text:
        if i in 'aeiouAEIOU':
            v.append(i)
    return v


# len() is builtin function to determine the length of a sequence. Write a unit test for len()
