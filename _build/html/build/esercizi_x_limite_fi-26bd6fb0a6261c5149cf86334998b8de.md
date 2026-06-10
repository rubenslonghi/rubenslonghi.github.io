## Esercizi: deduci i limiti osservando i grafici

```{admonition} Consegna
:class: important
Per ciascuna figura, osserva il grafico e deduci i limiti richiesti. Prima prova a rispondere a parole, poi scrivi il risultato in simboli.
```

```{code-cell} python3
:tags: [remove-input]
import numpy as np
import matplotlib.pyplot as plt

plt.rcParams.update({
    "font.size": 10,
    "figure.figsize": (12, 7),
    "axes.spines.top": False,
    "axes.spines.right": False,
})

blue = "#1f77b4"
orange = "#ff7f0e"

fig, axs = plt.subplots(2, 3, figsize=(12, 7))

def setup_axes(ax, xlim, ylim, xticks=None, yticks=None):
    ax.set_xlim(*xlim)
    ax.set_ylim(*ylim)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['left'].set_linewidth(1.0)
    ax.spines['bottom'].set_linewidth(1.0)
    ax.set_xticks([] if xticks is None else xticks)
    ax.set_yticks([] if yticks is None else yticks)
    ax.grid(False)
    ax.tick_params(length=3, width=0.8)
    ax.set_xlabel("")
    ax.set_ylabel("")
    ax.text(xlim[1]-0.2, -0.35, "$x$", fontsize=10)
    ax.text(0.15, ylim[1]-0.2, "$y$", fontsize=10)

# 47
ax = axs[0,0]
setup_axes(ax, (-0.5, 5.2), (-2.3, 4.5), xticks=[3], yticks=[1])
x = np.linspace(-0.2, 5, 400)
y = (x-3)**2 - 2
mask_left = x < 0.25
mask_right = x > 4.75
mask_mid = ~(mask_left | mask_right)
ax.plot(x[mask_mid], y[mask_mid], color=blue, linewidth=2.2)
ax.plot(x[mask_left], y[mask_left], color=blue, linewidth=2.2, linestyle=':')
ax.plot(x[mask_right], y[mask_right], color=blue, linewidth=2.2, linestyle=':')
ax.text(4.6, 2.6, "$f(x)$", color=blue)
ax.set_title("47", loc="left", color=orange, fontweight="bold")

# 48
ax = axs[0,1]
setup_axes(ax, (-0.8, 5.5), (-1.2, 3.7), xticks=[3,4], yticks=[1,2])
x1 = np.linspace(-0.6, 3, 250)
y1 = np.cbrt(x1+0.1) + 0.35
x2 = np.linspace(3, 5.2, 180)
y2 = 2 + 0.35*(x2-3)**1.5
mask_left = x1 < -0.3
mask_mid = x1 >= -0.3
ax.plot(x1[mask_mid], y1[mask_mid], color=blue, linewidth=2.2)
ax.plot(x1[mask_left], y1[mask_left], color=blue, linewidth=2.2, linestyle=':')
mask_right_mid = x2 < 4.9
mask_right_edge = x2 >= 4.9
ax.plot(x2[mask_right_mid], y2[mask_right_mid], color=blue, linewidth=2.2)
ax.plot(x2[mask_right_edge], y2[mask_right_edge], color=blue, linewidth=2.2, linestyle=':')
ax.plot(3, y1[-1], 'o', color=blue, ms=4)
ax.plot(3, 2, 'o', color=blue, ms=4)
ax.text(4.6, 2.7, "$f(x)$", color=blue)
ax.set_title("48", loc="left", color=orange, fontweight="bold")

# 49
ax = axs[0,2]
setup_axes(ax, (-3.8, 4.5), (-2.5, 3.8), xticks=[-2,1,2], yticks=[1])
x = np.linspace(-3.5, 4.2, 500)
y = 0.11*(x+2.1)*(x-0.1)*(x-2.4) + 0.3
mask_left = x < -3.1
mask_right = x > 3.8
mask_mid = ~(mask_left | mask_right)
ax.plot(x[mask_mid], y[mask_mid], color=blue, linewidth=2.2)
ax.plot(x[mask_left], y[mask_left], color=blue, linewidth=2.2, linestyle=':')
ax.plot(x[mask_right], y[mask_right], color=blue, linewidth=2.2, linestyle=':')
ax.text(1.7, 2.1, "$f(x)$", color=blue)
ax.set_title("49", loc="left", color=orange, fontweight="bold")

# 50
ax = axs[1,0]
setup_axes(ax, (-5.2, 7.5), (-1.8, 7.2), xticks=[-4,4,6], yticks=[6])
xA = np.linspace(-5, 2, 80)
yA = xA + 4
xB = np.linspace(2, 4, 20)
yB = np.full_like(xB, 6.0)
xC = np.linspace(4, 7, 50)
yC = -xC + 10
for xx, yy in [(xA,yA),(xB,yB),(xC,yC)]:
    left = xx < xx.min() + 0.25*(xx.max()-xx.min())/max(1,len(xx))
    right = xx > xx.max() - 0.25*(xx.max()-xx.min())/max(1,len(xx))
    if len(xx) > 5:
        edge_n = max(2, len(xx)//8)
        ax.plot(xx[edge_n:-edge_n], yy[edge_n:-edge_n], color=blue, linewidth=2.2)
        ax.plot(xx[:edge_n], yy[:edge_n], color=blue, linewidth=2.2, linestyle=':')
        ax.plot(xx[-edge_n:], yy[-edge_n:], color=blue, linewidth=2.2, linestyle=':')
ax.text(4.7, 5.3, "$f(x)$", color=blue)
ax.set_title("50", loc="left", color=orange, fontweight="bold")

# 51
ax = axs[1,1]
setup_axes(ax, (-0.2, 4.2), (-0.4, 3.4), xticks=[0.5,1,2,3], yticks=[1])
xl = np.linspace(0.02, 0.95, 200)
yl = 0.12 + 0.55/(1-xl)
xr = np.linspace(1.05, 4, 300)
yr = (xr-3)**2
ax.plot(xl[xl<0.85], yl[xl<0.85], color=blue, linewidth=2.2)
ax.plot(xl[xl>=0.85], yl[xl>=0.85], color=blue, linewidth=2.2, linestyle=':')
ax.plot(xr[xr<3.75], yr[xr<3.75], color=blue, linewidth=2.2)
ax.plot(xr[xr>=3.75], yr[xr>=3.75], color=blue, linewidth=2.2, linestyle=':')
ax.axvline(1, color=blue, linestyle=':', alpha=0.6)
ax.text(1.65, 2.6, "$f(x)$", color=blue)
ax.set_title("51", loc="left", color=orange, fontweight="bold")

# 52
ax = axs[1,2]
setup_axes(ax, (-0.6, 5.8), (-2.8, 4.4), xticks=[1,2,3,4,5], yticks=[2])
x1 = np.linspace(0, 2, 120)
y1 = 0.6*x1 + 1.0
x2 = np.linspace(2.05, 5.2, 260)
y2 = -(x2-4)**2 + 1
ax.plot(x1[x1<1.85], y1[x1<1.85], color=blue, linewidth=2.2)
ax.plot(x1[x1>=1.85], y1[x1>=1.85], color=blue, linewidth=2.2, linestyle=':')
ax.plot(x2[x2<4.9], y2[x2<4.9], color=blue, linewidth=2.2)
ax.plot(x2[x2>=4.9], y2[x2>=4.9], color=blue, linewidth=2.2, linestyle=':')
ax.axvline(2, color=blue, linestyle=':', alpha=0.5)
ax.text(1.25, 1.25, "$f(x)$", color=blue)
ax.set_title("52", loc="left", color=orange, fontweight="bold")

plt.tight_layout()
plt.show()
```

### Quesiti

::::{grid} 1 1 2 2
:::{card}
**47**

- $\lim_{x \to 3} f(x)$
- $\lim_{x \to 4} f(x)$
:::

:::{card}
**48**

- $\lim_{x \to 3^-} f(x)$
- $\lim_{x \to 4^+} f(x)$
:::

:::{card}
**49**

- $\lim_{x \to -2} f(x)$
- $\lim_{x \to 1} f(x)$
:::

:::{card}
**50**

- $\lim_{x \to 4^-} f(x)$
- $\lim_{x \to 4^+} f(x)$
- $\lim_{x \to 6} f(x)$
:::

:::{card}
**51**

- $\lim_{x \to \frac{1}{2}} f(x)$
- $\lim_{x \to 1^-} f(x)$
- $\lim_{x \to 3} f(x)$
:::

:::{card}
**52**

- $\lim_{x \to 2^-} f(x)$
- $\lim_{x \to 2^+} f(x)$
- $\lim_{x \to 4} f(x)$
- $\lim_{x \to 5} f(x)$
:::
::::

```{dropdown} Soluzioni rapide

- **47**: $-2$; $0$.
- **48**: $1$; valore del ramo destro in $x=4$.
- **49**: valore letto sul minimo in $x=-2$; valore letto sul dosso in $x=1$.
- **50**: $6$; $6$; $4$.
- **51**: valore del ramo sinistro in $x=\frac{1}{2}$; $+\infty$; $0$.
- **52**: valore del tratto lineare in $x=2$; valore del tratto parabolico in $x=2$; $1$; $0$.
```