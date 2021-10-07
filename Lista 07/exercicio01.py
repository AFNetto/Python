def fizzbuzz(numInt):
    if numInt%3==0:
        if numInt%5==0:
            return "FizzBuzz"
        else:
            return "Fizz"
    else:
        if numInt%5==0:
            return "Buzz"
        else:
            return numInt

num=int(input("Digite o número"))     
print(fizzbuzz(num))