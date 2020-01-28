#include <iostream>
#include <stdio.h>
#include <math.h>
using namespace std;

int main(){
	
	/* Per al càlcul del temps, s'empraran les LLeis de Kepler.
	   Les òrbites el·líptiques al voltant d'un mateix astre tenen un període que únicament depèn del semieix major (Tercera llei de Kepler).
	   A més a més, la segona llei de Kepler descriu que en temps iguals, un cos celestial en ˜rbita escombra àrees iguals.
	   Mitjançant els paràmetres de la el·lipse calculats mitjançant els programes anteriors, es podrà obtenir l'àrea total i el període.
	   Tot seguit, s'utilitzarà un programa CAD per dibuixar les el·lipses i calcular de forma fàcil l'àrea recorreguda pel cos.
	   Amb totes aquestes dades, només s'haurà fer un a regla de 3 per a obtenir el temps emprat (Aplicaclbe ja que la relació és lineal).	
	*/
	
	double a; // semieix major el·lipse (m)
	double e; // excentricitat el·lipse 
	double c; // semidistància focal el·Lipse (m)
	double b;  //semieix menor el·lipse (m)
	double beta; // angle anomalia	(si partim d'una posició ja amb anomalia s'hauràn de fer les correccions necessàries)
	double mu_sol=6.674*pow(10,-11)*1.9891*pow(10,30); // mu_sol (m^3/s^2)
	double T; // període (s)
	double areatotal; // àrea de la el·lipse (m^2)
	double area; //àrea que recórre el cos (UA)
	double pi=3.14159;
	double R_t=149600000000; // radi de la terra (m)
	
	
	//Introducció de les dades conegudes de la el·lipse i la posició de la nau
	
	cout<<"Introdueix a="; 
	cin>>a;
	cout<<"Introdueix e=";
	cin>>e;
	cout<<"Introdueix angle=";
	cin>>beta;
	
	c=e*a;
	b=sqrt(pow(a,2)-pow(c,2));

	//Informació necessària per a dibuixar la el·lipse en UA i graus decimals (La conversió es realitza per a tractar amb dades més reduides i fàcils de treballar)

	cout<<"a="<<a/R_t<<"	b="<<b/R_t<<"	angle="<<beta*360/(2*pi)<<endl; 
	cout<<"a+c="<<a/R_t+c/R_t<<"	a-c="<<a/R_t-c/R_t<<endl;
	areatotal=pi*a*b;
		
	//Període de la el·lipse
	
	T=sqrt(4*pow(pi,2)*pow(a,3)/mu_sol);
	
	//Conversió de segons a anys, dies, hores, minuts
	
	cout<<"Periode="<<T<<"    "<<int(T/(365*24*60*60))<<" anys  "<<int((T/(365*24*60*60)-int(T/(365*24*60*60)))*365)<<" dies  "<<
	int(((T/(365*24*60*60)-int(T/(365*24*60*60)))*365-int((T/(365*24*60*60)-int(T/(365*24*60*60)))*365))*60)<<" hores  "<<
	int((((T/(365*24*60*60)-int(T/(365*24*60*60)))*365-int((T/(365*24*60*60)-int(T/(365*24*60*60)))*365))*60-int(((T/(365*24*60*60)-int(T/(365*24*60*60)))*365-int((T/(365*24*60*60)-int(T/(365*24*60*60)))*365))*60))*60)<<" minuts	"<<
	endl;
	cout<<"Area total="<<areatotal/pow(R_t,2)<<endl;
	
	// Un cop dibuixada la el·lipse, es pot determinar l'àrea recorreguda que s'introduirà a continuació
	
	cout<<"Introdueix area recorreguda:";
	cin>>area;
	area=area*pow(R_t,2);
	T=(area*T/areatotal);
	
	// temps emprat en el recorregut dins aquella òrbita
	
	cout<<"temps emprat="<<T<<"    "<<int(T/(365*24*60*60))<<" anys  "<<int((T/(365*24*60*60)-int(T/(365*24*60*60)))*365)<<" dies  "<<
	int(((T/(365*24*60*60)-int(T/(365*24*60*60)))*365-int((T/(365*24*60*60)-int(T/(365*24*60*60)))*365))*24)<<" hores  "<<
	int((((T/(365*24*60*60)-int(T/(365*24*60*60)))*365-int((T/(365*24*60*60)-int(T/(365*24*60*60)))*365))*24-int(((T/(365*24*60*60)-int(T/(365*24*60*60)))*365-int((T/(365*24*60*60)-int(T/(365*24*60*60)))*365))*24))*60)<<" minuts	"<<
	endl;
	
};

// Per a saber el temps total de viatge, és necessari calcular el temps emprat en l'el·lipse Terra-Júpiter i sumar-li el temps de la el·lipse Júpiter-Saturn. S'introdueixen les dades de les dues elálipses al programa i es sumen els temps calculats per aix’ obtenir el temps total de vol.
