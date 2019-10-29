# Navn: Grunde Gregersen
# Studentnummer: 220511

# Importerer library's
import matplotlib.pyplot as plt 

# Deklarerer array
x = [0,1,2,3,4,5,6,7,8,9]
y = [5.3,4.9,4.1,5.1,4.2,4.0,2.8,1.0,0.9,0.0]

# Velger å bruke trapesmetoden for å beregne området omtrentlig.
X0 = x[0]
Xn = x[-1]
n = 9 # Velger 9 ettersom det passer med antall målepunkter
deltaX = (Xn-X0)/n

fx = (y[0]+y[-1])

i=1
for i in range(1,n,1):
    fx += 2*y[i]

fx = (deltaX/2) * (fx)

print("Det omtrentlige arealet av nedbrent skog blir: ",fx,"km^2")
