---
title: "Quante coordinate rimangono?"
---

*Per richiamare le idee già viste:* [Leggere e trasformare le espressioni algebriche](../algebra/index.md) · [Classi di equivalenza e partizioni](../relazioni-grafi/classi-di-equivalenza-e-partizioni.md).


(r-sec-dp-coordinate)=

:::{admonition} Attività — Il grado del modulo decide il formato
:class: attention

Quale forma può avere il resto dividendo per un polinomio di grado
$1$, $2$, $3$? Quanti coefficienti devi comunicare per descriverlo,
anche quando alcuni sono zero? Il numero di classi è finito?
:::

Se $Q$ ha grado $d\ge1$, ogni classe si descrive univocamente con
un resto

$$
a_0+a_1x+\cdots+a_{d-1}x^{d-1}.
$$

Servono $d$ coordinate reali. Ci sono però infinite classi:
già le costanti reali forniscono infinite scelte diverse.
Questo distingue il quoziente dei polinomi dall'orologio modulo $7$,
che ha soltanto sette classi.

| Modulo | Forma del resto | Coordinate |
| --- | --- | --- |
| $x-a$ | costante | una |
| $x^2+1$ | $a+bx$, con $x^2\equiv-1$ | due |
| $x^2$ | $a+bx$, con $x^2\equiv0$ | due |
| $x^3$ | $a+bx+cx^2$ | tre |

Nel linguaggio degli spazi vettoriali, che non è necessario padroneggiare
ora, si dice che $\R[x]/(Q)$ ha *dimensione $d$*.
L'insieme di tutti i polinomi richiede invece arbitrariamente tanti
coefficienti: non c'è un limite al grado.
Quozientare modulo $Q$ identifica tutti i suoi multipli con zero:
$Q,xQ,x^2Q,\ldots$. Non significa soltanto togliere una coordinata
o eliminare un unico polinomio.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-dp-sintesi-es)=
### Collegare le idee

Spiega con un esempio ciascuna distinzione:

1. uguaglianza di polinomi e congruenza;

2. quoziente $S$ di una divisione e insieme quoziente $\R[x]/(Q)$;

3. due coordinate per i complessi e due coordinate per i duali;

4. resto costante modulo $x-a$ e resto lineare modulo $(x-a)^2$.

:::{dropdown} Mostra la soluzione

1) $x^2\ne-1$, ma $x^2\equiv-1\pmod{x^2+1}$.
2) $S$ è un polinomio in $P=QS+R$; l'insieme quoziente raccoglie classi.
3) Entrambi usano coppie $(a,b)$, ma $i^2=-1$ e $\varepsilon^2=0$
producono moltiplicazioni diverse.
4) Per $P=x^2$ e $a=2$, i resti sono rispettivamente $4$ e $4x-4$.
:::
