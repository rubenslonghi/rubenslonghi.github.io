---
title: "La regola di Ruffini per dividere"
---

*Per richiamare le idee già viste:* [Leggere e trasformare le espressioni algebriche](../algebra/index.md) · [Classi di equivalenza e partizioni](../relazioni-grafi/classi-di-equivalenza-e-partizioni.md).


(r-sec-dp-ruffini-regola)=

:::{admonition} Attività — Lavorare solo con i coefficienti
:class: attention

Sviluppa $(x-2)(x^2-4x+3)$. Confronta i coefficienti ottenuti con
quelli di $x^3-6x^2+11x-6$. Riesci a ricostruire i coefficienti del
quoziente, da sinistra a destra, usando il numero $2$?
:::

La **regola di Ruffini** è un procedimento rapido per dividere
per $x-a$. È distinta dal teorema del fattore: il teorema spiega
quando il resto è zero; la regola calcola quoziente e resto.

Scrivi i coefficienti in ordine decrescente, includendo gli zeri.
Riporta il primo; moltiplica ogni risultato per $a$ e somma il
prodotto al coefficiente successivo. L'ultimo numero è il resto;
i precedenti sono i coefficienti del quoziente.

|  | $1$ | $-6$ | $11$ | $-6$ |
| --- | --- | --- | --- | --- |
| $2$ |  | $2$ | $-8$ | $6$ |
|  | $1$ | $-4$ | $3$ | $0$ |

Quindi $S=x^2-4x+3$, $R=0$.
Perché funziona? In $(x-a)S+r$ il coefficiente iniziale di $S$
coincide con quello di $P$; ogni coefficiente successivo deve
compensare il prodotto $-a$ per quello precedente.
Le somme dello schema realizzano esattamente questo confronto.

La forma ordinaria dello schema vale per $x-a$. Per $2x-4=2(x-2)$
puoi prima dividere per $x-2$, poi dividere il quoziente per $2$:
il resto rimane lo stesso. Per divisori di grado maggiore usiamo
la divisione generale.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-dp-schema-es)=
### Zeri mancanti e segni

Usa la regola e controlla ricostruendo $P$:
$x^3+2x-3$ diviso per $x-1$;
$x^3+1$ diviso per $x+1$;
$x^2+1$ diviso per $x-2$.
Quale numero metti a sinistra dello schema nel secondo caso?

:::{dropdown} Mostra la soluzione

I coefficienti del primo dividendo sono $1,0,2,-3$:
$S=x^2+x+3$, $R=0$.
Nel secondo si usa $-1$: $S=x^2-x+1$, $R=0$.
Nel terzo $S=x+2$, $R=5$.
:::
