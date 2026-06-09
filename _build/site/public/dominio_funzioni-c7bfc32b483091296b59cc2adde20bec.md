---
author: Rubens Longhi
description: Classificazione delle funzioni e calcolo del dominio
---

# Classificazione delle Funzioni e Calcolo del Dominio

Lo studio di funzione inizia sempre dalla sua classificazione e dalla determinazione del **Dominio** (o Insieme di Definizione). 

:::{note} Definizione
Il **Dominio naturale** di una funzione matematica $y = f(x)$ è l'insieme più ampio dei valori reali che si possono assegnare alla variabile indipendente $x$ affinché esista il corrispondente valore reale $y$.
:::

## 1. L'albero delle Funzioni Elementari

La prima cosa da fare davanti a una nuova funzione è classificarla. Di seguito è riportato lo schema ad albero completo delle funzioni analitiche elementari.

```{mermaid}
%% Diagramma ad albero della classificazione delle funzioni
graph TD
    %% Nodi Principali
    F["FUNZIONI ANALITICHE"] --> A["ALGEBRICHE"]
    F --> T["TRASCENDENTI"]
    
    %% Ramo Algebriche
    A --> R["Razionali"]
    A --> I["Irrazionali"]
    
    R --> RI["Intere <br/> y = P_n(x)"]
    R --> RF["Fratte <br/> y = N(x)/D(x)"]
    
    I --> II["Indice Pari <br/> y = √f(x)"]
    I --> ID["Indice Dispari <br/> y = ∛f(x)"]
    
    %% Ramo Trascendenti
    T --> E["Esponenziali <br/> y = a^f(x)"]
    T --> L["Logaritmiche <br/> y = log_a f(x)"]
    T --> G["Goniometriche <br/> y = sin(x), cos(x)..."]
    
    %% Styling
    classDef main fill:#2C3E50,stroke:#2C3E50,stroke-width:2px,color:#fff,font-weight:bold;
    classDef algebriche fill:#2980B9,stroke:#2980B9,stroke-width:2px,color:#fff;
    classDef trascendenti fill:#8E44AD,stroke:#8E44AD,stroke-width:2px,color:#fff;
    classDef sub fill:#ECF0F1,stroke:#BDC3C7,stroke-width:1px,color:#333;
    
    class F main;
    class A algebriche;
    class T trascendenti;
    class R,I,RI,RF,II,ID,E,L,G sub;
```

## 2. Regole Pratiche per il Dominio

Una volta classificata la funzione usando l'albero superiore, applichiamo le condizioni di esistenza.

:::{warning} Attenzione
Le uniche operazioni matematiche che richiedono restrizioni nel campo dei numeri Reali $\mathbb{R}$ sono: **divisioni**, **radici di indice pari** e **logaritmi** (oltre ad alcune funzioni goniometriche inverse).
:::

Ecco le regole fondamentali riassunte:

| Tipo di Funzione | Struttura | Condizione di Esistenza (C.E.) |
|:---|:---:|:---|
| **Polinomiale (Intera)** | $y = 3x^2 - 5x + 2$ | $\forall x \in \mathbb{R}$ |
| **Razionale Fratta** | $y = \frac{N(x)}{D(x)}$ | $D(x) \neq 0$ |
| **Irrazionale (indice pari)** | $y = \sqrt[2k]{f(x)}$ | $f(x) \geq 0$ |
| **Irrazionale (indice dispari)**| $y = \sqrt[2k+1]{f(x)}$ | Nessuna restrizione aggiuntiva |
| **Logaritmica** | $y = \log_a(f(x))$ | $f(x) > 0$ |
| **Esponenziale** | $y = a^{f(x)}$ | Esiste dove esiste l'esponente $f(x)$ |

## 3. Laboratorio Python: Visualizzare il Dominio

Come visto a lezione, a volte il calcolo algebrico può ingannare. Usiamo Python (libreria `sympy`) per calcolare e visualizzare il dominio di una funzione irrazionale fratta:
$$f(x) = \frac{\sqrt{x^2 - 4}}{x - 3}$$

```{code-cell} python3
import sympy as sp

# Definiamo la variabile e la funzione
x = sp.Symbol('x', real=True)
f = sp.sqrt(x**2 - 4) / (x - 3)

# Calcoliamo il dominio con SymPy
dominio = sp.calculus.util.continuous_domain(f, x, sp.S.Reals)

print(f"La funzione è: f(x) = {f}")
print(f"Il dominio calcolato è: {dominio}")
```

::::{tab-set}

:::{tab-item} Spiegazione Passo-Passo
1. **Radice pari al numeratore**: poniamo l'argomento maggiore o uguale a zero $\rightarrow x^2 - 4 \geq 0 \rightarrow x \leq -2 \cup x \geq 2$.
2. **Denominatore**: poniamo il denominatore diverso da zero $\rightarrow x - 3 \neq 0 \rightarrow x \neq 3$.
3. **Sistema**: Intersecando le due condizioni otteniamo esattamente $x \in (-\infty, -2] \cup [2, 3) \cup (3, +\infty)$.
:::

:::{tab-item} Soluzione per DSA
**Schema semplificato:**
- $x^2 - 4 \geq 0$ (Radice) $\rightarrow$ Valori esterni: $x \leq -2$, $x \geq 2$
- $x \neq 3$ (Denominatore) $\rightarrow$ "Buco" in $3$.
:::

::::