import matplotlib.pyplot as plt
import numpy as np
import csv
import time
import random
import sys

then = time.time()

csvfile = "donnees.csv"

with open(csvfile, 'r') as f:
	reader = csv.reader(f, delimiter= ' ')
	for item in reader:
		print("Printing list")
		print(item)
		print("Printing test value")
		print(item[0])

#
# variables
#

a=float(item[0])
b=float(item[1])
nmax=float(item[2])
x0=float(item[3])
erreurmax=float(item[4])
flag=float(item[5])
c=float(item[6])
m=float(item[7])
g=float(item[8])
l=float(item[9])
xq=float(item[10])
yq=float(item[11])

#print(b)

#fonc potentiel
def potentiel(x):
	y = m*g*l*np.cos(x)+c/((l*np.sin(x)-xq)**2+(l*(1.-np.cos(x))-yq)**2)**0.5
	return y

#fonc deriv potentiel
def derivpotent(x):
	y = m*g*l*np.sin(x)+c*l*(xq*np.cos(x)+(yq-l)*np.sin(x))/((l*np.sin(x)-xq)**2+(l*(1.-np.cos(x))-yq)**2)**1.5
	#now = time.time()
	#print("time taken", now - then, end='\r')
	return y

#func deriv seconde
def deriv2nd(x):
	y = m*g*l*np.cos(x)+3.0*c*l*l*((l-yq)*np.sin(x)-xq*np.cos(x))**2/((xq-l*np.sin(x))**2+(yq+l*np.cos(x)-l)**2)**2.5+c*l*((yq*l)*np.cos(x)-xq*np.sin(x))/((xq-l*np.sin(x))**2+(yq+l*np.cos(x)-l)**2)**1.5
	return y

#trace fct pot

x = np.linspace(0,np.pi, 1000)
y = potentiel(x)
z = derivpotent(x)
w = deriv2nd(x)

#
# DRAW FUNCTIONS
#

#potent V
def DRAWpotent():
	plt.axis([0,np.pi,-0.5,0.1])
	name = "potentielV.png"
	plt.title("potentiel V")
	plt.xlabel ("angle")
	plt.ylabel ("V(x)")
	plt.plot(x,y,c="red")
	plt.savefig("potentielV.png")

	plt.show()
	#plt.close()

#deriv
def DRAWderiv():
	plt.axis([0,np.pi,-1,1])
	plt.xlabel("angle")
	plt.ylabel("V1(x)")
	plt.plot(x,y,c="blue")
	plt.savefig("deriv.png")

	plt.show()
	#plt.close()

#deriv seconde
def DRAWderiv2nd():
	plt.axis([0,np.pi,-1,10])
	plt.title("deriv seconde")
	plt.xlabel("angle")
	plt.ylabel("V2(x)")
	plt.plot(x,y,c="yellow")
	plt.savefig("deriv2.png")

	plt.show()
	#plt.close()

#DRAWpotent()
#DRAWderiv2nd()
#DRAWderiv()

# erreur =/= erreurmax
#
#
# functions :
# potentiel(x)
# derivpotent(x)
# deriv2nd(x)


# dichotomie

erreur = 1.0
new_erreur = erreur

def dichotomie():
	if True:
		erreur= 1.0
		i = 0

		bis_a = a
		bis_b = b
		bis_rec = (a+b)/2.0
#	print(a)
#	print(b)

		new_erreur = erreur

		while new_erreur > erreurmax and i < nmax:
			bis_rec = (bis_a + bis_b)/2.0
			#print(i)
			if derivpotent(bis_a) * derivpotent(bis_rec) < 0:
				bis_b = bis_rec
			else:
				bis_a = bis_rec
				#bis_rec = (bis_a + bis_b) / 2.0
			i += 1
			new_erreur = abs(bis_b - bis_a)

		print("Erreur:", new_erreur, " || Rec:", bis_rec, " || Nombre d'iter:", i)
	#print(i)

#list_erreur = [0.1, 0.01, 0.001, 0.00001, 0.000001, 0.0000001, 0.00000001]

#for i in list_erreur(new_erreur):
#	if True:
#		dichotomie[i]()




#newton
# Nmax = 1000
# i nbre iter

if 1==0:
	erreur = 1.0
	i = 0
	x_preced = x0

	while erreur > erreurmax and i < nmax:
		x_new = x_preced - derivpotent(x_preced) / deriv2nd(x_preced)
		erreur = np.abs(x_new - x_preced)
		x_preced = x_new
		i += 1
	print(i)

