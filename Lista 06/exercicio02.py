def éprimo(k):
    aux=1
    conta=0
    while aux<=k:
        if k%aux==0:
          conta+=1
        aux=aux+1

    if conta>2:
        return False
    else:
        return True

def maior_primo(num):
    prm=n=0
    while n<=num:
        if éprimo(n)==True:
            prm=n
        n+=1
    return prm


num=int(input("Digite o número"))
print(maior_primo(num))