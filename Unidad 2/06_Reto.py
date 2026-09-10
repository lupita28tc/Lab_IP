Total = float (input("Total de la cuenta: "))
propina = float ( input ("propina (%):"))
personas=int(input ("numero de personas: "))

propina = Total * (propina / 100)
Total = Total + propina
por_persona = Total / personas

print(f"total final : ${Total:.2f}")
print(f"total por persona : ${por_persona:.2f}")
