[English](#english)    

## Project Euler - Problema 60 - Solución 

### *Descripción del problema
Los números primos 3, 7, 109 y 673 son bastante notables. Al tomar dos números primos cualesquiera y concatenarlos en cualquier orden, el resultado siempre será primo. Por ejemplo, tomando 7 y 9, tanto 7109 como 1097 son primos. La suma de estos cuatro primos, 792, representa la suma más baja para un conjunto de cuatro primos con esta propiedad.

Encuentre la suma más baja para un conjunto de cinco primos para los cuales dos primos cualesquiera se concatenan para producir otro primo.


### *Solución
Mi solución, no necesariamente la mejor, fue comenzar primero por encontrar cada número primo a partir del 3, ya que el 2 no cumpliría con la regla propuesta.  
Con cada primo, agrego una clave a un diccionario, cuyo valor será una lista.  
La idea es que estas listas contengan las distintas combinaciones de primos que cumplan la regla.  
Por ejemplo, para el 673 el diccionario tendra esta forma:  
[[673], [3, 673], [7, 673], [3, 7, 673], [109, 673], [3, 109, 673], [7, 109, 673], [3, 7, 109, 673], [199, 673], [109, 199, 673], [397, 673], [457, 673], [499, 673], [3, 499, 673], [613, 673], [3, 613, 673]]  
Por cada nuevo primo encontrado, busco en el diccionario las claves que cumplan la regla con ese nuevo primo.  
Cuando encuentro que cumple la regla, hay que buscar para cuales listas de esa clave, el nuevo primo cumple la regla con todos los valores de la lista.  
Luego a medida que voy encontrando esas listas dentro de una clave, las almaceno temporalmente, y cuando ya terminé de analizar una clave completa, le agrego a esa clave cada una de las listas encontrada, pero con el valor del primo agregado a cada una de estas listas.  
Volviendo al ejemplo, si el primo es el 673, y la clave que estoy recorriendo es la '3', las listas temporales serán
[[3], [3, 7], [3, 109], [3, 7, 109], [3, 499], [3, 613]]  
como se ve, en todas está el 3, que es la clave, hay más listas en la clave 3, pero no todos los números dentro cumplirán con la regla al compararlos con el 673, entonces descarto esas listas. 
Luego a esas listas les agrego el 673, y las almaceno como items nuevos en el valor de la clave '673'.  
Como última cosa importaante, cada vez que encuentro

<a name="english"></a>
## Solutions for Project Euler problems

### *Problem description
The primes 3, 7, 109, and 673, are quite remarkable. By taking any two primes and concatenating them in any order the result will always be prime. For example, taking 7 and 9, both 7109 and 1097 are prime. The sum of these four primes, 792, represents the lowest sum for a set of four primes with this property.

Find the lowest sum for a set of five primes for which any two primes concatenate to produce another prime.

### *Solution
