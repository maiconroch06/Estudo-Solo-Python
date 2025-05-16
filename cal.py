operacao = input('''Olá, que operação matemática deseja fazer?
1. Adição
2. Subtração
3. Multiplicação
4. Divisão
''')

num_1 = int(input("Insira um número: "))
num_2 = int(input("Insira um outro número: "))

if operacao == "1":
  print((num_1, num_2))
  print(f"O resultado é: {num_1 + num_2}")
  
elif operacao == "2":
  print((num_1, num_2))
  print(f"O resultado é: {num_1 - num_2}")

elif operacao == "3":
  print((num_1, num_2))
  print(f"O resultado é: {num_1 * num_2}")

elif operacao == "4":
  print((num_1, num_2))
  print(f"O resultado é: {num_1 // num_2}")

else:
    nov = input("Você não digitou um operador válido, quer executar o programa novamente? (S ou N) ")

