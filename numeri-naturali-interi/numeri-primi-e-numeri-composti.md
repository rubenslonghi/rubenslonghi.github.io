---
title: "Numeri primi e numeri composti"
---

(r-sec-primi)=

*Lezione: 26 settembre*

(r-primi-domanda)=

:::{admonition} Attività — Quali numeri non si lasciano scomporre?
:class: attention

Scrivi i divisori di $1,2,3,4,5,6,7,8,9,10,11,12$.

1. Quali numeri hanno esattamente due divisori? Quali ne hanno più di due?

2. Perché $1$ non sta in nessuno dei due gruppi?

3. Confronta il primo gruppo con gli orologi in cui hai verificato la legge di annullamento del prodotto.
:::

(r-def-primo)=

:::{note} Definizione — Primo e composto

Un naturale $p>1$ è **primo** se ha esattamente due divisori positivi:
$1$ e $p$. Un naturale $n>1$ che non è primo è detto **composto**:
si può scrivere $n=ab$ con $1<a<n$ e $1<b<n$.
Zero e uno non sono né primi né composti.
:::

I primi iniziali sono $2,3,5,7,11,13,17,19,23,\ldots$.
Il $2$ è l'unico primo pari: ogni altro pari maggiore di $2$ ha anche
$2$ come divisore, distinto da $1$ e da sé stesso.

(r-oss-composti-orologio)=

:::{note} Osservazione — Un collegamento da dimostrare con cura

Se $n$ è composto e $n=ab$ con $1<a,b<n$, sull'orologio a $n$ posizioni
il prodotto di $a$ e $b$ dà resto zero. È un controesempio alla legge di annullamento del prodotto, che quindi non vale in questi insiemi numerici sull'orologio.
Per gli orologi primi fra $2$ e $12$ abbiamo verificato l'assenza di
questi controesempi con le tabelline complete. Si può dimostrare che la legge di annullamento del prodotto vale se e solo se l'orologio è a $n$ posizioni, con $n$ numero primo.
:::

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-primi-es)=
### Decidere e giustificare

Classifica $1,17,21,29,39,49,51,91$ come primo, composto o nessuno dei due.
Per ogni composto scrivi una scomposizione; per i primi spiega quali divisori hai controllato.

:::{dropdown} Mostra la soluzione

$1$: nessuno; $17,29$: primi; $21=3\cdot7$, $39=3\cdot13$, $49=7^2$,
$51=3\cdot17$, $91=7\cdot13$:
composti. Basta controllare $2,3$ per $17$ e $2,3,5$ per $29$:
se entrambi i fattori superassero la radice quadrata, il prodotto supererebbe il numero.
:::

(r-composti-clock)=
### Costruisci il controesempio

Senza compilare intere tabelle, trova due fattori non nulli il cui
prodotto dia zero sugli orologi a $8$, $9$, $10$ e $12$ posizioni.

:::{dropdown} Mostra la soluzione

Possibili coppie: $(2,4)$, $(3,3)$, $(2,5)$, $(3,4)$.
:::
