#EJEMPLO_1 
q = 3;
t = 2;
x = 5 + 3 + t + q;
x = 8 + t + q;
print("EJEMPLO_1")
print(x);
#OPTIMIZACION LOCAL
q = 3;
t = 2;
x = 8 + t + q;
print(x);
#se remplaza la expresion x = 5 + 3 + t + q; por el resultado de x = 8 + t + q;
#por que se puede evaluar entiempo de ejecucion y es optimizacion local.

#EJEMPLO_2
x= 1;
y= 2;
x = x * 0;
y = y**2;
print("EJEMPLO_2")
print(x,y);  
#OPTIMIZACION LOCAL
y= 2;
x = 0;
y = y * y;
print(x,y);  
#algunas de las declaraciones se pueden sinplificar,
#asi eleminar algunas delcaraciones,simplificacion algebraica.

#EJEMPLO_3
a = 5;
x = 2 * a;
y = x + 6;
print("EJEMPLO_3")
print(x,y);
#optimizacion local
a=5;
x=10;
y=16;
print(x,y);
#este ejemplo propaga el codigo y recuce las constantes
#de las vaiables que esta utilizando.

#EJEMPLO_4
print("EJEMPLO_4")
z=2;
y=2;
x=z+y;
a=x;
x= 2*a;
print(x);
#optimizacion Local
z=2;
y=2;
b=z+y;
x=2*b;
print(x);
#en el ejemplo la optimizacion elimina codigo muerto osea que
#no contribuye al resultado de la operacion.

#EJEMPLO_5
y=1;
z=1;
x=y+z;
w=y+z;
print("EJEMPLO_5")
print(w);
#OPTIMIZACION LOCAL
x=y+z;
w=x;
print(w);
#el ejmplo muestra como se eliminan las subexpresiones comunes donde estan calculando
#el mismo valor pero se eliminan

#EJEMPLO_6
i=1;
c=2;
m=2;
a=3+i;
f=a;
b=f+c;
d=a+m;
m=f+d;
print("EJEMPLO_6")
print(m);
#OPTIMIZACION LOCAL
i=1;
c=2;
m=2;
a=3+i;
b=a+c;
d=a+m;
m=a+d;
print(m);

#EJEMPLO_7
print("EJEMPLO_7")
a=2;
b=2;
a = a * 1;
b = b * 0;
print(a,b);
#OPTIMIZACION DE CICLOS
a = a * 1;
b = 0;
print(a,b);
#este ejemplo es optimizacion de mirrilla por que elimina 
#instrucciones inutiles por medio de un conjunto de reglas de remplazamiento.