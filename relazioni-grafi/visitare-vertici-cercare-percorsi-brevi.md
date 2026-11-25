---
title: "Visitare vertici, cercare percorsi brevi"
---

*Per richiamare le idee già viste:* [Prodotto cartesiano e principio di moltiplicazione](../insiemi-logica/prodotto-cartesiano-e-principio-di-moltiplicazione.md) · [Che cos'è un insieme?](../insiemi-logica/che-cos-e-un-insieme.md).


(r-ham-avvio)=

:::{admonition} Attività — Eulero o Hamilton?
:class: attention

Disegna due triangoli che condividono un solo vertice.
Puoi percorrere ogni arco una volta tornando alla partenza?
Puoi visitare ogni vertice una volta e tornare alla partenza?
Spiega perché sono domande diverse.
:::

Un cammino hamiltoniano visita ogni vertice una sola volta;
un ciclo hamiltoniano torna al vertice iniziale, senza altre ripetizioni.
Un percorso euleriano usa invece tutti gli archi: può ripetere vertici.
Nei due triangoli condivisi tutti i gradi sono pari, ma un ciclo
hamiltoniano dovrebbe ripassare dal vertice comune.
Il criterio dei gradi di Eulero non si trasferisce a Hamilton.

### Approfondimento: condizioni sufficienti

Per un grafo semplice con $n\ge3$ vertici, il teorema di Dirac
garantisce un ciclo hamiltoniano se ogni grado è almeno $n/2$.
Il teorema di Ore basta quando la somma dei gradi di ogni coppia
di vertici distinti non adiacenti è almeno $n$.
Sono condizioni sufficienti, non necessarie: un ciclo di dieci vertici
ha gradi $2$ ed è comunque hamiltoniano. Gli enunciati sono qui
un orizzonte di approfondimento, non risultati da dimostrare in prima.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-tsp)=
### Un piccolo commesso viaggiatore

Fra quattro città le distanze simmetriche sono $AB=10$, $AC=15$,
$AD=20$, $BC=35$, $BD=25$, $CD=30$.
Con partenza e ritorno in $A$, confronta i tre circuiti diversi,
considerando uguali un circuito e il suo inverso. Qual è il più breve?
Prova poi la strategia «vai alla città non ancora visitata più vicina»:
su questi dati trova il minimo? Questo dimostra che funziona sempre?

:::{dropdown} Mostra la soluzione

$A B C D A=95$, $A B D C A=80$, $A C B D A=95$.
Qui il vicino più prossimo dà $80$, ma un esempio favorevole non è
una dimostrazione generale. Per $n$ città distinte, simmetriche e tutte
collegate, i circuiti da confrontare sono $(n-1)!/2$, per $n\ge3$.
:::
