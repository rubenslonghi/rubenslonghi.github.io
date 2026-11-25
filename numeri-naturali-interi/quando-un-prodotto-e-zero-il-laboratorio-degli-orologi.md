---
title: "Quando un prodotto è zero? Il laboratorio degli orologi"
---

:::{note} Nel percorso della 1 SP

- [21 settembre 2026](../cronologia-1sp.md#giorno-2026-09-21) — Proprietà delle operazioni e laboratorio degli orologi.

[Apri tutta la linea del tempo](../cronologia-1sp.md).
:::

(r-sec-annullamento)=

*Lezione: 21--24 settembre*

(r-orologi)=

:::{admonition} Attività — Due numeri non nulli possono dare zero?
:class: attention

**Lavoro a gruppi.** Ogni gruppo riceve un orologio con $n$ posizioni,
numerate da $0$ a $n-1$, e la sua tabella vuota.
Per moltiplicare $a$ e $b$, calcolate il prodotto usuale e conservate
il resto della divisione per $n$. Per esempio, su sei posizioni,
$4\cdot2=8$ porta alla posizione $2$: un giro completo e due passi.

1. Completate tutte le tabelline, inclusa la riga dello zero.

2. Cerchiate gli zeri ottenuti con due fattori entrambi diversi da zero.

3. Se il risultato è zero, almeno un fattore deve essere zero?
    Rispondete con una verifica dell'intera tabella oppure con un controesempio.

4. Confrontate gli orologi da $2$ a $12$ posizioni: quali si comportano allo stesso modo?
:::

```{figure} ../figure/schema-0e5851f7c22d.svg
:alt: Orologio modulo 5
:width: 90%

Orologio modulo 5
```

```{figure} ../figure/schema-0e4dc22f228c.svg
:alt: Orologio modulo 6
:width: 90%

Orologio modulo 6
```

(r-prop-annullamento)=

:::{important} Proposizione — Zero assorbente e annullamento del prodotto in $\N$

Lo zero è **assorbente** per la moltiplicazione: $0a=a0=0$.
Nei naturali vale inoltre la **legge di annullamento del prodotto**:

$$
ab=0\quad\Longleftrightarrow\quad a=0\ \text{oppure}\ b=0.
$$

«Oppure» ammette anche il caso in cui entrambi i fattori siano zero.
:::

:::{admonition} Dimostrazione
:class: tip

Se un fattore è zero, il prodotto è zero. Viceversa, se entrambi i
fattori naturali fossero diversi da zero, sarebbero almeno $1$ e il
loro prodotto sarebbe almeno $1$: non potrebbe essere zero.
:::

(r-oss-orologi-zero)=

:::{note} Osservazione — Cambiare operazione cambia le proprietà

Sull'orologio a $6$ posizioni, $2\cdot3$ dà resto $0$ benché i fattori
non siano zero. Lo zero rimane assorbente, ma la legge di annullamento
del prodotto *non* vale per questa moltiplicazione.
:::

:::{warning} Non è un permesso di dividere per zero

Neppure sugli orologi si divide per zero: $0\cdot x$ dà sempre zero.
Non produce un risultato non nullo e, se il risultato è zero,
non determina un unico $x$.
:::

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-orologi-es)=
### Una verifica e un controesempio

Completa le tabelle degli orologi a $4$ e $5$ posizioni nelle schede del laboratorio.
Spiega perché, per escludere la legge, basta una casella, mentre per
verificarla su un orologio devi controllare tutti i prodotti fra fattori non nulli.

:::{dropdown} Mostra la soluzione

Modulo $4$, $2\cdot2$ ha resto $0$: la legge non vale.
Modulo $5$, le quattro righe non nulle, limitate alle colonne $1,2,3,4$,
sono $(1,2,3,4)$, $(2,4,1,3)$, $(3,1,4,2)$, $(4,3,2,1)$: nessuno zero.
Fra $2$ e $12$ la legge vale per $2,3,5,7,11$; non vale per
$4,6,8,9,10,12$. Torneremo su questa distinzione con i numeri primi.
:::


## Materiali per questa lezione

- [Schede degli orologi](/materiali/schede-orologi.pdf)
