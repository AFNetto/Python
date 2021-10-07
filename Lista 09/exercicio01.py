def éprimo(n):
    soma=0
    aux=1
    while aux<=n:
        if n%aux==0:
            soma=soma+1
        aux=aux+1
    if soma>2:
        return False
    else:
        return True

aux=2
somando=0
num=int(input("Digite o número"))
#print(éprimo(num))
while aux<=num:
    if (éprimo(aux))==True:
        somando=somando+1
    aux=aux+1
print(somando)

    