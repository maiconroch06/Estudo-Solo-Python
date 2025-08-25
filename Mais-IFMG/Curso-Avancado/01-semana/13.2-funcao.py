def fat(num):
    if num <= 1:
        return 1
    return num * fat(num - 1)

n = int(input('Informe um número: '))
print('O fatorial de', n, 'é', fat(n))