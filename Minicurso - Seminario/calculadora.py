def soma(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    return a / b


print("\n ============ CALCULADORA ============")
print("  [1] Some")
print("  [2] Subtraia")
print("  [3] Multiplique")
print("  [4] Divida")
print(" =====================================")

opcao = int(input(" - Escolha o operador: "))

print("\n ============== NÚMEROS ==============")
a = int(input(" Digite o primeiro número: "))
b = int(input(" Digite o segundo número: "))

print("\n ============= RESULTADO =============")
if opcao == 1:
    resultado = soma(a, b)
    print(" -> ", a, " + ", b, " = ", resultado)

elif opcao == 2:
    resultado = subtracao(a, b)
    print(" -> ", a, " - ", b, " = ", resultado)

elif opcao == 3:
    resultado = multiplicacao(a, b)
    print(" -> ", a, " * ", b, " = ", resultado)

elif opcao == 4:
    if b == 0:
        print(" #ERRO: divisão por 0!")

    else:
        resultado = divisao(a, b)
        print(" -> ", a, " / ", b, " = ", resultado)
        
else:
    print(" #ERRO: opção errada!")
print(" =====================================")