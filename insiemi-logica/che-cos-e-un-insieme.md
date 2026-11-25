---
title: "Che cos'è un insieme?"
---

:::{note} Nel percorso della 1 SP

- [30 ottobre 2026](../cronologia-1sp.md#giorno-2026-10-30) — Definizioni e proprietà degli insiemi.
- [31 ottobre 2026](../cronologia-1sp.md#giorno-2026-10-31) — Esercizi sugli insiemi.

[Apri tutta la linea del tempo](../cronologia-1sp.md).
:::

*Per richiamare le idee già viste:* [Achille, i decimali infiniti e nuovi numeri](../razionali-reali/achille-i-decimali-infiniti-e-nuovi-numeri.md).


Un insieme è un raggruppamento di oggetti, detti *elementi*,
definito in modo oggettivo. Due insiemi sono uguali se contengono
esattamente gli stessi elementi: ordine e ripetizioni non contano.
Gli insiemi si indicano di solito con lettere maiuscole $A,B,C$;
gli elementi con minuscole $x,a,b$. Scriviamo $x\in A$ se appartiene,
$x\notin A$ se non appartiene. L'insieme vuoto è $\varnothing=\{\}$,
non $\{\varnothing\}$, che contiene un elemento.

(r-es-ins-rappresentazioni)=

:::{tip} Esempio — Tre rappresentazioni

Per elencazione: $B=\{3,5,87,-21\}=\{-21,3,5,87\}$.
Un diagramma di Eulero--Venn colloca gli elementi dentro una linea chiusa.
Per proprietà caratteristica:

$$
D=\{x\in\N\setminus\{0\}\mid36/x\in\N\}
=\{1,2,3,4,6,9,12,18,36\}.
$$

A sinistra della barra si specifica l'universo; a destra la proprietà.
L'esclusione di $0$ evita la divisione per zero.
Gli insiemi infiniti si possono descrivere con una proprietà o con
un'elencazione accompagnata da una regola chiara, come $\N=\{0,1,2,\ldots\}$.
:::

Per $E=\{x\in\R\mid x\ge4\}$, sia $4$ sia $4{,}000001$ appartengono a $E$.
Per $F=\{x\in\R\mid x>3\}$, invece, $3\notin F$, ma $3{,}000001\in F$.

## Inclusione e insieme delle parti

$A\subseteq B$ significa che ogni elemento di $A$ appartiene a $B$.
Si ammette l'uguaglianza: $A\subseteq A$.
In questo libro $A\subset B$ indica l'inclusione stretta, cioè anche $A\ne B$.
Il vuoto è sottoinsieme di ogni insieme. Attenzione:
$2\in\N$, mentre $\{2\}\subseteq\N$.

$$
\N\subset\Z\subset\Q\subset\R.
$$

```{figure} ../figure/schema-2974569c43b5.svg
:alt: Che cos'è un insieme? — diagramma
:width: 90%

Che cos'è un insieme? — diagramma
```

L'insieme delle parti $\mathcal P(A)$ è l'insieme di tutti i sottoinsiemi di $A$.
Se $A=\{x,y\}$,
$\mathcal P(A)=\{\varnothing,\{x\},\{y\},\{x,y\}\}$.
Se $|A|=n$ è finito, $|\mathcal P(A)|=2^n$: per ogni elemento ci sono
due possibilità, includerlo o escluderlo.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-ins-parti)=
### Elemento oppure sottoinsieme?

Elenca $\mathcal P(\{c,k,f\})$. Spiega la differenza fra
$\{c\}\subseteq\{c,k,f\}$ e $\{c\}\in\mathcal P(\{c,k,f\})$.
Quanti sottoinsiemi hanno tre elementi? Quanti nessun elemento?

:::{dropdown} Mostra la soluzione

$\varnothing,\{c\},\{k\},\{f\},\{c,k\},\{c,f\},\{k,f\},\{c,k,f\}$.
Il primo simbolo confronta due insiemi per inclusione; il secondo
afferma che un insieme è elemento di una famiglia di insiemi.
C'è un solo sottoinsieme di tre elementi e un solo vuoto.
:::
