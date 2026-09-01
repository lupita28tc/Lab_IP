n=int(input("Ingrese un número:"))
if n <=1:
    print ("El número NO es primo")
i=2
while i <=n:
    if n == 2:
        print ("El número ES primo ")
        break
    if n%1 == 0:
        print("El número NO es primo")
        break
    elif n%1 ==0 and i== n:
        print("El número ES primo ")
        break
    elif n%1 !=0 and i< n:
        print ("El numero ES primo")
        break 
    i+=1 