---
title: "Numeri duali: la regola ε²=0"
---

*Per richiamare le idee già viste:* [Leggere e trasformare le espressioni algebriche](../algebra/index.md) · [Classi di equivalenza e partizioni](../relazioni-grafi/classi-di-equivalenza-e-partizioni.md).


(r-sec-dp-duali)=

:::{admonition} Attività — Stesse coppie, un prodotto diverso
:class: attention

Questa volta lavora modulo $x^2$. Qual è il resto di $x$?
E quello di $x^2$? Chiama $\varepsilon$ la classe di $x$ e calcola
$(1+\varepsilon)^2$. Perché $\varepsilon$ non è zero,
anche se il suo quadrato lo è?
:::

**Laboratorio di approfondimento.** Confrontiamo una nuova
regola con quella dei complessi e con gli orologi del primo capitolo.

(r-def-dp-duale)=

:::{note} Definizione — Numero duale

Un **numero duale** si scrive $a+b\varepsilon$, con $a,b\in\R$,
dove $\varepsilon\ne0$ e $\varepsilon^2=0$.
Due duali sono uguali se hanno uguali le due componenti.
Questi numeri rappresentano le classi di $\R[x]/(x^2)$.
:::

Il polinomio $x$ non è multiplo di $x^2$, quindi $[x]\ne[0]$;
invece $[x]^2=[x^2]=[0]$. Da distributiva e nuova regola otteniamo

$$
\begin{aligned}
(a+b\varepsilon)+(c+d\varepsilon)&=(a+c)+(b+d)\varepsilon,\\
(a+b\varepsilon)(c+d\varepsilon)&=ac+(ad+bc)\varepsilon.
\end{aligned}
$$

Per esempio $(1+2\varepsilon)(3-\varepsilon)=3+5\varepsilon$:
il termine contenente $\varepsilon^2$ diventa zero.
La somma delle coppie è la stessa dei complessi; il prodotto cambia.

### Un numero non nullo può avere quadrato zero

Nei duali la legge di annullamento del prodotto non vale:
$\varepsilon\cdot\varepsilon=0$ con entrambi i fattori non nulli.
È un fenomeno simile a quello visto negli orologi a modulo composto,
ma qui il nuovo mondo è costruito con resti di polinomi.
$\varepsilon$ non è un reale molto piccolo e la regola non è
un'approssimazione: il suo quadrato è *esattamente* zero.

Più in generale, $a+b\varepsilon$ ha inverso se e solo se $a\ne0$:

$$
(a+b\varepsilon)^{-1}=\frac1a-\frac{b}{a^2}\varepsilon.
$$

Se $a=0$, la parte costante di qualunque prodotto rimane zero,
quindi il prodotto non può essere $1$.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-dp-duali-es)=
### Confrontare due mondi

Calcola $(2+\varepsilon)(3-2\varepsilon)$ e $(1+\varepsilon)^3$.
Confronta $(1+\varepsilon)(1-\varepsilon)$ con $(1+i)(1-i)$.
Trova l'inverso di $1+\varepsilon$. Può $\varepsilon$ avere un inverso?

:::{dropdown} Mostra la soluzione

$6-\varepsilon$, $1+3\varepsilon$.
I due prodotti sono rispettivamente $1$ e $2$.
L'inverso di $1+\varepsilon$ è $1-\varepsilon$.
Se $\varepsilon u=1$, moltiplicando per $\varepsilon$ avremmo
$0=\varepsilon$, impossibile.
:::
