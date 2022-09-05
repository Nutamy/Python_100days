def add(*numbers):
    sum_of_numbers = 0
    for number in numbers:
        sum_of_numbers += number
    return sum_of_numbers

print(add(1, 2, 3, 4, 7, 8, 2, 2, 2))

def calc(n, **kwargs):
    n += kwargs["add"]
    n *= kwargs["mult"]
    return n

print(calc(3, add=4, mult=7))
