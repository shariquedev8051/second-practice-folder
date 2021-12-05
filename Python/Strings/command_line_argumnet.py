from sys import argv
total = 0
for num in argv[1:]:  # argv[0] is file name so try to use argv[1] for operations
    total += int(num)

print(total)
