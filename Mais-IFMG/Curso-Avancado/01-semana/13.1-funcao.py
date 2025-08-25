# Funções são trechos de código que executam determinada tarefa ao serem chamados e depois retornam o controle para o ponto em que foram chamadas. Quando chamamos uma função devemos informar os parâmetros necessários. Após a declaração, vem o chamado corpo da função com suas instruções endentadas. No corpo da função, quando a função precisar tiver que retornar algum valor, é usada a instrução return.
def exibição():
    print(" ============== CALCULADORA ==============")
    print("  > [1] Soma")
    print("  > [2] Subtração")
    print("  > [3] Multiplicação")
    print("  > [4] Divisão")
    print("  > [5] Divisão Inteira")
    print("  > [6] Resto")
    print("  > [7] Potenciação")
    print("  > [8] Raiz Quadrada")
    print("  > [0] Sair da calculadora")
    print(" =========================================")

# Passagem de parâmetros e retorno de resultado
def soma(num1, num2):
    return num1 + num2

def subtração(num1, num2):
    return num1 - num2
    
def multiplicação(num1, num2):
    return num1 * num2
    
def divisão(num1, num2):
    return num1 / num2
    
def divisão_inteira(num1, num2):
    return num1 // num2
    
def resto(num1, num2):
    return num1 % num2
    
def potenciação(num1, num2):
    return num1 ** num2

def raiz_quadrada(num1, num2):
    return num1 ** (1 / num2)


while True:
    exibição()
    escolha = int(input(" > Opção: "))

    if escolha == 1:
        num1 = float(input(" > Digite um número: "))
        num2 = float(input(" > Digite outro número: "))
        # Chamada de função soma(num1, num2)
        print(f"\n RESULTADO: {num1} + {num2} = {soma(num1, num2)}\n")

    elif escolha == 2:
        num1 = float(input(" > Digite um número: "))
        num2 = float(input(" > Digite outro número: "))
        print(f"\n RESULTADO: {num1} - {num2} = {subtração(num1, num2)}\n")

    elif escolha == 3:
        num1 = float(input(" > Digite um número: "))
        num2 = float(input(" > Digite outro número: "))
        print(f"\n RESULTADO: {num1} * {num2} = {multiplicação(num1, num2)}\n")

    elif escolha == 4:
        while True:
            num1 = float(input(" > Digite um número: "))
            num2 = float(input(" > Digite outro número: "))

            if num2 != 0:
                print(f"\n RESULTADO: {num1} / {num2} = {divisão(num1, num2)}\n")
                break
            else:
                print("\n #ERRO: divisão por zero.\n")

    elif escolha == 5:
        num1 = float(input(" > Digite um número: "))
        num2 = float(input(" > Digite outro número: "))
        print(f"\n RESULTADO: {num1} // {num2} = {divisão_inteira(num1, num2)}\n")

    elif escolha == 6:
        num1 = float(input(" > Digite um número: "))
        num2 = float(input(" > Digite outro número: "))
        print(f"\n RESULTADO: {num1} % {num2} = {resto(num1, num2)}\n")

    elif escolha == 7:
        num1 = float(input(" > Digite um número: "))
        num2 = float(input(" > Digite outro número: "))
        print(f"\n RESULTADO: {num1} ** {num2} = {potenciação(num1, num2)}\n")

    elif escolha == 8:
        while 1:
            num1 = float(input(" > Digite um número: "))
            num2 = float(input(" > Digite outro número: "))
            if num1 > 0:
                print(f"\n RESULTADO: {num2} ¬/¨¨ {num1} = {raiz_quadrada(num1, num2)}\n")
                break
            else:
                print("\n #ERRO: 'radiano?' negativo.\n")

    elif escolha == 0:
        print(" Saindo......")
        exit(1)
    else:
        print(" #ERRO: escolha inválida.\n")


