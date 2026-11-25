---
title: "Cifre, posizioni e numerazione binaria"
---

(r-sec-base-due)=

:::{admonition} Attività — Una mano, trentadue configurazioni
:class: attention

Assegna alle dita, dal pollice al mignolo, i valori $1,2,4,8,16$.
Un dito disteso vale il proprio numero; uno ripiegato vale zero.
Rappresenta $0,1,2,3,7,13,16,31$. Come fai a non confondere $13$ con $22$?
Puoi rappresentare $32$? Quante configurazioni diverse esistono?
:::

Una scrittura posizionale attribuisce valore a una cifra in base al suo posto.
In base due $100111_2=2^5+2^2+2^1+2^0=39$.
I due successivi sono $101000_2$ e $101001_2$.
In base dieci $307=3\cdot10^2+0\cdot10+7$; in base due
$1101_2=1\cdot2^3+1\cdot2^2+0\cdot2+1=13$.
Ogni cifra binaria è $0$ oppure $1$. Cinque posizioni danno $2^5=32$
configurazioni: rappresentano i numeri da $0$ a $31$, non da $1$ a $32$.

:::{note} La convenzione della mano

La macro della mano legge le dita
dal pollice al mignolo: `10110` significa $1+4+8=13$.
La scrittura binaria usuale, dal peso maggiore al minore, è invece $01101_2$.
:::

```{figure} ../figure/schema-90da35a86bfc.svg
:alt: Cifre, posizioni e numerazione binaria — diagramma
:width: 90%

Cifre, posizioni e numerazione binaria — diagramma
```

### Cambiare base con divisioni successive

Dividi il numero per la base, conserva il resto e ripeti con il quoziente.
Per $13$ in base $2$: $13=2\cdot6+1$, $6=2\cdot3+0$,
$3=2\cdot1+1$, $1=2\cdot0+1$. Leggendo i resti dall'ultimo al primo
ottieni $1101_2$. L'algoritmo termina perché i quozienti positivi diminuiscono.
Funziona in ogni base intera $b\ge2$, con cifre fra $0$ e $b-1$.
Il primo resto determina l'ultima cifra; ripetendo il ragionamento si vede
anche perché la scrittura è unica, a meno degli zeri iniziali.

(r-cripto-primi)=

:::{admonition} Attività — Messaggi segreti e investigatori
:class: attention

Dividetevi in mittenti, destinatari e investigatori. I mittenti scelgono
due primi piccoli e comunicano il loro prodotto. Il destinatario conosce
i due fattori; gli investigatori provano a recuperarli dal prodotto.
Prima manche: usate la scomposizione in fattori primi. Seconda manche:
scegliete liberamente una strategia. Annotate dati noti, tempo e tentativi.
Confrontate $77,143,221$. Che differenza c'è fra moltiplicare e risalire ai fattori?
:::

È un modello di indagine sui fattori, non un sistema di cifratura sicuro:
con numeri piccoli la scomposizione è rapida. La sfida riguarda le
informazioni necessarie per ricostruire un calcolo.

[La mano binaria: disegno finale e convenzione delle dita — PDF](/materiali/mano-binaria.pdf)

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-bin-es)=
### Contatore e riporti

Scrivi in base due $19,24,31,32,45$. Conta da $0$ a $12$ in base tre.
Spiega il riporto in $1111_2+1$. Inventa una prova per riconoscere
se un numero binario è pari senza convertirlo in base dieci.

:::{dropdown} Mostra la soluzione

$10011_2,11000_2,11111_2,100000_2,101101_2$.
In base tre: $0,1,2,10,11,12,20,21,22$, $100,101,102,110$.
$1111_2+1=10000_2$; è pari se e solo se l'ultima cifra è $0$.
:::
