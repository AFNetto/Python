import math
x1=int(input("Digite a coordenada x do primero ponto"))
y1=int(input("Digite a coordenada y do primero ponto"))
x2=int(input("Digite a coordenada x do segundo ponto"))
y2=int(input("Digite a coordenada y do segundo ponto"))
dist=math.sqrt(((x1-x2)**2)+((y1-y2)**2))
if dist>=10:
   print("Longe")
else:
   print("perto")