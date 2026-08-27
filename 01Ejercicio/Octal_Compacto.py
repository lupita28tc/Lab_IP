num1,octal = 8,"" #indica el numero y la variable octal con una cadena vacia 
if num1 == 0: print ("0") # si es 0 tiene que imprimir 0 
while num1 > 0: octal = str(num1%8) + octal; num1 = num1 // 8 # mientras el numero sea > a 0 se divide entre 8 y se queda el residuo se junta con la cadena vacia y se divide entre 8 el numero 
print (octal)   


