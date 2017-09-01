def calc(x, y, op):
    res = 0
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
    elif data == '':
        continue
    o = data.split(' ')
    try:
        x = float(o[0])
        y = float(o[2])
        print('{0} = {1}'.format(data, calc(x, y, o[1])))
    except ValueError:
        print('Please, use numeric values for operands.')
