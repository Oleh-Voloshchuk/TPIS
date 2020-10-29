# print built-in constants
a1 = True
print(a1)
a2 = None
print(a2, '\n')
# print built-in funcs
print(f" abs(-99) є рівним {abs(-99)}")
print(f" hex(17) є рівним {hex(17)}")
# using compound statements(if and while)
a = -5
while a != 0:
    print(a)
    a += 1
a = -5
while a != 15:
    if a <= 5 and a >= 0:
        pass
    elif a < 0:
        print(abs(a))
    else:
        print(a ** 2)
    a += 1
# using try blocks
A = 'sds'
try:
    print('Що буде якщо', A + 10, "?")
except Exception as e:
    print(e)
finally:
    print("А вот воно що!")

# using with
with open("README.md", 'r') as my_file:
    print(my_file.read(256))
# using lambda
arr = list(range(0, 10, 3))
arr1 = list(map(lambda x: x**2, arr))
print(arr1, "\n")
