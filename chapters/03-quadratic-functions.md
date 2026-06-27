# Quadratic Functions

## Overview

A **quadratic function** is any function of the form $f(x) = ax^2 + bx + c$ with
$a \neq 0$. Its graph is a *parabola*. Quadratics are the first place where
algebra and geometry meet head-on: the same object can be read as a formula, as
a shape, and as the solution set of an equation. By the end of this chapter you
will be able to sketch any parabola, find its vertex and roots, and switch
freely between the three standard forms.

## Prerequisites

- Expanding and factoring linear expressions.
- Solving linear equations.
- Plotting points in the Cartesian plane.

## Exposition

### 1. The standard form and the shape of a parabola

The **standard form** is

$$ f(x) = ax^2 + bx + c, \qquad a \neq 0. $$

The sign of $a$ controls the orientation:

- if $a > 0$, the parabola opens **upward** (a "valley", with a lowest point);
- if $a < 0$, it opens **downward** (a "hill", with a highest point).

The magnitude of $a$ controls the width: larger $|a|$ gives a narrower parabola.

> **Example.** $f(x) = 2x^2$ is narrower than $g(x) = \tfrac{1}{2}x^2$, and both
> open upward. $h(x) = -x^2$ is the mirror image of $x^2$ across the $x$-axis.

### 2. The vertex and the axis of symmetry

Every parabola is symmetric about a vertical line, the **axis of symmetry**. The
point where the parabola meets this axis is the **vertex** — the lowest point
(if $a>0$) or highest point (if $a<0$).

The axis of symmetry is

$$ x = -\frac{b}{2a}, $$

and the vertex is the point $\left(-\dfrac{b}{2a},\; f\!\left(-\dfrac{b}{2a}\right)\right)$.

> **Example.** For $f(x) = x^2 - 6x + 5$ we have $a=1,\ b=-6$, so the axis is
> $x = -\frac{-6}{2} = 3$. Then $f(3) = 9 - 18 + 5 = -4$, so the vertex is
> $(3, -4)$.

### 3. Vertex form and completing the square

**Vertex form** writes the function as

$$ f(x) = a(x - h)^2 + k, $$

where $(h, k)$ is the vertex directly. We pass from standard to vertex form by
**completing the square**.

> **Example.** Convert $f(x) = x^2 - 6x + 5$.
>
> $$ x^2 - 6x + 5 = (x^2 - 6x + 9) - 9 + 5 = (x-3)^2 - 4. $$
>
> So $h = 3,\ k = -4$, agreeing with the vertex found above.

In general, completing the square on $ax^2 + bx + c$ gives

$$ a\left(x + \frac{b}{2a}\right)^2 + \left(c - \frac{b^2}{4a}\right), $$

which is where the formula $x = -\tfrac{b}{2a}$ comes from.

### 4. Roots and the quadratic formula

The **roots** (or zeros) are the $x$-values where $f(x) = 0$, i.e. where the
parabola crosses the $x$-axis. Solving $ax^2 + bx + c = 0$ gives the
**quadratic formula**:

$$ x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}. $$

The quantity under the root, the **discriminant** $D = b^2 - 4ac$, tells you how
many real roots there are:

| Discriminant | Real roots | Geometry |
|---|---|---|
| $D > 0$ | two distinct | crosses the $x$-axis twice |
| $D = 0$ | one (repeated) | touches the $x$-axis at the vertex |
| $D < 0$ | none | does not meet the $x$-axis |

> **Example.** For $x^2 - 6x + 5 = 0$: $D = 36 - 20 = 16 > 0$, and
> $x = \frac{6 \pm 4}{2}$, giving $x = 5$ and $x = 1$.

### 5. Factored form and Vieta's formulas

When the roots $x_1, x_2$ are real, the function factors as

$$ f(x) = a(x - x_1)(x - x_2). $$

Expanding and matching coefficients gives **Vieta's formulas**:

$$ x_1 + x_2 = -\frac{b}{a}, \qquad x_1 x_2 = \frac{c}{a}. $$

These let you read off or check roots without the full formula.

> **Example.** $x^2 - 6x + 5$ has roots summing to $6$ and multiplying to $5$ —
> namely $1$ and $5$ — so $x^2 - 6x + 5 = (x-1)(x-5)$.

## Summary

- **Three forms:** standard $ax^2+bx+c$, vertex $a(x-h)^2+k$, factored
  $a(x-x_1)(x-x_2)$.
- **Axis of symmetry:** $x = -\dfrac{b}{2a}$; the vertex sits on it.
- **Quadratic formula:** $x = \dfrac{-b \pm \sqrt{b^2-4ac}}{2a}$.
- **Discriminant** $D = b^2 - 4ac$: sign gives the number of real roots.
- **Vieta:** $x_1 + x_2 = -\dfrac{b}{a}$, $\ x_1 x_2 = \dfrac{c}{a}$.

## Exercises

### Warm-up

1. State the direction of opening and the vertex of $f(x) = (x-2)^2 + 3$.
2. Compute the discriminant of $x^2 + 4x + 4$ and say how many real roots it has.

### Standard

3. Convert $f(x) = x^2 + 8x + 11$ to vertex form and give its vertex.
4. Solve $2x^2 - 7x + 3 = 0$.
5. Without solving, find the sum and product of the roots of $3x^2 - 12x + 5 = 0$.

### Challenge

6. For which values of $m$ does $x^2 + mx + 9 = 0$ have exactly one real root?
7. A parabola passes through $(0, 5)$, has vertex at $(2, 1)$. Find $f(x)$ in
   standard form.

## Solutions

<details>
<summary>Click to reveal solutions</summary>

**1.** Opens upward ($a = 1 > 0$); vertex $(2, 3)$.

**2.** $D = 4^2 - 4\cdot1\cdot4 = 0$, so one repeated real root (namely $x=-2$).

**3.** $x^2 + 8x + 11 = (x^2 + 8x + 16) - 16 + 11 = (x+4)^2 - 5$. Vertex $(-4, -5)$.

**4.** $D = 49 - 24 = 25$, so $x = \dfrac{7 \pm 5}{4}$, giving $x = 3$ and
$x = \tfrac{1}{2}$.

**5.** Sum $= -\dfrac{-12}{3} = 4$; product $= \dfrac{5}{3}$.

**6.** One real root means $D = 0$: $m^2 - 36 = 0$, so $m = \pm 6$.

**7.** Use vertex form $f(x) = a(x-2)^2 + 1$. From $(0,5)$: $5 = a\cdot4 + 1$, so
$a = 1$. Thus $f(x) = (x-2)^2 + 1 = x^2 - 4x + 5$.

</details>
