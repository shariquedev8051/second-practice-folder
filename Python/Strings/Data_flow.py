# strings
s = 'string'
# print(s[::]) # To print string as it is
# print(s[::-1]) # to print string in reverse


# finding substring in a string
s = ' haveyoufoundsubstring '


def is_in_substring(s, sub):
    print("you have found substring" if sub in s else "substring not found")

# is_in_substring(s,'found')


# striping the spaces from a string
print(s.strip())
print(s.rstrip())
print(s.lstrip())


# Finding substring from the string
