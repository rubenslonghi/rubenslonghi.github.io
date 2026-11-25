---
title: "Numeri interi: descrivere due versi"
---

:::{note} Nel percorso della 1 SP

- [8 ottobre 2026](../cronologia-1sp.md#giorno-2026-10-08) — Numeri interi, valore assoluto e potenze.
- [9 ottobre 2026](../cronologia-1sp.md#giorno-2026-10-09) — Calcolare con interi e valori assoluti.
- [10 ottobre 2026](../cronologia-1sp.md#giorno-2026-10-10) — Potenze a base intera: lavoro nei due gruppi.
- [12 ottobre 2026](../cronologia-1sp.md#giorno-2026-10-12) — Restituzione delle verifiche ed espressioni con interi.
- [19 ottobre 2026](../cronologia-1sp.md#giorno-2026-10-19) — Preparazione alla verifica su interi e razionali.
- [22 ottobre 2026](../cronologia-1sp.md#giorno-2026-10-22) — Riepilogo su interi e razionali.
- [23 ottobre 2026](../cronologia-1sp.md#giorno-2026-10-23) — Verifica su interi e razionali.

[Apri tutta la linea del tempo](../cronologia-1sp.md).
:::

(r-sec-interi-integrazione)=

:::{admonition} Attività — Spostamenti e saldo
:class: attention

Un atleta parte dal punto $0$, avanza di $4$ passi e arretra di $7$.
Dove arriva? Un conto ha saldo $5$ euro e registra una spesa di $8$ euro:
quale numero descrive il nuovo saldo? Disegna entrambe le situazioni.
:::

(r-def-z-def)=

:::{note} Definizione — Interi, opposto e valore assoluto

Gli interi sono $\Z=\{\ldots,-3,-2,-1,0,1,2,3,\ldots\}$.
L'opposto di $a$ è $-a$ e soddisfa $a+(-a)=0$.
Il valore assoluto $|a|$ è la distanza di $a$ da zero sulla retta.
:::

Sulla retta i numeri crescono verso destra: $-7<-3<0<2$.
Sommare un positivo significa avanzare, sommare un negativo arretrare.
Sottrarre significa sommare l'opposto: $a-b=a+(-b)$, dunque
$4-(-3)=4+3=7$. Il segno di un numero e il simbolo di sottrazione
possono avere lo stesso aspetto ma ruoli diversi.

(r-z-prod-avvio)=

:::{admonition} Attività — Quale regola conserva la distributiva?
:class: attention

Sappiamo che $(-3)\cdot2=-6$ e $(-3)\cdot0=0$.
Sviluppa $(-3)[2+(-2)]$. Quale valore deve avere $(-3)(-2)$
perché la distributiva continui a valere?
:::

Il prodotto di due interi di uguale segno è positivo se i fattori non
sono nulli; di segno diverso è negativo. Il ragionamento dell'attività
dà $0=-6+(-3)(-2)$, quindi $(-3)(-2)=6$.
Le proprietà di somma e prodotto e la legge di annullamento restano valide.
La divisione non è interna a $\Z$: $3:2$ richiede un nuovo insieme.

Con cinque cifre in base $b$ si rappresentano $b^5$ configurazioni,
da $0$ a $b^5-1$. Con dieci dita binarie: $2^{10}=1024$
configurazioni, da $0$ a $1023$.

## Segni, opposti e distanze negli appunti

Due numeri non nulli sono *concordi* se hanno lo stesso segno
($-3,-12$), *discordi* se hanno segni diversi ($-3,+5$).
Lo zero coincide con il suo opposto: $+0=-0=0$.
Scriviamo $\Z^+=\{1,2,\ldots\}$, $\Z^-=\{\ldots,-2,-1\}$ e
$\Z_0^+=\{0,1,2,\ldots\}=\N$.
Gli interi sono discreti e non hanno né minimo né massimo.

```{figure} ../figure/schema-1824b4ffd41d.svg
:alt: Numeri interi: descrivere due versi — diagramma
:width: 90%

Numeri interi: descrivere due versi — diagramma
```

Il simbolo meno ha tre ruoli: in $15-10$ indica una sottrazione;
in $-8$ il segno; in $-(+10)$ l'operazione di prendere l'opposto.
La variazione di una coordinata si descrive con
$\Delta x=x_{\mathrm{finale}}-x_{\mathrm{iniziale}}$.

$$
|a|=\begin{cases}a& a\ge0,\\-a& a<0.\end{cases}
\qquad |+16|=|-16|=16.
$$

La distanza fra $a$ e $b$ è $|a-b|$: non dipende dall'ordine dei punti.

## Somma algebrica e regola dei segni

$$
\begin{aligned}
(-2)+(-6)&=-(2+6)=-8,\\
(-3)+(+1)&=-(3-1)=-2,\\
(-2)+(+4)&=+(4-2)=+2,\\
(+5)+(-5)&=0.
\end{aligned}
$$

Concordi: somma i valori assoluti e conserva il segno. Discordi:
sottrai il valore assoluto minore dal maggiore e conserva il segno del
numero con valore assoluto maggiore. Una *somma algebrica* raccoglie
addizioni e sottrazioni, usando $a-b=a+(-b)$.
Perché $(-1)(-1)=1$? Posto $x=(-1)(-1)$, la distributiva impone

$$
0=(-1)\cdot0=(-1)[1+(-1)]=-1+x,
$$

quindi $x=1$. Così $-5\cdot(-4)=-(-20)=20$.
Un prodotto di fattori non nulli è negativo esattamente quando il
numero dei fattori negativi è dispari:
$(-2)(-3)(-1)=-6$, mentre $(-2)(+3)(-1)=6$.
La stessa regola dei segni vale nella divisione, quando è possibile:
$(-8):(-2)=4$, $0:(-5)=0$, $9:(-3)=-3$.

(r-es-z-argh)=

:::{tip} Esempio — ARGH: la base va letta prima di calcolare

$-5^2=-25$, mentre $(-5)^2=25$.
Con esponente naturale positivo, una base negativa dà potenza positiva
per esponente pari e negativa per esponente dispari.
L'esponente zero richiede base non nulla; $0^0$ resta escluso in questo percorso.
:::

### ARGHONE: il meno davanti alla parentesi

$$
+(3-5+7^2)=3-5+7^2,\qquad
-(3-5+7^2)=-3+5-7^2.
$$

Il secondo passaggio è la proprietà distributiva del fattore $-1$.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-z-primi-es)=
### Retta, segni e parentesi

Ordina $-8,3,-2,0,-5$; calcola $|-8|$, $-|{-8}|$, $-(-8)$.
Poi calcola $-4+7$, $-4-7$, $6-(-2)$, $-3-(-9)$ e
$5-[2-(-3)]$. Per due calcoli accompagna il risultato con una retta.

:::{dropdown} Mostra la soluzione

$-8<-5<-2<0<3$; $8,-8,8$; risultati $3,-11,8,6,0$.
:::

(r-z-potenze)=
### Conta i fattori negativi

Calcola $(-2)^4$, $-2^4$, $(-2)^3$, $(-1)^{101}$ e $(-1)^{100}$.
Spiega perché le parentesi cambiano il primo confronto e perché
la parità dell'esponente decide il segno di una potenza a base negativa.

:::{dropdown} Mostra la soluzione

$16,-16,-8,-1,1$. In $-2^4$ la potenza riguarda $2$,
poi si prende l'opposto; in $(-2)^4$ la base è $-2$.
:::

(r-z-appunti-vf)=
### Verificare una frase, cercare un controesempio

Decidi se le seguenti affermazioni valgono per tutti gli interi.

1. $|a|=|b|$ implica $a=b$.

2. $|-a|=-|a|$; $|-a|=|a|$.

3. $|a|=0$ implica $a=0$.

4. $||a||=a$; $||a||=|a|$.

Quanti interi sono compresi fra $-8$ e $1$, estremi inclusi?
Se $a<0$, quale segno hanno $-a$, $-|a|$ e $|-a|$?

:::{dropdown} Mostra la soluzione

Falsa: $a=3,b=-3$. La prima uguaglianza del punto 2 vale solo per $a=0$,
la seconda sempre. Il punto 3 è vero. Al punto 4 la prima è falsa per
$a<0$, la seconda è sempre vera. Gli interi sono $10$.
I tre segni sono rispettivamente positivo, negativo, positivo.
:::

(r-z-appunti-potenze)=
### Le potenze della lezione

Semplifica riconducendo le basi a fattori primi:

$$
\begin{gathered}
(-3)^{12}:(-3)^9,\quad (-5)^7:5^5,\quad (-3)^{12}:3^9,\\
(-27)^3\cdot(+3)^2:(-9)^5,\quad
(-2)^{11}:2^8,\quad (-49)^3:(+7)^5.
\end{gathered}
$$

:::{dropdown} Mostra la soluzione

$-27,-25,27,3,-8,-7$.
Nel quarto calcolo i due segni negativi si dividono e
$3^9\cdot3^2:3^{10}=3$.
:::
