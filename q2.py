print("Este programa te imprime una piramide de T del numero que des.")
def triangulo(size):
    letra=""
    for i in range(size):
        letra=letra+"T"
        print(letra)

    for b in range(size):
        letra=letra[:-1]
        print(letra+"T")

p=int(input("Dime el tamano del triangulo: "))
triangulo(p)
