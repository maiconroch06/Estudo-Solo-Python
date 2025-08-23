print(' = = = Parametros sep & end = = =')
print('1 > SEP')

# O parâmetro sep (abreviação de "separator") define o separador entre os itens passados para o print().
print(" Python", "é", "incrível", sep="-") # Python-é-incrível
print(" A", "B", "C", sep=",")  # Saída: A,B,C
print(" 1", "2", "3", sep=" | ")  # Saída: 1 | 2 | 3
print(" Olá", "Mundo", sep="")  # Saída: OláMundo (sem espaço)

print('2 > END')

# O parâmetro end define o que será adicionado ao final da linha impressa.
print(" Python", end="!")
print(" é incrível")

# Sem quebra de linha
print(" Linha 1", end=" ")
print(" continua na mesma linha")  # Saída: Linha 1 continua na mesma linha

# Usando outros caracteres no final
print(" Fim da frase", end="...")  # Saída: Fim da frase...

