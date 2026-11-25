---
title: "Proposizioni, connettivi e tavole di verità"
---

:::{note} Nel percorso della 1 SP

- [12 novembre 2026](../cronologia-1sp.md#giorno-2026-11-12) — Logica, deduzioni e negazioni.

[Apri tutta la linea del tempo](../cronologia-1sp.md).
:::

*Per richiamare le idee già viste:* [Achille, i decimali infiniti e nuovi numeri](../razionali-reali/achille-i-decimali-infiniti-e-nuovi-numeri.md).


Una proposizione è una frase di cui si può stabilire oggettivamente
il valore di verità. Negli appunti poniamo
$p=$ «Paolo gioca a tennis» e $q=$ «Paolo gioca a golf».
$p\land q$ significa che fa entrambe le cose;
$p\lor q$ che ne fa almeno una, anche entrambe.
$\overline p$ significa «Paolo non gioca a tennis».
La barra si può indicare anche con $\neg p$.

| $p$ | $q$ | $\overline p$ | $p\land q$ | $p\lor q$ | $p\Rightarrow q$ | $p\Leftrightarrow q$ |
| --- | --- | --- | --- | --- | --- | --- |
| V | V | F | V | V | V | V |
| V | F | F | F | V | F | F |
| F | V | V | F | V | V | F |
| F | F | V | F | F | V | V |

«E» corrisponde a $\cap$, «oppure» a $\cup$, «non» al complementare.
«Ma non» combina una congiunzione con una negazione e corrisponde
alla differenza fra insiemi. «Ma» da solo ha valore logico di «e».

## Implicazione, condizione necessaria e sufficiente

Per un triangolo, essere equilatero implica essere isoscele,
intendendo isoscele con almeno due lati congruenti.
L'insieme degli equilateri è incluso in quello degli isosceli.

```{figure} ../figure/schema-8b65f2e72298.svg
:alt: Proposizioni, connettivi e tavole di verità — diagramma
:width: 90%

Proposizioni, connettivi e tavole di verità — diagramma
```

Per $p\Rightarrow q$, diciamo che $p$ è condizione sufficiente per $q$
e $q$ condizione necessaria per $p$. L'implicazione è falsa soltanto
con premessa vera e conclusione falsa; non afferma da sola la premessa.
La frase «$p$ se $q$» significa $q\Rightarrow p$;
«$p$ solo se $q$» significa $p\Rightarrow q$.
La doppia implicazione $p\Leftrightarrow q$ richiede entrambi i versi:
un triangolo è equilatero se e solo se ha tre lati congruenti.
