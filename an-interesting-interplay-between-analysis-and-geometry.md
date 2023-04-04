-------
title: An interesting interplay between analysis and geometry
authors: @rubenslonghi
description: Describe your article in 1-2 sentences.
preview_image: 
# allowable values: review, research, tutorial
article_type: review
published: false
-------

Let $M=\mathbb{R}/2 \pi \mathbb{Z}=S^1$ and let $E=F=M \times \mathbb{C}$ be the trivial complex line bundle with the usual Hermitian metric. We consider functions on $M$ as periodic functions on $\mathbb{R}$. Let $a, b: M \rightarrow \mathbb{C}$ be smooth and let $a(x) \neq 0$ for all $x$. Let $P=a(x) \frac{d}{d x}+b(x)$

a) Show that $\operatorname{dim}(\operatorname{ker}(P)) \in\{0,1\}$.

b) Show by example that both cases in a) occur.

c) Show that $\operatorname{dim}(\operatorname{ker}(P))=\operatorname{dim}\left(\operatorname{ker}\left(P^{*}\right)\right)$.

-----------------------------------------------------------------

Solution:

We start by noticing the following:
$$
C^{\infty}\left(S^{1}, \mathbb{C}\right)=\left\{u \in C^{\infty}(\mathbb{R}, \mathbb{C}) \mid u(x+2 \pi)=u(x), \ \forall x \in \mathbb{R}\right\}.
$$

a) $P=a(x) \frac{d}{d x}+b(x), a \neq 0$, so from the theory of ordinary differential equations, we can use the separation of variables technique to get

$$
\begin{aligned}
& a(x) u^{\prime}+b(x) u=0 \quad \frac{u^{\prime}}{u}=-\frac{b}{a}.
\end{aligned}
$$


By integrating both sides we then get

\begin{equation*}
\underbrace{\int_0^x \frac{u^{\prime}(t)}{u(t)} d t}_{=\ln \left(\frac{u(x)}{u(0)}\right)}=-\int_0^x \frac{b(t)}{a(t)} d t,
\end{equation*}

which in turn implies
$$
u(x)=u(0) e^{-\int_0^x \frac{b(t)}{a(t)} d t}, u(0) \in \mathbb{C}
$$

$$
\begin{aligned}
& \Rightarrow \operatorname{ker}\left(P: C^{\infty}(\mathbb{R},\mathbb{C}) \to C^{\infty}(\mathbb{R},\mathbb{C}) \right)=1.
\end{aligned}
$$

Now, to look at $\ker\left(P: C^{\infty}\left(S^{1}, \mathbb{C}\right) \to C^{\infty}\left(S^{1}, \mathbb{C}\right) \right)$ we ask for periodicity of the solution $u$, i.e.

$$
\begin{aligned}
 u(x+2 \pi) &=u(x) \quad \text{for any } x \in \mathbb{R}: \\
 u(x+2 \pi) &=u(0) e^{-\int_{0}^{x+2 \pi} \frac{b(t)}{a(t)}dt}=u(0) e^{-\int_{0}^{x} \frac{b(t)}{a(t)} d t} \cdot e^{-\int_{x}^{x+2 \pi} \frac{b(t)}{a(t)}  d t} \\
&=u(x) = u(0) e^{-\int_{0}^{x} \frac{b(t)}{a(t)} d t}\\
& \Leftrightarrow e^{-\int_{0}^{2 \pi} \frac{b(t)}{a(t)}  d t}=1=e^{2 \pi k i}, k \in \mathbb{Z}.
\end{aligned}
$$

Since, due to periodicity of $a$ and $b$ we get $\int_{x}^{x+2 \pi} \frac{b(t)}{a(t)} d t=\int_{0}^{2 \pi} \frac{b(t)}{a(t)} d t$. Hence the periodicity condition becomes

$$
\int_{0}^{2 \pi} \frac{b(t)}{a(t)} d t \in 2 \pi i \mathbb{Z}.
$$

If the condition is verified, $\operatorname{ker} P|_{S^1}=1$ otherwise we have the trivial solution $u=0$, so $\operatorname{ker} P|_{S^1}=0$. This implies the sought result:
$$
\operatorname{ker}\left(P: C^{\infty}\left(S^{1}, \mathbb{C}\right) \to C^{\infty}\left(S^{1}, \mathbb{C}\right)\right) \in\{0,1\}.
$$


b) 1.a) $a \equiv 1, b(x)=\cos (x) \Rightarrow b \in C^{\infty}\left(S^1\right)$ and

$$
\begin{aligned}
& \int_{0}^{2 \pi} \cos (x) d x=\sin (2 \pi k)-\sin (0)=0 \in 2 \pi i \mathbb{Z} \\
& u(x)=u(0) e^{-\sin (x)} \Rightarrow u^{\prime}(x)=-u(0) \cos x \,e^{-\sin (x)} \\
& \Rightarrow \operatorname{dim} \operatorname{ker}\left(\frac{d}{d x}+\cos (x)\right)=1
\end{aligned}
$$

1.b) $a \equiv i, b(x)=-n \in \mathbb{Z}$, then the operator becomes $P=i \frac{d}{d x}-n$

$$
\begin{aligned}
& \int_{0}^{2 \pi} \frac{-n}{i} d t=2 \pi n i \in 2 \pi i \mathbb{Z} \\
& \Rightarrow  u(x)=u(0) e^{-\int_{0}^{x}-\frac{n}{i} d t}=u(0) e^{-i n x} \\
& \Rightarrow \operatorname{dim} \operatorname{ker}\left(i \frac{d}{d x}-n\right)=1
\end{aligned}
$$

SPOILER ALERT: $D:=i \frac{d}{d x}$ on $S^1$ is a self-adjoint Dirac-type operator since $D^{*}=D$ and $D^{2}=-\frac{d^{2}}{d x^{2}}$. The exercise shows that $D u=\lambda u$ has solutions $u \neq 0$ on $S^{1} \Leftrightarrow \lambda \in \mathbb{Z}$, i.e. $\operatorname{Spec}(D)=\mathbb{Z}$.

2) $a \equiv 1, b \equiv 1 \Rightarrow u(x)=u(0) e^{-x}$ is not periodic, hence $u=0$ is the only solution

c) The formal adjoint reads $P^{*}=-\bar{a} \frac{d}{d x}+\bar{b}-\bar{a}^\prime$.

Proceeding as before, we find that the set of solutions on $\mathbb{R}$ is the $\mathbb{C}$-span of $e^{\int_{0}^{x} \frac{\overline{b(t)-a^{\prime}(t)}}{\overline{a(t)}} d t}$, which descends to a solution on $S^{1}$ if and only if
$$
\begin{aligned}
    \int_{0}^{2 \pi} \frac{\bar{b}-\bar{a}^{\prime}}{\bar{a}} d t \in 2 \pi i \mathbb{Z} \Leftrightarrow\left(\int_{0}^{2 \pi} \frac{b}{a} d t-\int_{0}^{2 \pi} \frac{a^{\prime}}{a} d t\right) \in 2 \pi i \mathbb{Z},
\end{aligned}
$$
which in turn is equivalent to $\int_{0}^{2 \pi} \frac{b}{a} d t\in 2 \pi i \mathbb{Z}$ since $a: S^{1} \rightarrow \mathbb{C}\setminus\{0\}$ is a loop and
$$
\int_{0}^{2 \pi} \frac{a^{\prime}(t)}{a(t)} d t=\oint_{a\left(S^1\right)} \frac{1}{z} d z=2 \pi i \,\underbrace{W(a, 0)}_{\in \mathbb{Z}} \in 2 \pi i \mathbb{Z},
$$
where $W(a, 0)$ is the winding number of $a\left(S^1\right)$ around $0 \in \mathbb{C}$.

Hence, $P^{*}$ has nontrivial periodic solutions if and only if $P$ does.