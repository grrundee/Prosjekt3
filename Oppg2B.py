# Navn: Grunde Gregersen
# Studentnummer: 220511

# Importerer library
import math as m 
import matplotlib.pyplot as plt 
import numpy as np 

def y(x):
    return m.sqrt(x + 3)

plotX = np.array([])
plotY = np.array([])
Xn = -2
deltaX = 0.001
d = 10000
punktx = 0
i=0
while(Xn < 0 and d != 0.0 and i < 3000):
    a = m.sqrt((y(Xn))**2 + (abs(y(Xn + deltaX)))**2)

    if(a<d):
        d = a
        punktx = Xn
    
    plotX = np.append(plotX,Xn)
    plotY = np.append(plotY,a) # Gjør så vi får "d" langs y-aksen

    Xn += deltaX 
    i +=1

print("Minste avstand fra origo til kurven:",d, "\nPunktet \"d\" finner vi ved x lik:", punktx, " Denne x-verdien passer godt med plottet")

plt.plot(plotX,plotY) 
plt.xlim(-2.5,0.5)
plt.ylim(0,2.5)

plt.show()
