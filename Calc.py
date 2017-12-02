a = float(input())
b = float(input())
c = str(input())

if c == '+':
    print(a + b)
elif c == '-':
    print(a - b)
elif c == '*':
    print(a * b)
elif c == 'mod' and b != 0:
    print(a % b)
elif c == 'mod' and b == 0:
    print('Деление на 0!')
elif c == 'pow':
    print(a ** b)
elif c == 'div' and b != 0:
    print(a // b)
elif c == 'div' and b == 0:
    print('Деление на 0!')
elif c == '/' and b != 0:
    print(a / b)
elif c == '/' and b == 0:
    print('Деление на 0!')
