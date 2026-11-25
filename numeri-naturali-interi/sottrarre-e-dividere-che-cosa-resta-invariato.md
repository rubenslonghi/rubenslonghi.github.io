---
title: "Sottrarre e dividere: che cosa resta invariato?"
---

(r-sec-invariantiva)=

:::{admonition} Attività — Spostare due punti insieme
:class: attention

Segna $7$ e $12$ su una semiretta. Spostali entrambi di due unità verso
destra. La loro distanza cambia?
Poi confronta $9:3$ con $18:6$: raddoppiare entrambi i numeri cambia il quoziente?
Proponi due regole e cerca i casi in cui non puoi applicarle.
:::

(r-prop-invariantive)=

:::{important} Proposizione — Le proprietà invariantive

Per la sottrazione, aggiungere lo stesso naturale ai due termini non
cambia la differenza:

$$
a-b=(a+c)-(b+c)\qquad(a\ge b).
$$

Si può anche sottrarre lo stesso numero, purché i termini restino naturali.

Per la divisione esatta, con $b\ne0$ e $c\ne0$,

$$
a:b=(ac):(bc).
$$

Si possono dividere entrambi i termini per lo stesso numero non nullo,
purché tutte le divisioni indicate siano esatte in $\N$.
:::

(r-es-invariantiva-calcoli)=

:::{tip} Esempio — Rendere comodi i numeri

$8921-721=8200-0=8200$, sottraendo $721$ a entrambi i termini.
$270:18=135:9=15$, dividendo entrambi i termini per $2$.
:::

(r-prop-divisione-distrib)=

:::{important} Proposizione — Distribuire una divisione sul dividendo

Se $c\ne0$ e $a$, $b$ sono divisibili per $c$, allora

$$
(a+b):c=a:c+b:c.
$$

Per la differenza vale $(a-b):c=a:c-b:c$ se inoltre $a\ge b$.
:::

:::{warning} Non spezzare il divisore

$12:(2+2)=3$, mentre $12:2+12:2=12$.
La divisione non si distribuisce su una somma posta al divisore.
Inoltre aggiungere lo stesso numero a dividendo e divisore non è
un'applicazione dell'invariantiva: $8:4\ne(8+2):(4+2)$.
:::

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-invariantiva-es)=
### Giustifica ogni scorciatoia

Calcola

- $1003-497$

- $172-98$

- $360:24$

- $324:12+36:12$

- $642:6+18:6$

Per ogni calcolo indica la proprietà usata. Controlla poi se
$(18+6):3=18:3+6:3$ e se $18:(6+3)=18:6+18:3$.

:::{dropdown} Mostra la soluzione

$1006-500=506$; $172-98=(172+2)-(98+2)=174-100=74$,
per l'invariantiva della sottrazione; $180:12=90:6=15$; $(324+36):12=30$;
$(642+18):6=110$. La prima uguaglianza è vera ($8=8$), la seconda falsa ($2\ne9$).
:::
