---
title: "Dai tre coefficienti al piano dei resti"
---

*Per richiamare le idee già viste:* [Leggere e trasformare le espressioni algebriche](../algebra/index.md) · [Classi di equivalenza e partizioni](../relazioni-grafi/classi-di-equivalenza-e-partizioni.md).


(r-sec-dp-piano)=

:::{admonition} Attività — Tre numeri in ingresso, due in uscita
:class: attention

Per $P=a+bx+cx^2$, usa $x^2\equiv-1\pmod{x^2+1}$.
Quali sono i due coefficienti del resto?
Confronta $3+x+2x^2$, $1+x$ e $5+x+4x^2$.
Che cosa cambia nei tre coefficienti quando aggiungi $t(x^2+1)$?
:::

Rappresentiamo un polinomio di grado al massimo $2$ con la terna
$(a,b,c)$. Il suo resto è $(a-c)+bx$ e ha coordinate $(a-c,b,0)$.
Per esempio $3+x+2x^2$ va in $1+x$.
I punti della forma $(r+t,b,t)$ hanno tutti lo stesso resto $r+bx$:
formano una retta, che incontra il piano $c=0$ nel punto $(r,b,0)$.

```{figure} ../figure/schema-381fb3aad1ff.svg
:alt: Dai tre coefficienti al piano dei resti — diagramma
:width: 90%

Dai tre coefficienti al piano dei resti — diagramma
```

La freccia segue la retta della classe: si sottrae $c(1,0,1)$.
Non è una proiezione perpendicolare al piano, che lascerebbe
invariato $a$. Qui cambia anche il coefficiente costante.
Questa figura mostra solo i polinomi di grado al massimo $2$.
Nell'insieme di *tutti* i polinomi, una classe contiene anche
$P+xQ$, $P+x^2Q$, e così via: non è tutta rappresentata da quella retta.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-dp-piano-es)=
### Leggere la proiezione

Trova il resto modulo $x^2+1$ dei polinomi rappresentati da
$(4,2,3)$ e $(1,2,0)$. Sono nella stessa classe?
Trova altri due punti della stessa retta. Che cosa accade invece
alle coordinate $(a,b,c)$ se il modulo è $x^2$?

:::{dropdown} Mostra la soluzione

Entrambi danno $1+2x$. Altri punti sono $(2,2,1)$ e $(3,2,2)$.
Modulo $x^2$ il resto è $a+bx$: la mappa è $(a,b,c)\mapsto(a,b,0)$.
:::
