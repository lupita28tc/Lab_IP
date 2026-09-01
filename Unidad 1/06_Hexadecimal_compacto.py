numero,hexadecimal = 11,"" #indica que el numero y la cadena donde se va a hacer el resultado
if numero == 0: #si es cero el resultado es cero 
    hexadecimal = "0" 
while numero>0: # mientras el numero sea mayor a cero y se repite 
     residuo=numero %16 #saco el residuo de dividir 16 y ese el digito que toca 
     hexadecimal =("ABCDEF"[residuo - 10] if residuo >=10 else str (residuo))+ hexadecimal #si el residuo es 10 o mas uso la letra si no uso el numero 
     numero //=16 #se divide el numero entre 16 entero sin decimal para seguirm con el siguiente digito
print (hexadecimal) #imprime el resultado