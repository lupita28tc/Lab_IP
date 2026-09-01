numero=8
if numero == 0:
    print("0")
    
binario = ""
while numero > 0:
    binario=str(numero%2) + binario
    numero = numero // 2 
    print(binario)    