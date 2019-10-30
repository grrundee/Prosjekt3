# Navn: Grunde Gregersen
# Studentnummer: 220511

# Imprterer library
import numpy as np 

def f(x):
    return((x**2)*np.sin(x-2)-4*x) # x E [15/2,10]

def dfdx(x):
    return (x * (x * (np.sin(2) * np.sin(x) + np.cos(2) * np.cos(x)) - 2 * np.sin(2 - x)) - 4)

x = 15/2
stopval = 10**(-10)
i = 0

while (abs(f(x))>stopval and i<100):
    x-=(f(x)/dfdx(x))
    i+=1
    print("Tilnermet løsning for x =",x)
    print("Dette er irretasjon nr.", i)

print("Vi ser at metoden jobber seg inn mot et nullpunkt og vi finner ett annet nullpunkt", end='')
print("enn i oppgave B, men dette nullpunktet ligger uten for \ndeffinisjonsområdet.")
