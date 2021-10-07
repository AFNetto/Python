def maximo (num1,num2,num3):
    if num1>num2 and num1>num3:
        return num1
    if num2>num1 and num2>num3:
        return num2
    else:
        return num3

NUM1=int(input("Digite o primeiro número"))
NUM2=int(input("Digite o segundo número"))
NUM3=int(input("Digite o terceiro número"))
print(maximo(NUM1,NUM2,NUM3))
       