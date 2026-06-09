---
title: "Le Funzioni Elementari: Classificazione e Dominio"
author: "Rubens Longhi"
description: Classificazione delle funzioni e calcolo del dominio per la classe quarta IT
---

Nello studio di funzione, il primo passo fondamentale è capire di che tipo di funzione stiamo parlando. Questo ci permette di applicare le regole corrette per trovare il **Dominio**, chiamato anche *Campo di Esistenza* o *Insieme di Definizione* della funzione.

:::{note} Definizione di Dominio
Il **Dominio naturale** di una funzione matematica $y = f(x)$ è l'insieme più ampio dei valori reali che si possono assegnare alla variabile indipendente $x$ affinché esista e sia calcolabile il corrispondente valore reale $y$.
Graficamente, rappresenta la proiezione del grafico della funzione sull'asse delle $x$.
:::

## 1. Classificazione delle Funzioni

Possiamo suddividere le funzioni matematiche in due grandi macrogruppi: le **Funzioni Algebriche** (dove compaiono solo operazioni di addizione, sottrazione, moltiplicazione, divisione, elevamento a potenza e radice) e le **Funzioni Trascendenti** (logaritmi, esponenziali, goniometriche).

Ecco lo schema completo che devi imparare a memoria per riconoscere le funzioni a prima vista:

```{mermaid}
flowchart TB

    %% Radice
    F["FUNZIONI ANALITICHE"]

    %% Primo livello
    F --> A["ALGEBRICHE"]
    F --> T["TRASCENDENTI"]

    %% Algebraiche
    A --> R["Razionali"]
    A --> I["Irrazionali"]

    %% Razionali
    R --> RI["Intere
es: $y = x^2 - 3x + 1$
dominio: $\\mathbb{R}$"]

    R --> RF["Fratte
es: $y = \\dfrac{1}{x - 2}$
dominio: $\\mathbb{R} \\setminus \\{2\\}$"]

    %% Irrazionali
    I --> IP["Indice pari
es: $y = \\sqrt{x + 4}$
dominio: $x \\ge -4$"]

    I --> ID["Indice dispari
es: $y = \\sqrt{x - 1}$
dominio: $\\mathbb{R}$"]

    %% Trascendenti
    T --> E["Esponenziali
es: $y = e^{2x}$
dominio: $\\mathbb{R}$"]

    T --> L["Logaritmiche
es: $y = \\ln(x - 5)$
dominio: $x > 5$"]

    T --> G["Goniometriche
es: $y = \\cos x$
dominio: $\\mathbb{R}$"]

    %% Stili
    classDef root fill:#2C3E50,stroke:#2C3E50,stroke-width:2px,color:#fff,font-weight:bold;
    classDef branchA fill:#2471A3,stroke:#2471A3,stroke-width:2px,color:#fff,font-weight:bold;
    classDef branchT fill:#884EA0,stroke:#884EA0,stroke-width:2px,color:#fff,font-weight:bold;
    classDef mid fill:#D6EAF8,stroke:#7FB3D5,stroke-width:1.5px,color:#1B2631;
    classDef leaf fill:#FBFCFC,stroke:#BFC9CA,stroke-width:1px,color:#17202A;

    class F root;
    class A branchA;
    class T branchT;
    class R,I mid;
    class RI,RF,IP,ID,E,L,G leaf;
```

---

## 2. Definizione e Dominio per ogni Categoria

Ora che sappiamo classificare le funzioni, vediamo quali sono le restrizioni per ogni categoria.

:::{warning} Attenzione alle Operazioni Critiche
Nel campo dei numeri Reali ($\mathbb{R}$), le operazioni che ci obbligano a porre delle condizioni di esistenza sono essenzialmente tre:
1. Non si può dividere per zero.
2. Non si può fare la radice di indice pari di un numero negativo.
3. Non si può calcolare il logaritmo di un numero negativo o nullo.
:::

::::{grid} 1 1 2 2
:::{grid-item-card} Funzioni Razionali Intere (Polinomi)
La variabile $x$ **non** si trova al denominatore e **non** sotto radice.  
- **Esempio:** $y = x^3 - 5x^2 + 7x$
- **Dominio:** $\forall x \in \mathbb{R}$ oppure $D: (-\infty; +\infty)$.
Non ci sono operazioni vietate!
:::
:::{grid-item-card} Funzioni Razionali Fratte
La variabile $x$ compare al denominatore.  
- **Esempio:** $y = \frac{3x}{x - 5}$
- **Dominio:** Il denominatore deve essere diverso da zero $\rightarrow x - 5 \neq 0$.
:::
::::

::::{grid} 1 1 2 2
:::{grid-item-card} Funzioni Irrazionali Pari
La $x$ è sotto una radice quadrata, quarta, ecc.
- **Esempio:** $y = \sqrt{2x + 6}$
- **Dominio:** Il radicando deve essere maggiore o uguale a zero $\rightarrow 2x + 6 \geq 0$.
:::
:::{grid-item-card} Funzioni Logaritmiche
La $x$ fa parte dell'argomento di un logaritmo.
- **Esempio:** $y = \log(x - 3)$
- **Dominio:** L'argomento deve essere strettamente maggiore di zero $\rightarrow x - 3 > 0$.
:::
::::

---

## 3. Esercizi Svolti Passo-Passo

Mettiti alla prova. Prova a risolvere l'esercizio sul quaderno, poi clicca sul menu a tendina "Mostra Soluzione" per controllare i passaggi e il risultato.

### Esercizio 1: Razionale Fratta

Calcolare il dominio della seguente funzione:
$$f(x) = \frac{x^2 - 1}{x^2 - 5x + 6}$$

:::{dropdown} Mostra Soluzione Esercizio 1
**Passo 1: Classificazione.**  
Si tratta di una funzione algebrica razionale fratta, perché la $x$ compare al denominatore e non ci sono radici.

**Passo 2: Condizione di Esistenza.**  
Bisogna porre il denominatore diverso da zero. Il numeratore ($x^2-1$) non crea alcun problema e non va studiato.
$$x^2 - 5x + 6 \neq 0$$

**Passo 3: Risoluzione.**  
Risolviamo l'equazione di secondo grado associata. Troviamo due numeri la cui somma sia $-5$ e il prodotto sia $+6$, ovvero $2$ e $3$.
$$x \neq 2 \quad \land \quad x \neq 3$$

**Risultato (Dominio):**
$D: \forall x \in \mathbb{R} \setminus \{2, 3\}$  
Oppure in forma di intervalli: $(-\infty; 2) \cup (2; 3) \cup (3; +\infty)$.
:::


### Esercizio 2: Irrazionale a Indice Pari

Calcolare il dominio della seguente funzione:
$$f(x) = \sqrt{x^2 - 4}$$

:::{dropdown} Mostra Soluzione Esercizio 2
**Passo 1: Classificazione.**  
Si tratta di una funzione algebrica irrazionale intera ad indice pari (radice quadrata).

**Passo 2: Condizione di Esistenza.**  
Il radicando (tutto ciò che sta sotto la radice) deve essere maggiore o uguale a zero.
$$x^2 - 4 \geq 0$$

**Passo 3: Risoluzione.**  
Risolviamo l'equazione associata $x^2 - 4 = 0 \rightarrow x = \pm 2$. Essendo una parabola rivolta verso l'alto ed essendoci il segno $\geq$, prendiamo i valori esterni.
$$x \leq -2 \quad \lor \quad x \geq 2$$

**Risultato (Dominio):**
$D: (-\infty; -2] \cup [2; +\infty)$. (Le parentesi quadre indicano che il $-2$ e il $2$ sono inclusi).
:::


### Esercizio 3: Irrazionale Fratta (Misto)

Calcolare il dominio della seguente funzione:
$$f(x) = \frac{\sqrt{x - 3}}{x - 5}$$

:::{dropdown} Mostra Soluzione Esercizio 3
**Passo 1: Classificazione.**  
Questa è una funzione algebrica irrazionale fratta. Attenzione: presenta due "problemi", una radice al numeratore e una variabile al denominatore. Dobbiamo impostare un sistema per farle valere contemporaneamente.

**Passo 2: Condizione di Esistenza.**  
$$
\begin{cases} 
x - 3 \geq 0 & \text{(per la radice al numeratore)} \\ 
x - 5 \neq 0 & \text{(per il denominatore)} 
\end{cases}
$$

**Passo 3: Risoluzione.**  
Risolviamo le due condizioni separatamente e poi intersechiamo i risultati.
$$
\begin{cases} 
x \geq 3 \\ 
x \neq 5 
\end{cases}
$$

Dobbiamo prendere tutti i numeri maggiori o uguali a 3, escludendo il numero 5.

**Risultato (Dominio):**
$D: [3; 5) \cup (5; +\infty)$.
:::