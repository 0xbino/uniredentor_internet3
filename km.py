minutos=float(input("qts min gastou: "))
if minutos < 200:
    conta=minutos*0.2
    print ("%f" %conta)
elif minutos > 400:
    conta=minutos*0.15
    print ("%f" %conta)
else:
    conta=minutos*0.18
    print ("%f" %conta)
    
