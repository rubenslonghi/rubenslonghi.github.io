---
title: "Ripasso: Notazione degli Intervalli"
author: Rubens Longhi
description: Ripasso sulla notazione degli intervalli per la classe quarta IT
kernelspec:
  name: python3
  display_name: Python 3
---

```{code-cell} ipython3
:tags: ["remove-cell"]
# Questo blocco carica le librerie e definisce la funzione, ma "remove-cell" lo nasconde completamente dal libro HTML.
import matplotlib.pyplot as plt

def draw_interval(
    left_closed=True,
    right_closed=True,
    left_infinite=False,
    right_infinite=False,
    color="#2980B9",
    label="[a,b]",
    inequality="a $\leq$ x $\leq$ b"
):
    fig, ax = plt.subplots(figsize=(5,1.2))

    xmin, xmax = 0, 10
    a, b = 2, 8

    # asse
    ax.plot([xmin, xmax], color="black", linewidth=1)

    # intervallo
    start = xmin if left_infinite else a
    end = xmax if right_infinite else b

    ax.plot([start, end], color=color, linewidth=5)

    # estremo sinistro
    if not left_infinite:
        ax.plot(
            a, 0, 'o',
            markersize=8,
            markeredgecolor=color,
            markerfacecolor=color if left_closed else "white"
        )
        ax.text(a, 0.15, "$a$", ha="center", fontsize=12, color=color, style='italic')

    # estremo destro
    if not right_infinite:
        ax.plot(
            b, 0, 'o',
            markersize=8,
            markeredgecolor=color,
            markerfacecolor=color if right_closed else "white"
        )
        ax.text(b, 0.15, "$b$", ha="center", fontsize=12, color=color, style='italic')

    # frecce per infinito
    if left_infinite:
        ax.arrow(
            xmin+0.7, 0,
            -0.6, 0,
            length_includes_head=True,
            head_width=0.1,
            head_length=0.2,
            color=color
        )

    if right_infinite:
        ax.arrow(
            xmax-0.7, 0,
            0.6, 0,
            length_includes_head=True,
            head_width=0.1,
            head_length=0.2,
            color=color
        )

    # Etichette in basso
    ax.text(0.5, -0.3, f"${label}$", transform=ax.transAxes, ha="center", fontsize=14)
    ax.text(0.5, -0.6, f"${inequality}$", transform=ax.transAxes, ha="center", fontsize=12)

    ax.set_xlim(xmin-0.5, xmax+0.5)
    ax.set_ylim(-0.4, 0.4)
    ax.axis("off")

    plt.show()
```

Per scrivere correttamente il **Dominio** (e successivamente lo studio del segno) di una funzione, è fondamentale saper tradurre le disuguaglianze matematiche nella formale **notazione ad intervalli**.

:::{note} Cos'è un intervallo?
Un intervallo è un sottoinsieme continuo di numeri reali $\mathbb{R}$. Può essere immaginato come un "segmento" o una "semiretta" sulla linea dei numeri. 
- Usiamo le **parentesi quadre** `[ ]` quando il numero estremo è **incluso** (pallino pieno).
- Usiamo le **parentesi tonde** `( )` quando il numero estremo è **escluso** (pallino vuoto).
:::

---

## 1. Intervalli Limitati sulla Retta Reale

Gli intervalli limitati sono racchiusi tra due numeri finiti, $a$ e $b$.

::::{grid} 1 1 2 2

:::{grid-item-card} INTERVALLO CHIUSO LIMITATO
```{code-cell} ipython3
:tags: ["remove-input"]
draw_interval(
    left_closed=True, right_closed=True, color="#2980B9",
    label=r"\lbrack a, b \rbrack", inequality=r"a \leq x \leq b"
)
```
:::

:::{grid-item-card} INTERVALLO APERTO LIMITATO
```{code-cell} ipython3
:tags: ["remove-input"]
draw_interval(
    left_closed=False, right_closed=False, color="#E74C3C",
    label=r"( a, b )", inequality=r"a < x < b"
)
```
:::

:::{grid-item-card} INTERVALLO SEMIAPERTO A DX
```{code-cell} ipython3
:tags: ["remove-input"]
draw_interval(
    left_closed=True, right_closed=False, color="#27AE60",
    label=r"\lbrack a, b )", inequality=r"a \leq x < b"
)
```
:::

:::{grid-item-card} INTERVALLO SEMIAPERTO A SX
```{code-cell} ipython3
:tags: ["remove-input"]
draw_interval(
    left_closed=False, right_closed=True, color="#2980B9",
    label=r"( a, b \rbrack", inequality=r"a < x \leq b"
)
```
:::
::::

---

## 2. Intervalli Illimitati: Verso l'Infinito

Quando uno degli estremi del nostro insieme non ha fine, parliamo di intervalli illimitati. In questo caso utilizziamo il simbolo dell'infinito negativo ($-\infty$) o positivo ($+\infty$).

:::{warning} Regola d'oro
**L'infinito è SEMPRE escluso!** Non è un numero raggiungibile. Pertanto, vicino al simbolo $\infty$ o $-\infty$ si usa **sempre e solo la parentesi tonda**.  
:::

::::{grid} 1 1 2 2

:::{grid-item-card} CHIUSO ILLIMITATO DX
```{code-cell} ipython3
:tags: ["remove-input"]
draw_interval(
    left_closed=True, right_infinite=True, color="#2980B9",
    label=r"\lbrack a, +\infty )", inequality=r"x \geq a"
)
```
:::

:::{grid-item-card} APERTO ILLIMITATO DX
```{code-cell} ipython3
:tags: ["remove-input"]
draw_interval(
    left_closed=False, right_infinite=True, color="#E74C3C",
    label=r"( a, +\infty )", inequality=r"x > a"
)
```
:::

:::{grid-item-card} CHIUSO ILLIMITATO SX
```{code-cell} ipython3
:tags: ["remove-input"]
draw_interval(
    right_closed=True, left_infinite=True, color="#27AE60",
    label=r"( -\infty, b \rbrack", inequality=r"x \leq b"
)
```
:::

:::{grid-item-card} APERTO ILLIMITATO SX
```{code-cell} ipython3
:tags: ["remove-input"]
draw_interval(
    right_closed=False, left_infinite=True, color="#2980B9",
    label=r"( -\infty, b )", inequality=r"x < b"
)
```
:::
::::

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
   **Soluzione:** $\lbrack -3, 5)$

3. **$x \leq 0 \quad \lor \quad x > 7$** $\rightarrow$ Due intervalli illimitati separati, uniti dal simbolo $\cup$.  
   **Soluzione:** $(-\infty, 0 \rbrack \cup (7, +\infty)$
:::

### Esercizio 2: Da Intervallo a Disuguaglianza
Fai l'operazione inversa. Traduci i seguenti intervalli in disuguaglianze matematiche:
1. $\lbrack -2, 8 \rbrack$
2. $(-\infty, 4) \cup \lbrack 10, +\infty)$
3. $\mathbb{R} \setminus \{3\}$ (Tutti i reali escluso il numero 3)

:::{dropdown} Soluzioni Esercizio 2
1. **$\lbrack -2, 8 \rbrack$** $\rightarrow$ Intervallo chiuso limitato.  
   **Soluzione:** $-2 \leq x \leq 8$

2. **$(-\infty, 4) \cup \lbrack 10, +\infty)$** $\rightarrow$ Due semirette. La prima aperta in 4, la seconda chiusa in 10.  
   **Soluzione:** $x < 4 \quad \lor \quad x \geq 10$

3. **$\mathbb{R} \setminus \{3\}$** $\rightarrow$ Significa prendere l'intervallo prima del 3 e quello dopo il 3, quindi $(-\infty, 3) \cup (3, +\infty)$.  
   **Soluzione:** $x < 3 \quad \lor \quad x > 3$, che in modo compatto scriviamo semplicemente come $x \neq 3$.
:::