---
title: "Tre insiemi e problemi di conteggio"
---

:::{note} Nel percorso della 1 SP

- [29 ottobre 2026](../cronologia-1sp.md#giorno-2026-10-29) — Insiemi: attività a squadre.

[Apri tutta la linea del tempo](../cronologia-1sp.md).
:::

*Per richiamare le idee già viste:* [Achille, i decimali infiniti e nuovi numeri](../razionali-reali/achille-i-decimali-infiniti-e-nuovi-numeri.md).


(r-ins-tre)=

::::{admonition} Attività — Calcio, nuoto e tennis
:class: attention

In una scuola, $200$ studenti praticano calcio ($A$), $140$ nuoto ($B$),
$110$ tennis ($C$). Nuoto e tennis sono praticati da $30$ studenti;
$150$ praticano soltanto calcio; $20$ calcio e nuoto ma non tennis;
$10$ tutti e tre gli sport; $40$ nessuno. Quanti sono gli studenti?

:::{dropdown} Mostra la soluzione

Solo $B\cap C$: $30-10=20$. Solo $A\cap C$: $200-150-20-10=20$.
Solo $B$: $140-20-20-10=90$; solo $C$: $110-20-20-10=60$.
L'unione ha $370$ elementi; con i $40$ esterni, il totale è $410$.
:::
::::

Compila prima il centro, poi le regioni doppie, infine quelle singole.
«Nuoto e tennis» comprende anche il centro; «calcio e nuoto ma
non tennis» lo esclude. Non confondere almeno due con esattamente due.

```{figure} ../figure/schema-faac568757ef.svg
:alt: Tre insiemi e problemi di conteggio — diagramma
:width: 90%

Tre insiemi e problemi di conteggio — diagramma
```

Per tre insiemi finiti:

$$
\begin{split}
|A\cup B\cup C|={}&|A|+|B|+|C|\\
&-|A\cap B|-|A\cap C|-|B\cap C|+|A\cap B\cap C|.
\end{split}
$$

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-ins-tre-regioni)=
### Leggere un secondo diagramma

Un diagramma ha queste regioni: solo $A$: $30$; solo $B$: $25$;
solo $C$: $12$; solo $A\cap B$: $10$; solo $A\cap C$: $8$;
solo $B\cap C$: $10$; tutti e tre: $5$.
Calcola $|A|,|B|,|C|$, l'unione, almeno due ed esattamente due.

:::{dropdown} Mostra la soluzione

$53,50,35$; unione $100$; almeno due $33$;
esattamente due $28$.
:::
