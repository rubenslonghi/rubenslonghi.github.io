---
title: "Ruffini: radici e fattori"
---

*Per richiamare le idee già viste:* [Leggere e trasformare le espressioni algebriche](../algebra/index.md) · [Classi di equivalenza e partizioni](../relazioni-grafi/classi-di-equivalenza-e-partizioni.md).


(r-sec-dp-ruffini-teorema)=

:::{admonition} Attività — Quando il resto scompare
:class: attention

Calcola $P(1)$, $P(2)$ e $P(3)$ per
$P=x^3-6x^2+11x-6$. Quali fattori di primo grado ti aspetti?
Verifica sviluppando $(x-1)(x-2)(x-3)$.
:::

(r-teo-dp-ruffini)=

:::{important} Teorema — Teorema di Ruffini o del fattore

Il polinomio $P$ è divisibile per $x-a$ se e solo se $P(a)=0$.
Un numero $a$ con $P(a)=0$ si chiama **radice** o **zero** di $P$.
:::

:::{admonition} Dimostrazione
:class: tip

Per il teorema del resto, la divisione per $x-a$ ha resto $P(a)$.
La divisibilità equivale al fatto che quel resto sia zero.
:::

Il teorema collega una proprietà dei *valori* a una proprietà
della *scomposizione*. Non fornisce automaticamente le radici:
una volta trovata una radice, però, consente di estrarre un fattore.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-dp-radici-es)=
### Un valore che rivela un fattore

Per $P=x^2-x-6$, controlla se $-2$, $2$, $3$ sono radici e scomponi $P$.
Trova poi $k$ affinché $x^2+kx+6$ sia divisibile per $x-2$.

:::{dropdown} Mostra la soluzione

Le radici sono $-2$ e $3$; $P=(x+2)(x-3)$, mentre $P(2)=-4$.
La condizione $4+2k+6=0$ dà $k=-5$.
:::
