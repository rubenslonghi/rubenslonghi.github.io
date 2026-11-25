---
title: "Le espressioni: scegliere l'ordine corretto"
---

(r-sec-espressioni)=

:::{admonition} Attività — Due risultati per la stessa riga?
:class: attention

Due studenti digitano sulla **calcolatrice** $$2+3\cdot4$$ uno ottiene $20$, l'altro $14$.
Descrivi le operazioni che hanno eseguito. Quali parentesi renderebbero
esplicita ciascuna intenzione? Confronta poi $24:6\cdot2$ con $24:(6\cdot2)$.
:::

:::{note} L'ordine delle operazioni

1. Risolvi le parentesi dall'interno verso l'esterno.

2. Calcola le potenze.

3. Esegui moltiplicazioni e divisioni nell'ordine da sinistra a destra.

4. Esegui addizioni e sottrazioni nell'ordine da sinistra a destra.

Ogni riga deve rappresentare lo stesso valore della precedente.
:::

(r-es-espressione)=

:::{tip} Esempio — Scrivere passaggi controllabili

$$
\begin{aligned}
2^5+3\,[10-(2^3+1)]&=32+3\,[10-9]\\
&=32+3\cdot1=35.
\end{aligned}
$$

Invece $24:6\cdot2=4\cdot2=8$, mentre $24:(6\cdot2)=24:12=2$.
:::

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-espressioni-es)=
### Calcolo con spiegazione

Calcola mostrando i passaggi. Usa le proprietà delle potenze quando opportuno.

1. $3^2+2\cdot(8-5)$.

2. $48:[2\cdot(3+1)]+5^0$.

3. $(2^3)^2:2^4+7\cdot3-5$.

4. $5^4:(5^3-5^2)+2^0$.

5. $\bigl[(2^3)^2:2^4+3\cdot(5^2-3\cdot7)\bigr]:(2^3:2^2)+5^0$.

6. $\bigl[(3^2)^2:3^3+2^4\cdot2^2:2^5\bigr]+3\cdot(5^2-2^3\cdot3)$.

Prima di completare d), controlla se tutte le divisioni sono esatte in $\N$.

:::{dropdown} Mostra la soluzione

a) $15$; b) $7$; c) $4+21-5=20$.
d) Il divisore è $125-25=100$, che non divide $625$.
L'espressione non si può completare mediante sole operazioni esatte in $\N$.

$$
\begin{aligned}
\text{e)}\quad &[2^6:2^4+3\cdot(25-21)]:(8:4)+1\\
&=[4+3\cdot4]:2+1=16:2+1=9;\\
\text{f)}\quad &[3^4:3^3+2^6:2^5]+3\cdot(25-8\cdot3)\\
&=[3+2]+3\cdot1=8.
\end{aligned}
$$

In f) si eseguono moltiplicazione e divisione da sinistra a destra:
$(2^4\cdot2^2):2^5=2$.
:::

(r-espressioni-errore)=
### Caccia al passaggio scorretto

 Uno studente scrive $2^3+2^2=2^5=32$. Un altro scrive
$18-(7-2)=18-7-2=9$. Individua il primo passaggio scorretto e correggi i risultati.

:::{dropdown} Mostra la soluzione

La somma delle potenze vale $8+4=12$; non si sommano gli esponenti.
La parentesi vale $5$, quindi $18-5=13$: sottrarre una differenza
non significa sottrarre entrambi i termini.
:::
