---
title: "Unione, intersezione, differenza e complementare"
---

*Per richiamare le idee già viste:* [Achille, i decimali infiniti e nuovi numeri](../razionali-reali/achille-i-decimali-infiniti-e-nuovi-numeri.md).


Fissato un universo $U$, definiamo

$$
\begin{aligned}
A\cup B&=\{x\in U\mid x\in A\text{ oppure }x\in B\},\\
A\cap B&=\{x\in U\mid x\in A\text{ e }x\in B\},\\
A\setminus B&=\{x\in A\mid x\notin B\},\qquad
\overline A=U\setminus A.
\end{aligned}
$$

Il complementare, indicato negli appunti con una barra, dipende da $U$.
«Oppure» include la possibilità che entrambe le condizioni valgano.
Per esempio, i quadrati sono l'intersezione fra i rombi e i rettangoli,
adottando le definizioni inclusive di queste figure.

```{figure} ../figure/schema-a25470a2f486.svg
:alt: Unione, intersezione, differenza e complementare — diagramma
:width: 90%

Unione, intersezione, differenza e complementare — diagramma
```

Nell'indagine iniziale: inglese $300$, francese $150$, nessuna lingua
$100$, almeno una $400$. Quindi entrambe $300+150-400=50$,
soltanto inglese $250$, soltanto francese $100$.
La cardinalità di un insieme finito $A$ si indica $|A|$.

$$
|A\cup B|=|A|+|B|-|A\cap B|.
$$

## Le proprietà delle operazioni

$$
\begin{aligned}
A\cup A&=A,&A\cap A&=A,\\
A\cup B&=B\cup A,&A\cap B&=B\cap A,\\
(A\cup B)\cup C&=A\cup(B\cup C),&
(A\cap B)\cap C&=A\cap(B\cap C),\\
A\cup(A\cap B)&=A,&A\cap(A\cup B)&=A.
\end{aligned}
$$

Sono, nell'ordine, idempotenza, commutatività, associatività e assorbimento.
Valgono entrambe le proprietà distributive:

$$
\begin{aligned}
A\cap(B\cup C)&=(A\cap B)\cup(A\cap C),\\
A\cup(B\cap C)&=(A\cup B)\cap(A\cup C).
\end{aligned}
$$

Le leggi di De Morgan sono

$$
\overline{A\cap B}=\overline A\cup\overline B,
\qquad \overline{A\cup B}=\overline A\cap\overline B.
$$

```{figure} ../figure/schema-2dfeb9b58b87.svg
:alt: Unione, intersezione, differenza e complementare — diagramma
:width: 90%

Unione, intersezione, differenza e complementare — diagramma
```

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-ins-due-problemi)=
### Biblioteche e sport

1. $50$ studenti frequentano la biblioteca d'istituto; fra questi,
    $42$ non frequentano quella comunale. La comunale è frequentata da
    $60$ studenti e $18$ non frequentano nessuna delle due. Quanti sono in tutto?

2. In una scuola di $400$ studenti, $150$ praticano calcio,
    $100$ tennis e $30$ entrambi. Quanti non praticano nessuno dei due?

:::{dropdown} Mostra la soluzione

Intersezione $8$, totale $50+60-8+18=120$.
Nel secondo problema $400-(150+100-30)=180$.
:::

(r-ins-demorgan)=
### I divisori e il significato di «oppure»

Sia $U=\{x\in\N\mid x\le36\}$, con $0\in U$.
Siano $A$ e $B$ gli insiemi dei divisori positivi di $36$ e di $15$.
Elenca $A,B,A\cap B$; descrivi $\overline{A\cap B}$ e
$\overline A\cup\overline B$. «Non è divisore di $36$ oppure non è
divisore di $15$» equivale a «non è divisore di nessuno dei due»?

:::{dropdown} Mostra la soluzione

$A=\{1,2,3,4,6,9,12,18,36\}$; $B=\{1,3,5,15\}$;
$A\cap B=\{1,3\}$. Entrambi i complementari richiesti danno $U\setminus\{1,3\}$.
Le frasi non sono equivalenti: la seconda richiede
$\overline A\cap\overline B$. Per esempio $2$ soddisfa la prima ma non la seconda.
:::
