import matplotlib.pyplot as plt
import numpy as np
import csv
import pandas as pd
from math import *

#file = "donnees.dat"
csvfile = "donnees.csv"

#pd.read_csv("donnees.csv", header=None, delimiter=r"\s+")

with open(csvfile, 'r') as f:
	reader = csv.reader(f, delimiter=' ')
	for item in reader:
		print(item)
		print(item[0]

#Eq 1.1 attempt
def gfunc():
	g=vg+ve

def ffunc():
	f=((derVg+ve)/derTh)

#Convert Variables

a=float(item[0]) #
b=float(item[1]) #
nmax=float(item[2]) #
x0=float(item[3]) #
epsilon=float(item[4]) #
flag=float(item[5]) #
c=float(item[6])
m=float(item[7])
g=float(item[8])
l=float(item[9])
xq=float(item[10])
yq=float(item[11])

# end

def ve():
	return c*((l)/(sqrt(l*math.sin(x))**2 + (l*(1-math.cos(x)) - yq)**2

def eq11(x):
	first_memb = m*g*math.sin(x)
	second = first_memb + c
	third = ((xq*math.cos(x) + (yq - l) * math.sin(x)
	fourth = ((l*math.sine(x) - yq)**2 + (l*(1-math.cos(x))- yq)**2)/**1/2
		return y = second*(third)/(fourth)

x = np.linspace(0, np.pi, 1000)
y = eq11(x)

plt.axis([0, np.pi, -0.5, 0.1])
plt.title = "Potentiel"
plt.plot(x)

#Bisect method

while(erreur>epsilon):
	xm = (xplus + xminus)/2
	if f(xn) * f(xminus) < 0):
		xplus = xm
	else
		xminus  = xm

#end

#Confirmer que les valeurs du fichier sont OK
print("Safeguard")
print(item[0])

if (item[0] == "0.0"):
	print("equal - considered string")
else:
	print("not equal or considered smth else")

if (a == 0.0):
	print("equal, considered float")
