---
title: "I numeri primi finiscono?"
---

(r-sec-infiniti-primi)=

*Lezione: 28 settembre*

### Un numero che sfugge all'elenco

Prendi i primi $2,3,5$ e costruisci $2\cdot3\cdot5+1$.
Quale resto ottieni dividendolo per ciascuno di quei primi?
Ripeti con $2,3,5,7,11,13$. Il numero costruito deve essere primo,
oppure potrebbe avere un divisore primo che non hai elencato?

(r-teo-infiniti-primi)=

:::{important} Teorema — Infinità dei numeri primi (Euclide)

I numeri primi sono infiniti.
:::

:::{admonition} Dimostrazione
:class: tip

Supponiamo per assurdo che i primi siano in numero finito e che
l'elenco completo sia $p_1,p_2,\ldots,p_k$. Costruiamo

$$
M=p_1p_2\cdots p_k+1.
$$

Dividendo $M$ per ciascun $p_i$ otteniamo resto $1$:
nessuno dei primi dell'elenco divide $M$.
Ma $M>1$, quindi, per il teorema fondamentale dell'aritmetica,
ha almeno un divisore primo $q$. Questo primo non può essere
nessuno dei $p_i$: contraddice l'ipotesi che l'elenco fosse completo.
I numeri primi, dunque, non possono essere finiti.
:::

:::{note} Attenzione al passaggio

Non abbiamo dimostrato che
$M$ sia sempre primo. Per esempio
$2\cdot3\cdot5\cdot7\cdot11\cdot13+1=30031=59\cdot509$.
Ci basta un suo divisore primo fuori dall'elenco.
:::


## Materiali per questa lezione

- [Gara prime — testo](/materiali/gara-prime-testo.pdf)

:::{dropdown} Soluzioni della gara
[Scarica le soluzioni](/materiali/gara-prime-soluzioni.pdf)
:::
