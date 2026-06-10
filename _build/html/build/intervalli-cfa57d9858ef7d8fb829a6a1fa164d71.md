---
title: "Ripasso: Notazione degli Intervalli"
description: Ripasso sulla notazione degli intervalli per la classe quarta IT
kernelspec:
  name: python3
  display_name: Python 3
---

Per scrivere correttamente il **Dominio** (e successivamente lo studio del segno) di una funzione, è fondamentale saper tradurre le disuguaglianze matematiche nella formale **notazione ad intervalli**.

:::{note} Cos'è un intervallo?
Un intervallo è un sottoinsieme continuo di numeri reali $\mathbb{R}$. Può essere immaginato come un "segmento" o una "semiretta" sulla linea dei numeri.
:::

:::{note}
Regola di base:
- si usano le **parentesi quadre** quando l'estremo è incluso;
- si usano le **parentesi tonde** quando l'estremo è escluso;
- con $+\infty$ e $-\infty$ si usano **sempre** le parentesi tonde.
:::

```{code-cell} python3
:tags: ["remove-cell"]

import matplotlib.pyplot as plt

plt.rcParams["font.family"] = "serif"
plt.rcParams["mathtext.fontset"] = "stix"

def draw_interval(
    left_closed=True,
    right_closed=True,
    left_infinite=False,
    right_infinite=False,
    color="#2980B9",
    label=r"[a,b]",
    inequality=r"a \leq x \leq b"
):
    fig, ax = plt.subplots(figsize=(6.0, 1.65))

    xmin, xmax = 0, 10
    y = 0
    a, b = 3.2, 7.1

    # Asse tratteggiato con freccia nera a destra
    ax.plot(
        [xmin + 0.8, xmax - 0.9], [y, y],
        linestyle=(0, (3, 3)),
        color="black",
        linewidth=1.1,
        alpha=0.75
    )
    ax.annotate(
        "",
        xy=(xmax - 0.45, y),
        xytext=(xmax - 1.05, y),
        arrowprops=dict(arrowstyle="->", color="black", lw=1.1)
    )

    # Segmento colorato
    start = xmin + 1.0 if left_infinite else a
    end = xmax - 1.0 if right_infinite else b
    ax.plot(
        [start, end], [y, y],
        color=color,
        linewidth=2.4,
        solid_capstyle="round",
        zorder=3
    )

    # Freccia verso -infinito
    if left_infinite:
        ax.annotate(
            "",
            xy=(xmin + 0.35, y),
            xytext=(xmin + 1.0, y),
            arrowprops=dict(arrowstyle="->", color=color, lw=2.4)
        )

    # Freccia verso +infinito
    if right_infinite:
        ax.annotate(
            "",
            xy=(xmax - 0.35, y),
            xytext=(xmax - 1.0, y),
            arrowprops=dict(arrowstyle="->", color=color, lw=2.4)
        )

    # Estremo sinistro
    if not left_infinite:
        ax.plot(
            a, y,
            marker="o",
            markersize=5.6,
            markeredgewidth=1.4,
            markeredgecolor=color,
            markerfacecolor=color if left_closed else "white",
            zorder=5
        )
        ax.text(
            a, y + 0.18, r"$a$",
            ha="center", va="bottom",
            fontsize=12.5, color=color
        )

    # Estremo destro
    if not right_infinite:
        ax.plot(
            b, y,
            marker="o",
            markersize=5.6,
            markeredgewidth=1.4,
            markeredgecolor=color,
            markerfacecolor=color if right_closed else "white",
            zorder=5
        )
        ax.text(
            b, y + 0.18, r"$b$",
            ha="center", va="bottom",
            fontsize=12.5, color=color
        )

    # Etichetta a sinistra
    ax.text(
        1.0, -0.35, f"${label}$",
        ha="left", va="center",
        fontsize=15, color=color
    )

    # Disuguaglianza sotto
    mid = (a + b) / 2 if (not left_infinite and not right_infinite) else 5.2
    ax.text(
        mid, y - 0.35, f"${inequality}$",
        ha="center", va="center",
        fontsize=15, color=color
    )

    ax.set_xlim(xmin, xmax)
    ax.set_ylim(-0.62, 0.55)
    ax.axis("off")
    plt.tight_layout()
    plt.show()
```

## Intervalli limitati

Gli intervalli limitati sono compresi tra due numeri reali finiti, che qui indichiamo con $a$ e $b$, con $a<b$.

::::{grid} 1 1 2 2
:::{grid-item-card} **INTERVALLO CHIUSO LIMITATO**
```{code-cell} python3
:tags: ["remove-input"]

draw_interval(
    left_closed=True,
    right_closed=True,
    color="#1f77b4",
    label=r"[a,b]",
    inequality=r"a \leq x \leq b"
)
```
:::

:::{grid-item-card} **INTERVALLO SEMIAPERTO A DX**
```{code-cell} python3
:tags: ["remove-input"]

draw_interval(
    left_closed=True,
    right_closed=False,
    color="#1f9d55",
    label=r"[a,b)",
    inequality=r"a \leq x < b"
)
```
:::

:::{grid-item-card} **INTERVALLO APERTO LIMITATO**
```{code-cell} python3
:tags: ["remove-input"]

draw_interval(
    left_closed=False,
    right_closed=False,
    color="#c92525",
    label=r"(a,b)",
    inequality=r"a < x < b"
)
```
:::

:::{grid-item-card} **INTERVALLO SEMIAPERTO A SX**
```{code-cell} python3
:tags: ["remove-input"]

draw_interval(
    left_closed=False,
    right_closed=True,
    color="#1f77b4",
    label=r"(a,b]",
    inequality=r"a < x \leq b"
)
```
:::
::::

## Intervalli illimitati

Quando uno dei due estremi è infinito, l'intervallo diventa una semiretta. In questi casi l'infinito non è mai un estremo incluso, quindi compare sempre con parentesi tonda.

:::{warning} Regola d'oro
**L'infinito è SEMPRE escluso!** Non è un numero raggiungibile. Pertanto, vicino al simbolo $\infty$ o $-\infty$ si usa **sempre e solo la parentesi tonda**.  
:::

::::{grid} 1 1 2 2
:::{grid-item-card} **INTERVALLO CHIUSO ILLIMITATO**
```{code-cell} python3
:tags: ["remove-input"]

draw_interval(
    left_closed=True,
    right_infinite=True,
    color="#1f77b4",
    label=r"[a,+\infty)",
    inequality=r"x \geq a"
)
```
:::

:::{grid-item-card} **INTERVALLO CHIUSO ILLIMITATO**
```{code-cell} python3
:tags: ["remove-input"]

draw_interval(
    right_closed=True,
    left_infinite=True,
    color="#1f9d55",
    label=r"(-\infty,b]",
    inequality=r"x \leq b"
)
```
:::

:::{grid-item-card} **INTERVALLO APERTO ILLIMITATO**
```{code-cell} python3
:tags: ["remove-input"]

draw_interval(
    left_closed=False,
    right_infinite=True,
    color="#c92525",
    label=r"(a,+\infty)",
    inequality=r"x > a"
)
```
:::

:::{grid-item-card} **INTERVALLO APERTO ILLIMITATO**
```{code-cell} python3
:tags: ["remove-input"]

draw_interval(
    right_closed=False,
    left_infinite=True,
    color="#1f77b4",
    label=r"(-\infty,b)",
    inequality=r"x < b"
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