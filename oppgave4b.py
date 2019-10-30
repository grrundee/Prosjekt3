
import matplotlib.pyplot as plt
import numpy as np


f_upper = []  #oppretter en tom vektor f_upper

f = open('input_oppgave4_upper_curve.txt', 'r')
for line in f:
    f_upper.append(float(line)) #Her lagres verdiene fra fil i vektoren f_upper


g_lower = []  #oppretter en tom vektor g_lower

g = open('input_oppgave4_lower_curve.txt', 'r')
for line in g:
    g_lower.append(float(line)) #Her lagres verdiene fra fil i vektoren g_lower


x_upper = np.linspace(186, 350, 163) #Her er x-verdiene for observasjonene f_upper
x_lower = np.linspace(79, 350, 270) #Her er x-verdiene for observasjonene g_lower
     
plt.plot(x_lower, g_lower, 'b*', x_upper, f_upper, 'r*')
plt.axis('equal')
plt.show()


#her kan du skrive programmet ditt

