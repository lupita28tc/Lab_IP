numero=15
if numero == 0:
    print("0")
    
hexadecimal = ""
while numero > 0:
    residuo = numero % 16
    if residuo < 10:
        hexadecimal = str(residuo) + hexadecimal
    if residuo == 10:
        hexadecimal = "A" + hexadecimal
    if residuo == 11:
        hexadecimal = "B" + hexadecimal
    if residuo == 12:
        hexadecimal = "C" + hexadecimal
    if residuo == 13:
        hexadecimal = "D" + hexadecimal
    if residuo == 14:
        hexadecimal = "E" + hexadecimal
    if residuo == 15:
        hexadecimal = "F" + hexadecimal
    numero = numero // 16

print(hexadecimal)