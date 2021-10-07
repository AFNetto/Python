def soma_elementos(listaOF):
    aux=0
    for i in listaOF:
        aux=aux+i
    return aux

def main():
    lista=[]
    aux=0
    quantidade=int(input("digite a quantidade de elementos da sua lista"))
    while aux<quantidade:
        numero=int(input("Digite o elemento da sua lista"))
        lista.append(numero)
        aux=aux+1
    print(soma_elementos(lista))

main()