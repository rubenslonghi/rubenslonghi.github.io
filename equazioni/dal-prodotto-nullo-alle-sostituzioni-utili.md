---
title: "Dal prodotto nullo alle sostituzioni utili"
---

*Per richiamare le idee già viste:* [Leggere e trasformare le espressioni algebriche](../algebra/index.md) · [Scomporre: riscrivere una somma come prodotto](../algebra/scomporre-riscrivere-una-somma-come-prodotto.md).


(r-eq-sost-avvio)=

:::{admonition} Attività — Un'equazione di quarto grado più semplice del previsto
:class: attention

Confronta $x^4-10x^2+9=0$ con $t^2-10t+9=0$.
Scomponi la seconda. Se $t=x^2$, ogni valore reale di $t$ è ammissibile?
:::

Si ottiene $(t-1)(t-9)=0$: $x^2=1$ oppure $x^2=9$,
quindi $S=\{-3,-1,1,3\}$. La sostituzione semplifica la struttura,
ma alla fine bisogna ritornare alla variabile iniziale e controllare i vincoli.
Per $(x-2)^2[(x-2)^2-4]=0$ basta separare i fattori, senza
sviluppare tutte le potenze. Una radice ripetuta si scrive una sola volta in $S$.

[Staffetta di equazioni: due schede A--D con autocontrollo — PDF](/materiali/striscioline-equazioni.pdf)

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-eq-sost-es)=
### Scegli una lettera provvisoria

Risolvi $x^4-13x^2+36=0$ e
$[(x-1)^2-4]^2-12[(x-1)^2-4]=0$.
Confronta il metodo strutturale con lo sviluppo completo: quale controllo finale usi?

:::{dropdown} Mostra la soluzione

Prima $S=\{-3,-2,2,3\}$.
Nella seconda ponendo $t=(x-1)^2-4$ si ha $t(t-12)=0$:
$(x-1)^2=4$ oppure $16$, quindi $S=\{-3,-1,3,5\}$.
:::
