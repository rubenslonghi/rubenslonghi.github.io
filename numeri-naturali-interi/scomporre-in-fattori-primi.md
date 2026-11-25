---
title: "Scomporre in fattori primi"
---

:::{note} Nel percorso della 1 SP

- [26 settembre 2026](../cronologia-1sp.md#giorno-2026-09-26) — Multipli, divisori e numeri primi.

[Apri tutta la linea del tempo](../cronologia-1sp.md).
:::

(r-sec-scomposizione-primi)=

:::{admonition} Attività — Due strade, gli stessi mattoni?
:class: attention

Un gruppo parte da $90=9\cdot10$, un altro da $90=2\cdot45$.
Continuate a scomporre i fattori composti finché rimangono soltanto primi.
Cambiano i fattori finali? Cambia quante volte compare ciascun primo?
:::

(r-teo-fondamentale)=

:::{important} Teorema — Teorema fondamentale dell'aritmetica

Ogni numero naturale maggiore di $1$ si può scrivere come prodotto
di numeri primi. La scomposizione è unica a meno dell'ordine dei fattori.
:::

L'enunciato non comprende zero e uno: ecco perché non fanno parte della definizione di numero primo. L'unicità riguarda i fattori
*primi* e le loro ripetizioni: scrivere $90=9\cdot10$ oppure
$90=2\cdot45$ non la contraddice, perché la scomposizione non è terminata.

(r-es-novanta)=

:::{tip} Esempio — Divisioni successive

| 90 | 2 |
| --- | --- |
| 45 | 3 |
| 15 | 3 |
| 5 | 5 |
| 1 |  |

 $90=2\cdot3\cdot3\cdot5=2\cdot3^2\cdot5$.

A ogni passo dividiamo per un primo che sia divisore del numero rimasto.
Ci fermiamo a $1$. Per controllare, moltiplichiamo di nuovo i fattori.
:::

:::{note} Che cosa abbiamo costruito

Un numero può essere rappresentato sulla semiretta, descritto attraverso
condizioni, trasformato dalle operazioni e analizzato attraverso i suoi
divisori. Le proprietà giustificano le trasformazioni; le condizioni
dicono quando sono lecite; i controesempi mostrano quando una regola non vale.
:::

## Dalle parole alle espressioni: il 2 ottobre

Il numero $64$ può essere descritto come $2\cdot32$, $65-1$,
$16\cdot4$, $8^2$, $4^3$, oppure $5\cdot12+4$.
Nell'ultima forma si leggono divisore, quoziente e resto:
$a=bq+r$. Per confronto $2025=45^2$.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-scomposizioni-es)=
### Scomponi e ricomponi

Scomponi in fattori primi $60$, $84$, $126$, $225$ e $360$.
Controlla ogni risultato ricomponendo il numero. Due compagni trovano
$84=2^2\cdot3\cdot7$ e $84=2\cdot6\cdot7$: entrambi hanno terminato?

:::{dropdown} Mostra la soluzione

$60=2^2\cdot3\cdot5$;
$84=2^2\cdot3\cdot7$;
$126=2\cdot3^2\cdot7$;
$225=3^2\cdot5^2$;
$360=2^3\cdot3^2\cdot5$.
Il secondo compagno deve ancora scomporre $6=2\cdot3$.
:::

(r-n-rossi)=
### Vincita, debito e risparmio

Una vincita è di $12600$ euro. Si salda un debito di $4000$ euro;
si spende per le vacanze un quarto della somma rimasta e si divide
il resto in parti uguali fra tre figli. Scrivi un'unica espressione
e calcola quanto riceve ciascun figlio.

:::{dropdown} Mostra la soluzione

$[(12600-4000)-(12600-4000)/4]/3=2150$ euro.
Il quarto riguarda la somma dopo il debito, non la vincita iniziale.
:::
