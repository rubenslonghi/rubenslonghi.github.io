---
title: "Dalle funzioni alle classi, e ritorno"
---

*Per richiamare le idee già viste:* [Prodotto cartesiano e principio di moltiplicazione](../insiemi-logica/prodotto-cartesiano-e-principio-di-moltiplicazione.md) · [Che cos'è un insieme?](../insiemi-logica/che-cos-e-un-insieme.md).


(r-sec-rf-fibre)=

:::{admonition} Attività — Informazioni sufficienti
:class: attention

Conosci soltanto il resto modulo $7$ di un numero. Puoi dire dove
finirà sull'orologio dopo altri $2$ passi? Puoi dire se è pari?
Cerca due numeri con lo stesso resto che aiutino a rispondere.
:::

Data una funzione $f:A\to B$, diciamo $a\sim b$ quando $f(a)=f(b)$.
È un'equivalenza. Le classi sono i gruppi di ingressi che hanno la
stessa uscita, chiamati anche **fibre** non vuote della funzione.
Per $r_7$ ritroviamo proprio le classi di congruenza.

Se una funzione $g$ ha lo stesso valore su tutti gli elementi di
ciascuna classe, possiamo applicarla direttamente alle classi:
$\overline g([a])=g(a)$. Il risultato non dipende dal rappresentante.
Il percorso è

$$
a\ \xrightarrow{\ \pi\ }\ [a]\
\xrightarrow{\ \overline g\ }\ g(a).
$$

Per esempio, avanzare di due passi dipende solo dal resto iniziale.
La parità invece non si può ricavare dalla classe modulo $7$:
$1$ e $8$ sono nella stessa classe, ma hanno parità diversa.

La stessa idea tornerà con i polinomi: dividerli per un polinomio
fissato produce una funzione resto, e avere lo stesso resto
produce classi di equivalenza. Il capitolo [Divisibilità tra polinomi](../polinomi/index.md)
costruisce questo collegamento passo dopo passo.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-rf-fibre-es)=
### Quale informazione sopravvive?

Nel quoziente modulo $7$ su $\N$, stabilisci se ciascuna istruzione
ha senso senza scegliere un rappresentante particolare:
«prendi il resto dopo aver moltiplicato per $3$»;
«scrivi il numero di cifre»; «aggiungi $1$, poi prendi il resto».
Per le istruzioni ammesse calcola l'uscita della classe $[4]$.

:::{dropdown} Mostra la soluzione

La prima e la terza sono ammesse: $3\cdot4=12$ dà resto $5$,
$4+1=5$ dà resto $5$. Il numero di cifre non è costante sulla classe:
$4$ e $11$ sono equivalenti, ma hanno rispettivamente una e due cifre.
:::
