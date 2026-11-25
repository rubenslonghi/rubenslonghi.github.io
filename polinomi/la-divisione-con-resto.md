---
title: "La divisione con resto"
---

*Per richiamare le idee già viste:* [Leggere e trasformare le espressioni algebriche](../algebra/index.md) · [Classi di equivalenza e partizioni](../relazioni-grafi/classi-di-equivalenza-e-partizioni.md).


(r-sec-dp-divisione)=

:::{admonition} Attività — Cancellare il termine di grado più alto
:class: attention

Vuoi dividere $x^2+3x+4$ per $x+1$.
Quale multiplo del divisore elimina $x^2$? Che cosa rimane sottraendolo?
Quale altro multiplo elimina il nuovo termine di grado più alto?
Confronta con l'uguaglianza dell'apertura del capitolo.
:::

(r-teo-dp-divisione)=

:::{important} Teorema — Divisione euclidea dei polinomi

Per polinomi $P,Q$ a coefficienti reali, con $Q\ne0$, esistono unici
polinomi $S,R$ tali che

$$
P=QS+R,\qquad R=0\ \text{oppure}\ \deg R<\deg Q.
$$

$S$ è il **quoziente**, $R$ è il **resto**.
:::

Riserviamo $Q$ al divisore fissato e $S$ al quoziente, per non confonderli
quando parleremo di congruenza modulo $Q$.
Nei numeri si confronta il resto con il divisore in grandezza;
nei polinomi si confrontano i *gradi*. Non chiediamo che i
coefficienti del resto siano positivi o più piccoli di quelli di $Q$.

### Un algoritmo che si può controllare

Ordina le potenze in ordine decrescente. Dividi il termine di grado
più alto del polinomio rimasto per quello del divisore; scrivi il
risultato nel quoziente. Moltiplicalo per tutto il divisore, sottrai
e ripeti finché il grado del residuo è minore di quello del divisore.
Il grado diminuisce a ogni passaggio, quindi il procedimento termina.

(r-es-dp-divisione-esempio)=

:::{tip} Esempio — Un divisore di secondo grado

Dividiamo $P=2x^3+3x^2-5x+4$ per $Q=x^2+1$.
Il primo termine del quoziente è $2x^3:x^2=2x$:

$$
P-2x(x^2+1)=3x^2-7x+4.
$$

Il secondo è $3x^2:x^2=3$:

$$
(3x^2-7x+4)-3(x^2+1)=-7x+1.
$$

Ci fermiamo al grado $1$: $S=2x+3$, $R=1-7x$.
Il controllo è $P=(x^2+1)(2x+3)+(1-7x)$.
:::

### Perché la coppia quoziente--resto è unica

Se $P=QS_1+R_1=QS_2+R_2$, allora
$Q(S_1-S_2)=R_2-R_1$. Se $S_1\ne S_2$, il membro sinistro
ha grado almeno $\deg Q$, mentre il destro, se non nullo, ha grado
minore di $\deg Q$: impossibile. Quindi $S_1=S_2$ e poi $R_1=R_2$.
Se $Q$ è una costante non nulla, il resto deve essere zero:
basta dividere tutti i coefficienti per quella costante.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-dp-divisioni-es)=
### Dividere e ricostruire

Trova quoziente e resto e verifica sempre $P=QS+R$:

1. $P=x^2+4x+5$, $Q=x+2$;

2. $P=x^3+2x^2+3x+4$, $Q=x^2+1$;

3. $P=x+1$, $Q=x^2+1$;

4. $P=x^2+1$, $Q=2x+1$.

:::{dropdown} Mostra la soluzione

1) $S=x+2$, $R=1$.
2) $S=x+2$, $R=2x+2$.
3) $S=0$, $R=x+1$.
4) $S=\frac12x-\frac14$, $R=\frac54$.
L'ultimo caso mostra perché può essere necessario usare frazioni.
:::
