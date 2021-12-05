n = int(input('Enter a number:- '))
# for i in range(1, n + 1):
#     for j in range(1, n + 1):
#         print(chr(64 + n + 1 - i), end='')
#     print()

for i in range(1, n + 1):
    print(" " * (n - i), '*' * (2 * i - 1), end=' ')
    print()
