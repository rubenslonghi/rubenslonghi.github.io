---
title: "Il quoziente: ogni classe diventa un oggetto"
---

*Per richiamare le idee già viste:* [Prodotto cartesiano e principio di moltiplicazione](../insiemi-logica/prodotto-cartesiano-e-principio-di-moltiplicazione.md) · [Che cos'è un insieme?](../insiemi-logica/che-cos-e-un-insieme.md).


(r-sec-rf-quoziente)=

:::{admonition} Attività — Sette scatole al posto di infiniti numeri
:class: attention

Sull'orologio a sette posizioni, parti da $10$ oppure da $3$ e aggiungi
$5$: cambia la posizione finale? Prova a sostituire anche $5$ con $12$.
Per moltiplicare, confronta $3\cdot5$, $10\cdot5$, $3\cdot12$.
Che cosa occorre conservare dei numeri per prevedere il risultato?
:::

(r-def-rf-quoziente)=

:::{note} Definizione — Insieme quoziente e proiezione

L'**insieme quoziente** $A/{\sim}$ è l'insieme delle classi
dell'equivalenza $\sim$. La **proiezione** manda ogni elemento
nella sua classe:

$$
\pi:A\longrightarrow A/{\sim},\qquad a\longmapsto[a].
$$
:::

Per la congruenza modulo $7$ il quoziente di $\N$ contiene esattamente
sette oggetti: $[0],[1],\ldots,[6]$. Non cancelliamo gli altri numeri:
li consideriamo insieme quando danno la stessa posizione.

Possiamo definire $[a]+[b]=[a+b]$ e $[a]\cdot[b]=[ab]$.
Occorre verificare che cambiare i rappresentanti non cambi la classe
del risultato: questa richiesta si chiama *buona definizione*.
Se $a=7q+r$ e $b=7s+t$, la somma ha lo stesso resto di $r+t$;
il prodotto ha lo stesso resto di $rt$, perché gli altri termini
sono multipli di $7$. Il risultato dipende solo dalle classi.

Negli interi la stessa costruzione si indica spesso con $\Z/7\Z$.
La riprenderemo dopo lo studio degli interi: qui bastano i naturali.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-rf-operazioni-es)=
### Operare sulle classi

Calcola $[5]+[6]$, $[4]\cdot[5]$ modulo $7$, usando i rappresentanti
fra $0$ e $6$. Ripeti sostituendo $5$ con $12$ e $6$ con $13$.
Un compagno propone «il maggiore dei due rappresentanti» come numero
associato a una coppia di classi: perché questa scelta non è indipendente
dai rappresentanti?

:::{dropdown} Mostra la soluzione

$[5]+[6]=[11]=[4]$; $[4]\cdot[5]=[20]=[6]$.
$12+13=25\equiv4$ e $4\cdot12=48\equiv6\pmod7$.
Invece il maggiore fra $1$ e $2$ è $2$, mentre fra $8$ e $2$ è $8$;
$[1]=[8]$, ma i numeri scelti sono diversi, e anche le loro classi.
:::
