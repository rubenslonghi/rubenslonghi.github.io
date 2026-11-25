---
title: "Prodotto cartesiano e principio di moltiplicazione"
---

:::{note} Nel percorso della 1 SP

- [5 novembre 2026](../cronologia-1sp.md#giorno-2026-11-05) — Operazioni tra insiemi e prodotto cartesiano.

[Apri tutta la linea del tempo](../cronologia-1sp.md).
:::

*Per richiamare le idee già viste:* [Achille, i decimali infiniti e nuovi numeri](../razionali-reali/achille-i-decimali-infiniti-e-nuovi-numeri.md).


(r-ins-menu)=

:::{admonition} Attività — Pantaloni e magliette
:class: attention

I pantaloni hanno colori $P=\{V,N,R\}$; le magliette
$M=\{V,N,R,B\}$. Elenca gli abbinamenti, prima il pantalone e poi
la maglietta. Confronta $(N,R)$ e $(R,N)$.
:::

Il prodotto cartesiano è
$P\times M=\{(x,y)\mid x\in P,\ y\in M\}$.
Una coppia è *ordinata*: scambiare i posti può cambiare l'abbinamento.
Negli insiemi, invece, $\{N,R\}=\{R,N\}$.

```{figure} ../figure/schema-9cde20755f20.svg
:alt: Prodotto cartesiano e principio di moltiplicazione — diagramma
:width: 90%

Prodotto cartesiano e principio di moltiplicazione — diagramma
```

Se ogni prima scelta ammette tutte le seconde,
$|P\times M|=|P||M|=3\cdot4=12$.

(r-ins-strette)=

::::{admonition} Attività — Sei persone si stringono la mano
:class: attention

Ogni coppia si saluta una volta. Perché $6\cdot5$ conta ogni stretta
due volte? Confronta $6\cdot5/2$ con $1+2+3+4+5$.
Estendi il ragionamento a $n$ persone. Poi calcola $1+2+\cdots+100$
accoppiando primo e ultimo termine.

:::{dropdown} Mostra la soluzione

$15$ strette; in generale $n(n-1)/2$.
La somma è $50\cdot101=5050$.
:::
::::

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-ins-conteggio)=
### Scelte indipendenti, ripetizioni e vincoli

1. Un menu offre $4$ antipasti, $3$ primi e $3$ secondi. Quanti pranzi
    con una scelta per portata?

2. Quante password di quattro caratteri si possono comporre con
    sole cifre? E con cifre e $26$ lettere? Le ripetizioni sono ammesse.

3. Per targhe nel formato di `SG026GF`, con $26$ lettere e
    $10$ cifre disponibili, quante scritture si possono formare nel modello?

4. Michele sceglie fra $4$ paia di scarpe, $3$ pantaloni e $5$
    magliette. Può indossare uno dei suoi $3$ cappelli oppure nessuno.
    Quanti abbigliamenti?

:::{dropdown} Mostra la soluzione

$36$; $10^4$ e $36^4$; $26^4\cdot10^3$;
$4\cdot3\cdot5\cdot4=240$. Per i cappelli si contano quattro scelte,
compresa l'assenza del cappello.
:::
