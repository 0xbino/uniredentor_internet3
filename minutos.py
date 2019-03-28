minutos=float(input("qts min gastou: "))

if minutos < 200:
    conta=minutos*0.2

elif minutos > 400:
    conta=minutos*0.15

else:
    conta=minutos*0.18

print ("%f" %conta)
