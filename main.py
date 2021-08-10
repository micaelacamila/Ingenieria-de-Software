dia = input("Ingresa el dia de inicio ")
hora = int(input("Hora de inicio (horas): "))
min = int(input("Minuto de inicio (minutos): "))
dura = int(input("Duración del evento (minutos): "))

# coloca tu código aqui
new_m = min + dura
new_h = int(new_m / 60)
new_m = new_m%60
new_h = new_h+hora
if(new_h>=24):
    new_h=new_h%24
print("El evento inicia el día ",dia, "a las ",hora,":",min);
print("\n Y finaliza: ",new_h,":",new_m)
