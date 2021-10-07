A=int(input("Digite o a da equação"))
B=int(input("Digite o b da equação"))
C=int(input("Digite o c da equação"))
delta=(B**2)-(4*A*C)
if delta<0:
    print("esta equação não possui raízes reais")
else:
    raiz1=((-B)+(delta**(1/2)))/(2*A)
    if delta==0:
        print("a raiz desta equação é",raiz1)
    else:
        raiz2=((-B)-(delta**(1/2)))/(2*A)
        if(raiz1<raiz2):
           print("as raízes da equação são",raiz1,"e",raiz2)
        else:
           print("as raízes da equação são",raiz2,"e",raiz1)