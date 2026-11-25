---
title: "Mettere in ordine e tradurre le condizioni"
---

(r-sec-ordine)=

*Lezione: 17--19 settembre*

(r-indovina)=

:::{admonition} Attività — Indovina il numero, senza indovinarlo
:class: attention

Un compagno pensa un naturale e dice: «È almeno $2$, ma è minore di $7$».

1. Scrivi tutti i numeri possibili. Le parole «almeno» e «maggiore di» dicono la stessa cosa?

2. Rappresenta i numeri su una semiretta: quale distanza scegli tra $0$ e $1$?

3. Ora l'indizio è «maggiore di $6$ e minore di $7$». Può aver scelto un naturale?
:::

Fissiamo un'origine, un verso e un'unità. Rappresentiamo $0$ nell'origine
e ogni successivo un'unità più a destra. Tra due naturali consecutivi
non ci sono altri naturali: in questo senso $\N$ è **discreto**.

```{figure} ../figure/schema-ea4de05efe79.svg
:alt: Mettere in ordine e tradurre le condizioni — diagramma
:width: 90%

Mettere in ordine e tradurre le condizioni — diagramma
```

:::{note} Dal linguaggio alle relazioni

| $a<b$ | $a$ è minore di $b$ |
| --- | --- |
| $a\le b$ | $a$ è minore o uguale a $b$ |
| $a> b$ | $a$ è maggiore di $b$ |
| $a\ge b$ | $a$ è maggiore o uguale a $b$ |

In $2\le m<7$ devono essere vere *entrambe* le condizioni:
$2\le m$ e $m<7$. L'estremo $2$ è incluso, $7$ è escluso.
:::

(r-es-estremi)=

:::{tip} Esempio — Elencare senza dimenticare gli estremi

I naturali che soddisfano $2<m<7$ formano l'insieme $\{3,4,5,6\}$.
Se invece $2\le m<7$, si aggiunge $2$.
Per $6<m<7$ non troviamo elementi: l'insieme delle soluzioni è
l'**insieme vuoto**, indicato con $\varnothing$ o $\{\}$.
:::

:::{warning} Due segni non garantiscono un intervallo

$5>m>7$ richiede $m<5$ e $m>7$: nessun numero soddisfa entrambe.
$5<m>7$ richiede $m>5$ e $m>7$: equivale a $m>7$.
Non basta leggere da sinistra a destra: bisogna controllare ogni relazione.
:::

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-ordine-simboli)=
### Dai simboli alle parole

Per ogni condizione, con $m\in\N$, scrivi una frase e l'insieme di tutti
i valori ammessi.

1. $2<m<7$;  b) $2\le m<7$;  c) $4<m\le8$.

2. **d)** $0\le m\le3$;  e) $m<5$;  f) $6<m<7$.

:::{dropdown} Mostra la soluzione

a) Tra $2$ e $7$, esclusi: $\{3,4,5,6\}$.
b) Da $2$ incluso a $7$ escluso: $\{2,3,4,5,6\}$.
c) Maggiore di $4$ e al massimo $8$: $\{5,6,7,8\}$.
d) Da $0$ a $3$ inclusi: $\{0,1,2,3\}$.
e) Minore di $5$: $\{0,1,2,3,4\}$.
f) Tra $6$ e $7$ esclusi: $\varnothing$.
:::

(r-ordine-parole)=
### Dalle parole ai simboli

Scrivi le condizioni in simboli e tutti i naturali che le soddisfano.

1. $m$ è maggiore di $3$ e minore o uguale a $7$.

2. $m$ è compreso tra $5$ e $9$, con entrambi gli estremi esclusi.

3. $m$ è compreso tra $2$ e $6$, con $2$ incluso e $6$ escluso.

4. $m$ è almeno $4$ e al massimo $8$.

5. $m$ è minore o uguale a $4$.

6. $m$ è maggiore o uguale a $7$.

:::{dropdown} Mostra la soluzione

a) $3<m\le7$: $\{4,5,6,7\}$.
b) $5<m<9$: $\{6,7,8\}$.
c) $2\le m<6$: $\{2,3,4,5\}$.
d) $4\le m\le8$: $\{4,5,6,7,8\}$.
e) $m\le4$: $\{0,1,2,3,4\}$.
f) $m\ge7$: $\{7,8,9,\ldots\}$.
:::

(r-ordine-trappola)=
### L'ultima riga del compito

Trova i naturali che soddisfano $5>m<7$. Spiega perché la risposta non è
«i numeri tra $5$ e $7$». Scrivi poi una condizione che individui soltanto $6$.

:::{dropdown} Mostra la soluzione

$m<5$ e $m<7$ equivalgono a $m<5$: $\{0,1,2,3,4\}$.
Una risposta alla seconda richiesta è $5<m<7$ con $m\in\N$.
:::
