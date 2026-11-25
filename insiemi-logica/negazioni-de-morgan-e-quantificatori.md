---
title: "Negazioni, De Morgan e quantificatori"
---

*Per richiamare le idee già viste:* [Achille, i decimali infiniti e nuovi numeri](../razionali-reali/achille-i-decimali-infiniti-e-nuovi-numeri.md).


Negando una congiunzione basta che almeno una parte sia falsa;
negando una disgiunzione devono essere false entrambe:

$$
\overline{p\land q}\Leftrightarrow\overline p\lor\overline q,
\qquad
\overline{p\lor q}\Leftrightarrow\overline p\land\overline q.
$$

La negazione di «Paolo gioca a tennis e a golf» è «non gioca
a tennis oppure non gioca a golf», non «non pratica nessuno dei due».
Con $p=$ «oggi piove», $q=$ «c'è freddo», negare «piove e c'è
freddo» dà «non piove oppure non c'è freddo».

(r-es-log-intervalli)=

:::{tip} Esempio — Negare condizioni sui numeri

Per $p$: $x>5$, $q$: $x<-3$, la negazione di $p\lor q$ è
$x\le5\land x\ge-3$, cioè $-3\le x\le5$.
Per $t$: $x>7$, $u$: $x<5$, la congiunzione è impossibile;
la sua negazione $x\le7\lor x\ge5$ vale per ogni $x\in\R$.
:::

```{figure} ../figure/schema-f00a83bc5105.svg
:alt: Negazioni, De Morgan e quantificatori — diagramma
:width: 90%

Negazioni, De Morgan e quantificatori — diagramma
```

«Per ogni» si indica con $\forall$, «esiste almeno un» con $\exists$.

$$
\overline{\forall x\ P(x)}\Leftrightarrow\exists x\ \overline{P(x)},
\qquad
\overline{\exists x\ P(x)}\Leftrightarrow\forall x\ \overline{P(x)}.
$$

La negazione di «esiste un asino che vola» è «nessun asino vola».
La negazione di «ogni oggetto d'avorio è bianco» è «esiste un
oggetto d'avorio che non è bianco»: non deve necessariamente essere nero.

[Schede su insiemi e logica per il liceo sportivo — PDF](/materiali/insiemi-schede.pdf)

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-log-eta)=
### L'età e il complemento

In $U=[0,+\infty)$, traduci «l'età è almeno $7$ anni e minore di $12$»
e la sua negazione. Rappresentale con tratti ondeggiati e pallini pieni
o vuoti; controlla unione uguale a $U$ e intersezione vuota.

:::{dropdown} Mostra la soluzione

$7\le x<12$ e $x<7$ oppure $x\ge12$;
gli insiemi sono $[7,12)$ e $[0,7)\cup[12,+\infty)$.
:::
