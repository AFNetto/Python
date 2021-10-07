def computador_escolhe_jogada(n,m):
    y=m+1
    aux=1
    jogada_computador=m
    while(aux<=m):
        if (n-aux)%y==0:
            jogada_computador=aux
        aux=aux+1
    return jogada_computador

def informe_jogada():
    print("")
    jogada_usuario=int(input("Digite sua jogada "))
    return jogada_usuario

def usuario_escolhe_jogada(m,n):
    jogadaUsuario=int(informe_jogada())
    if jogadaUsuario<1 or jogadaUsuario>m or jogadaUsuario>n:
        while jogadaUsuario<1 or jogadaUsuario>m or jogadaUsuario>n:
            print("")
            print("Oops! jogada inválida! tente de novo.")
            print("")
            jogadaUsuario=int(informe_jogada())
        return jogadaUsuario
    else:
        return jogadaUsuario

def Quem_começa(m,n):
    if(n%(m+1)==0):
        print("")
        print("Você começa!")
        print("")
        return 1
    else :
        print("")
        print("Computador começa!")
        print("")
        return 0

def partida():
    jogUsu=JogPC=n=0
    print("")
    n=int(input("Quantas peças? "))
    m=int(input("Limite de peças por jogada? "))
    if Quem_começa(m,n)==1:
        while n>0:
            jogUsu=usuario_escolhe_jogada(m,n)
            n=n-jogUsu
            if(n==0):
                print("Você ganhou!")
            else:
                JogPC=computador_escolhe_jogada(n,m)
                print("O computador tirou",JogPC,"peças")
                n=n-JogPC
                if(n==0):
                  print("Fim de jogo! o computador ganhou!")
                else:
                    print("Restam no tabuleiro",n,"peças")
            
    else:
        while n>0:
            JogPC=computador_escolhe_jogada(n,m)
            print("O computador tirou",JogPC,"peças")
            n=n-JogPC
            if(n==0):
                print("Fim de jogo! o computador ganhou!")
            else:
                jogUsu=int(usuario_escolhe_jogada(m,n))
                n=n-jogUsu
                if(n==0):
                  print("Você ganhou!")
                else:
                    print("você tirou",jogUsu,"peças")
                    print("Restam no tabuleiro",n,"peças")

            
def execução():
    aux=1
    print ("Bem-vindo ao jogo do NIM! Escolha:")
    print("1 - para jogar uma partida isolada ")
    op=int(input("2 - para jogar um campeonato 2 ")) 
    print("")
    if op==1:
        print("Você escolheu uma partida isolada!")
        partida()
    else:
        print("Voce escolheu um campeonato!")
        print("")
        while aux<4:
             print("**** Rodada",aux,"****")
             print("")
             partida()
             print("")
             print("Placar: Você 0 X",aux,"Computador")
             print("")
             aux+=1

execução()