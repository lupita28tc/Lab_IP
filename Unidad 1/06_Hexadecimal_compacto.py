numero,hexadecimal = 11,""
if numero == 0: print ("0")

while numero>0:
    residuo=numero %16
    if residuo >=10:
       hexadecimal ="ABCDEF"[residuo - 10]+ hexadecimal
    else:
        hexadecimal = str (residuo)+ hexadecimal
        
    numero //=16
    
    print (hexadecimal)