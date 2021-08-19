numeros =[1,2,5,9,12,15,17,19,21,39]
for numero in numeros:
    if(numero%3==0 and numero%5==0):
        print(f"{numero} es multiplo de 3 y de 5")
    elif(numero%3==0):
        print(f"{numero} es multiplo de 3")
    elif(numero%5==0):
        print(f"{numero} es multiplo de 5")
   
    