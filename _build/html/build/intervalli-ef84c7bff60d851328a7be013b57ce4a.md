---
title: "Ripasso: Notazione degli Intervalli"
author: Rubens Longhi
description: Ripasso sulla notazione degli intervalli per la classe quarta IT
---

Per scrivere correttamente il **Dominio** (e successivamente lo studio del segno) di una funzione, è fondamentale saper tradurre le disuguaglianze matematiche nella formale **notazione ad intervalli**.

:::{note} Cos'è un intervallo?
Un intervallo è un sottoinsieme continuo di numeri reali $\mathbb{R}$. Può essere immaginato come un "segmento" o una "semiretta" sulla linea dei numeri. 
- Usiamo le **parentesi quadre** `[ ]` quando il numero estremo è **incluso** (pallino pieno).
- Usiamo le **parentesi tonde** `( )` quando il numero estremo è **escluso** (pallino vuoto).
:::

<svg width="400" height="80" xmlns="http://www.w3.org/2000/svg">

  <line x1="20" y1="40" x2="380" y2="40"
        stroke="black" stroke-width="2"/>

  <line x1="100" y1="40" x2="300" y2="40"
        stroke="blue" stroke-width="5"/>

  <circle cx="100" cy="40" r="5" fill="blue"/>
  <circle cx="300" cy="40" r="5" fill="blue"/>

  <text x="95" y="25">a</text>
  <text x="295" y="25">b</text>

</svg>
---

## 3. Esercizi: Traduzioni tra Notazioni

Spesso il calcolo algebrico ci fornisce risultati sotto forma di disuguaglianze, ma noi dobbiamo scrivere la soluzione finale con la notazione degli intervalli. Ricorda che se ci sono più pezzi separati, li uniamo con il simbolo di unione $\cup$.

Prova a svolgere gli esercizi e poi controlla le soluzioni!

### Esercizio 1: Da Disuguaglianza a Intervallo
Traduci i seguenti risultati algebrici in notazione ad intervalli:
1. $x < -4$
2. $-3 \leq x < 5$
3. $x \leq 0 \quad \lor \quad x > 7$

:::{dropdown} Soluzioni Esercizio 1
1. **$x < -4$** $\rightarrow$ Tutti i numeri prima di -4, infinito a sinistra, pallino vuoto sul -4.  
   **Soluzione:** $(-\infty, -4)$

2. **$-3 \leq x < 5$** $\rightarrow$ Intervallo limitato. Il -3 ha il pallino pieno (minore *o uguale*), il 5 ha il pallino vuoto (strettamente minore).  
   **Soluzione:** $[-3, 5)$

3. **$x \leq 0 \quad \lor \quad x > 7$** $\rightarrow$ Due intervalli illimitati separati, uniti dal simbolo $\cup$.  
   **Soluzione:** $(-\infty, 0] \cup (7, +\infty)$
:::


### Esercizio 2: Da Intervallo a Disuguaglianza
Fai l'operazione inversa. Traduci i seguenti intervalli in disuguaglianze matematiche:
1. $[-2, 8]$
2. $(-\infty, 4) \cup [10, +\infty)$
3. $\mathbb{R} \setminus \{3\}$ (Tutti i reali escluso il numero 3)

:::{dropdown} Soluzioni Esercizio 2
1. **$[-2, 8]$** $\rightarrow$ Intervallo chiuso limitato.  
   **Soluzione:** $-2 \leq x \leq 8$

2. **$(-\infty, 4) \cup [10, +\infty)$** $\rightarrow$ Due semirette. La prima aperta in 4, la seconda chiusa in 10.  
   **Soluzione:** $x < 4 \quad \lor \quad x \geq 10$

3. **$\mathbb{R} \setminus \{3\}$** $\rightarrow$ Significa prendere l'intervallo prima del 3 e quello dopo il 3, quindi $(-\infty, 3) \cup (3, +\infty)$.  
   **Soluzione:** $x < 3 \quad \lor \quad x > 3$, che in modo compatto scriviamo semplicemente come $x \neq 3$.
:::