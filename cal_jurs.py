# C) Considere a fórmula para cálculo de juros simples, J = (C × I × T) / 100, onde J, C, I e T 
# correspondem a juros, capital, taxa e tempo, respectivamente. Construa um código que solicite 
# ao usuário os valores de C, I e T e calcule J.

print("Calculo de juros simples")
ds = input("Qual variavel deseja trabalhar: J, C, I ou T? ").upper()
    
if ds == "J":
    C = float(input("Capital: "))
    I = float(input("Taxa: "))
    T = float(input("Tempo: "))
    
    J = (C * I * T) / 100
    print(f"Juros:{J}, Capital: {C}, Taxa:{I}, Tempo:{T}")
    
elif ds == "C":
    J = float(input("Juros: "))
    I = float(input("Taxa: "))
    T = float(input("Tempo: "))
    
    C = (J * 100) / (I * T)
    print(f"Capital: {C}, Juros:{J}, Taxa:{I}, Tempo:{T}")
    
elif ds == "I":
    J = float(input("Juros: "))
    C = float(input("Capital: "))
    T = float(input("Tempo: "))
    
    I = (J * 100) / (C * T)
    print(f"Taxa:{I}, Juros:{J}, Capital: {C}, Tempo:{T}")

elif ds == "T":
    J = float(input("Juros: "))
    C = float(input("Capital: "))
    I = float(input("Taxa: "))
    
    T = (J * 100) / (C * I)
    print(f"Tempo:{T}, Juros:{J}, Capital: {C}, Taxa:{I}")

else:
    print("Escolha invalida")
