
import matplotlib.pyplot as plt
import numpy as np


f_upper = []  #oppretter en tom vektor f_upper

f = open('input_oppgave4_upper_curve.txt', 'r')
for line in f:
    f_upper.append(float(line)) #Her lagres verdiene fra fil i vektoren f_upper


x_upper=np.linspace(186, 350, 163) #Her er x-verdiene for observasjonene f_upper

                
p = [145, 227] #Her er det faste punktet "på sørsiden av vannet"                
     
plt.plot(p[0], p[1], 'b*', x_upper,f_upper, 'r*')
plt.axis('equal')
#plt.show()


#her kan du skrive programmet ditt

z = np.array([])

for i in range(0,163,1):
    x = x_upper[i] - p[0]
    y = f_upper[i] - p[1]
    z = np.append(z,np.sqrt(x**2 + y**2))

minZ = np.min(z)

print("Den minste avstanden mellom punktet og kurven er ",minZ)
plt.show()