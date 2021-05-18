segundoStr = input("Por favor, entre com o número de segundos que deseja converter: ")
totalsegundos = int(segundoStr)

dias = totalsegundos // 86400
segundosRes = totalsegundos % 86400

horas = segundosRes // 3600
segundosRes2 = segundosRes % 3600

minutos = segundosRes2 // 60
segundosFinais = segundosRes2 % 60

print(dias,"Dias,", horas,"horas,",minutos,"minutos e", segundosFinais,"segundos")
