# Navn: Grunde Gregersen
# Studentnummer: 220511

# Importerer library's
import matplotlib.pyplot as plt 
import math as m 

# Deklarerer array
x = [0,1,2,3,4,5,6,7,8,9]
y = [5.3,4.9,4.1,5.1,4.2,4.0,2.8,1.0,0.9,0.0]


X0 = x[0]
Xn = x[-1]
n = 9 # Velger 9 ettersom det passer med antall målepunkter
deltaX = (Xn-X0)/n

fx = 0
i=1
for i in range(1,n,1):
    fx += m.sqrt(deltaX**2 + (abs(y[i]-y[i+1]))**2)

print("Det estimerte lengden av grenseskille mellom frisk og nedbrent skog blir: ",fx,"km")
