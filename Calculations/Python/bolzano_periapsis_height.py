import matplotlib
import numpy

#_1 --> elipse tierra-jupiter
#_2 --> elipse jupiter-saturno

# unitats: 	distÃ ncia(m)
# 			velocitat(m/s)
#	 		angles(radians)

## definim totes les constants que seran utilitzades als càlculs
UA = 149597870700
mu_sol = float(6.674 * 10**(-11) * 1.9891 * 10**30)
mu_j = float(6.674 * 10**(-11) * 1.899 * 10**27)
mu_sat = float((6.674 * 10**(-11) * 5.683 * 10**26))
R_sat = float(1.4267254*10**12)
R_t  = 149597870691
R_j = 778412026000

#paràmetres de l'òrbita heliocèntrica de la Terra a Júpiter
Vhp_1 = 38857.39912 #calculada fora del codi
h_1 = Vhp_1 * R_t
e_1 = -1+(h_1**2)/(mu_sol*R_t)
AV_jupiter_1 = 2*numpy.pi - 2.855610116 #anomalia verdadera amb què s'intercepta Júpiter

#components de la velocitat d'excés (respecte Júpiter)
Vinf_rad_1 = (mu_sol/h_1) * e_1*numpy.sin(AV_jupiter_1)
Vinf_tan_1 = (mu_sol/h_1) * (1 + e_1*numpy.cos(AV_jupiter_1)) - numpy.sqrt(mu_sol/R_j)

Vinf_1_modulo = numpy.sqrt(Vinf_tan_1**2 + Vinf_rad_1**2)

def delta(rp): #angle de gir en funció del radi del periapsi

	delta = 2*(numpy.arcsin(1/(1+((Vinf_1_modulo**2)*rp)/mu_j)))

	return delta

#components de la velocitat de sortida respecte el sol un cop aplicada la matriu de gir (funció del radi del periapsi de la hipèrbola al voltant de Júpiter):

def Vinf_rad_2(rp): 
	
	Vinf_rad_2 = Vinf_rad_1 * numpy.cos(delta(rp)) - Vinf_tan_1 * numpy.sin(delta(rp))
	
	return Vinf_rad_2

def Vinf_tan_2(rp):

	Vinf_tan_2 = Vinf_rad_1 * numpy.sin(delta(rp)) + Vinf_tan_1*numpy.cos(delta(rp)) + numpy.sqrt(mu_sol/R_j)

	return Vinf_tan_2

def Vinf_2_modulo (rp): #mòdul de la velocitat de sortida

	Vinf_2_modulo = numpy.sqrt((Vinf_tan_2(rp))**2+Vinf_rad_2(rp)**2)

	return Vinf_2_modulo

def Emec_2(rp): #energia mecànica respecte el sol de l'òrbita de sortida. Cal saber si és positiva o negativa per assegurar-nos que no escapem del Sistema Solar
                #(funció del radi del periapsi de la hipèrbola al voltant de Júpiter)
	Emec_2 = 0.5*(Vinf_2_modulo(rp))**2 - mu_sol/R_j

	return Emec_2

#paràmetres de l'òrbita heliocèntrica de sortida
#(funció del radi del periapsi de la hipèrbola al voltant de Júpiter)

def a_2 (rp): #semieix major

	a_2 = -mu_sol/(2*Emec_2(rp))

	return a_2


def h_2(rp): #moment angular

	h_2 = R_j * Vinf_tan_2(rp)

	return h_2

def e_2(rp): #excentricitat

	e_2 = numpy.sqrt(1-((h_2(rp))**2)/(a_2(rp)*mu_sol))

	return e_2

def AV_2_salida (rp): #anomalia verdadera

	AV_2_salida = numpy.arccos((1/e_2(rp))*((h_2(rp)**2)/(mu_sol*R_j)-1))

	if Vinf_rad_2 < 0: return (numpy.pi - AV_2_salida)

	else: return AV_2_salida

#equació de la distància al focus (Sol) de la nova òrbita. Funció del periapsi de la hipèrbola seguida al voltant de Júpiter i de l'anomalia de la nova òrbita

def r_2(rp,AV): 

	r_2 = (h_2(rp)**2/mu_sol)/(1+e_2(rp)*numpy.cos(AV))

	return r_2

#equació el resultat de la qual volem que sigui zero. La distància màxima al focus de la nova òrbita (afeli, anomalia=pi) ha de ser igual al radi orbital de Saturn. 

def final(rp):

	final = R_sat - r_2(rp,numpy.pi)

	return final

rp = 70000000 #radi de saturn. No es pot fer un flyby a una distància inferior.
a = final(rp) #càlcul de la funció "final amb l'rp més baix possible"

if a<0: # la nova òrbita sobrepassa Saturn. S'augmentarà rp fins que s'hi quedi
    
    while a < 0:
	
	    a = final(rp)
	    rp = rp + 10000 #salt de 10km. Poc precís, per a un processament ràpid.
	
    print (rp)

    while a>0:
        
        a = final (rp)
        rp = rp - 10 #salt de 10m. Molt precís. Começa a computar amb valors pròxims a la solució
    
    
    
elif a>0: # la nova òrbita no arriba a Saturn. S'augmentarà rp fins que hi arribi
    
    b = Emec_2(rp)
    print ("Emec rp min: ", Emec_2(rp)) #Comprovem si amb rp mínim la nova òrbita s'escapa del Sistema Solar
    
    while b>0: #Augmentem rp fins que la nova òrbita sigui el·líptica
        b = Emec_2(rp)
        rp = rp + 10000 
        
    print ("rp min no esc: ", rp) #rp mínim per no escapar-se del Sistema Solar
    print (final(rp))
    
    a = final (rp) #Càlcul de la funció "final" per al valor d'rp acabat de calcular
    
    if a>0: # la nova òrbita no arriba a Saturn. S'augmentarà rp fins que hi arribi
        while a > 0:
            a = final(rp)
            rp = rp + 10000
            
        while a<0:
	        a = final(rp)
	        rp = rp - 10
	    
    elif a<0: # la nova òrbita sobrepassa Saturn. S'augmentarà rp fins que s'hi quedi
        while a < 0:
	        a = final(rp)
	        rp = rp + 10000
	        
        while a>0:
            a = final(rp)
            rp = rp - 10
    

print ("rp: ",rp) #el rpograma dona el valor final del radi del periapsi necessari al voltant de Júpiter per arribar a Saturn a la òrbita de sortida.
print ("delta: ",delta(rp)) #angle de gir al voltant de Júpiter
print ("e_h: ", (1+((Vinf_1_modulo**2)*rp)/mu_j) ) #Excentricitat de la hipèrbola al voltant de Júpiter
print ("Vinf h: ", Vinf_1_modulo) #Velocitat d'excés respecte Júpiter
print ("V_2 sol: ", Vinf_2_modulo(rp)) #Velocitat de sortida respecte el sol

print ("Vrad 2: ", Vinf_rad_2(rp)) #Velocitat radial de sortida. Cal saber-ne el signe per interpretar correctament la orientació de la nova òrbita
print ("e_2: ", e_2 (rp)) #excentricitat de la nova òrbita
print ("a_2: ", a_2(rp)) #semieix major de la nova òrbita
print ("Emec_2: ", Emec_2(rp)) #Energia mecànica de la nova òrbita
print ("h_2: ",h_2(rp)) #moment angular
print ("final: ",final (rp)) #valor de la funció "final amb l'rp calculat. Ha de ser el més proper a zero possible"
print ("afelio2: ", r_2(rp,numpy.pi)) #afeli de la nova òrbita. Ha de ser igual al radi orbital de Saturn
print ("Rsat: ", R_sat) #Radi orbital de Saturn

print ("Vel_afeli_2: ", (mu_sol/h_2(rp)) * (1 + e_2(rp)*numpy.cos(numpy.pi)))

print ("Vsat: ", numpy.sqrt(mu_sol/R_sat))

#print ("afeli max: ",r_2(432590000,numpy.pi))
