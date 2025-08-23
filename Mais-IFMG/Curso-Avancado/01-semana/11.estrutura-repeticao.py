while True:
    print("\n ================== VERIFICADOR DE NÚMEROS ==================")
    entrada = input(" Digite um número inteiro positivo (ou 'sair'): ")

    if entrada.lower() == "sair":
        print(" Encerrando o programa...")
        break

    if not entrada.isdigit():
        print(" Entrada inválida. Tente novamente.")
        continue  # Volta para o início do while

    numero = int(entrada)


    print(f"\n Verificando os números de 1 até {numero}:")

    for i in range(1, numero + 1):
        if i % 2 == 0:
            print(f" {i} é par")
        else:
            print(f" {i} é ímpar")

    print("\n ======================================================")