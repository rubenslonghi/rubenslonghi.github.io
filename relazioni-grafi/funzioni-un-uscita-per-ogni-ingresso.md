---
title: "Funzioni: un'uscita per ogni ingresso"
---

*Per richiamare le idee già viste:* [Prodotto cartesiano e principio di moltiplicazione](../insiemi-logica/prodotto-cartesiano-e-principio-di-moltiplicazione.md) · [Che cos'è un insieme?](../insiemi-logica/che-cos-e-un-insieme.md).


(r-sec-rf-funzioni)=

:::{admonition} Attività — Una macchina con una risposta sola
:class: attention

Confronta tre istruzioni su $A=\{0,1,2,3\}$: «raddoppia»;
«associa un numero maggiore»; «dividi per due e restituisci un naturale».
Per ciascun ingresso c'è sempre una risposta? È unica?
:::

(r-def-rf-funzione)=

:::{note} Definizione — Funzione, dominio, codominio, immagine

Una **funzione** $f:A\to B$ assegna a ogni elemento $a$ del
**dominio** $A$ uno e un solo elemento $f(a)$ del
**codominio** $B$. L'**immagine** della funzione è
$f(A)=\{f(a):a\in A\}$, un sottoinsieme di $B$.
:::

La funzione $f:\N\to\N$, $f(n)=2n$, ha immagine l'insieme dei pari,
che non coincide con il codominio. Più ingressi possono avere la
stessa uscita: $r_7(n)$, il resto modulo $7$, manda sia $3$ sia $10$ in $3$.
Una tabella, un diagramma a frecce e una formula sono modi diversi
di descrivere una funzione; nel grafico cartesiano si segnano le
coppie $(a,f(a))$ quando ingressi e uscite sono numeri.

### Iniettiva, suriettiva, biiettiva

Una funzione è **iniettiva** se ingressi diversi hanno uscite
diverse; è **suriettiva** se ogni elemento del codominio è
raggiunto; è **biiettiva** se ha entrambe le proprietà.
La scelta del codominio conta: raddoppiare da $\N$ a $\N$ non è
suriettivo, mentre da $\N$ all'insieme dei pari lo è.
Una biiezione permette di tornare indietro con una funzione inversa.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-rf-funzioni-es)=
### Controllare ingressi e uscite

Per $f:\N\to\N$, $f(n)=n+1$, e
$r_7:\N\to\{0,1,\ldots,6\}$, costruisci una tabella con gli ingressi
da $0$ a $10$. Quali sono iniettive? Quali suriettive?
La relazione «$a+b=5$» su $\{1,2,3,4\}$ del primo esercizio
definisce una funzione da questo insieme a sé stesso? È biiettiva?

:::{dropdown} Mostra la soluzione

$f$ è iniettiva, non suriettiva: manca $0$ nell'immagine.
$r_7$ è suriettiva, non iniettiva: per esempio $r_7(0)=r_7(7)$.
La relazione definisce $a\mapsto5-a$: ogni ingresso ha un'unica uscita,
tutte le uscite sono raggiunte e diverse, quindi è biiettiva.
:::
