print("Este programa te da la potencia que quieras del numero que quieras.")
def superpower(a,b):
    conta=1
    multi=a
    while(conta!=b):
        multi=multi*a 
        conta=conta+1
    return multi

num=int(input("Dime que numero quieres elevar: "))
potencia=int(input("A la cuanto lo quieres elevar: "))
print(superpower(num,potencia))

