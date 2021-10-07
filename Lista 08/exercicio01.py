aux=largura=int(input("digite a largura"))
altura=int(input("digte a altura"))
while altura>0:
    largura=aux
    while largura>0:
        print("#",end="")
        largura=largura-1
    print()
    altura=altura-1