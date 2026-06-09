---
kernelspec:
  name: python3
  display_name: Python 3
---

# Il limite finito per $x$ che tende a un valore finito

## Un'idea da cui partire: lo zero assoluto

```{admonition} Domanda guida
:class: important
Possiamo raffreddare la materia senza limite?
```

In termodinamica compare un valore che funziona come una soglia teorica: **-273,15 °C**, lo zero assoluto. Quando la temperatura si avvicina a questo valore da destra, il volume di un gas ideale tende a zero.

$$ \lim_{t \to -273{,}15^+} V(t)=0 $$

L'idea importante, prima ancora del formalismo, è questa: una grandezza può **avvicinarsi** a un valore preciso anche se quel valore non viene effettivamente raggiunto nel modello considerato.

```{code-cell} python3
:tags: [remove-input]
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "figure.figsize": (8, 4.8),
    "axes.spines.top": False,
    "axes.spines.right": False,
    "font.size": 11,
})

T0 = -273.15
m = 1/80
V0 = -m*T0

t = np.linspace(T0 + 0.5, 60, 300)
V = m*t + V0

t_ext = np.linspace(T0, T0 + 35, 100)
V_ext = m*t_ext + V0

fig, ax = plt.subplots()
ax.plot(t, V, color="#1f4e79", linewidth=2.5)
ax.plot(t_ext, V_ext, color="#1f4e79", linewidth=2, linestyle=":", alpha=0.8)
ax.scatter([T0], [0], color="#b22222", zorder=5)
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)
ax.text(T0, -0.18, "-273.15 °C", color="#b22222", ha="center")
ax.text(2, V0 + 0.03, "$V_0$", color="#1f4e79")
ax.annotate(r"$\lim_{t\to -273.15^+}V(t)=0$",
            xy=(T0 + 20, m*(T0+20)+V0),
            xytext=(T0 + 55, 0.35),
            arrowprops=dict(arrowstyle="->", color="black"),
            fontsize=12)
ax.set_xlabel("$t$ (Temperatura)")
ax.set_ylabel("$V$ (Volume)")
ax.set_xlim(T0 - 15, 70)
ax.set_ylim(-0.2, 4.2)
ax.grid(alpha=0.2)
plt.show()
```

```{note}
Questo esempio serve a fissare l'intuizione: il limite descrive un **comportamento di avvicinamento**.
```

## Dall'esempio fisico al caso matematico

Passiamo ora a un esempio puramente teorico, in cui il limite si vede molto bene sia nel grafico sia in una tabella di valori.

Consideriamo la funzione

$$
f(x)=\frac{2x^2-6x}{x-3}.
$$

Osserviamo che il numeratore si può raccogliere:

$$
2x^2-6x = 2x(x-3).
$$

Perciò, per $x\neq 3$, possiamo scrivere

$$
f(x)=\frac{2x(x-3)}{x-3}=2x.
$$

La funzione quindi coincide con la retta $y=2x$, **tranne** nel punto $x=3$, dove l'espressione iniziale non è definita. Il grafico è dunque quello di una retta con un **buco** nel punto $(3,6)$.

## Una domanda intrigante

```{admonition} Cosa succede esattamente in $x=3$?
:class: warning
La funzione non è definita nel punto $x=3$, ma il grafico sembra indicare chiaramente verso quale valore si stanno avvicinando le ordinate.
```

Il dominio è:

$$
D=\mathbb{R}\setminus\{3\}=(-\infty,3)\cup(3,+\infty).
$$

```{code-cell} python3
:tags: [remove-input]
import numpy as np
import matplotlib.pyplot as plt

x1 = np.linspace(-1, 2.98, 200)
x2 = np.linspace(3.02, 5, 200)

fig, ax = plt.subplots(figsize=(7.5, 5))
ax.plot(x1, 2*x1, color="#1f77b4", linewidth=2.5)
ax.plot(x2, 2*x2, color="#1f77b4", linewidth=2.5)
ax.scatter([3], [6], s=90, facecolors="white", edgecolors="#1f77b4", linewidths=2, zorder=5)
ax.annotate("Non definita qui!", xy=(3,6), xytext=(3.7,7.6),
            arrowprops=dict(arrowstyle="->", color="black"), fontsize=11)
ax.axhline(0, color="black", linewidth=1)
ax.axvline(0, color="black", linewidth=1)
ax.set_xlim(-1, 5)
ax.set_ylim(-2, 10)
ax.set_xticks([1,2,3,4])
ax.set_yticks([3,6])
ax.grid(alpha=0.2)
ax.set_xlabel("$x$")
ax.set_ylabel("$y$")
plt.show()
```

## L'intuizione del limite finito

Per capire meglio il comportamento della funzione vicino a $x=3$, non guardiamo subito la formula: osserviamo prima i valori numerici.

|  **Direzione**   |        | **Sinistra ($x \to 3^-$)** |        |        | PUNTO | **Destra ($x \to 3^+$)** |        |     |
|--------------|--------|---------------------------|--------|--------|-------|--------------------------|--------|-----|
| | $x$    | 2.9                       | 2.99   | 2.999  | **3** | 3.001                    | 3.01   | 3.1 |
|              | $f(x)$ | 5.8                       | 5.98   | 5.998  | $\dfrac{0}{0}$ **(indet.)** | 6.002 | 6.02 | 6.2 |

Osserviamo il significato della tabella:

- quando $x$ si avvicina a 3 da sinistra, i valori di $f(x)$ si avvicinano a 6;
- quando $x$ si avvicina a 3 da destra, i valori di $f(x)$ si avvicinano ancora a 6;
- nel punto $x=3$, invece, la funzione **non è definita**.

Questo porta all'idea fondamentale:

$$
\lim_{x\to 3} \frac{2x^2-6x}{x-3}=6.
$$

```{important}
Il limite non ci dice necessariamente quanto vale la funzione **nel punto**, ma a quale valore tende la funzione **quando ci avviciniamo al punto**.
```

## La direzione conta: sinistra e destra

Quando si parla di limite, bisogna distinguere due modi di avvicinarsi al punto $x_0$:

- da **sinistra**, usando valori minori di $x_0$;
- da **destra**, usando valori maggiori di $x_0$.

In simboli:

- $x\to x_0^-$ significa che ci avviciniamo a $x_0$ da sinistra;
- $x\to x_0^+$ significa che ci avviciniamo a $x_0$ da destra.

```{code-cell} python3
:tags: [remove-input]
import matplotlib.pyplot as plt

fig, ax = plt.subplots(figsize=(8, 2.8))
ax.set_xlim(-3, 3)
ax.set_ylim(-1, 1.5)
ax.axis("off")

ax.annotate("", xy=(2.7, 0), xytext=(-2.7, 0),
            arrowprops=dict(arrowstyle="->", linewidth=1.8, color="black"))
ax.plot([0,0], [-0.12, 0.12], color="black", linewidth=2)
ax.text(0, -0.35, "$x_0$", ha="center", fontsize=12)
ax.text(2.75, -0.05, "$x$", fontsize=12)

ax.annotate("", xy=(-0.15, 0.55), xytext=(-2.3, 0.55),
            arrowprops=dict(arrowstyle="->", linewidth=2.5, color="#1f77b4"))
ax.text(-1.55, 0.8, "$x\to x_0^-$", color="#1f77b4", fontsize=13)

ax.annotate("", xy=(0.15, 0.55), xytext=(2.3, 0.55),
            arrowprops=dict(arrowstyle="->", linewidth=2.5, color="#b22222"))
ax.text(0.55, 0.8, "$x\to x_0^+$", color="#b22222", fontsize=13)

plt.show()
```

Nel nostro esempio, sia da sinistra sia da destra il valore verso cui la funzione tende è lo stesso: 6.

$$
\lim_{x\to 3^-} f(x)=6
\qquad \text{e} \qquad
\lim_{x\to 3^+} f(x)=6
$$

Poiché i due limiti laterali coincidono, possiamo concludere che

$$
\lim_{x\to 3} f(x)=6.
$$

## Idea intuitiva di definizione

Possiamo esprimere l'idea in questo modo:

```{admonition} Definizione intuitiva
:class: note
Dire che $\lim_{x\to x_0} f(x)=\ell$ significa che, prendendo $x$ sempre più vicino a $x_0$ ma diverso da $x_0$, i valori di $f(x)$ si avvicinano sempre più a $\ell$.
```

Questa definizione mette in evidenza tre idee chiave:

- conta ciò che succede **vicino** al punto;
- non è necessario conoscere o usare il valore della funzione **nel punto**;
- il comportamento da sinistra e da destra deve essere compatibile.

## Esercizi guidati

### Esercizio 1

Considera la funzione

$$
g(x)=\frac{x^2-1}{x-1}.
$$

1. Semplifica l'espressione per $x\neq 1$.
2. Individua il valore verso cui tende $g(x)$ quando $x\to 1$.
3. Spiega se nel grafico compare un buco.

```{dropdown} Suggerimento
Poiché $x^2-1=(x-1)(x+1)$, per $x\neq 1$ si ha $g(x)=x+1$.
```

### Esercizio 2

Completa la tabella per la funzione

$$
h(x)=\frac{x^2-4}{x-2}
$$

usando valori di $x$ vicini a 2 da sinistra e da destra, poi formula la congettura sul limite.

```{dropdown} Traccia di lavoro
Fattorizza prima il numeratore: $x^2-4=(x-2)(x+2)$.
```

### Esercizio 3

Osserva il grafico di una funzione che presenta un buco nel punto $(a,L)$. Spiega con parole tue perché è possibile che il limite esista anche se la funzione non è definita nel punto.

## Da ricordare

::::{grid} 1 1 2 2
:::{card}
**Limite finito per $x\to x_0$**

Descrive il valore verso cui tende la funzione quando la variabile indipendente si avvicina a un punto fissato.
:::

:::{card}
**Idea chiave**

Il limite riguarda il comportamento della funzione **intorno** al punto, non necessariamente **nel** punto.
:::
::::

```{tip}
Quando studi un limite, chiediti sempre: da sinistra e da destra la funzione tende allo stesso valore?
```
