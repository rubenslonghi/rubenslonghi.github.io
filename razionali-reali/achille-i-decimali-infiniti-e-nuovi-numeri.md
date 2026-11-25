---
title: "Achille, i decimali infiniti e nuovi numeri"
---

*Per richiamare le idee già viste:* [Numeri interi: descrivere due versi](../numeri-naturali-interi/numeri-interi-descrivere-due-versi.md) · [MCD e mcm](../numeri-naturali-interi/mcd-e-mcm.md).


(r-q-zenone)=

:::{admonition} Attività — Infiniti tratti, distanza limitata
:class: attention

Somma $1/2$, poi $1/2+1/4$, poi $1/2+1/4+1/8$.
Disegna ogni volta la parte di un segmento unitario ancora mancante.
Per arrivare a meno di $1/1000$ dalla fine basta un numero finito di passaggi?
Qual è la differenza fra numero di suddivisioni e lunghezza totale?
:::

Dopo $n$ passaggi la somma è $1-1/2^n$: non è ancora $1$,
ma la distanza mancante può diventare più piccola di ogni soglia assegnata.
Non serve introdurre ora la definizione di limite per riconoscere la struttura.
Anche $0{,}999\ldots=1$: se $x=0{,}\overline9$, $10x-x=9$.
Le scritture periodiche infinite possono rappresentare numeri razionali.

(r-q-radice)=

:::{admonition} Attività — La diagonale del quadrato
:class: attention

Nel quadrato di lato $1$, la diagonale ha quadrato $2$.
Confronta $1{,}4^2$, $1{,}41^2$, $1{,}42^2$ e $1{,}414^2$.
Costruisci intervalli via via più stretti per la sua lunghezza.
Essere capaci di approssimare un numero significa averlo scritto esattamente?
:::

La diagonale è $\sqrt2$, che non è razionale. Infatti, se
$\sqrt2=p/q$ in minimi termini, $p^2=2q^2$ rende $p$ pari;
scrivendo $p=2k$, anche $q$ risulta pari: contraddizione.
Fra due razionali distinti c'è sempre un altro razionale, la loro media,
ma questa densità non basta a contenere tutte le lunghezze.

:::{note} Densità e completezza

Avere sempre un numero intermedio
non significa avere tutti i punti della retta. La costruzione dei reali
e la completezza saranno riprese più avanti; l'ipotesi del continuo
riguarda invece le cardinalità degli infiniti ed è una domanda diversa.
:::

## Trasportare la diagonale sulla retta

Il teorema di Pitagora dà $x=\sqrt{1^2+1^2}=\sqrt2$.
L'arco trasporta questa lunghezza sulla retta: il punto esiste,
anche se non ha coordinata razionale.

```{figure} ../figure/schema-31a9a1c525d8.svg
:alt: Achille, i decimali infiniti e nuovi numeri — diagramma
:width: 90%

Achille, i decimali infiniti e nuovi numeri — diagramma
```

Per un quadrato di lato $L\ge0$ e diagonale $d$:
$d=\sqrt2\,L$ e $L=d/\sqrt2$.

## La spirale di Teodoro

Costruisci un triangolo rettangolo con cateti $1$ e $1$.
Aggiungi poi un cateto lungo $1$, perpendicolare all'ipotenusa precedente.
Le distanze dall'origine diventano $\sqrt2,\sqrt3,\sqrt4,\ldots$.

```{figure} ../figure/schema-72dbc2683be5.svg
:alt: Achille, i decimali infiniti e nuovi numeri — diagramma
:width: 90%

Achille, i decimali infiniti e nuovi numeri — diagramma
```

Non tutte queste radici sono irrazionali: $\sqrt4=2$, $\sqrt9=3$,
$\sqrt{16}=4$. Per $m\in\N$, $\sqrt m$ è irrazionale esattamente
quando $m$ non è un quadrato perfetto.
Analogamente $\sqrt[3]2$, $\sqrt[3]3$, $\sqrt[4]2$ e $\sqrt[5]5$
sono irrazionali, mentre $\sqrt[3]8=2$ e $\sqrt[5]{32}=2$.

## Numeri irrazionali e insieme reale

Fra gli esempi degli appunti compaiono
$\pi\simeq3{,}1415$, $\varphi\simeq1{,}618$ e $e\simeq2{,}718$.
Per una circonferenza di raggio $r$, $C=2\pi r$ e $A=\pi r^2$.
Il numero aureo $\varphi=(1+\sqrt5)/2$ soddisfa
$\varphi-1=1/\varphi$.
Un altro esempio è $0{,}101001000100001\ldots$, con blocchi di zeri
sempre più lunghi fra due cifre $1$. Non può essere definitivamente
periodico: un periodo contenente un $1$ imporrebbe un limite alla
lunghezza dei blocchi di zeri; un periodo di soli zeri escluderebbe
gli infiniti $1$ successivi.

```{figure} ../figure/schema-a0c0555fdcc4.svg
:alt: Achille, i decimali infiniti e nuovi numeri — diagramma
:width: 90%

Achille, i decimali infiniti e nuovi numeri — diagramma
```

L'insieme dei numeri razionali e irrazionali si chiama $\R$, insieme
dei numeri reali. A ogni punto della retta corrisponde un unico reale
e viceversa. La completezza esprime che nella retta reale non restano
«buchi»; la densità dei razionali da sola non bastava.
Le misure sperimentali si riportano con approssimazioni e incertezze:
usare i reali come modello non rende esatta una misura fisica.

## Nelle cifre di un irrazionale troviamo qualsiasi sequenza?

L'essere infinito e non periodico non basta: il numero
$0{,}1010010001\ldots$ appena costruito non contiene neppure la cifra $2$.
La costante di Champernowne

$$
C=0{,}123456789101112131415161718192021\ldots
$$

si ottiene concatenando gli interi positivi e contiene ogni sequenza
finita di cifre. Per una sequenza che comincia con zeri, basta
considerare l'intero ottenuto anteponendole un $1$.
Per $\pi$ o $\sqrt2$, la sola irrazionalità non garantisce che una
sequenza assegnata, per esempio un numero di telefono, compaia.
Cercarla fra le cifre già calcolate è una verifica specifica,
diversa da una dimostrazione valida per tutte le sequenze.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-q-esatto)=
### Esatto o approssimato?

Classifica $1/3$, $0{,}333$, $0{,}\overline3$, $\sqrt2$.
Trova un razionale fra $2/5$ e $3/7$. Per la somma dei segmenti
di Achille trova il primo $n$ con distanza mancante minore di $1/1000$.

:::{dropdown} Mostra la soluzione

I primi tre numeri sono razionali; $0{,}333$ non è $1/3$.
$\sqrt2$ è irrazionale. La media è $29/70$. Serve $n=10$, perché $2^{10}=1024$.
:::

(r-r-classificare)=
### Vero, falso e insieme più piccolo

Giustifica: il quadrato di un irrazionale è sempre irrazionale;
il quadrato di un razionale è razionale; la radice di un razionale
non negativo può essere irrazionale; ogni punto della retta è razionale.
Indica poi il più piccolo fra $\N,\Z,\Q,\R$ che contiene ciascun numero:

$$
(-2)^3,\quad(-2)^4,\quad0{,}1\overline5,\quad
(-1/3)^{-3},\quad\sqrt{11},\quad1{,}\overline9,\quad
\sqrt{3^{-2}},\quad\pi+2.
$$

:::{dropdown} Mostra la soluzione

Falso ($\sqrt2$ al quadrato è $2$); vero; vero ($\sqrt2$);
falso (il punto $\sqrt2$).
Nell'ordine: $\Z,\N,\Q,\Z,\R,\N,\Q,\R$.
Infatti $0{,}1\overline5=7/45$, $(-1/3)^{-3}=-27$,
$1{,}\overline9=2$, $\sqrt{3^{-2}}=1/3$.
:::

(r-r-operazioni)=
### Operazioni con razionali e irrazionali

Classifica $\sqrt{(1/3)^{-2}}$, $\sqrt{(1/2)^{-1}}$,
$\sqrt{5^7:5^6}$ e $\pi+1$.
Mostra con esempi che il prodotto di due irrazionali può essere
razionale o irrazionale. Dimostra per assurdo che, se $a$ è razionale
e $b$ irrazionale, $a+b$ è irrazionale; se inoltre $a\ne0$, anche $ab$ lo è.

:::{dropdown} Mostra la soluzione

$3$ è razionale; $\sqrt2$, $\sqrt5$, $\pi+1$ sono irrazionali.
$\sqrt2\sqrt2=2$, mentre $\sqrt2\sqrt3=\sqrt6$.
Se $a+b=c\in\Q$, allora $b=c-a\in\Q$: assurdo.
Se $ab=c\in\Q$ e $a\ne0$, allora $b=c/a\in\Q$: assurdo.
Per $a=0$ il prodotto è invece razionale. La stessa dimostrazione
giustifica $\pi+1\notin\Q$, senza ragionare sulle sole cifre approssimate.
:::


## Materiali per questa lezione

- [Zenone e gli infinitesimi — approfondimento](/materiali/zenone-infinitesimi.pdf)

```{figure} ../media/achille-tartaruga.mp4
:alt: Video su Achille e la tartaruga

Achille e la tartaruga: una lettura del paradosso.
```

[Apri o scarica il video](/media/achille-tartaruga.mp4)
