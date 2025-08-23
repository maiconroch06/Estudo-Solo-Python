print(' ============== CALCULADORA =============')
n1 = float(input(' > Informe o primeiro numero: '))
n2 = float(input(' > Informe o segundo numero: '))

soma = n1 + n2
subtracao = n1 - n2
multplicacao = n1 * n2
divisao = n1 / n2
divisao_int = n1 // n2
resto = n1 % n2
potenciacao = n1 ** n2
print(' ============== RESULTADOS ==============')
print(' ', n1, '+', n2, '=', soma)
print(' ', n1, '-', n2, '=', subtracao)
print(' ', n1, '*', n2, '=', multplicacao)
print(' ', n1, '/', n2, '=', divisao)
print(' ', n1, '//', n2, '=', divisao_int)
print(' ', n1, '%', n2, '=', resto)
print(' ', n1, '**', n2, '=', potenciacao)
print(' ========================================')