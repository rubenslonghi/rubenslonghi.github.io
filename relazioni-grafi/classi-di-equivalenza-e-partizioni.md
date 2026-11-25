---
title: "Classi di equivalenza e partizioni"
---

*Per richiamare le idee già viste:* [Prodotto cartesiano e principio di moltiplicazione](../insiemi-logica/prodotto-cartesiano-e-principio-di-moltiplicazione.md) · [Che cos'è un insieme?](../insiemi-logica/che-cos-e-un-insieme.md).


(r-sec-rf-classi)=

:::{admonition} Attività — Un numero, tutto il suo gruppo
:class: attention

Scrivi i naturali da $0$ a $27$. Metti insieme quelli che danno lo
stesso resto dividendo per $7$. Dove collochi $3$, $10$, $17$, $24$?
Un numero può stare in due gruppi diversi? Quanti gruppi ottieni?
:::

(r-def-rf-classe)=

:::{note} Definizione — Classe e partizione

Data un'equivalenza $\sim$ su $A$, la **classe di $a$** è

$$
[a]=\{b\in A:b\sim a\}.
$$

Una **partizione** di $A$ è una famiglia di sottoinsiemi non vuoti,
senza elementi in comune a due a due, la cui unione è $A$.
:::

Per la congruenza modulo $7$ sui naturali,

$$
[3]=\{3,10,17,24,31,\ldots\}=[10].
$$

Un **rappresentante** è un elemento usato per indicare una classe.
$3$ e $10$ rappresentano la stessa classe; scegliamo normalmente il
resto $3$, perché sta fra $0$ e $6$. Il rappresentante è un numero,
la classe è un insieme di numeri: $3\ne[3]$.

(r-prop-rf-partizione)=

:::{important} Proposizione — Le classi formano una partizione

Ogni elemento appartiene alla propria classe. Due classi di equivalenza
sono uguali oppure non hanno elementi in comune. Le classi, quindi,
formano una partizione dell'insieme.
:::

:::{admonition} Dimostrazione
:class: tip

La riflessività dà $a\in[a]$. Se $c$ appartiene sia a $[a]$ sia a $[b]$,
allora $a\sim c\sim b$ per simmetria e transitività. Ogni elemento
equivalente ad $a$ è perciò equivalente anche a $b$, e viceversa:
$[a]=[b]$. Tutti gli elementi sono coperti e non ci sono sovrapposizioni
fra classi distinte.
:::

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-rf-classi-es)=
### Cambiare rappresentante

Descrivi $[0]$, $[1]$ e $[6]$ modulo $7$ su $\N$.
Fra $[2]$, $[9]$, $[16]$, $[3]$, quante classi diverse ci sono?
Poi parti dalla partizione $\{\{1,3,5\},\{2,4,6\}\}$ e inventa
un criterio di equivalenza che la produca.

:::{dropdown} Mostra la soluzione

$[0]=\{0,7,14,\ldots\}$, $[1]=\{1,8,15,\ldots\}$,
$[6]=\{6,13,20,\ldots\}$. Le classi distinte sono due, perché
$[2]=[9]=[16]\ne[3]$. Sull'insieme $\{1,\ldots,6\}$ si può usare
«ha la stessa parità di».
:::
