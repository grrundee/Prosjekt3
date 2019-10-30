# Navn: Grunde Gregersen
# Studentnummer: 220511

# Imprterer library
import numpy as np 

x = np.linspace(15/2,10,1000)

x0pkt = 0

def f(x):
    return((x**2)*np.sin(x-2)-4*x) # x E [15/2,10]

for i in range(0,999,1):
    if((f(x[i]) * f(x[i+1]))<0):
        x0pkt=(x[i]+x[i+1])/2

print("Denne x verdien er et tilnærmet nullpunkt", x0pkt, "\nVerdien til f(x) for det tilnærmede ",end='')
print("nullpunktet blir",f(x0pkt))