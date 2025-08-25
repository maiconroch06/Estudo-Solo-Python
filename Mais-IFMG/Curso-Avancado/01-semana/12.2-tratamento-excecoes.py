while True:
    try:
        print(' Informe dois números')
        n1 = float(input('n1: '))
        n2 = float(input('n2: '))
        r = n1 / n2
        break
    except ValueError as e:
        print(e)
        print(' Número inválido! Tente novamente.')
    except ZeroDivisionError as e:
        print(e)
        print(' Divisão por zero! Tente novamente.')
print(f'{n1} / {n2} = {r}')