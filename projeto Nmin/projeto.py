def computador_escolhe_jogada(m,n):
    aux=resto=0
    jogadaPc=m
    while(aux<=m):
        resto=n-aux
        if resto%aux==0:
            jogadaPc=m
        aux+=1
    return jogadaPc

def usuario_escolhe_jogada(m,n):
    jogada_usuario=int(input("Digite sua jogada"))
    if jogada_usuario<=m:
            return m
    else:
            print("informe uma jogada válida")
            jogada_usuario=int(input("Digite sua jogada"))

def partida():
    n=int(input("Digite o número de peças"))
    m=int(input("Digite o número de peças que podem ser tiradas por vez"))
    if (n%(m+1)==0):
        print("Você começa")
        usuario_escolhe_jogada(m,n)
        while (n>0):
          n=n-computador_escolhe_jogada(m,n)
          n=n-usuario_escolhe_jogada(m,n)
          if n<=0:
              print("O computador venceu o jogo")

    else: 
        print ("Computador começa")
        computador_escolhe_jogada(m,n)
        while (n>0):
          n-= usuario_escolhe_jogada(m,n)
          if n<=0:
              print("O computador venceu o jogo")
          n-= computador_escolhe_jogada(m,n)
            
        
