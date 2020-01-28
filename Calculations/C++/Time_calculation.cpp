#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

int main(){
	
	/* Per al c�lcul del temps, s'empraran les LLeis de Kepler.
	   Les �rbites el�l�ptiques al voltant d'un mateix astre tenen un per�ode que �nicament dep�n del semieix major (Tercera llei de Kepler).
	   A m�s a m�s, la segona llei de Kepler descriu que en temps iguals, un cos celestial en �rbita escombra �rees iguals.
	   Mitjan�ant els par�metres de la el�lipse calculats mitjan�ant els programes anteriors, es podr� obtenir l'�rea total i el per�ode.
	   Tot seguit, s'utilitzar� un programa CAD per dibuixar les el�lipses i calcular de forma f�cil l'�rea recorreguda pel cos.
	   Amb totes aquestes dades, nom�s s'haur� fer un a regla de 3 per a obtenir el temps emprat (Aplicaclbe ja que la relaci� �s lineal).	
	*/
	
	double a; // semieix major el�lipse (m)
	double e; // excentricitat el�lipse 
	double c; // semidist�ncia focal el�Lipse (m)
	double b;  //semieix menor el�lipse (m)
	double beta; // angle anomalia	(si partim d'una posici� ja amb anomalia s'haur�n de fer les correccions necess�ries)
	double mu_sol=6.674*pow(10,-11)*1.9891*pow(10,30); // mu_sol (m^3/s^2)
	double T; // per�ode (s)
	double areatotal; // �rea de la el�lipse (m^2)
	double area; //�rea que rec�rre el cos (UA)
	double pi=3.14159;
	double R_t=149600000000; // radi de la terra (m)
	
	
	//Introducci� de les dades conegudes de la el�lipse i la posici� de la nau
	
	cout<<"Introdueix a="; 
	cin>>a;
	cout<<"Introdueix e=";
	cin>>e;
	cout<<"Introdueix angle=";
	cin>>beta;
	
	c=e*a;
	b=sqrt(pow(a,2)-pow(c,2));

	//Informaci� necess�ria per a dibuixar la el�lipse en UA i graus decimals (La conversi� es realitza per a tractar amb dades m�s reduides i f�cils de treballar)

	cout<<"a="<<a/R_t<<"	b="<<b/R_t<<"	angle="<<beta*360/(2*pi)<<endl; 
	cout<<"a+c="<<a/R_t+c/R_t<<"	a-c="<<a/R_t-c/R_t<<endl;
	areatotal=pi*a*b;
		
	//Per�ode de la el�lipse
	
	T=sqrt(4*pow(pi,2)*pow(a,3)/mu_sol);
	
	//Conversi� de segons a anys, dies, hores, minuts
	
	cout<<"Periode="<<T<<"    "<<int(T/(365*24*60*60))<<" anys  "<<int((T/(365*24*60*60)-int(T/(365*24*60*60)))*365)<<" dies  "<<
	int(((T/(365*24*60*60)-int(T/(365*24*60*60)))*365-int((T/(365*24*60*60)-int(T/(365*24*60*60)))*365))*60)<<" hores  "<<
	int((((T/(365*24*60*60)-int(T/(365*24*60*60)))*365-int((T/(365*24*60*60)-int(T/(365*24*60*60)))*365))*60-int(((T/(365*24*60*60)-int(T/(365*24*60*60)))*365-int((T/(365*24*60*60)-int(T/(365*24*60*60)))*365))*60))*60)<<" minuts	"<<
	endl;
	cout<<"Area total="<<areatotal/pow(R_t,2)<<endl;
	
	// Un cop dibuixada la el�lipse, es pot determinar l'�rea recorreguda que s'introduir� a continuaci�
	
	cout<<"Introdueix area recorreguda:";
	cin>>area;
	area=area*pow(R_t,2);
	T=(area*T/areatotal);
	
	// temps emprat en el recorregut dins aquella �rbita
	
	cout<<"temps emprat="<<T<<"    "<<int(T/(365*24*60*60))<<" anys  "<<int((T/(365*24*60*60)-int(T/(365*24*60*60)))*365)<<" dies  "<<
	int(((T/(365*24*60*60)-int(T/(365*24*60*60)))*365-int((T/(365*24*60*60)-int(T/(365*24*60*60)))*365))*24)<<" hores  "<<
	int((((T/(365*24*60*60)-int(T/(365*24*60*60)))*365-int((T/(365*24*60*60)-int(T/(365*24*60*60)))*365))*24-int(((T/(365*24*60*60)-int(T/(365*24*60*60)))*365-int((T/(365*24*60*60)-int(T/(365*24*60*60)))*365))*24))*60)<<" minuts	"<<
	endl;
	
};

// Per a saber el temps total de viatge, �s necessari calcular el temps emprat en l'el�lipse Terra-J�piter i sumar-li el temps de la el�lipse J�piter-Saturn. S'introdueixen les dades de les dues el�lipses al programa i es sumen els temps calculats per aix� obtenir el temps total de vol.
