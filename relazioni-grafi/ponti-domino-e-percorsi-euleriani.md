---
title: "Ponti, domino e percorsi euleriani"
---

*Per richiamare le idee già viste:* [Prodotto cartesiano e principio di moltiplicazione](../insiemi-logica/prodotto-cartesiano-e-principio-di-moltiplicazione.md) · [Che cos'è un insieme?](../insiemi-logica/che-cos-e-un-insieme.md).


(r-eulero-avvio)=

:::{admonition} Attività — Attraversare senza ripassare
:class: attention

Disegna quattro zone $A,B,C,D$. Collega $A$ a $B$ con due ponti,
$B$ a $C$ con due, $A$ a $D$ con uno, $C$ a $D$ con uno,
$B$ a $D$ con uno. Puoi attraversare ogni ponte esattamente una volta?
Prima prova, poi cerca una ragione che valga anche senza tentativi.
:::

Per i ponti usiamo un grafo non orientato: i vertici sono le zone,
gli archi i ponti. Sono ammessi archi multipli.
Il grado di un vertice conta le estremità degli archi incidenti;
un cappio contribuisce $2$. La somma dei gradi è $2E$, con $E$ numero
degli archi: ogni arco contribuisce due estremità. Il numero di vertici
di grado dispari è quindi pari.

(r-teo-eulero)=

:::{important} Teorema — Criterio per un percorso euleriano

In un grafo finito non orientato con almeno un arco, tutti i vertici
incidenti ad archi devono stare nella stessa componente connessa.
Sotto questa condizione, esiste un percorso che usa ogni arco una sola volta
se e solo se i vertici di grado dispari sono zero oppure due.
Con zero si può chiudere il percorso; con due essi sono partenza e arrivo.
:::

Quando attraversiamo un vertice intermedio, ogni entrata si abbina a
un'uscita: il grado deve essere pari. Solo i due estremi possono fare eccezione.
Per costruire il percorso quando la condizione vale, parti da un estremo
dispari, se c'è, e unisci via via i circuiti rimasti al percorso già costruito.
Nella mappa iniziale i gradi sono $3,5,3,3$: quattro dispari rendono impossibile il percorso.

```{figure} ../figure/schema-ab58c7a8fa99.svg
:alt: Ponti, domino e percorsi euleriani — diagramma
:width: 90%

Ponti, domino e percorsi euleriani — diagramma
```

:::{note} La connessione conta

Due circuiti separati hanno tutti i gradi pari,
ma non puoi usare tutti gli archi in una sola passeggiata. Controlla sempre
anche la connessione dei vertici che hanno archi.
:::

[Otto esercizi: relazioni, famiglie, piano cartesiano, ponti e domino — PDF](/materiali/relazioni-grafi.pdf)

:::{dropdown} Scarica il fascicolo con le soluzioni

[Versione docente — PDF](/materiali/relazioni-grafi-docente.pdf)
:::

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-eulero-domino)=
### Tessere come archi

Rappresenta ogni valore del domino con un vertice e ogni tessera con un arco.
Studia le tessere $(0,1),(1,2),(2,0),(0,3),(3,3)$.
Trova una catena che le usi tutte e spiega se può essere chiusa.
Ripeti sostituendo i numeri con frazioni equivalenti: gli estremi
si possono accostare quando rappresentano lo stesso razionale.

:::{dropdown} Mostra la soluzione

Gradi $3,2,2,3$ sui vertici $0,1,2,3$;
una catena è $0,1,2,0,3,3$, aperta. Il doppio $3$ è un cappio.
Nel domino di frazioni i vertici rappresentano numeri, non singole scritture.
:::

(r-eulero-tre-grafi)=
### I tre grafi degli appunti

In ciascun grafo conta gli archi incidenti, includendo quelli multipli.
Stabilisci se esiste un percorso che usi ogni arco una sola volta;
se esiste, indica partenza e arrivo e numera gli archi nell'ordine scelto.

```{figure} ../figure/schema-3c52be10a53f.svg
:alt: Ponti, domino e percorsi euleriani — diagramma
:width: 90%

Ponti, domino e percorsi euleriani — diagramma
```

:::{dropdown} Mostra la soluzione

1. I gradi di $A,B,C,D$ sono $2,4,3,3$: percorso aperto fra $C$ e $D$,
per esempio $C,A,B,D,B,C,D$ (le due traversate fra $B,D$ usano archi diversi).
2. I gradi di $E,F,G,H,I$ sono $3,4,2,3,4$: percorso fra $E,H$,
per esempio $E,F,G,H,F,I,E,I,H$.
3. I gradi di $L,M,N,P,Q$ sono $3,2,3,3,1$: quattro dispari,
quindi il percorso non esiste.
:::
