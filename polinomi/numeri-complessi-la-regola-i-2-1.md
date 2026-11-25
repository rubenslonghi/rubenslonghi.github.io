---
title: "Numeri complessi: la regola i²= −1"
---

*Per richiamare le idee già viste:* [Leggere e trasformare le espressioni algebriche](../algebra/index.md) · [Classi di equivalenza e partizioni](../relazioni-grafi/classi-di-equivalenza-e-partizioni.md).


(r-sec-dp-complessi)=

:::{admonition} Attività — Un nuovo nome per la classe di $x$
:class: attention

Modulo $x^2+1$, calcola il resto di $x^2$, $x^3$ e $x^4$.
Ora chiama $i$ la classe di $x$. Come scriveresti i risultati?
Prova a moltiplicare $(1+i)(1-i)$ usando la distributiva.
:::

**Laboratorio di approfondimento.** Bastano coppie di numeri,
calcolo letterale e la regola scoperta; non occorrono radici di
polinomi di grado alto o formule trigonometriche.

(r-def-dp-complesso)=

:::{note} Definizione — Forma algebrica di un numero complesso

Un **numero complesso** si scrive $a+bi$, con $a,b\in\R$,
e si calcola con la regola $i^2=-1$.
Due complessi sono uguali quando hanno uguali entrambe le componenti.
La **parte reale** è $a$, la **parte immaginaria** è $b$.
:::

Il simbolo $i$ non indica un reale: il quadrato di un reale non è
negativo. La costruzione con le classi assicura invece un significato
coerente alla nuova regola: $i=[x]$ in $\R[x]/(x^2+1)$.

$$
\begin{aligned}
(a+bi)+(c+di)&=(a+c)+(b+d)i,\\
(a+bi)(c+di)&=(ac-bd)+(ad+bc)i.
\end{aligned}
$$

Queste formule sono semplicemente i resti della somma e del prodotto
di $a+bx$ e $c+dx$ modulo $x^2+1$.
In particolare $(1+2i)(3-i)=5+5i$.

### Il piano di Gauss

Rappresentiamo $a+bi$ con il punto $(a,b)$: asse orizzontale per la
parte reale, verticale per quella immaginaria.
Sommare significa sommare le coordinate.
Moltiplicare per $i$ manda $(a,b)$ in $(-b,a)$: è un quarto di giro
in senso antiorario. Le potenze $1,i,-1,-i,1,\ldots$ formano un ciclo.
Il piano dei resti della sezione precedente si legge così come piano complesso.

### Coniugato e divisione

Il **coniugato** di $z=a+bi$ è $\overline z=a-bi$.
$z\overline z=a^2+b^2$, positivo se $z\ne0$.
Perciò ogni complesso non nullo ha un inverso:

$$
\frac1{a+bi}=\frac{a-bi}{a^2+b^2}.
$$

Per esempio $1/(1+i)=(1-i)/2$. Moltiplicare per il coniugato
consente di dividere senza lasciare $i$ nel denominatore.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-dp-complessi-es)=
### Calcolare e rappresentare

Calcola $(2+i)+(1-3i)$, $(2+i)(1-3i)$, $i^7$ e $(1+i)^2$.
Disegna i punti di $z=2+i$ e di $iz$. Verifica che $i$ e $-i$
risolvono $z^2+1=0$.

:::{dropdown} Mostra la soluzione

$3-2i$, $5-5i$, $-i$, $2i$.
I punti sono $(2,1)$ e $(-1,2)$.
$i^2=(-i)^2=-1$, quindi entrambi soddisfano l'equazione.
:::

(r-dp-complessi-inverso)=
### Verificare un inverso

Trova l'inverso di $2+i$ e controlla che il prodotto sia $1$.
Può esistere un complesso non nullo il cui quadrato sia zero?

:::{dropdown} Mostra la soluzione

L'inverso è $(2-i)/5$. Il prodotto è $(4+1)/5=1$.
Se $z\ne0$ e $z^2=0$, moltiplicando per il suo inverso si avrebbe
$z=0$, una contraddizione. Quindi non può esistere.
:::
