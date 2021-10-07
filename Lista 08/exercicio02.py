aux=linha=largura=int(input("digite a largura"))
coluna=altura=int(input("digte a altura"))
while altura>0:
    largura=aux
    while largura>0:
        if altura==1 or altura==coluna or largura==1 or largura==linha:
            print("#",end="")
        else:
            print(" ",end="")
        largura=largura-1
    print()
    altura=altura-1