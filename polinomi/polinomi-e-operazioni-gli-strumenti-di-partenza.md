---
title: "Polinomi e operazioni: gli strumenti di partenza"
---

*Per richiamare le idee già viste:* [Leggere e trasformare le espressioni algebriche](../algebra/index.md) · [Classi di equivalenza e partizioni](../relazioni-grafi/classi-di-equivalenza-e-partizioni.md).


(r-sec-dp-strumenti)=

:::{admonition} Attività — Quanti dati servono per descrivere una scrittura?
:class: attention

Confronta $3+2x+x^2$, $x^2+3+2x$, $3+2x+0x^2$.
Quali sono lo stesso polinomio? Scrivi per ciascuno i coefficienti
del termine costante, di $x$ e di $x^2$. Poi calcola il valore per $x=2$.
:::

(r-def-dp-polinomio)=

:::{note} Definizione — Polinomio in una variabile e grado

Un **polinomio in $x$** è una somma finita di termini $a_kx^k$,
con coefficienti numerici ed esponenti naturali.
Per un polinomio non nullo il **grado** è il più grande esponente
con coefficiente non nullo. Il grado di una costante non nulla è $0$;
al polinomio nullo qui non assegniamo un grado.
:::

Il polinomio $2x^3-x+4$ si può scrivere come $2x^3+0x^2-x+4$.
I coefficienti mancanti sono zero: non si deve saltare il loro posto.
Due polinomi sono uguali se, una volta raccolti i termini simili,
hanno gli stessi coefficienti per ogni potenza di $x$.
Il valore $P(2)$, invece, si ottiene sostituendo $2$ a $x$.
L'uguaglianza $P(2)=S(2)$ da sola non implica $P=S$.

Per sommare e sottrarre si combinano i coefficienti dei termini simili;
per moltiplicare si usa la distributiva e $x^mx^n=x^{m+n}$.

(r-es-dp-operazioni)=

:::{tip} Esempio — Ridurre e sviluppare

$$
\begin{aligned}
(2x^2+3x-1)+(x^2-x+4)&=3x^2+2x+3,\\
(2x^2+3x-1)-(x^2-x+4)&=x^2+4x-5,\\
(x+1)(x+2)&=x^2+3x+2.
\end{aligned}
$$
:::

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-dp-strumenti-es)=
### Preparare il calcolo

1. Ordina $4-2x+x^3$, scrivi anche il coefficiente mancante e calcola $P(2)$.

2. Sviluppa $(x-2)(x+3)$ e $(2x+1)(x-1)$.

3. Per $P=x^2$ e $S=2x$, verifica $P(2)=S(2)$ e spiega perché
    non sono lo stesso polinomio.

:::{dropdown} Mostra la soluzione

$P=x^3+0x^2-2x+4$, $P(2)=8$.
I prodotti sono $x^2+x-6$ e $2x^2-x-1$.
$P(2)=S(2)=4$, ma i coefficienti sono diversi;
anche $P(1)=1$ e $S(1)=2$ mostrano che i valori non coincidono sempre.
:::
