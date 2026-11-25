---
title: "Criteri di divisibilità: leggere le cifre"
---

(r-sec-criteri)=

:::{admonition} Attività — Una divisione senza farla
:class: attention

Senza divisioni in colonna, stabilisci se $256$, $241$, $372$ e $14880$
sono divisibili per $2$, per $3$ e per $4$.
Confronta le strategie. Perché per alcuni divisori bastano le ultime
cifre, mentre per altri si sommano tutte le cifre?
:::

:::{note} I criteri usati in classe

Un naturale è divisibile:

- per $2$ se l'ultima cifra è $0,2,4,6$ oppure $8$;

- per $3$ se la somma delle cifre è divisibile per $3$;

- per $4$ se il numero formato dalle ultime due cifre è divisibile per $4$;

- per $5$ se l'ultima cifra è $0$ oppure $5$;

- per $6$ se è divisibile sia per $2$ sia per $3$;

- per $9$ se la somma delle cifre è divisibile per $9$.

- per $10$ se l'ultima cifra è $0$.

Per un numero di una sola cifra il criterio del $4$ si applica al numero stesso.
:::

(r-es-criterio-tre)=

:::{tip} Esempio — Da dove viene il criterio del tre?

Nella scrittura decimale $372=3\cdot100+7\cdot10+2$.
Poiché $100=99+1$ e $10=9+1$,

$$
372=3\cdot99+7\cdot9+(3+7+2).
$$

I primi due addendi sono multipli di $3$: il resto dipende dalla somma
delle cifre, $12$, che è divisibile per $3$.
Lo stesso ragionamento vale per qualsiasi numero di cifre e anche per $9$.
:::

Per il $4$, invece, scriviamo $14880=148\cdot100+80$.
Il primo addendo è multiplo di $4$, quindi basta controllare $80$.

:::{warning} Non basta combinare due criteri qualsiasi

Essere divisibile per $2$ e per $3$ implica esserlo per $6$.
Non puoi sostituire questi numeri con una coppia qualunque: $12$ è
divisibile per $2$ e per $4$, ma non per $8$.
:::

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-criteri-es)=
### Una tabella di decisioni

Per ognuno dei numeri $135$, $248$, $372$, $14880$ e $974\,130$ indica quali fra
$2,3,4,5,6,9,10$ sono divisori. Giustifica le risposte con i criteri di divisibilità.
Trova poi tutte le cifre da inserire nel riquadro affinché il numero

$$
4\,\rispostanum\,2
$$

sia divisibile per $3$.

:::{dropdown} Mostra la soluzione

$135$: $3,5,9$; $248$: $2,4$; $372$: $2,3,4,6$;
$14880$: $2,3,4,5,6,10$; $974\,130$: $2,3,5,6,10$.
Quest'ultimo termina in $0$, ha somma delle cifre $24$ e ultime due cifre $30$:
è divisibile per $3$ ma non per $9$, né per $4$.
Indicando la cifra mancante con $c$, la somma delle cifre è $6+c$:
le cifre possibili sono $0,3,6,9$.
:::
