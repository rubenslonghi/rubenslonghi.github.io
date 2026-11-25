---
title: "Divisione con resto anche per numeri negativi"
---

:::{note} Differenze come coppie

Una pista di approfondimento descrive
l'intero $a-b$ con la coppia di naturali $(a,b)$.
Le coppie $(a,b)$ e $(c,d)$ danno lo stesso intero se $a+d=b+c$.
Per esempio $(2,5)$ e $(4,7)$ descrivono entrambe $-3$.
La somma delle coppie è $(a+c,b+d)$: un altro collegamento con le classi di equivalenza.
:::

(r-z-resto-avvio)=

:::{admonition} Attività — Una posizione anche andando all'indietro
:class: attention

In un orologio a sette posizioni, da $0$ arretra di $1$, poi di $8$.
Scrivi $-1$ e $-8$ come $7q+r$ con $0\le r<7$. Quale resto ottieni?
:::

Con divisore positivo $b$, anche per un intero $a$ cerchiamo
$a=bq+r$, con $q\in\Z$ e $0\le r<b$. Per esempio
$-8=7(-2)+6$: il resto è $6$, non $-1$.
Il quoziente può essere negativo, ma la convenzione sul resto è la stessa.

## Gli orologi degli appunti, estesi agli interi

I naturali proseguono verso l'esterno in blu, i negativi verso l'interno
in rosso. Ogni petalo raccoglie una classe di resto. Per esempio
$-1\equiv6\equiv13\pmod7$: tre numeri diversi, una stessa posizione.

```{figure} ../figure/schema-c700a4ec47fe.svg
:alt: Classi di resto modulo 2, con gli interi negativi
:width: 90%

Classi di resto modulo 2, con gli interi negativi
```

```{figure} ../figure/schema-9251d66ae3c1.svg
:alt: Classi di resto modulo 3, con gli interi negativi
:width: 90%

Classi di resto modulo 3, con gli interi negativi
```

```{figure} ../figure/schema-3f32586f34f9.svg
:alt: Classi di resto modulo 5, con gli interi negativi
:width: 90%

Classi di resto modulo 5, con gli interi negativi
```

```{figure} ../figure/schema-d71e3d73920d.svg
:alt: Classi di resto modulo 7, con gli interi negativi
:width: 90%

Classi di resto modulo 7, con gli interi negativi
```

```{figure} ../figure/schema-39ae8049c12a.svg
:alt: Classi di resto modulo 10, con gli interi negativi
:width: 90%

Classi di resto modulo 10, con gli interi negativi
```

```{figure} ../figure/schema-44e87ab3df05.svg
:alt: Classi di resto modulo 12, con gli interi negativi
:width: 90%

Classi di resto modulo 12, con gli interi negativi
```

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-z-resti-es)=
### Giri completi e resto

Trova quoziente e resto di $-17$ per $5$ e di $-25$ per $6$.
Mostra che $-1,6,13$ sono congruenti modulo $7$. La figura a petali
del capitolo mostrava soltanto i naturali: ora immagina come estenderla verso l'interno.

:::{dropdown} Mostra la soluzione

$-17=5(-4)+3$; $-25=6(-5)+5$.
I tre numeri hanno tutti resto $6$ modulo $7$.
:::
