*/
//EJEMPLO_8
//OPTIMIZACION DE CICLOS(BUCLES)
for (i=0; i<4; i++){
    a[i] = 0;
}
/*expasion de bucles (loop unroolling)
este aplica al bucle que conoce  el numero de 
interaciones en tiempo de compilacion*/

/*EJEMPLO_9
OPTIMIZACION DE CICLOS (REDUCCION DE FRECUENCIA)*/

while (i< (limite*2-1)){

}
/*detecta las operaciones invariantes (+,-,*,/,sin,ln) de bucle y las calcula
una vez delante del bucle.
*/

/*EJEMPLO_10
OPTIMIZACION DE CICLOS (REDUCCION DE POTENCIA)
*/
i = 1;
while i<-1000 do{
    a = 4 *i + 3;
    b = 2 * i;

    i = i + 1;
}
/*aplica para las operaciones que cumplen con
solo calcular el resultado, el resultado depende de los operandos
que se consideran operaciones invariantes de bucle.
*/
