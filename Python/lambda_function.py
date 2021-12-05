
# def is_bigger(x, y): return True if x > y else False

# print('x is bigger than y' if is_bigger(20, 30) else 'Y is bigger than X')

def power(n):
    return lambda x: x * n


square = power(2)
cube = power(3)
print(square(4))
print(cube(4))
