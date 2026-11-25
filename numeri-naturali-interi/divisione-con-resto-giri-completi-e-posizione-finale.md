---
title: "Divisione con resto: giri completi e posizione finale"
---

(r-sec-resto)=

*Lezione: 21--24 settembre*

(r-tredici-passi)=

:::{admonition} Attività — Tredici passi su cinque posizioni
:class: attention

Parti da $0$ su un orologio a $5$ posizioni e avanza di $13$ passi.

1. Quanti giri completi hai fatto? Dove ti trovi?

2. Anche $13=5\cdot1+8$ è un'uguaglianza vera. Perché $8$ non è il resto della divisione per $5$?

3. Trova altri tre numeri di passi che ti portino nella stessa posizione.
:::

(r-def-divisione-resto)=

:::{note} Definizione — Quoziente intero e resto

Per $a,b\in\N$, con $b>0$, esistono unici naturali $q,r$ tali che

$$
a=bq+r,\qquad 0\le r<b.
$$

$q$ è il **quoziente intero**; $r$ è il **resto**.
Se $r=0$, la divisione è esatta.
:::

La condizione $r<b$ dice che non resta abbastanza per formare un altro
gruppo completo. Su un orologio a $b$ posizioni, $q$ conta i giri e
$r$ identifica la posizione finale.

(r-es-resto-esempio)=

:::{tip} Esempio — Due letture dello stesso calcolo

$13=5\cdot2+3$: due giri e posizione $3$.
$8=6\cdot1+2$: un giro e posizione $2$.
Scriviamo anche $8\equiv2\pmod6$, letto «otto è congruente a due modulo sei».
:::

(r-def-congruenza)=

:::{note} Definizione — Congruenza

Due naturali sono **congruenti modulo** $n$, con $n\ge1$, se
hanno lo stesso resto nella divisione per $n$. Il simbolo è $\equiv$.
Sull'orologio significa raggiungere la stessa posizione.
:::

$8\equiv2\pmod6$ non significa $8=2$: l'orologio conserva la posizione,
ma non il numero di giri. L'addizione e la moltiplicazione sull'orologio
si eseguono prendendo il resto della somma e del prodotto usuali.

(r-fig-petali-sette)=

```{figure} ../figure/schema-4fe57fe858e5.svg
:alt: Sette petali, sette classi di resto
:width: 90%

Sette petali, sette classi di resto
```

Segui la spirale in senso orario: il primo giro è nero, i successivi
sono blu. Ogni passo rappresenta il naturale successivo; dopo sette
passi torni nella stessa direzione, più all'esterno.
I numeri di uno stesso petalo hanno lo stesso resto modulo $7$:
per esempio $3,10,17,\ldots$ e $0,7,14,\ldots$.
La spirale continua: il disegno ne mostra soltanto un tratto.

**Prova tu:** in quale petalo collocheresti $24$? E $35$?
Un numero può appartenere a due petali? Nel capitolo sulle relazioni
chiameremo questi gruppi *classi di equivalenza*.

La figura [Divisione con resto: giri completi e posizione finale](#r-fig-petali-sette) conserva anche i giri che l'orologio
ordinario nasconde: numeri diversi possono indicare la stessa posizione.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-resto-es)=
### Dal calcolo all'orologio

Trova $q$ e $r$ nelle divisioni $38:5$, $50:7$, $4:9$ e $2026:12$.
Per ciascuna scrivi la verifica $a=bq+r$ e controlla $0\le r<b$.
Calcola poi sull'orologio a $6$ posizioni $4+5$ e $4\cdot5$.
Infine elenca i naturali minori di $30$ congruenti a $2$ modulo $6$.

:::{dropdown} Mostra la soluzione

$38=5\cdot7+3$, $50=7\cdot7+1$, $4=9\cdot0+4$,
$2026=12\cdot168+10$: $(q,r)=(7,3),(7,1),(0,4),(168,10)$.
In ciascun caso $0\le r<b$. Somma sull'orologio con resto $3$, prodotto con resto $2$.
L'elenco è $\{2,8,14,20,26\}$.
:::

(r-calendario)=
### Giorni e appuntamenti

Rispondi motivando con divisioni con resto.

1. Oggi è martedì. Che giorno sarà tra $100$ giorni?

2. Una sveglia con indicazione delle ore da $0$ a $23$ segna le 9:00.
    Che ora segnerà fra $200$ ore?

3. Due amici si salutano mercoledì alle 12:40 e si danno appuntamento
    dopo $4000$ minuti. In quale giorno e a quale ora si ritrovano?

:::{dropdown} Mostra la soluzione

$100=7\cdot14+2$: giovedì.
$200=24\cdot8+8$: dopo otto giorni e altre otto ore segnerà le 17:00.
$4000=1440\cdot2+1120$ e $1120=60\cdot18+40$.
Dopo due giorni è venerdì alle 12:40; aggiungendo 18 ore e 40 minuti
si arriva a sabato alle 7:20.
:::
