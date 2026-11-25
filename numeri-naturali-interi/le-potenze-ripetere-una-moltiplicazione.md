---
title: "Le potenze: ripetere una moltiplicazione"
---

:::{note} Nel percorso della 1 SP

- [25 settembre 2026](../cronologia-1sp.md#giorno-2026-09-25) — Potenze ed espressioni.

[Apri tutta la linea del tempo](../cronologia-1sp.md).
:::

(r-sec-potenze)=

*Lezione: 25 settembre*

(r-raddoppio)=

:::{admonition} Attività — Raddoppiare a ogni passo
:class: attention

Parti da un gettone. A ogni passo raddoppi il numero dei gettoni.

1. Quanti ne hai dopo uno, due, tre e quattro passi?

2. Come scriveresti il calcolo dopo dieci passi, senza elencare tutti i fattori?

3. Quanti gettoni hai prima di fare passi? Che significato suggerisce per $2^0$?
:::

(r-def-potenza)=

:::{note} Definizione — Potenza con esponente naturale

Per un naturale $a$ e un intero $n\ge1$,

$$
a^n=\underbrace{a\cdot a\cdots a}_{n\text{ fattori}}.
$$

$a$ è la **base**; $n$ è l'**esponente**. In particolare $a^1=a$.
Per $a\ne0$ definiamo inoltre $a^0=1$.
L'espressione $0^0$ non è definita.
:::

:::{note} Perché l'esponente zero dà uno?

Per $a\ne0$, $a^3:a^3=1$. Se vogliamo estendere coerentemente la regola
di sottrarre gli esponenti nei quozienti, dobbiamo porre $a^{3-3}=a^0=1$.
Questo ragionamento non vale per $a=0$, perché richiederebbe di dividere per zero.
:::

(r-oss-perche-0-0-non-e-definita)=

:::{note} Osservazione — Perché $0^0$ non è definita?

Due ragionamenti in contraddizione: da una parte dovremmo avere $0^0=1$, poiché tutte le altre basi elevate alla $0$ danno $1$. Dall'altra avremmo $0^0=0$ poiché $0$ elevato a qualsiasi altro esponente dà $0$.
:::

Notiamo che $2^3=2\cdot2\cdot2=8$: l'esponente conta i fattori, non è un fattore
per cui moltiplicare la base. Inoltre $0^n=0$ per $n\ge1$ e $1^n=1$ per ogni $n\in\N$.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-potenze-base)=
### Leggere la scrittura

Calcola $2^5$, $5^2$, $7^1$, $7^0$, $0^4$, $1^{20}$.
Scrivi come potenza $3\cdot3\cdot3\cdot3$.
Spiega la differenza fra $3^4$ e $3\cdot4$.

:::{dropdown} Mostra la soluzione

$32,25,7,1,0,1$; il prodotto è $3^4=81$, mentre $3\cdot4=12$.
:::
