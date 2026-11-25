---
title: "Tre proprietà da controllare"
---

*Per richiamare le idee già viste:* [Prodotto cartesiano e principio di moltiplicazione](../insiemi-logica/prodotto-cartesiano-e-principio-di-moltiplicazione.md) · [Che cos'è un insieme?](../insiemi-logica/che-cos-e-un-insieme.md).


(r-sec-rf-proprieta)=

:::{admonition} Attività — Un criterio che funziona sempre?
:class: attention

Confronta «ha la stessa lunghezza di» e «ha almeno una lettera in comune
con». Ogni parola è collegata a sé stessa? Puoi invertire un collegamento?
Se una parola è collegata a una seconda, e la seconda a una terza,
la prima deve essere collegata alla terza? Cerca esempi e controesempi.
:::

(r-def-rf-tre-proprieta)=

:::{note} Definizione — Riflessiva, simmetrica, transitiva

Una relazione su $A$ è:

- **riflessiva** se $a\mathrel{\mathcal R}a$ per ogni $a\in A$;

- **simmetrica** se $a\mathrel{\mathcal R}b$ implica
    $b\mathrel{\mathcal R}a$;

- **transitiva** se $a\mathrel{\mathcal R}b$ e
    $b\mathrel{\mathcal R}c$ implicano $a\mathrel{\mathcal R}c$.

Una relazione che ha tutte e tre le proprietà è una
**relazione di equivalenza**.
:::

«Ha la stessa lunghezza di» è un'equivalenza: ciascuna parola ha la
propria lunghezza; l'uguaglianza si può invertire; due uguaglianze
successive di lunghezze danno la stessa lunghezza anche agli estremi.

«Ha una lettera in comune con», sulle parole non vuote, è riflessiva e
simmetrica, ma non transitiva: *ala* e *ape* hanno una lettera
comune, come *ape* e *pepe*; *ala* e *pepe* non ne hanno.

### Equivalenza e ordine rispondono a domande diverse

Un'equivalenza permette di dire «stesso gruppo». Un ordine permette
di dire «prima» o «più piccolo». $\le$ è anche *antisimmetrica*:
$a\le b$ e $b\le a$ implicano $a=b$. Questo non significa «non simmetrica»:
è una proprietà distinta. La divisibilità ordina i naturali positivi,
ma non tutte le coppie sono confrontabili: né $2\mid3$ né $3\mid2$.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-rf-proprieta-es)=
### Giustificare o smentire

Stabilisci quali delle tre proprietà valgono per le relazioni:
«ha lo stesso resto modulo $7$» su $\N$; «è minore o uguale a» su $\N$;
«divide» sui naturali positivi. Giustifica ciò che vale e fornisci
un controesempio per ciò che non vale.

:::{dropdown} Mostra la soluzione

Lo stesso resto dà tutte e tre le proprietà, perché si confrontano
valori uguali. $\le$ è riflessiva e transitiva, ma non simmetrica:
$1\le2$, mentre $2\not\le1$.
La divisibilità è riflessiva e transitiva: $b=ak$ e $c=bh$ danno
$c=a(kh)$. Non è simmetrica: $2\mid6$, ma $6\nmid2$.
:::
