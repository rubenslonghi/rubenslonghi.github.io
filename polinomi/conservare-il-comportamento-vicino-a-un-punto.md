---
title: "Conservare il comportamento vicino a un punto"
---

*Per richiamare le idee già viste:* [Leggere e trasformare le espressioni algebriche](../algebra/index.md) · [Classi di equivalenza e partizioni](../relazioni-grafi/classi-di-equivalenza-e-partizioni.md).


(r-sec-dp-vicino)=

:::{admonition} Attività — Il quadrato di un piccolo spostamento
:class: attention

Nell'identità $(2+h)^2=4+4h+h^2$, confronta il valore completo con
$4+4h$ per $h=1$, $h=1/10$, $h=1/100$.
Quanto vale la differenza? Quale parte hai trascurato?
:::

Per descrivere ciò che accade vicino a $a$, poniamo $h=x-a$ e
riscriviamo il polinomio in potenze di $h$.
Modulo $(x-a)^2=h^2$ rimangono soltanto una costante e il termine
di primo grado in $h$. Per $P(x)=x^2$ vicino a $2$,

$$
x^2=(x-2)^2+4(x-2)+4.
$$

Il resto è $4+4(x-2)=4x-4$.
In termini duali, $(2+\varepsilon)^2=4+4\varepsilon$.

```{figure} ../figure/schema-de73fba8790b.svg
:alt: Conservare il comportamento vicino a un punto — diagramma
:width: 90%

Conservare il comportamento vicino a un punto — diagramma
```

La differenza fra curva e retta è $(x-2)^2$: vicino a $2$ diventa
molto piccola. La retta incontra la curva in $(2,4)$ e ne segue la
direzione in quel punto: è la **tangente** alla parabola.
Qui lo vediamo con un'identità algebrica; una definizione generale
di tangente e di derivata verrà più avanti.

Occorre distinguere i due calcoli: nei duali $\varepsilon^2=0$
esattamente; per un reale $h\ne0$, $h^2$ non è zero.
Usare la retta per stimare $P(a+h)$ è un'approssimazione,
e il termine trascurato ne misura l'errore.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-dp-locale-es)=
### Una retta ottenuta dal resto

Riscrivi $P(x)=x^2+3x+1$ ponendo $x=1+h$.
Trova il resto modulo $(x-1)^2$ e il punto comune a curva e retta.
Confronta i valori per $x=1+1/10$: quanto differiscono?

:::{dropdown} Mostra la soluzione

$P(1+h)=5+5h+h^2$. Il resto è $5+5(x-1)=5x$;
il punto comune è $(1,5)$. Per $x=11/10$ la retta dà $11/2=5{,}5$,
il polinomio $551/100=5{,}51$: la differenza è $1/100$.
:::
