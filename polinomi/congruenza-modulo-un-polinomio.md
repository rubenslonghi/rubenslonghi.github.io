---
title: "Congruenza modulo un polinomio"
---

*Per richiamare le idee già viste:* [Leggere e trasformare le espressioni algebriche](../algebra/index.md) · [Classi di equivalenza e partizioni](../relazioni-grafi/classi-di-equivalenza-e-partizioni.md).


(r-sec-dp-congruenza)=

:::{admonition} Attività — Polinomi diversi, stesso resto
:class: attention

Dividi $x^2+3x+4$ e $5x+2$ per $x+1$. I resti sono uguali?
Sottrai i due polinomi e verifica se la differenza è divisibile
per $x+1$. Ripeti confrontando $x^2$ e $-1$ modulo $x^2+1$.
:::

(r-def-dp-congruenza)=

:::{note} Definizione — Congruenza tra polinomi

Fissato $Q\ne0$, due polinomi $P,T$ sono **congruenti modulo $Q$**
se la loro differenza è un multiplo di $Q$:

$$
P\equiv T\pmod Q\quad\Longleftrightarrow\quad Q\mid(P-T).
$$

Questo equivale ad avere lo stesso resto nella divisione per $Q$.
:::

Per vedere l'equivalenza, scriviamo $P=QS+R_P$ e $T=QU+R_T$.
Se $R_P=R_T$, la differenza è $Q(S-U)$.
Viceversa, se $P-T$ è multiplo di $Q$, $R_P-R_T$ lo è anch'esso;
ma una differenza non nulla di resti ha grado minore di $\deg Q$,
quindi non può essere un multiplo non nullo di $Q$. I resti coincidono.

Nell'attività il primo resto è $2$, il secondo è $-3$:
non sono congruenti. Invece $x^2\equiv-1\pmod{x^2+1}$ perché
$x^2-(-1)=x^2+1$. La congruenza non è un'uguaglianza di polinomi:
$x^2$ non è diventato il polinomio costante $-1$.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-dp-equivalenza-es)=
### Dimostrare un'equivalenza

Mostra che la congruenza modulo $Q$ è riflessiva, simmetrica e transitiva.
Usa rispettivamente $P-P$, $T-P=-(P-T)$ e
$P-U=(P-T)+(T-U)$. Poi verifica se $x^2+3$ e $2$ sono congruenti
modulo $x^2+1$.

:::{dropdown} Mostra la soluzione

$P-P=Q\cdot0$; se $P-T=QS$, allora $T-P=Q(-S)$;
se $P-T=QS$ e $T-U=QV$, allora $P-U=Q(S+V)$.
Per l'ultimo confronto $(x^2+3)-2=x^2+1$: sì.
:::
