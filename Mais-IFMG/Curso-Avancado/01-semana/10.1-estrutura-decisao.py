import statistics
print(" ============= VERIFICAOR DE NOTAS =============")
n1 = float(input("  > Infome sua primeira nota (0-100): "))
n2 = float(input("  > Infome sua segunda nota (0-100): "))

media = (n1 + n2) / 2

print(" ================== RESULTADO ==================")
if (media >= 60): {
    print("  # RECUPERAÇÃO!")
}
elif (media >= 40): {
    print("  # RECUPERAÇÃO!")
}
else: {
    print("  # REPROVADO!")
}
print(" ===============================================")