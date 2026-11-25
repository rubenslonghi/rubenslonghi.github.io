---
title: "Dalle relazioni ai grafi"
---

*Per richiamare le idee già viste:* [Prodotto cartesiano e principio di moltiplicazione](../insiemi-logica/prodotto-cartesiano-e-principio-di-moltiplicazione.md) · [Che cos'è un insieme?](../insiemi-logica/che-cos-e-un-insieme.md).


(r-sec-grafi)=

:::{admonition} Attività — Persone e frecce
:class: attention

Fra Anna, Luca, Marta e Omar, Anna e Luca sono nella stessa classe,
gli altri due in classi diverse. Disegna una freccia rossa da $x$ a $y$
quando frequentano la stessa classe. Servono anche frecce da un punto a sé stesso?
Confronta questa relazione con «è genitore di» e «è fratello o sorella di».
:::

In un grafo orientato i vertici rappresentano gli elementi e una freccia
da $x$ a $y$ rappresenta la coppia $(x,y)$. Un cappio rappresenta $(x,x)$.
Riflessività significa un cappio su ogni vertice; simmetria significa
che ogni freccia fra vertici diversi ha anche la propria inversa.
La transitività richiede che ogni percorso $x\to y\to z$ abbia la freccia $x\to z$.
Non va confusa con l'esistenza di una qualunque catena di frecce.

```{figure} ../figure/schema-d010026556de.svg
:alt: Dalle relazioni ai grafi — diagramma
:width: 90%

Dalle relazioni ai grafi — diagramma
```
