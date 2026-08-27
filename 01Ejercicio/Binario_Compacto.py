num1,binario = 8,"" # me dice el numero y la variable binario que es la que va a almacenar el resultado 
if num1 == 0: print ("0") # si es 0 tiene que imprimir 0 
while num1 > 0: binario = str(num1%2) + binario; num1 = num1 // 2 #mientras el numero sea mas grande que 0 se divide entre 2 y se queda el residuo con la cadena vacis y se divide entre 2 y el numero
print (binario) # imprime el resultado de binario