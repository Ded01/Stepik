a = float(input('Введите второе число: '))
c = str(input('Введите вид операции:'))
b = float(input('Введите второе число: '))

if c == '+':
    print('Ответ: ', a + b)
elif c == '-':
    print('Ответ: ', a - b)
elif c == '*':
    print('Ответ: ', a * b)
elif c == 'mod' and b != 0:
    print('Ответ: ', a % b)
elif c == 'mod' and b == 0:
    print('Деление на 0!')
elif c == 'pow':
    print('Ответ: ', a ** b)
elif c == 'div' and b != 0:
    print('Ответ: ', a // b)
elif c == 'div' and b == 0:
    print('Ответ: ', 'Деление на 0!')
elif c == '/' and b != 0:
    print('Ответ: ', a / b)
elif c == '/' and b == 0:
    print('Деление на 0!')



# решение задачи из курса на https://stepik.org
