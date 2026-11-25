---
title: "Le proprietà delle potenze"
---

:::{note} Nel percorso della 1 SP

- [25 settembre 2026](../cronologia-1sp.md#giorno-2026-09-25) — Potenze ed espressioni.

[Apri tutta la linea del tempo](../cronologia-1sp.md).
:::

(r-sec-prop-potenze)=

:::{admonition} Attività — Conta i fattori, non fare il prodotto
:class: attention

Scrivi in forma estesa $2^3\cdot2^4$, $(2^3)^4$ e $2^3\cdot5^3$.

1. Quanti fattori $2$ compaiono nei primi due casi?

2. Nel terzo, puoi raggruppare ciascun $2$ con un $5$?

3. Quale caratteristica devi controllare prima di scegliere una regola?
:::

(r-prop-regole-potenze)=

:::{important} Proposizione — Cinque regole con le loro condizioni

Per basi naturali positive e $m,n\in\N$:

$$
\begin{aligned}
a^m a^n&=a^{m+n},& (a^m)^n&=a^{mn},\\
a^m:a^n&=a^{m-n}\quad(m\ge n),& a^n b^n&=(ab)^n.
\end{aligned}
$$

Se inoltre $a:b$ è un naturale, allora $a^n:b^n=(a:b)^n$.
Le regole del prodotto e della potenza di potenza si estendono alla base
zero quando tutti gli esponenti coinvolti sono positivi; le divisioni
richiedono sempre un divisore diverso da zero.
:::

Nel prodotto con la stessa base si sommano gli esponenti perché si
accodano le liste di fattori. Nella potenza di potenza si moltiplicano
perché si ripete l'intera lista. Con lo stesso esponente si possono
raggruppare i fattori a coppie.

(r-es-potenze-esempi)=

:::{tip} Esempio — Riconoscere che cosa è uguale

$5^2\cdot5^7=5^9$; $(2^3)^4=2^{12}$;
$12^5:6^5=(12:6)^5=2^5$.
Per $16^2:4^4$, riscriviamo $16^2=(2^4)^2=2^8$ e $4^4=(2^2)^4=2^8$:
il quoziente è $1$.
:::

:::{warning} La somma non è un prodotto

$a^m+a^n$ non si semplifica sommando gli esponenti.
Per esempio $2^3+2^2=12$, mentre $2^{3+2}=32$.
Anche $(a+b)^2$ non è in generale $a^2+b^2$: prova con $a=b=1$.
:::

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-potenze-regole)=
### Prima la regola, poi il risultato

Riduci a una potenza, quando possibile:
$3^2\cdot3^4$; $7^5:7^3$; $(5^2)^3$; $2^4\cdot5^4$;
$18^3:6^3$. Calcola separatamente $3^2+3^2$ e spiega perché non è $3^4$.

:::{dropdown} Mostra la soluzione

$3^6$; $7^2$; $5^6$; $10^4$; $3^3$.
$3^2+3^2=18$, mentre $3^4=81$. Si può raccogliere: $2\cdot3^2$.
:::

(r-potenza-resto-difficile)=
### Difficile -- Una potenza enorme, un resto piccolo

**Facoltativo.** Senza calcolare $3^{100}$, trova il resto della
sua divisione per $7$ usando le congruenze.
*Suggerimento: inizia a calcolare i resti della divisione per $7$
delle potenze di $3$, partendo dalle più piccole.*

:::{dropdown} Mostra la soluzione

I resti di $3,3^2,\ldots,3^6$ modulo $7$ sono $3,2,6,4,5,1$.
Il ciclo ricomincia moltiplicando ancora per $3$.
Poiché $100=6\cdot16+4$,

$$
3^{100}=(3^6)^{16}\cdot3^4
\equiv1^{16}\cdot4\equiv4\pmod7.
$$

Il resto è $4$.
:::
