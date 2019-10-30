
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
plt.show()


#her kan du skrive programmet ditt

