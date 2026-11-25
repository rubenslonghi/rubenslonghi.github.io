---
title: "Divisibilità e teorema del resto"
---

*Per richiamare le idee già viste:* [Leggere e trasformare le espressioni algebriche](../algebra/index.md) · [Classi di equivalenza e partizioni](../relazioni-grafi/classi-di-equivalenza-e-partizioni.md).


(r-sec-dp-resto)=

:::{admonition} Attività — Il resto senza tutta la divisione
:class: attention

Nell'identità $P=(x-2)S+r$, sostituisci $x=2$.
Quale parte scompare? Per $P=x^3+2x+1$, prova a prevedere il resto
della divisione per $x-2$ senza cercare prima il quoziente.
:::

(r-def-dp-divisore)=

:::{note} Definizione — Divisore e multiplo di un polinomio

Per $Q\ne0$, diciamo che $Q$ **divide** $P$, e scriviamo $Q\mid P$,
se esiste un polinomio $S$ tale che $P=QS$.
Questo equivale ad avere resto zero nella divisione per $Q$.
:::

(r-teo-dp-resto)=

:::{important} Teorema — Teorema del resto

Il resto della divisione di $P(x)$ per $x-a$ è il numero $P(a)$.
:::

:::{admonition} Dimostrazione
:class: tip

Il divisore ha grado $1$, quindi il resto è una costante $r$.
Da $P(x)=(x-a)S(x)+r$, sostituendo $x=a$, otteniamo $P(a)=r$.
:::

Nell'attività $P(2)=8+4+1=13$. La congruenza modulo $x-a$ conserverà
quindi soltanto il valore assunto dal polinomio in $a$.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-dp-resto-es)=
### Calcolare soltanto ciò che serve

Senza effettuare la divisione, trova il resto di $P=x^3-2x+4$
per $x-1$, $x+1$ e $x-2$. Un compagno, per il divisore $x+1$,
calcola $P(1)$: quale segno ha dimenticato?

:::{dropdown} Mostra la soluzione

I resti sono $P(1)=3$, $P(-1)=5$, $P(2)=8$.
$x+1=x-(-1)$: bisogna sostituire $-1$.
:::
