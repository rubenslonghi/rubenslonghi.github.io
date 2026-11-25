---
title: "Multipli e divisori: dividere senza resto"
---

(r-sec-multipli)=

*Lezione: 26 settembre*

(r-tessere)=

:::{admonition} Attività — Rettangoli con ventotto tessere
:class: attention

Hai $28$ tessere quadrate. Disponile in rettangoli senza lasciare tessere fuori.

1. Quali numeri di righe sono possibili? Scrivi le coppie «righe, colonne».

2. Puoi trovare tutti i multipli di $8$? E tutti i divisori di $28$?

3. Che cosa cambia se le tessere sono zero?
:::

(r-def-divisore)=

:::{note} Definizione — Multiplo e divisore

Un naturale $a$ è **multiplo** di un naturale $b$ se esiste
$q\in\N$ tale che $a=bq$.
Quando $b>0$, diciamo anche che $b$ è un **divisore** di $a$,
che $b$ divide $a$ (scrittura $b\mid a$), oppure che $a$ è divisibile per $b$.
In questo libro i divisori sono sempre diversi da zero.
:::

Per $b>0$, essere divisibile per $b$ equivale ad avere resto zero:

$$
a=bq\quad\Longleftrightarrow\quad a\equiv0\pmod b.
$$

Per $b=1$ tutti i naturali hanno resto zero, anche se non usiamo un orologio a una sola posizione.

(r-es-multipli-zero)=

:::{tip} Esempio — Il caso ordinario e il caso zero

I multipli di $8$ sono $0,8,16,24,\ldots$: sono infiniti.
I divisori di $28$ sono $1,2,4,7,14,28$: sono finiti.
Ogni naturale positivo divide $0$, perché $0=b\cdot0$.
I divisori di $0$ sono quindi infiniti; il solo multiplo di $0$ è $0$.
:::

:::{note} Perché i divisori positivi sono finiti

Se $a>0$ e $b\mid a$, allora $1\le b\le a$.
Quindi basta cercare in un elenco finito. Questa spiegazione non si
applica a $a=0$, dove il fattore $q$ può essere zero.
:::

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-divisori-es)=
### Elencare e motivare

Elenca in ordine crescente tutti i divisori positivi di $18$, $24$ e $36$;
i multipli di $7$ minori di $40$;
i divisori di $1$. Stabilisci se $6\mid42$, $4\mid18$, $9\mid0$ e spiega ogni risposta.

:::{dropdown} Mostra la soluzione

$D(18)=\{1,2,3,6,9,18\}$; $D(24)=\{1,2,3,4,6,8,12,24\}$;
$D(36)=\{1,2,3,4,6,9,12,18,36\}$;
$\{0,7,14,21,28,35\}$; $D(1)=\{1\}$.
Vero: $42=6\cdot7$; falso: $18=4\cdot4+2$; vero: $0=9\cdot0$.
:::
