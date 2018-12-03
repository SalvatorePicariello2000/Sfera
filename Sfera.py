import math

def volume(r)
	V=(4.0/3.0*math.pi)*r**3
	return V



r=input ("Inserisci il raggio della sfera:")
r=int (r)
ris=volume(r)
print (ris)