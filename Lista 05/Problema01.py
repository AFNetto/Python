num=int(input("Digite o valor de n:"))
fatorial=1
if num==0:
    print("1")
else:
    while num>1:
        fatorial=fatorial*num
        num-=1
    print(fatorial)