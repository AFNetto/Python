def remove_repetidos(listaOF):
    listaCopy=[]
    aux=0
    tamanholista=0
    for i in listaOF:
        tamanholista=len(listaCopy)
        contador=0
        aux=0
        while aux<tamanholista:
            if i==listaCopy[aux]:
                contador=contador+1
            aux=aux+1
        if contador<=0:
            listaCopy.append(i)
    listaCopy.sort()
    return listaCopy

def main():
    lista=[]
    aux=0
    quantidade=int(input("digite a quantidade de elementos da sua lista"))
    while aux<quantidade:
        numero=int(input("Digite o elemento da sua lista"))
        lista.append(numero)
        aux=aux+1
    print(remove_repetido(lista))

main()



