---
title: "La geometria delle operazioni"
---

(r-sec-geometria)=

*Lezione: 24 settembre*

(r-geometria)=

:::{admonition} Attività — Quattro istruzioni sulla linea dei numeri
:class: attention

Disegna una linea graduata e scegli i punti $0,1,2,3,4,5,6$.
Applica a ciascuno le istruzioni «aggiungi $3$», «sottrai $4$»,
«moltiplica per $2$», «dividi per $2$».

1. Quali istruzioni spostano tutti i punti della stessa quantità?

2. Quali cambiano le distanze tra i punti?

3. In quali casi non puoi rappresentare il risultato con un naturale?
:::

```{figure} ../figure/schema-3f9b040626a3.svg
:alt: Aggiungere tre sulla retta
:width: 90%

Aggiungere tre sulla retta
```

```{figure} ../figure/schema-a5b0df53fff6.svg
:alt: Sottrarre quattro sulla retta
:width: 90%

Sottrarre quattro sulla retta
```

```{figure} ../figure/schema-ef0740860992.svg
:alt: Moltiplicare per due sulla retta
:width: 90%

Moltiplicare per due sulla retta
```

```{figure} ../figure/schema-61377513d136.svg
:alt: Dividere per due sulla retta
:width: 90%

Dividere per due sulla retta
```

Nella sottrazione gli ingressi sono almeno $4$. Dividere un naturale dispari per $2$ porta fuori da $\N$.

:::{note} Operazioni viste come trasformazioni

- Aggiungere $3$: traslare di tre unità verso destra. Le distanze si conservano.

- Sottrarre $4$: traslare di quattro unità verso sinistra; in $\N$ è possibile solo partendo da almeno $4$.

- Moltiplicare per $2$: raddoppiare le distanze dall'origine e tra i punti.

- Dividere per $2$: dimezzare le distanze. Il risultato resta naturale solo per i numeri pari.
:::

Attenzione a distinguere la linea continua dai punti che rappresentano
i naturali: il punto a metà tra $1$ e $2$ esiste geometricamente,
ma non rappresenta un naturale.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-geometria-es)=
### Prevedere senza ridisegnare tutto

I punti $2$ e $5$ distano tre unità. Dove vanno e quanto distano dopo
un'addizione di $3$? E dopo una moltiplicazione per $2$?
Confronta poi «aggiungi $3$, quindi raddoppia» con «raddoppia, quindi aggiungi $3$»,
partendo da $4$. Sono la stessa trasformazione?

:::{dropdown} Mostra la soluzione

Vanno in $5,8$, distanza $3$; oppure in $4,10$, distanza $6$.
Partendo da $4$, si ottengono $(4+3)\cdot2=14$ e $4\cdot2+3=11$:
l'ordine delle due istruzioni conta.
:::
