---
title: "Giochi, stati e invarianti"
---

*Per richiamare le idee già viste:* [Prodotto cartesiano e principio di moltiplicazione](../insiemi-logica/prodotto-cartesiano-e-principio-di-moltiplicazione.md) · [Che cos'è un insieme?](../insiemi-logica/che-cos-e-un-insieme.md).


(r-grafi-giochi)=

:::{admonition} Attività — Che cosa rappresentano i vertici?
:class: attention

Confrontate domino, mosse del cavallo e lupo--capra--cavolo.
Per ciascuno definite vertici, archi e significato della soluzione.
Nel rompicapo del fiume una barca porta il contadino e al massimo
un altro oggetto; non si possono lasciare da soli lupo e capra,
né capra e cavolo senza il contadino.
:::

Nel domino gli archi sono le tessere; per il cavallo i vertici sono
caselle e gli archi sono mosse ammesse; nei rompicapi i vertici possono
essere intere configurazioni. Risolvere significa raggiungere lo stato finale.
Per il fiume una soluzione è: porta la capra, torna solo, porta il lupo,
riporta la capra, porta il cavolo, torna solo, porta la capra.

### Piste di laboratorio emerse nelle conversazioni

- **Hashiwokakero.** Isole numerate, ponti orizzontali o verticali,
    al massimo due per collegamento, senza incroci: tutti i vertici devono
    essere connessi e avere il grado indicato. Una somma dei gradi dispari
    rende impossibile il rompicapo, ma la somma pari da sola non basta.

- **Slitherlink.** Disegna un unico circuito sulla griglia rispettando
    i numeri dei lati delle celle. I vertici usati hanno grado $2$;
    questa condizione da sola consentirebbe circuiti separati.

- **Hex e Bridg-It.** Due giocatori cercano connessioni fra lati opposti.
    Modellizza i collegamenti disponibili e confronta una mossa che allunga
    il proprio cammino con una che interrompe quello avversario.

- **Puntini e caselle.** Un segmento completa un quadrato? Conta
    vertici, archi e facce, includendo l'esterno. Per un disegno piano
    connesso verifica $V-E+F=2$; due componenti richiedono una formula diversa.

- **Sprouts.** Collega due punti senza incrociare curve e inserisci
    un nuovo punto sulla curva; nessun punto supera grado $3$.
    Conta le nuove estremità e studia perché il gioco deve terminare.

- **Gioco del quindici.** Le configurazioni sono vertici; una mossa
    consentita è un arco. Lo scambio isolato di $14$ e $15$ dalla posizione
    risolta non è raggiungibile: la parità è una pista per trovare un invariante.

- **Nim.** Con mucchi $(1,2)$ rappresenta tutte le mosse che tolgono
    una o più pedine da un solo mucchio. Vince chi prende l'ultima.
    Parti dagli stati finali e marca quelli perdenti e vincenti; poi prova
    a collegare la strategia generale alle cifre binarie e allo XOR.

- **Cubo di Rubik.** Considera come vertici solo configurazioni
    raggiungibili tramite mosse legali. Distingui «esiste una sequenza»
    da «qual è la più breve», precisando che cosa conti come una mossa.

:::{note} Direzioni come classi

Le rette parallele del piano hanno
una stessa direzione: raggrupparle è un altro esempio di equivalenza.
Nella geometria proiettiva una direzione dà un punto all'infinito.
Le sole direzioni non sono l'intero piano proiettivo: sono la sua retta all'infinito.
:::
