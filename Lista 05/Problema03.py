nu=int(input("Digite o numero inteiro"))
soma=0
while(nu>0):
   n=nu%10
   nu=nu//10
   soma+=n
print(soma)