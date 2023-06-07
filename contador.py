hour = int(input("Hora de início (horas): "))
mins = int(input("Hora de início (minutos): "))
dura = int(input("Duração do evento (minutos): "))

totalMin = hour * 60 + mins
hour = (totalMin + dura) // 60
hour = hour % 24  
mins = (mins + dura) % 60  

print(hour, ":", mins, sep='')
