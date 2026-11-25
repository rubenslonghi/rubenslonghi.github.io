---
title: "Revisionare gli errori senza affidarsi al solo PDF"
---

*Per richiamare le idee già viste:* [Proporzioni, rapporti e percentuali](../razionali-reali/proporzioni-rapporti-e-percentuali.md).


(r-latex-errori)=

::::{admonition} Attività — Compila, ma è corretto?
:class: attention

Il documento seguente contiene intenzionalmente errori di matematica
e di scrittura LaTeX. Individua il primo passaggio falso; ricostruisci
tutti quelli che ne dipendono. Correggi anche parentesi, allineamenti,
rimandi e insieme soluzione. Controlla infine nell'equazione iniziale.

:::{dropdown} Mostra la soluzione

Nell'equazione della scheda le condizioni sono
$x\ne0,\pm2/3$; la soluzione corretta è $x=1/3$ e i due membri
valgono entrambi $13/2$. Compilare un documento non ne certifica i calcoli.
:::
::::

[Svolgimento intenzionalmente errato da revisionare — PDF](/materiali/equazione-errori-latex.pdf)

Questa richiesta riprende un modello prodotto nelle conversazioni:
diversamente dal titolo originario, non porta a una soluzione scomparsa.
Il controllo algebrico fa emergere un'equazione di secondo grado;
la risoluzione completa va affrontata dopo quel prerequisito.

## Esercizi

Prova prima sul quaderno. Apri la soluzione solo quando vuoi confrontare il tuo tentativo.

(r-latex-variante)=
### Controllare anche il modello: approfondimento

Risolvi $\frac{x^2}{x-2}-4-\frac4{x+1}=\frac{x^2+2x}{x+1}$,
indicando condizioni ed esito. Scrivi lo svolgimento in un documento
con formule allineate; poi costruisci una variante e verifica la tua conclusione.
Se chiedi a uno strumento di IA un indizio, conserva il tentativo,
la domanda e il controllo svolto dopo aver ricevuto l'aiuto.

:::{dropdown} Mostra la soluzione

$x\ne2,-1$. Moltiplicando per $(x-2)(x+1)$
si ottiene $x^2(x+1)-4(x-2)(x+1)-4(x-2)=(x^2+2x)(x-2)$,
cioè $-3x^2+4x+16=0$, che ha radici
$x=(2\pm2\sqrt{13})/3$, entrambe ammissibili.
Il titolo del modello non sostituisce il controllo: in questa equazione
non scompare alcuna delle due soluzioni.
:::


## Materiali per questa lezione

- [Compito LaTeX — consegna](/materiali/digitali/Compito_LaTeX_Gemini_2BS.pdf)
- [Modello modificabile](/materiali/digitali/Modello_risposta_2BS.tex)
