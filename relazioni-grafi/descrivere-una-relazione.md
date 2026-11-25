---
title: "Descrivere una relazione"
---

:::{note} Nel percorso della 1 SP

- [20 novembre 2026](../cronologia-1sp.md#giorno-2026-11-20) — Relazioni, grafi e ponti di Königsberg.

[Apri tutta la linea del tempo](../cronologia-1sp.md).
:::

*Per richiamare le idee già viste:* [Prodotto cartesiano e principio di moltiplicazione](../insiemi-logica/prodotto-cartesiano-e-principio-di-moltiplicazione.md) · [Che cos'è un insieme?](../insiemi-logica/che-cos-e-un-insieme.md).


(r-sec-rf-relazioni)=

:::{admonition} Attività — Chi è collegato a chi?
:class: attention

Considera $A=\{1,2,3\}$ e $B=\{2,4,6\}$. Collega $a\in A$ a $b\in B$
quando $a$ divide $b$. Disegna le frecce e scrivi le coppie collegate.
La coppia $(2,4)$ ha lo stesso significato della coppia $(4,2)$?
:::

(r-def-rf-relazione)=

:::{note} Definizione — Coppie ordinate e relazioni

Il **prodotto cartesiano** $A\times B$ è l'insieme delle coppie
ordinate $(a,b)$ con $a\in A$ e $b\in B$.
Una **relazione da $A$ a $B$** è un sottoinsieme di $A\times B$:
se $(a,b)$ appartiene alla relazione, scriviamo $a\mathrel{\mathcal R}b$.
Se $A=B$, parliamo di relazione *su* $A$.
:::

Nella coppia ordinata conta il posto: prima l'elemento di partenza,
poi quello di arrivo. Nell'attività la relazione contiene

$$
\{(1,2),(1,4),(1,6),(2,2),(2,4),(2,6),(3,6)\}.
$$

Si può rappresentare con un elenco, con frecce o con una tabella:
righe per $A$, colonne per $B$, un segno per ciascuna coppia ammessa.

## Parole e lettere: la relazione del 20 novembre

Poniamo $A=\{\text{STELLA},\text{LUNA},\text{ORO}\}$,
$B=\{a,e,i\}$ e colleghiamo $x\in A$ a $y\in B$ se
«$y$ è una lettera di $x$», senza distinguere maiuscole e minuscole.

```{figure} ../figure/schema-52abed04ed91.svg
:alt: Descrivere una relazione — diagramma
:width: 90%

Descrivere una relazione — diagramma
```

La relazione contiene $(\text{STELLA},a)$, $(\text{STELLA},e)$,
$(\text{LUNA},a)$. Il *dominio della relazione* è l'insieme
degli elementi di partenza che hanno almeno un'immagine:
$\{\text{STELLA},\text{LUNA}\}$. L'*insieme immagine* è $\{a,e\}$.
STELLA è una controimmagine di $a$ e di $e$; ORO non ha immagini.
Questa relazione non è una funzione da $A$ a $B$: STELLA ha due
immagini e ORO non ne ha nessuna. L'insieme di arrivo resta $B$,
anche se $i$ non è un'immagine.

## Un grafo su quattro elementi

Negli appunti $A=\{x,y,z,t\}$ e
$\mathcal R=\{(x,x),(x,y),(y,z),(y,t),(t,y),(z,x)\}$.

```{figure} ../figure/schema-3a882851172d.svg
:alt: Descrivere una relazione — diagramma
:width: 90%

Descrivere una relazione — diagramma
```

Un cappio indica una coppia $(x,x)$; due frecce opposte indicano
entrambe le coppie $(y,t)$ e $(t,y)$.
Il grafo non è riflessivo (mancano tre cappi), non è simmetrico
e non è transitivo: $(x,y)$ e $(y,z)$ ci sono, $(x,z)$ no.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-rf-rappresentare)=
### Dalla regola alla rappresentazione

Su $A=\{1,2,3,4\}$ considera la relazione «$a+b=5$».
Elenca le coppie, disegna le frecce e costruisci la tabella.
Ripeti per «$a\le b$». Quali coppie si trovano sulla diagonale della tabella?

:::{dropdown} Mostra la soluzione

La prima relazione è $\{(1,4),(2,3),(3,2),(4,1)\}$.
La seconda contiene le coppie con il primo elemento non maggiore del
secondo: $4+3+2+1=10$ coppie. Sulla diagonale sono $(a,a)$:
nessuna per la prima relazione, tutte e quattro per la seconda.
:::

(r-rf-coprimi)=
### La relazione «primi tra loro»

Per $A=\{2,3,4\}$, $B=\{4,5,6\}$, collega $x$ a $y$ se
$\operatorname{MCD}(x,y)=1$. Rappresenta la relazione con elenco,
frecce, tabella e punti cartesiani. Trova dominio e insieme immagine.

:::{dropdown} Mostra la soluzione

$\{(2,5),(3,4),(3,5),(4,5)\}$; dominio $A$, immagine $\{4,5\}$.
:::

(r-rf-multipli-appunti)=
### «È multiplo di»: attenzione al verso

Siano $A=\{6,8,12\}$ e $B=\{3,4,18\}$. Associa $x\in A$ a
$y\in B$ se $x$ è multiplo di $y$. Elenca prima tutte le nove coppie
di $A\times B$, poi seleziona quelle della relazione. Disegna frecce,
tabella e grafico cartesiano. Quale elemento di $B$ non riceve frecce?

:::{dropdown} Mostra la soluzione

La relazione è $\{(6,3),(8,4),(12,3),(12,4)\}$.
Dominio $A$, immagine $\{3,4\}$; $18$ non riceve frecce.
:::

(r-rf-quattro-regole)=
### Riconoscere le frecce

Su $\{1,2,3,4\}$ disegna i grafi di «$x$ è multiplo di $y$»,
«$x$ è il doppio di $y$», «$x$ è divisore di $y$»,
«$x$ è il quadrato di $y$». Quali richiedono cappi?
Per la divisibilità, ripeti su $\{2,3,4,6\}$.

:::{dropdown} Mostra la soluzione

Multiplo e divisore hanno tutti i cappi e frecce inverse fra loro.
Il doppio contiene $(2,1),(4,2)$; il quadrato $(1,1),(4,2)$.
Nell'ultimo insieme: quattro cappi e $(2,4),(2,6),(3,6)$.
:::
