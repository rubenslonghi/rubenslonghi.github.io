---
title: "Deduzioni valide e controesempi"
---

:::{note} Nel percorso della 1 SP

- [12 novembre 2026](../cronologia-1sp.md#giorno-2026-11-12) — Logica, deduzioni e negazioni.

[Apri tutta la linea del tempo](../cronologia-1sp.md).
:::

*Per richiamare le idee già viste:* [Achille, i decimali infiniti e nuovi numeri](../razionali-reali/achille-i-decimali-infiniti-e-nuovi-numeri.md).


Da $p\Rightarrow q$ e $p$ segue $q$. Da $p\Rightarrow q$ e
$q\Rightarrow r$ segue $p\Rightarrow r$.
Per esempio: Socrate è un uomo; ogni uomo è mortale; dunque Socrate è mortale.
La contrapposta è equivalente all'implicazione iniziale:

$$
(p\Rightarrow q)\Leftrightarrow(\overline q\Rightarrow\overline p).
$$

Non si possono scambiare soltanto i versi, né negare soltanto i due membri.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-log-validita)=
### I ragionamenti degli appunti

Valuta le deduzioni e giustifica con una catena di implicazioni o un controesempio.

1. Se Paolo è nella squadra di pallavolo, si allena ogni giorno;
    se si allena ogni giorno, va ogni giorno in palestra. Non va ogni
    giorno in palestra. Quindi non è nella squadra.

2. Alcuni dinosauri sono erbivori. Otto è erbivoro. Quindi Otto è un dinosauro.

3. Se viene Maria, non viene Paolo. Se viene Marco, viene Paolo.
    Viene Maria. Quindi non viene Marco.

4. Se Antonella fa parte della banda, suona uno strumento.
    Non fa parte della banda. Quindi non suona strumenti.

5. Le prime $100$ persone che prenotano partecipano al concorso;
    chi partecipa può vincere il viaggio. Hai vinto. Quindi eri fra le prime $100$.

:::{dropdown} Mostra la soluzione

1. Valida, per transitività e contrapposizione.
2. Non valida: Otto potrebbe essere un cavallo.
3. Valida: Maria implica non Paolo, che implica non Marco.
4. Non valida: può suonare senza essere nella banda.
5. Non valida: la vincita non implica essere fra i primi $100$;
inoltre la possibilità di vincere va distinta dalla vincita effettiva.
:::

(r-log-laureati)=
### Aldo, Bruno e Carlo

Almeno uno dei tre è laureato. Se Aldo lo è, anche Bruno lo è;
se Carlo lo è, anche Aldo lo è. Fra Bruno e Carlo è laureato
esattamente uno. Chi è necessariamente laureato? Sono necessariamente due?

:::{dropdown} Mostra la soluzione

Se Carlo fosse laureato, lo sarebbero Aldo e Bruno, contro l'ultimo dato.
Carlo non è laureato e Bruno sì. Aldo può esserlo oppure no:
sono possibili uno o due laureati, non necessariamente due.
:::
