# Descifra_mensaje

[Pincha aqui para acceder al link de este repositorio](https://github.com/pelahumi/Descifra_mensaje.git)

---

## Cifrado Espejo

En el alfabeto contamos con 27 letras, y en el cifrado espejo cada letra se corresponde con su posición invertida en el alfabeto, es decir, la clave de la primera letra del alfabeto se corresponde con la última, es decir, la letra "A" se corresponde con la "Z", la "B" con la "Y", y así sucesivamente. 

---

## Implementación python

En primer lugar creamos una lista con todas las letras del alfabeto, a las cuales les corresponde un determinado índice (a=0, b=1, ... , z=26). Por lo tanto para realizar el cifrado espejo, hemos de invertir el signo al índice, es decir multiplicar por -1. De esta manera recorremos la lista desde atrás, obtiendo la clave correspondiente para realizar dicho cifrado. Solamente tenemos que acordarnos de un pequeño detalle, la primera posición de una lista en python es 0, pero la última es -1. Por lo tanto, tenemos restar una unidad a este algoritmo para obtener el cifrado deseado:

---

$$
\begin{aligned}
  clave = alph[-alph.index(letra)-1]
\end{aligned}
$$

Siendo alph la lista con todas las letras del alfabeto, Esta línea se repite con todas las letras de la palabra que queremos descifrar hasta obtener el mensaje cifrado
