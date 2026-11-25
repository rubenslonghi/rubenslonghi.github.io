---
title: "MCD e mcm"
---

:::{note} Nel percorso della 1 SP

- [28 settembre 2026](../cronologia-1sp.md#giorno-2026-09-28) — MCD e mcm.

[Apri tutta la linea del tempo](../cronologia-1sp.md).
:::

(r-sec-mcdmcm)=

*Lezione: 28 settembre*

(r-sacchetti-pista)=

:::{admonition} Attività — Sacchetti e giri di pista
:class: attention

**Prepariamo dei sacchetti.** Abbiamo $24$ braccialetti rossi e
$36$ braccialetti blu. Vogliamo distribuirli in sacchetti identici,
senza avanzarne nessuno: ogni sacchetto deve contenere lo stesso numero
di braccialetti rossi e lo stesso numero di braccialetti blu.
Qual è il **massimo numero di sacchetti** che possiamo preparare?  

**Due atleti sulla pista.** Due atleti partono contemporaneamente
dalla stessa linea di partenza. Il primo completa un giro ogni $6$ minuti,
il secondo ogni $8$ minuti. Dopo quanti minuti dall'inizio si incontrano
per la prima volta **alla linea di partenza**?

Prima di leggere le spiegazioni, cercate una soluzione con disegni,
elenchi o calcoli. Confrontate i due problemi: quali numeri state cercando?
Come potete essere certi di aver trovato il massimo o il primo istante?
:::

## Dividere in gruppi: il MCD

Nel primo problema il numero di sacchetti deve dividere sia $24$ sia $36$.
Cerchiamo perciò i divisori comuni:

$$
\begin{aligned}
D(24)&=\{1,2,3,4,6,8,12,24\},\\
D(36)&=\{1,2,3,4,6,9,12,18,36\}.
\end{aligned}
$$

I divisori comuni sono $1,2,3,4,6,12$; il maggiore è $12$.
Possiamo preparare **12 sacchetti**, ciascuno con
$24:12=2$ braccialetti rossi e $36:12=3$ blu.

(r-def-mcd)=

:::{note} Definizione — Massimo comune divisore

Il **massimo comune divisore** di due o più naturali positivi è
il maggiore dei loro divisori comuni. Si indica con $\operatorname{MCD}$.
Due numeri sono **primi tra loro** se il loro MCD è $1$.
:::

Il numero $1$ è sempre un divisore comune: l'insieme in cui cerchiamo
il massimo non è vuoto. Essere primi tra loro non significa che i
numeri siano entrambi primi: per esempio $8$ e $9$ sono composti,
ma $\operatorname{MCD}(8,9)=1$.

### Calcolare il MCD con i fattori primi

Scomponiamo i numeri e prendiamo **solo i fattori primi comuni**,
ciascuno con l'**esponente più piccolo**:

$$
24=2^3\cdot3,\qquad 36=2^2\cdot3^2,
\qquad \operatorname{MCD}(24,36)=2^2\cdot3=12.
$$

Un divisore comune non può contenere più copie di un primo di quante
ne contenga ciascuno dei numeri. Scegliere l'esponente minimo consente
di prenderne il maggior numero possibile. Se non ci sono fattori primi
comuni, il MCD è $1$.

## Ritrovare una coincidenza: il mcm

Nel problema della pista gli istanti di ritorno alla partenza sono:

$$
\begin{aligned}
\text{primo atleta: }&0,6,12,18,24,30,\ldots\\
\text{secondo atleta: }&0,8,16,24,32,\ldots
\end{aligned}
$$

Il primo istante comune *dopo la partenza* è $24$ minuti:
il primo atleta ha percorso $4$ giri, il secondo $3$.
Stiamo cercando il più piccolo multiplo comune *positivo*.

(r-def-mcm)=

:::{note} Definizione — Minimo comune multiplo

Il **minimo comune multiplo** di due o più naturali positivi è
il più piccolo dei loro multipli comuni positivi. Si indica con
$\operatorname{mcm}$.
:::

:::{note} Perché escludere zero?

Zero è multiplo di entrambi i
tempi, ma rappresenta l'istante iniziale. Il problema chiede quando
i due atleti tornano insieme alla partenza.
:::

Un multiplo comune positivo esiste sempre: il prodotto dei numeri
è un esempio, anche se può non essere il più piccolo.

### Calcolare il mcm con i fattori primi

Scomponiamo i numeri e prendiamo **tutti i fattori primi presenti**,
comuni e non comuni, ciascuno con l'**esponente più grande**:

$$
6=2\cdot3,\qquad8=2^3,
\qquad\operatorname{mcm}(6,8)=2^3\cdot3=24.
$$

Un multiplo comune deve contenere almeno tutte le copie di ciascun primo
presenti in ognuno dei numeri. L'esponente massimo basta a soddisfare
questa richiesta senza aggiungere fattori inutili.

## Scegliere lo strumento e riflettere

### Prima di calcolare

Per ricavare quadrati uguali da un rettangolo, cercheresti divisori
o multipli? E per trovare quando due eventi periodici tornano insieme?
Spiega la scelta prima di usare una formula.

```{figure} ../figure/schema-2271ed0472fb.svg
:alt: MCD e mcm — diagramma
:width: 90%

MCD e mcm — diagramma
```

### Le domande della lezione

Per due naturali positivi $a,b$, discuti le seguenti domande e
giustifica le risposte con le definizioni.

1. Il MCD può essere maggiore di uno dei due numeri?

2. Il mcm può essere minore di uno dei due numeri?

3. Che cosa succede se $a$ e $b$ sono primi tra loro?

4. Senza scomporre, calcola $\operatorname{MCD}(17,34)$ e
    $\operatorname{mcm}(17,34)$, giustificando la risposta.

5. Calcola MCD, mcm e prodotto per $(6,8)$ e $(24,36)$.
    Quale relazione riconosci? Vale anche per tre numeri?

(r-prop-prodotto-mcd-mcm)=

:::{important} Proposizione — Una relazione fra MCD e mcm

Per due naturali positivi $a$ e $b$ vale

$$
\operatorname{MCD}(a,b)\cdot\operatorname{mcm}(a,b)=ab.
$$
:::

:::{admonition} Dimostrazione
:class: tip

Nelle due scomposizioni, un primo compare con esponenti $r$ e $s$;
se manca, gli attribuiamo esponente $0$.
Nel MCD compare con il minimo dei due esponenti e nel mcm con il massimo.
Moltiplicandoli, gli esponenti si sommano: il minimo più il massimo
è sempre $r+s$, proprio l'esponente di quel primo in $ab$.
Questo vale per ogni fattore primo, quindi i prodotti coincidono.
:::

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-mcd-es)=
### Divisori comuni e gruppi uguali

1. Calcola il MCD di $(18,30)$, $(48,72)$, $(35,64)$ e $(24,36,60)$.
    Per la prima coppia controlla anche elencando i divisori.

2. Una classe ha $30$ matite e $42$ penne da distribuire in kit
    identici senza avanzi. Qual è il massimo numero di kit? Che cosa contiene ciascuno?

:::{dropdown} Mostra la soluzione

I MCD sono rispettivamente $6,24,1,12$.
I divisori comuni di $18$ e $30$ sono $1,2,3,6$.
Si preparano $6$ kit, ciascuno con $5$ matite e $7$ penne.
:::

(r-mcm-es)=
### Multipli comuni e ritorni

1. Calcola il mcm di $(12,18)$, $(15,20)$, $(7,9)$ e $(8,24,16)$.
    Per la prima coppia controlla anche elencando i multipli positivi.

2. Due segnali si accendono rispettivamente ogni $10$ e ogni $15$
    secondi. Ora si accendono insieme: dopo quanto tempo accadrà di nuovo?
    Quante accensioni successive a quella iniziale avrà fatto ciascun segnale?

:::{dropdown} Mostra la soluzione

I mcm sono $36,60,63,48$. I primi multipli positivi sono
$12,24,36,\ldots$ e $18,36,54,\ldots$.
I segnali tornano insieme dopo $30$ secondi: il primo si è acceso
$3$ volte dopo l'inizio, il secondo $2$.
:::

(r-segnali-difficile)=
### Difficile -- Periodi con la virgola

**Facoltativo.** Due segnali luminosi di una pista si accendono
insieme all'istante iniziale. Il primo si riaccende ogni $5{,}5$ secondi;
il secondo ogni $12{,}1$ secondi. Dopo quanti secondi si riaccenderanno
insieme per la prima volta?

:::{dropdown} Mostra la soluzione

Esprimiamo i periodi in decimi di secondo: $55$ e $121$ decimi.
Poiché $55=5\cdot11$ e $121=11^2$,

$$
\operatorname{mcm}(55,121)=5\cdot11^2=605.
$$

Sono $605$ decimi di secondo, cioè $60{,}5$ secondi.
Verifica: $605:55=11$ cicli del primo segnale e $605:121=5$ del secondo.
Il cambio di unità permette di usare il mcm di due naturali.
:::

(r-mcd-mcm-problemi)=
### Squadre, tagli e appuntamenti

1. Due gruppi sportivi hanno rispettivamente $24$ e $36$ atleti.
    Si formano squadre tutte della stessa dimensione, la più grande possibile,
    senza mescolare i gruppi e senza lasciare fuori nessuno. Due esercizi di
    riscaldamento iniziano insieme alle 9:00 e si ripetono rispettivamente
    ogni $24$ e ogni $36$ minuti.
    Riprendi le scomposizioni in fattori primi di $24$ e $36$ e calcola MCD e mcm.
    Quanti atleti ci sono in ogni squadra e quante squadre forma ciascun gruppo?
    Dopo quanti minuti i due esercizi ricominciano insieme? A che ora?

2. Un rettangolo di stoffa misura $210$ cm per $360$ cm.
    Lo si vuole tagliare, senza scarti, in quadrati uguali con il lato
    più grande possibile. Trova il lato, l'area di ogni quadrato e il
    numero di quadrati ottenuti.

3. Tre persone hanno un giorno di riposo rispettivamente ogni
    $8$, $24$ e $16$ giorni. Oggi riposano tutte: fra quanti giorni
    accadrà di nuovo per la prima volta? Ci sono giorni in cui riposano
    la prima e la seconda, ma non la terza? E la seconda e la terza,
    ma non la prima? Motiva usando i multipli.

4. In un modello semplificato due fenomeni si ripetono ogni $365$
    e ogni $225$ giorni. Se oggi coincidono, dopo quanti giorni
    coincideranno di nuovo? Esprimi il risultato anche in periodi da $365$ giorni.

:::{dropdown} Mostra la soluzione

$24=2^3\cdot3$, $36=2^2\cdot3^2$:
$\operatorname{MCD}(24,36)=12$ e $\operatorname{mcm}(24,36)=72$.
Ogni squadra ha $12$ atleti: il primo gruppo forma $2$ squadre,
il secondo $3$. Gli esercizi ricominciano insieme dopo $72$ minuti,
alle 10:12.

$210=2\cdot3\cdot5\cdot7$ e $360=2^3\cdot3^2\cdot5$:
il lato è $\operatorname{MCD}(210,360)=30$ cm,
l'area è $900$ cm$^2$ e i quadrati sono $7\cdot12=84$.
Il primo riposo comune torna dopo $\operatorname{mcm}(8,24,16)=48$
giorni. Dopo $24$ giorni riposano la prima e la seconda, ma non la
terza. Ogni multiplo comune di $24$ e $16$ è anche multiplo di $8$,
quindi il secondo caso non può accadere.
Poiché $365=5\cdot73$ e $225=3^2\cdot5^2$, il mcm è
$3^2\cdot5^2\cdot73=16425$ giorni, cioè $45$ periodi da $365$ giorni.
:::

:::{dropdown} Mostra la soluzione

Il MCD non supera nessuno dei due numeri; il mcm non è inferiore
a nessuno dei due. Per numeri primi tra loro il MCD è $1$ e il mcm
è il prodotto. Poiché $34=2\cdot17$, il MCD di $17$ e $34$ è $17$
e il mcm è $34$. Per le due coppie: $2\cdot24=6\cdot8$ e
$12\cdot72=24\cdot36$. Per tre numeri la stessa formula non vale
in generale: $\operatorname{MCD}(2,4,8)=2$ e
$\operatorname{mcm}(2,4,8)=8$, ma $2\cdot8\ne2\cdot4\cdot8$.
:::

(r-mcd-mcm-controllo)=
### Un controllo rapido

Un compagno
scrive $\operatorname{MCD}(18,24)=6$ e
$\operatorname{mcm}(18,24)=144$. Usa la relazione fra i prodotti
per individuare e correggere l'errore.

:::{dropdown} Mostra la soluzione

$18\cdot24=432$, mentre $6\cdot144=864$.
Il mcm corretto è $432:6=72$.
:::
