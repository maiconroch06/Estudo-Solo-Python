#B) Escreva um código que receba um número de segundos e converta 
#este número em horas, minutos e segundos. Escreva também um código que faça o contrário.
def cal_tempo():
    ds = input("Convertor de tempo, escolha o valor que vai ser usado: S, M ou H? ").upper()

    if ds == "S":
        seg = float(input("Digite o número de segundos: "))
        seg_rest = int(seg % 60)
        min_rest = int((seg % 3600) // 60)
        hora = int(seg // 3600)
        print(f"Relogio: {hora:02}:{min_rest:02}:{seg_rest:02}")

    elif ds == "M":
        min = float(input("Digite a quantidade de minutos: "))
        min_rest = int(min % 60)
        seg = int((min * 60) % 60)
        hora = int(min // 60)
        print(f"Relogio: {hora:02}:{min_rest:02}:{seg:02}")
                
    elif ds == "H":
        hora = float(input("Digite a quantidade de horas: "))
        min = int(hora * 60)
        seg = int(hora * 3600)
        print(f"Relogio: {hora:02}:{min:02}:{seg:02}")

    else:
        print("Escolha errada")

    novamente()

def novamente():
    ds = input("Tentar novamente? S ou N. ").upper()

    if ds == "S":
        cal_tempo()

    elif ds == "N":
        print("Até mais!")

    else:
        novamente()

cal_tempo()