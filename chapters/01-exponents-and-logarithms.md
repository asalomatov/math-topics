# Exponents & Logarithms

## Overview

There is a famous old story. A king, delighted with the game of chess, offers
its inventor any reward he names. The inventor asks for something that sounds
absurdly modest: one grain of rice on the first square of the board, two on the
second, four on the third, and so on, doubling each time. The king laughs and
agrees — and then discovers he has promised more rice than has ever existed on
Earth. The last square alone calls for $2^{63}$ grains, a number with twenty
digits.

That collision between a tiny rule ("just keep doubling") and a monstrous
outcome is the subject of this chapter. The rule is **exponentiation**, and
understanding it well means understanding two things most people never separate:

1. What $a^n$ *really* means once $n$ stops being a friendly counting number —
   when it is zero, or negative, or a fraction, or even irrational.
2. How to run the machine *backwards*. If doubling takes me from $1$ to a
   billion, how many doublings was that? The answer is a **logarithm**, and
   logarithms turn out to be one of the most useful ideas in all of mathematics
   — for a reason that is almost a magic trick.

By the end you should be able to manipulate exponents and logarithms fluently,
but more importantly you should see *why* their rules are the only rules they
could possibly be, and why the two operations are reflections of each other.

## Prerequisites

- Comfort with the arithmetic of fractions and negative numbers.
- Square roots and $n$th roots.
- The idea of a function and its graph.

## Exposition

### 1. Where it begins: counting factors

When $n$ is a positive whole number, $a^n$ is nothing mysterious — it is just
shorthand for repeated multiplication:
$$ a^n = \underbrace{a \cdot a \cdots a}_{n \text{ factors}}. $$

From this single picture, three rules drop out *by counting*. If I multiply $a^m$
by $a^n$, I am putting $m$ factors next to $n$ factors, so I have $m+n$ of them:
$$ a^m \cdot a^n = a^{m+n}. \tag{L1} $$

If I raise $a^m$ to the power $n$, I have $n$ copies of a block of $m$ factors:
$$ (a^m)^n = a^{mn}. \tag{L2} $$

And a product raised to a power distributes, because multiplication doesn't care
about order:
$$ (ab)^n = a^n b^n. \tag{L3} $$

These are not laws handed down from above; they are *observations* about what
happens when you count factors. Of the three, **(L1) is the master rule** — the
one everything else will be forced to obey. Hold onto it.

> **A first warning.** Right now (L1)–(L3) are only justified for *positive whole
> number* exponents, because "repeated multiplication" only makes sense when you
> can count the repetitions. What on earth could $a^0$ or $a^{-3}$ or $a^{1/2}$
> mean? You cannot multiply $a$ by itself "zero times" or "half a time." The next
> section resolves this — and the resolution is the most important idea in the
> chapter.

### 2. The principle of permanence: extending the exponent

Here is the central move, and it is a move you will see again and again in
mathematics. We *want* to give meaning to $a^0$, $a^{-n}$, and $a^{1/n}$. We
could define them any way we like. But there is one definition that is not
arbitrary — the one that **keeps the master rule (L1) true**.

This is sometimes called the **principle of permanence of form**: when you
extend an operation to new cases, you choose the extension that preserves the
laws the operation already satisfied. Watch how (L1) alone *forces* every new
definition. There is no choice involved; we are merely refusing to break the
rule.

**Zero.** Whatever $a^0$ is, (L1) says $a^1 \cdot a^0 = a^{1+0} = a^1$. So $a^0$
must be the number that leaves $a$ unchanged under multiplication:
$$ a^0 = 1 \qquad (a \neq 0). $$
Not a convention, not a special case to memorize — a *consequence*.

**Negative exponents.** Whatever $a^{-n}$ is, (L1) says
$a^n \cdot a^{-n} = a^{n + (-n)} = a^0 = 1$. So $a^{-n}$ must be the reciprocal of
$a^n$:
$$ a^{-n} = \frac{1}{a^n}. $$

**Fractional exponents.** Whatever $a^{1/n}$ is, applying (L1) $n$ times (or
using (L2)) gives $\left(a^{1/n}\right)^n = a^{\,n \cdot \frac{1}{n}} = a^1 = a$.
So $a^{1/n}$ must be a number whose $n$th power is $a$ — that is, the $n$th root:
$$ a^{1/n} = \sqrt[n]{a}, \qquad a^{p/q} = \sqrt[q]{a^p}. $$

Every "rule for exponents" you have ever memorized is really just (L1) refusing
to be broken. That is the whole secret.

> **Example.** Evaluate $8^{-2/3}$. Read the exponent as instructions:
> $8^{-2/3} = \dfrac{1}{8^{2/3}} = \dfrac{1}{\left(\sqrt[3]{8}\right)^2}
> = \dfrac{1}{2^2} = \dfrac14.$ Negative means *reciprocal*, the $3$ in the
> denominator means *cube root*, the $2$ means *square*.

> **A necessary restriction.** For these fractional definitions to behave, we
> require the base $a > 0$. The trouble is that even roots of negatives escape
> the real numbers ($\sqrt{-1}$ is not real), and allowing them makes the laws
> contradict each other. So from here on, *when the exponent is not an integer,
> assume the base is positive.* (Negative bases return, gloriously, in the
> [Complex Numbers](12-complex-numbers.md) chapter, where $\sqrt{-1}$ is exactly
> the point.)

> **Deeper — irrational exponents.** We have now defined $a^x$ for every
> *rational* $x$. But what is $2^{\sqrt 2}$? There is no "$\sqrt2$ factors" to
> count, and $\sqrt2$ is not a fraction. The honest answer is that we define it
> by *approximation*: $\sqrt2 = 1.41421\ldots$, and we look at
> $2^{1.4},\, 2^{1.41},\, 2^{1.414},\ldots$ These rational-exponent values close
> in on a single real number, and *that* limit is what $2^{\sqrt 2}$ means. Making
> "close in on" precise is the business of calculus; for now, trust that $a^x$ is
> defined, and smoothly so, for every real $x$. This is why we can draw its graph
> as an unbroken curve.

### 3. The exponential function and the meaning of growth

Fix the base and let the *exponent* vary. The result is the **exponential
function**
$$ f(x) = a^x \qquad (a > 0,\ a \neq 1). $$

Rewriting the master rule (L1) in this language gives the property that *defines*
exponential behavior:
$$ f(x + y) = f(x)\,f(y). $$
In words: **adding in the input multiplies in the output.** This is the precise
sense in which exponential growth differs from the growth you are used to.

Compare two functions as $x$ marches $0, 1, 2, 3, \dots$:

| $x$ | linear $\;2x$ | exponential $\;2^x$ |
|---|---|---|
| 0 | 0 | 1 |
| 1 | 2 | 2 |
| 2 | 4 | 4 |
| 3 | 6 | 8 |
| 10 | 20 | 1024 |
| 64 | 128 | $\approx 1.8 \times 10^{19}$ |

A linear function adds a fixed amount per step; an exponential function
*multiplies* by a fixed factor per step. Equal steps in $x$ produce equal
*differences* for the line but equal *ratios* for the exponential. This is
exactly the chessboard: each square multiplies by $2$, and multiplication, run
long enough, buries any amount of mere addition. (That an exponential eventually
overtakes *every* polynomial, no matter how steep, is a fact worth carrying with
you; you will prove versions of it for years.)

This also reveals what an exponential function "is": the continuous version of a
**geometric sequence**. The sequence $1, 2, 4, 8, \dots$ is just $2^x$ sampled at
the integers. Sequences whose terms grow by a constant *ratio* are exponential;
sequences that grow by a constant *difference* are linear (arithmetic). Keep this
pairing in mind — it is the seed of the whole chapter:

$$\boxed{\;\text{arithmetic : difference :: geometric : ratio}\;}$$

> **Example (doubling time).** A colony of bacteria doubles every $3$ hours.
> Starting from $1000$, the count after $t$ hours is $N(t) = 1000 \cdot 2^{t/3}$.
> After a full day ($t = 24$), that is $1000 \cdot 2^{8} = 256{,}000$. Notice the
> exponent $t/3$ counts *how many doublings* have happened — a foretaste of the
> logarithm, which answers the reverse question.

### 4. Logarithms: running the machine backwards

Exponential growth raises an irresistible question. We know $2^{10} = 1024$. But
suppose I ask the reverse: *to what power must I raise $2$ to get $1024$?* The
answer, $10$, has a name. It is the **logarithm base $2$ of $1024$**:
$$ \log_a x = y \quad\text{means exactly}\quad a^y = x. $$

A logarithm is **an exponent** — specifically, the exponent you need. Read
$\log_a x$ aloud as *"the power to which $a$ must be raised to give $x$."* Every
fact about logarithms becomes obvious if you keep translating back to that
sentence.

Because the logarithm just *undoes* exponentiation, the laws of logarithms are
the laws of exponents seen in a mirror. The master rule
$a^{m} a^{n} = a^{m+n}$, read backwards, becomes the master rule of logarithms:
$$ \log_a(xy) = \log_a x + \log_a y. \tag{the mirror of L1} $$

Take a moment to feel how remarkable that statement is. **The logarithm converts
multiplication into addition.** The other two laws follow the same way:
$$ \log_a\!\left(\frac{x}{y}\right) = \log_a x - \log_a y, \qquad
   \log_a\!\left(x^k\right) = k\,\log_a x. $$

> **Why this was a revolution.** Before calculators, multiplying two ten-digit
> numbers — a routine necessity in astronomy and navigation — was hours of
> error-prone labor. In 1614 John Napier published tables of logarithms, and
> suddenly you could *multiply by adding*: look up the logs of your two numbers,
> add them (easy), and look up which number has that sum as its log. The
> astronomer Laplace said logarithms, "by shortening the labors, doubled the life
> of the astronomer." The slide rule — the engineer's constant companion until
> the 1970s — is nothing but two logarithmic scales sliding past each other,
> adding lengths to multiply numbers. The same idea, that the *right* change of
> viewpoint turns a hard operation into an easy one, runs through all of
> mathematics.

**Change of base.** Calculators carry only two logarithms (base $10$ and the
natural base $e$ of the next section), yet you can get any base from any other:
$$ \log_a x = \frac{\log_b x}{\log_b a}. $$
This isn't a new fact to memorize; it falls straight out of the definition. Let
$y = \log_a x$, so $a^y = x$. Take $\log_b$ of both sides and use the power law:
$y \log_b a = \log_b x$, which rearranges to the formula. Notice the family
resemblance to converting units (feet to meters): a logarithm is a kind of
*measuring*, and changing base is changing your unit of measurement.

### 5. Logarithms measure scale

Here is the idea that makes logarithms feel inevitable rather than clever. On the
number line, the marks $1, 2, 4, 8, 16, \dots$ crowd together near $1$ and race
apart as they grow. But their *exponents* $0, 1, 2, 3, 4, \dots$ are perfectly
evenly spaced. **A logarithm is what you get when you measure a number not by its
size but by its scale** — by how many factors it carries.

This is why so much of the world is reported on logarithmic scales: because we
perceive *ratios*, not differences. A sound ten times more intense feels like one
fixed step louder, so loudness (decibels) is logarithmic. So is the Richter scale
of earthquakes, the pH of acids, the brightness of stars. In each case a step on
the scale means *multiply by a fixed factor*.

One especially useful consequence, well worth knowing for competitions: **the
number of digits of a positive integer $N$ in base $10$ is**
$$ \lfloor \log_{10} N \rfloor + 1. $$
The reason is exactly the scale idea. A number has $d$ digits precisely when it
lies in $[10^{\,d-1}, 10^{\,d})$, i.e. when $d - 1 \le \log_{10} N < d$. So
$\log_{10} N$, rounded down, is one less than the digit count. The logarithm
*counts the digits* because digits are exactly the scale of a number in base ten.

> **Example.** How many digits does $2^{100}$ have? Using $\log_{10}2 \approx
> 0.30103$, we get $\log_{10}(2^{100}) = 100 \log_{10}2 \approx 30.103$, so the
> count is $\lfloor 30.103 \rfloor + 1 = 31$ digits. We have learned the *size*
> of a number we could never write out by hand, by measuring its scale.

### 6. A glimpse ahead: the natural base $e$

We have treated every base $a$ on equal footing, and for algebra that is right.
But one base is special, and you will meet it everywhere later: the number
$$ e = 2.71828\ldots $$
It arises the moment growth becomes *continuous*. Suppose a bank pays $100\%$
interest per year. Paid once, your dollar becomes $\$2$. Paid as $50\%$ twice, it
becomes $(1.5)^2 = \$2.25$. Paid as $\tfrac1n$ of the interest $n$ times, you get
$\left(1 + \tfrac1n\right)^n$ — and as the compounding gets finer and finer,
$n \to \infty$, this settles on $e$. The logarithm to base $e$, written $\ln x$,
is called the **natural logarithm**, and it is "natural" because the exponential
$e^x$ is the one function that is its own rate of change — the fact that makes it
the backbone of calculus. We point at it now only so the name is familiar; the
story is told properly later.

## Summary

- **One master rule**, $a^m a^n = a^{m+n}$, generates everything.
- **Permanence of form** forces the extended definitions, not convention:
  $$ a^0 = 1, \qquad a^{-n} = \frac{1}{a^n}, \qquad a^{p/q} = \sqrt[q]{a^p}\quad(a>0). $$
- **Exponential = constant ratio per step:** $f(x+y) = f(x)f(y)$; it is the
  continuous geometric sequence, and it outgrows every polynomial.
- **A logarithm is an exponent:** $\log_a x = y \iff a^y = x$.
- **The mirror laws** turn multiplication into addition:
  $$ \log_a(xy) = \log_a x + \log_a y, \quad \log_a(x^k) = k\log_a x, \quad
     \log_a x = \frac{\log_b x}{\log_b a}. $$
- **Logs measure scale:** a base-$10$ integer $N$ has $\lfloor \log_{10}N\rfloor + 1$
  digits.

## Exercises

### Warm-up

1. Using *only* the master rule $a^m a^n = a^{m+n}$, explain to a skeptic why
   $a^0$ must equal $1$ and why $a^{-1}$ must equal $1/a$. (You are re-deriving
   §2, in your own words.)
2. Evaluate without a calculator: $\;27^{2/3}$, $\;16^{-3/4}$, $\;\left(\tfrac19\right)^{-1/2}$.
3. Rewrite as a single logarithm: $\;\log_5 12 - \log_5 4$. Then evaluate it.
4. Compute $\;\log_2 3 \cdot \log_3 4 \cdot \log_4 5 \cdot \log_5 6 \cdot \log_6 7 \cdot \log_7 8$.
   (Hint: change everything to one base and watch what happens.)

### Standard

5. Solve for $x$: $\;\log_2 x + \log_2(x - 2) = 3$. (Mind the domain — check your
   answer is legal.)
6. A radioactive sample has a half-life of $5$ days: every $5$ days, half of it
   decays. What fraction remains after $3$ weeks? Express the answer as a power
   of $2$, then estimate it as a decimal.
7. How many digits does $5^{100}$ have? (Use $\log_{10}2 \approx 0.30103$ and the
   fact that $5 = 10/2$ — no other logarithm needed.)
8. Solve $\;\log_2 x + \log_4 x + \log_8 x = 11$. (Convert all three to base $2$
   first.)

### Challenge

9. Which is larger, $\;\sqrt{2}\;$ or $\;\sqrt[3]{3}\,$? Decide it *without a
   calculator* by raising both to a cleverly chosen power. (This is the heart of
   many AMC problems: replace an awkward comparison with an equivalent clean one.)
10. A function $f$, defined on the positive reals, satisfies
    $f(xy) = f(x) + f(y)$ for all positive $x, y$, and $f(2) = 1$. Find $f(1)$,
    $f(8)$, $f\!\left(\tfrac12\right)$, and $f(\sqrt2)$. What familiar function
    must $f$ be?
11. (AMC-flavored.) The number $2^{2025}$ is written out in full. Its leading
    (leftmost) digit is some value, and it has a certain number of digits. Using
    $\log_{10}2 \approx 0.30103$, find how many digits $2^{2025}$ has. *Then*,
    harder: explain how the fractional part of $2025\log_{10}2$ would let you
    recover the leading digit.

## Solutions

<details>
<summary>Click to reveal solutions</summary>

**1.** From $a^1 a^0 = a^{1+0} = a^1$, the factor $a^0$ leaves $a^1$ unchanged
under multiplication, and the only such number is $1$; hence $a^0 = 1$ (for
$a\neq0$). From $a^1 a^{-1} = a^{1+(-1)} = a^0 = 1$, the factor $a^{-1}$ is
whatever you multiply $a$ by to get $1$ — its reciprocal — so $a^{-1} = 1/a$. The
point of the exercise: these are *forced*, not decreed.

**2.** $27^{2/3} = (\sqrt[3]{27})^2 = 3^2 = 9$. $\;16^{-3/4} =
\dfrac{1}{(\sqrt[4]{16})^3} = \dfrac{1}{2^3} = \dfrac18$. $\;\left(\tfrac19\right)^{-1/2}
= \left(9\right)^{1/2} = 3$ (the negative exponent flips the fraction first).

**3.** $\log_5 12 - \log_5 4 = \log_5 \dfrac{12}{4} = \log_5 3$. As a decimal that
is between $0$ and $1$ since $3 < 5$; it is not a "nice" number, which is fine —
the point was the quotient law.

**4.** Change every factor to base $2$: $\log_k(k+1) = \dfrac{\log_2(k+1)}{\log_2 k}$.
The product telescopes,
$$\frac{\log_2 3}{\log_2 2}\cdot\frac{\log_2 4}{\log_2 3}\cdots\frac{\log_2 8}{\log_2 7}
= \frac{\log_2 8}{\log_2 2} = \log_2 8 = 3.$$
Every interior term cancels — the same collapse you'll see in telescoping sums
and products throughout competition math.

**5.** Combine: $\log_2[x(x-2)] = 3$, so $x(x-2) = 2^3 = 8$, i.e.
$x^2 - 2x - 8 = 0$, giving $x = 4$ or $x = -2$. But the original
$\log_2(x-2)$ requires $x > 2$, so $x = -2$ is illegal. **Answer: $x = 4$.** The
lesson: a logarithm silently demands a positive argument, and that demand can
delete an algebraically valid root.

**6.** Three weeks is $21$ days, which is $21/5 = 4.2$ half-lives, so the fraction
remaining is $2^{-4.2} = 2^{-4.2}$. Numerically $2^{4.2} \approx 18.4$, so about
$1/18.4 \approx 0.054$, a little over $5\%$.

**7.** $\log_{10}(5^{100}) = 100\log_{10}5 = 100\log_{10}\frac{10}{2} =
100(1 - \log_{10}2) \approx 100(0.69897) = 69.897$. Digit count
$= \lfloor 69.897\rfloor + 1 = 70$. (Notice we never needed $\log_{10}5$ directly
— we manufactured it from $\log_{10}2$.)

**8.** Write $\log_2 x = t$. Then $\log_4 x = \dfrac{\log_2 x}{\log_2 4} =
\dfrac t2$ and $\log_8 x = \dfrac t3$. The equation becomes
$t\left(1 + \tfrac12 + \tfrac13\right) = t \cdot \tfrac{11}{6} = 11$, so $t = 6$
and $x = 2^6 = 64$.

**9.** Raise both to the $6$th power (the least common multiple of the roots'
orders): $\left(\sqrt2\right)^6 = 2^3 = 8$ while $\left(\sqrt[3]{3}\right)^6 =
3^2 = 9$. Since $9 > 8$ and sixth powers preserve order for positive numbers,
$\sqrt[3]{3} > \sqrt2$. The technique — turn $\sqrt2$ vs $\sqrt[3]3$ into the
trivial $8$ vs $9$ — is worth more than the answer.

**10.** Set $x = y = 1$: $f(1) = f(1) + f(1)$ forces $f(1) = 0$. Then
$f(8) = f(2\cdot2\cdot2) = 3f(2) = 3$. From $f(2) + f(\tfrac12) = f(1) = 0$ we get
$f(\tfrac12) = -1$. And $f(\sqrt2) + f(\sqrt2) = f(2) = 1$ gives
$f(\sqrt2) = \tfrac12$. The defining property "product $\to$ sum" with $f(2)=1$ is
exactly $\log_2$; indeed $f(x) = \log_2 x$ for every positive $x$. You have
*reconstructed the logarithm from its single most important property.*

**11.** $\log_{10}(2^{2025}) = 2025 \cdot 0.30103 \approx 609.59$, so the digit
count is $\lfloor 609.59 \rfloor + 1 = 610$. For the leading digit: write
$2025\log_{10}2 = 609 + 0.59\ldots$ The integer part $609$ fixes the *scale*
($2^{2025}$ is between $10^{609}$ and $10^{610}$); the fractional part $f \approx
0.59$ fixes the *digits*, because $2^{2025} = 10^{609} \cdot 10^{f}$ and
$10^{0.59} \approx 3.9$. So the number looks like $3.9\ldots \times 10^{609}$ —
its leading digit is $3$. This split of $\log_{10} N$ into integer part (scale)
and fractional part (digits) is §5's idea pushed to its conclusion.

</details>
