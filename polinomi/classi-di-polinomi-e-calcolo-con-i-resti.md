---
title: "Classi di polinomi e calcolo con i resti"
---

*Per richiamare le idee già viste:* [Leggere e trasformare le espressioni algebriche](../algebra/index.md) · [Classi di equivalenza e partizioni](../relazioni-grafi/classi-di-equivalenza-e-partizioni.md).


(r-sec-dp-quoziente)=

:::{admonition} Attività — Ridurre prima o dopo?
:class: attention

Modulo $x^2+1$, riduci $(x^2+3)+x$ e $(x^2+3)x$.
Poi sostituisci prima $x^2+3$ con il suo resto $2$ e ripeti.
Ottieni gli stessi resti? Quale strada richiede meno calcoli?
:::

La classe di un polinomio $P$ contiene tutti i polinomi

$$
[P]=\{P+QS:S\in\R[x]\}.
$$

Qui $\R[x]$ è l'insieme dei polinomi a coefficienti reali.
Ogni classe ha un unico rappresentante di grado minore di $\deg Q$,
oppure il rappresentante zero: è il resto della divisione.
La notazione del quoziente è $\R[x]/(Q)$; $(Q)$ indica
*tutti i multipli* di $Q$, non il solo polinomio $Q$.
Il nome tecnico di questo insieme di multipli è *ideale generato da $Q$*.

Somma e prodotto fra classi si calcolano sommando o moltiplicando
i rappresentanti e prendendo il resto. La scelta del rappresentante
non cambia il risultato: sostituire $P$ con $P+QS$ aggiunge alla somma
un multiplo di $Q$ e al prodotto con $T$ il multiplo $QST$.

(r-es-dp-prodotto-resti)=

:::{tip} Esempio — Un prodotto nel mondo dei resti

Modulo $x^2+1$, $[x]^2=[-1]$ e

$$
(1+x)(2+x)=2+3x+x^2\equiv1+3x\pmod{x^2+1}.
$$

Modulo $x^2$, invece, lo stesso prodotto ha resto $2+3x$.
Lo stesso insieme di rappresentanti $a+bx$ può avere moltiplicazioni
diverse, perché cambia il polinomio scelto come modulo.
:::

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-dp-resti-es)=
### Un modulo, una regola

Trova i resti di $x^4+2x^3+3$ modulo $x^2+1$ e modulo $x^2$.
Poi riduci $(2+x)(3-x)$ nei due mondi. Infine descrivi la classe
del polinomio $1+x$ modulo $x^2+1$ con tre rappresentanti diversi.

:::{dropdown} Mostra la soluzione

I primi resti sono $4-2x$ e $3$.
Il prodotto ordinario è $6+x-x^2$: resti $7+x$ e $6+x$.
Possibili rappresentanti sono $1+x$, $2+x+x^2$,
$1+2x+x^3$, ottenuti aggiungendo rispettivamente $0$, $Q$ e $xQ$.
:::
