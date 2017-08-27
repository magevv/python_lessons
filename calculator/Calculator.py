def calc(x, y, op):
    res = 0
    x = float(x)
    y = float(y)
    if op == '+':
        res = x + y
    elif op == '-':
        res = x - y
    elif op == '*':
        res = x * y
    elif op == '/':
        res = x / y
    return res


while True:
    data = input('Type formula like \'x + y\' or \'quite\' to exit: ')
    if data == 'quit':
        break
    o = data.split(' ')
    print(data, ' = ', calc(o[0], o[2], o[1]))