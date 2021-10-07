import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:")

    wal = float(input("Entre o tamanho médio de palavra:"))
    ttr = float(input("Entre a relação Type-Token:"))
    hlr = float(input("Entre a Razão Hapax Legomana:"))
    sal = float(input("Entre o tamanho médio de sentença:"))
    sac = float(input("Entre a complexidade média da sentença:"))
    pal = float(input("Entre o tamanho medio de frase:"))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) +" (aperte enter para sair):")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,;:]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1
    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    '''IMPLEMENTAR. Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    aux=0
    somatorio=0
    while aux<6:
        diferença=as_a[aux]-as_b[aux]
        somatorio=somatorio + abs(diferença)
        aux=aux+1
    Sa_b=somatorio/6
    return Sa_b

def calcula_assinatura(texto):
    '''IMPLEMENTAR. Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    aux1=aux=aux2=0



    # CALCULANDO AS SENTENÇAS
    sentencas=separa_sentencas(texto)  
   

    # CALCULANDO AS FRASES
    frase=[]
    for A in sentencas:
        frasinha=separa_frases(A)
        frase=frase+frasinha


    # CALCULANDO AS PALAVRAS
    palavras=[]
    for D in frase:
        palavra=separa_palavras(D)
        palavras=palavras+palavra
        
            
    #CALCULANDO OS COMPONENTES DO TEXTO A SER ANALISADO
    
    total_palavras=len(palavras)
    


    for i in palavras:     #somatório da quantidade de caracteres nas palavras
        quant=len(i)
        aux=aux+quant
    Tam_medio_palavras=aux/total_palavras
    



    type_token=(n_palavras_diferentes(palavras))/total_palavras
    Hapax_legomana=(n_palavras_unicas(palavras))/total_palavras
    

    for j in sentencas:  #somatório da quantidade de caracteries na sentença
        quantSent=len(j)
        aux1=aux1+quantSent
    tam_medio_sentenças=aux1/(len(sentencas))
    
    complexidade_Sentença=len(frase)/len(sentencas)

    for w in frase:
        quantFrases=len(w)
        aux2=aux2+quantFrases
    tam_medio_frase=aux2/len(frase)

    return (Tam_medio_palavras,type_token,Hapax_legomana,tam_medio_sentenças,complexidade_Sentença,tam_medio_frase)

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''
    Menor_SAB=compara_assinatura(calcula_assinatura(textos[0]),ass_cp)
    numtexto=0
    texto=1
    for A in textos:
        Sa_b=compara_assinatura(calcula_assinatura(A),ass_cp)
        print(Sa_b)
        if Sa_b<Menor_SAB:
            Menor_SAB=Sa_b
            texto=numtexto+1
        numtexto=numtexto+1
    return texto
    
def main():
    infectado=le_assinatura()
    textos=le_textos()
    print("O autor do texto",avalia_textos(textos,infectado),"está infectado com COH-PIAH")

main()
