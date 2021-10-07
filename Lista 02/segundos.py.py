SegundosConversão=input("Por favor, entre com o número de segundos que deseja converter")
Dias=int(SegundosConversão)//86400
Horas=(int(SegundosConversão)%86400)//3600
aux=(int(SegundosConversão)%86400)%3600
Minutos=aux//60
Segundos=aux%60
print(Dias,"dias,",Horas,"horas,",Minutos,"minutos e",Segundos,"segundos.")
