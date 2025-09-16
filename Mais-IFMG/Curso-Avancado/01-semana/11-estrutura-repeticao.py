print("1#")
entrada = input(" Digite um número inteiro positivo: ")

if not entrada.isdigit():
    print(" Entrada inválida. Tente novamente.")

numero = int(entrada)

print(f"\n Verificando os números de 1 até {numero}:")

for i in range(1, numero + 1):
    if i % 2 == 0:
        print(f" {i} é par")
    else:
        print(f" {i} é ímpar")

# ---------------------------------------------------------------
print("\n2#")
lista = {2, 1, 4, 7, 3, 5, 6, 8}

for item in lista:
    print(' ', lista)
# ---------------------------------------------------------------
print("\n3#")
lista = {2, 1, 4, 7, 3, 5, 6, 8}

for item in range(lista):
    print(' ', item)
# ---------------------------------------------------------------
print("\n4#")
palavra = 'Meu nome é Maicon'

for letra in palavra:
    print(' ', letra)
# ---------------------------------------------------------------
print("\n5#")
nomes = {"Alan", "Cap", "Bit", "Fall", "VX", "Mount"}

for nomes in nomes:
    if nomes == "VX":
        continue
    print(' ', nomes)

    # ranger(valor_inicial, valor_final, incremento)