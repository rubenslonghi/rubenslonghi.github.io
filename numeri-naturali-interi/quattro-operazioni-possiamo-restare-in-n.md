---
title: "Quattro operazioni: possiamo restare in ℕ?"
---

:::{note} Nel percorso della 1 SP

- [19 settembre 2026](../cronologia-1sp.md#giorno-2026-09-19) — Le quattro operazioni e lo zero.

[Apri tutta la linea del tempo](../cronologia-1sp.md).
:::

(r-sec-operazioni)=

*Lezione: 19 settembre*

(r-macchina)=

:::{admonition} Attività — Una macchina che accetta solo naturali
:class: attention

La macchina riceve due naturali e deve restituire un naturale.
Provala con $12+8$, $15-4$, $4-15$, $3\cdot4$, $21:7$, $7:21$.

1. Quali richieste può eseguire? Per quali la risposta esce da $\N$?

2. Basta un esempio riuscito per dire che un'operazione funziona sempre?

3. Che cosa puoi concludere da un solo esempio che non funziona?
:::

(r-def-interna)=

:::{note} Definizione — Operazione interna

Un'operazione è **interna** a un insieme se, per ogni coppia di suoi
elementi, è definita e il risultato appartiene ancora all'insieme.
Addizione e moltiplicazione sono interne a $\N$; sottrazione e divisione
esatta non lo sono.
:::

:::{note} Nomi e significati

| $12+8=20$ | addendi $12,8$; somma $20$ |
| --- | --- |
| $15-4=11$ | minuendo $15$; sottraendo $4$; differenza $11$ |
| $3\cdot4=12$ | fattori $3,4$; prodotto $12$ |
| $21:7=3$ | dividendo $21$; divisore $7$; quoziente $3$ |
:::

La sottrazione cerca l'addendo mancante: $a-b=c$ significa $b+c=a$.
In $\N$ si può eseguire quando $a\ge b$.
La divisione esatta cerca il fattore mancante: con $b\ne0$,
$a:b=q$ significa $bq=a$. Il quoziente è naturale soltanto se esiste
un naturale $q$ che soddisfa questa uguaglianza.

:::{note} Il dividendo può essere più piccolo

$0:7=0$, perché $7\cdot0=0$. Non è quindi necessario che il dividendo
sia maggiore o uguale al divisore per avere un quoziente naturale.
Invece $3:7$ non è una divisione esatta in $\N$.
:::

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-inverse)=
### Calcolo e controllo inverso

Per 

$$
18-6\qquad 6-18 \qquad 24:8 \qquad 8:24 \qquad 0:9
$$

 indica se il risultato esiste
in $\N$. Quando esiste, controllalo con l'operazione inversa.
Trova poi due naturali la cui differenza non sia naturale e due la cui
divisione esatta non dia un naturale.

:::{dropdown} Mostra la soluzione

$18-6=12$ e $6+12=18$; $6-18$ non è naturale;
$24:8=3$ e $8\cdot3=24$; $8:24$ non è naturale;
$0:9=0$ e $9\cdot0=0$. Le altre coppie sono a scelta.
:::
