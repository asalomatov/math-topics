# Exponents & Logarithms

## Overview

There is a famous old story. A king, delighted with the game of chess, offers
its inventor any reward he names. The inventor asks for something that sounds
absurdly modest: one grain of rice on the first square of the board, two on the
second, four on the third, and so on, doubling each time. The king laughs and
agrees — and then discovers he has promised more rice than has ever existed on
Earth. The last square alone calls for $2^{63}$ grains, a number with twenty
digits.

The gap between that simple rule and its outcome is the subject of this chapter.
The rule is **exponentiation**, and understanding it well means understanding two
things that are often run together:

1. What $a^n$ *really* means once $n$ stops being a friendly counting number —
   when it is zero, or negative, or a fraction, or even irrational.
2. How to run the operation *backwards*. If doubling takes a quantity from $1$ to
   a billion, how many doublings was that? The answer is a **logarithm**, and
   logarithms are among the most useful tools in mathematics, for a reason we
   will come to: they convert multiplication into addition.

By the end you should be able to manipulate exponents and logarithms fluently,
and, more to the point, see why their rules are the only ones possible and why
the two operations are inverses of each other.

## Prerequisites

- Comfort with the arithmetic of fractions and negative numbers.
- Square roots and $n^{\text{th}}$ roots.
- The idea of a function and its graph.

## Exposition

### 1. Where it begins: counting factors

When $n$ is a positive whole number, $a^n$ is nothing mysterious — it is just
shorthand for repeated multiplication:

$$ a^n = \underbrace{a \cdot a \cdots a}_{n \text{ factors}}. $$

From this single picture, three rules drop out *by counting*. If I multiply $a^m$
by $a^n$, I am putting $m$ factors next to $n$ factors, so I have $m+n$ of them:

$$ a^m \cdot a^n = a^{m+n}. \qquad \text{(L1)} $$

If I raise $a^m$ to the power $n$, I have $n$ copies of a block of $m$ factors:

$$ (a^m)^n = a^{mn}. \qquad \text{(L2)} $$

And a product raised to a power distributes, because multiplication doesn't care
about order:

$$ (ab)^n = a^n b^n. \qquad \text{(L3)} $$

These are not laws handed down from above; they are observations about what
happens when you count factors. Of the three, **(L1) is the master rule** — the
one everything else follows from.

> **A first warning.** Right now (L1)–(L3) are only justified for *positive whole
> number* exponents, because "repeated multiplication" only makes sense when you
> can count the repetitions. What on earth could $a^0$ or $a^{-3}$ or $a^{1/2}$
> mean? You cannot multiply $a$ by itself "zero times" or "half a time." The next
> section resolves this — and the resolution is the most important idea in the
> chapter.

### 2. The principle of permanence: extending the exponent

This is a move worth recognizing, because it recurs throughout mathematics. We
want to give meaning to $a^0$, $a^{-n}$, and $a^{1/n}$. We could define them any
way we like. But there is one definition that is not arbitrary — the one that
**keeps the master rule (L1) true**.

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
using (L2)) gives $\left(a^{1/n}\right)^n = a^{\,n \cdot (1/n)} = a^1 = a$.
So $a^{1/n}$ must be a number whose $n^{\text{th}}$ power is $a$ — that is, the $n^{\text{th}}$ root:

$$ a^{1/n} = \sqrt[n]{a}, \qquad a^{p/q} = \sqrt[q]{a^p}. $$

Every rule for exponents is just (L1) applied consistently to new cases.

> **Example.** Evaluate $8^{-2/3}$. Read the exponent as instructions:
>
> $$ 8^{-2/3} = \frac{1}{8^{2/3}} = \frac{1}{\left(\sqrt[3]{8}\right)^2} = \frac{1}{2^2} = \frac14. $$
>
> Negative means *reciprocal*, the $3$ in the denominator means *cube root*, the
> $2$ means *square*.

> **A necessary restriction.** For these fractional definitions to behave, we
> require the base $a > 0$. The trouble is that even roots of negatives escape
> the real numbers ($\sqrt{-1}$ is not real), and allowing them makes the laws
> contradict each other. So from here on, *when the exponent is not an integer,
> assume the base is positive.* (Negative bases return in the
> [Complex Numbers](12-complex-numbers.md) chapter, where $\sqrt{-1}$ is exactly
> the point.)

> **Deeper — irrational exponents.** We have now defined $a^x$ for every
> *rational* $x$. But what is $2^{\sqrt 2}$? There is no way to count $\sqrt2$
> factors, and $\sqrt2$ is not a fraction. The honest answer is that we define it
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
exactly the chessboard: each square multiplies by $2$, and repeated
multiplication outgrows any linear function. An exponential eventually overtakes
every polynomial, however steep — a fact you will prove in various forms later.

This also reveals what an exponential function "is": the continuous version of a
**geometric sequence**. The sequence $1, 2, 4, 8, \dots$ is just $2^x$ sampled at
the integers. Sequences whose terms grow by a constant *ratio* are exponential;
sequences that grow by a constant *difference* are linear (arithmetic). Keep this
pairing in mind — it is the seed of the whole chapter:

$$ \boxed{\;\text{arithmetic : difference :: geometric : ratio}\;} $$

> **Example (doubling time).** A colony of bacteria doubles every $3$ hours.
> Starting from $1000$, the count after $t$ hours is $N(t) = 1000 \cdot 2^{t/3}$.
> After a full day ($t = 24$), that is $1000 \cdot 2^{8} = 256{,}000$. The
> exponent $t/3$ counts how many doublings have happened — which is the question
> the logarithm answers.

### 4. Logarithms: running the machine backwards

Exponentiation has a natural inverse question. We know $2^{10} = 1024$; the
reverse question asks to what power $2$ must be raised to give $1024$. The
answer, $10$, has a name. It is the **logarithm base 2 of 1024**:

$$ \log_a x = y \quad\text{means exactly}\quad a^y = x. $$

A logarithm is **an exponent** — specifically, the exponent you need. Read
$\log_a x$ aloud as "the power to which $a$ must be raised to give $x$." Every
fact about logarithms becomes obvious if you keep translating back to that
sentence.

Because the logarithm just *undoes* exponentiation, the laws of logarithms are
the laws of exponents seen in a mirror. The master rule
$a^{m} a^{n} = a^{m+n}$, read backwards, becomes the master rule of logarithms:

$$ \log_a(xy) = \log_a x + \log_a y. \qquad \text{(the mirror of L1)} $$

This property is what gives logarithms their importance: **the logarithm
converts multiplication into addition.** The other two laws follow the same way:

$$ \log_a\!\left(\frac{x}{y}\right) = \log_a x - \log_a y, \qquad
   \log_a\!\left(x^k\right) = k\,\log_a x. $$

> **Why logarithms were invented.** Before calculators, multiplying two
> ten-digit numbers — a routine necessity in astronomy and navigation — was
> hours of error-prone labor. In 1614 John Napier published tables of logarithms,
> which let one multiply by adding: look up the logs of the two numbers, add them,
> and look up which number has that sum as its log. Laplace remarked that
> logarithms, "by shortening the labors, doubled the life of the astronomer." The
> slide rule, standard equipment for engineers until the 1970s, is just two
> logarithmic scales sliding past each other, adding lengths to multiply numbers.
> The underlying idea — that the right change of viewpoint turns a hard operation
> into an easy one — recurs throughout mathematics.

**Change of base.** Calculators carry only two logarithms (base $10$ and the
natural base $e$ of the next section), yet you can get any base from any other:

$$ \log_a x = \frac{\log_b x}{\log_b a}. $$

This isn't a new fact to memorize; it falls straight out of the definition. Let
$y = \log_a x$, so $a^y = x$. Take $\log_b$ of both sides and use the power law:
$y \log_b a = \log_b x$, which rearranges to the formula. Notice the family
resemblance to converting units (feet to meters): a logarithm is a kind of
*measuring*, and changing base is changing your unit of measurement.

### 5. Logarithms measure scale

There is one more way to see what a logarithm does. On the number line, the marks
$1, 2, 4, 8, 16, \dots$ crowd together near $1$ and spread apart as they grow. But
their exponents $0, 1, 2, 3, 4, \dots$ are evenly spaced. **A logarithm measures a
number not by its size but by its scale** — by how many factors it carries.

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

> **Example.** How many digits does $2^{100}$ have? Using
> $\log_{10}2 \approx 0.30103$, we get
> $\log_{10}(2^{100}) = 100 \log_{10}2 \approx 30.103$, so the count is
> $\lfloor 30.103 \rfloor + 1 = 31$ digits. We have learned the *size* of a
> number we could never write out by hand, by measuring its scale.

### 6. A glimpse ahead: the natural base $e$

We have treated every base $a$ on equal footing, and for algebra that is right.
But one base is special, and you will meet it everywhere later: the number

$$ e = 2.71828\ldots $$

It arises the moment growth becomes *continuous*. Suppose a bank pays $100\%$
interest per year. Paid once, your dollar becomes \$2. Paid as $50\%$ twice, it
becomes $(1.5)^2 = 2.25$ dollars. Paid as $\tfrac1n$ of the interest $n$ times,
you get $\left(1 + \tfrac1n\right)^n$ dollars — and as the compounding gets finer
and finer, $n \to \infty$, this settles on $e$. The logarithm to base $e$, written $\ln x$,
is called the **natural logarithm**, and it is "natural" because the exponential
$e^x$ is the one function that is its own rate of change — the fact that makes it
the backbone of calculus. We point at it now only so the name is familiar; the
story is told properly later.

## Summary

- **One master rule**, $a^m a^n = a^{m+n}$, generates everything.
- **Permanence of form** forces the extended definitions, not convention:
  $a^0 = 1$, $\ a^{-n} = 1/a^n$, $\ a^{p/q} = \sqrt[q]{a^p}$ (for $a>0$).
- **Exponential = constant ratio per step:** $f(x+y) = f(x)f(y)$; it is the
  continuous geometric sequence, and it outgrows every polynomial.
- **A logarithm is an exponent:** $\log_a x = y \iff a^y = x$.
- **The mirror laws** turn multiplication into addition:
  $\log_a(xy) = \log_a x + \log_a y$, $\ \log_a(x^k) = k\log_a x$, and
  $\log_a x = \log_b x / \log_b a$.
- **Logs measure scale:** a base-$10$ integer $N$ has $\lfloor \log_{10}N\rfloor + 1$
  digits.

## Exercises

### Warm-up

1. Using only the master rule $a^m a^n = a^{m+n}$, explain why $a^0$ must equal
   $1$ and why $a^{-1}$ must equal $1/a$.
2. Evaluate without a calculator: $27^{2/3}$, $16^{-3/4}$, $\left(\tfrac19\right)^{-1/2}$.
3. Simplify to a single power: $2^5 \cdot 2^{-3}$; $(x^3)^2 \cdot x^{-4}$; $a^{-2}/a^{-5}$.
4. Evaluate directly from the definition: $\log_2 32$, $\log_9 3$, $\log_{1/2} 8$, $\log_{10} 0.001$.
5. Write as a single logarithm and evaluate: $\log_5 12 - \log_5 4$.
6. Expand $\log_b(a^2 b / c)$ in terms of $\log_b a$ and $\log_b c$.
7. Solve: $2^x = \tfrac{1}{16}$, and $8^{x} = 16$.
8. Solve: $\log_x 27 = 3$, and $\log_4 x = -\tfrac12$.
9. Compute $\log_2 3 \cdot \log_3 4 \cdot \log_4 5 \cdot \log_5 6 \cdot \log_6 7 \cdot \log_7 8$.
   (Change everything to one base.)
10. Evaluate using change of base: $\log_8 32$ and $\log_9 27$.

### Standard

11. Solve for $x$: $\log_2 x + \log_2(x - 2) = 3$. (Check the domain.)
12. A radioactive sample has a half-life of $5$ days. What fraction remains after
    $3$ weeks? Give the answer as a power of $2$, then as a decimal.
13. How many digits does $5^{100}$ have? Use $\log_{10}2 \approx 0.30103$ and
    $5 = 10/2$, with no other logarithm.
14. Solve $\log_2 x + \log_4 x + \log_8 x = 11$. (Convert to base $2$ first.)
15. Solve $4^x - 3\cdot 2^x + 2 = 0$. (Let $u = 2^x$.)
16. Solve $2^x = 3^{x-1}$, expressing $x$ with logarithms.
17. Evaluate $9^{\log_3 4}$ and $2^{\log_4 9}$.

### Challenge

18. Which is larger, $\sqrt{2}$ or $\sqrt[3]{3}$? Decide it without a calculator by
    raising both to a suitable power — replacing an awkward comparison with a clean
    one. This move appears in many AMC problems.
19. A function $f$ on the positive reals satisfies $f(xy) = f(x) + f(y)$ for all
    positive $x, y$, with $f(2) = 1$. Find $f(1)$, $f(8)$, $f\!\left(\tfrac12\right)$,
    and $f(\sqrt2)$, and identify $f$.
20. The number $2^{2025}$ is written out in full. Using $\log_{10}2 \approx 0.30103$,
    find how many digits it has, and then how the fractional part of
    $2025\log_{10}2$ determines the leading (leftmost) digit.
21. Solve $\log_2\!\big(\log_3(\log_4 x)\big) = 0$.
22. Let $N = 100!$. Evaluate
    $1/\log_2 N + 1/\log_3 N + \cdots + 1/\log_{100} N$.

## Solutions

<details>
<summary>Click to reveal solutions</summary>

**1.** From $a^1 a^0 = a^{1+0} = a^1$, the factor $a^0$ must leave $a$ unchanged
under multiplication, so $a^0 = 1$ (for $a \neq 0$). From $a^1 a^{-1} = a^0 = 1$,
the factor $a^{-1}$ is the reciprocal of $a$, so $a^{-1} = 1/a$. Both are forced
by (L1), not chosen.

**2.** $27^{2/3} = (\sqrt[3]{27})^2 = 3^2 = 9$.
$16^{-3/4} = 1/(\sqrt[4]{16})^3 = 1/2^3 = 1/8$.
$\left(\tfrac19\right)^{-1/2} = 9^{1/2} = 3$.

**3.** $2^5 \cdot 2^{-3} = 2^2 = 4$. $(x^3)^2 \cdot x^{-4} = x^6 \cdot x^{-4} = x^2$.
$a^{-2}/a^{-5} = a^{-2-(-5)} = a^3$.

**4.** $\log_2 32 = 5$; $\log_9 3 = \tfrac12$; $\log_{1/2} 8 = -3$ (since
$(1/2)^{-3} = 8$); $\log_{10} 0.001 = -3$.

**5.** $\log_5 12 - \log_5 4 = \log_5(12/4) = \log_5 3$. It is not a round number,
which is fine; the point is the quotient law.

**6.** $\log_b(a^2 b / c) = \log_b a^2 + \log_b b - \log_b c = 2\log_b a + 1 - \log_b c$,
using $\log_b b = 1$.

**7.** $2^x = 2^{-4}$ gives $x = -4$. For $8^x = 16$, write both sides in base $2$:
$2^{3x} = 2^4$, so $3x = 4$ and $x = \tfrac43$.

**8.** $\log_x 27 = 3$ means $x^3 = 27$, so $x = 3$. $\log_4 x = -\tfrac12$ means
$x = 4^{-1/2} = \tfrac12$.

**9.** Change every factor to base $2$: $\log_k(k+1) = \log_2(k+1)/\log_2 k$. The
product telescopes,

$$ \frac{\log_2 3}{\log_2 2}\cdot\frac{\log_2 4}{\log_2 3}\cdots\frac{\log_2 8}{\log_2 7}
= \frac{\log_2 8}{\log_2 2} = \log_2 8 = 3. $$

Every interior factor cancels — the same collapse seen in telescoping sums and
products generally.

**10.** $\log_8 32 = \log_2 32 / \log_2 8 = 5/3$.
$\log_9 27 = \log_3 27 / \log_3 9 = 3/2$.

**11.** Combine: $\log_2[x(x-2)] = 3$, so $x(x-2) = 8$, i.e. $x^2 - 2x - 8 = 0$,
giving $x = 4$ or $x = -2$. The term $\log_2(x-2)$ requires $x > 2$, so $x = 4$. A
logarithm requires a positive argument, which can eliminate an otherwise valid
root.

**12.** Three weeks is $21$ days $= 21/5 = 4.2$ half-lives, so the fraction
remaining is $2^{-4.2}$. Since $2^{4.2} \approx 18.4$, this is about $0.054$.

**13.** $\log_{10}(5^{100}) = 100\log_{10}5 = 100\log_{10}(10/2) = 100(1 - \log_{10}2) \approx 69.897$.
Digit count $= \lfloor 69.897\rfloor + 1 = 70$. We obtained $\log_{10}5$ from
$\log_{10}2$ alone.

**14.** With $t = \log_2 x$: $\log_4 x = t/2$ and $\log_8 x = t/3$. Then
$t\left(1 + \tfrac12 + \tfrac13\right) = t \cdot \tfrac{11}{6} = 11$, so $t = 6$
and $x = 2^6 = 64$.

**15.** Let $u = 2^x > 0$. Then $u^2 - 3u + 2 = 0$, so $u = 1$ or $u = 2$; that is
$2^x = 1$ or $2^x = 2$, giving $x = 0$ or $x = 1$. Writing $4^x = (2^x)^2$ turns
the equation into a quadratic — a recurring move.

**16.** Take $\log$ of both sides (any base): $x\log 2 = (x-1)\log 3$, so
$x(\log 2 - \log 3) = -\log 3$ and $x = (\log 3)/(\log 3 - \log 2) = \log_{3/2} 3 \approx 2.71$.

**17.** $9^{\log_3 4} = (3^2)^{\log_3 4} = 3^{2\log_3 4} = 3^{\log_3 16} = 16$.
$2^{\log_4 9} = 2^{(\log_2 9)/2} = (2^{\log_2 9})^{1/2} = 9^{1/2} = 3$. Both use
$a^{\log_a t} = t$ after matching bases.

**18.** Raise both to the $6^{\text{th}}$ power: $(\sqrt2)^6 = 2^3 = 8$ and
$(\sqrt[3]{3})^6 = 3^2 = 9$. Sixth powers preserve order for positive numbers, so
$\sqrt[3]{3} > \sqrt2$. The comparison $8$ versus $9$ is the whole content.

**19.** Set $x = y = 1$: $f(1) = 2f(1)$, so $f(1) = 0$. Then $f(8) = f(2^3) = 3f(2) = 3$.
From $f(2) + f(\tfrac12) = f(1) = 0$, $f(\tfrac12) = -1$. From $2f(\sqrt2) = f(2) = 1$,
$f(\sqrt2) = \tfrac12$. The property $f(xy) = f(x) + f(y)$ with $f(2) = 1$
characterizes $f = \log_2$.

**20.** $\log_{10}(2^{2025}) = 2025 \cdot 0.30103 \approx 609.59$, so $2^{2025}$ has
$\lfloor 609.59 \rfloor + 1 = 610$ digits. Writing $2025\log_{10}2 = 609 + 0.59\ldots$,
the integer part $609$ fixes the scale and the fractional part fixes the digits:
$2^{2025} = 10^{609} \cdot 10^{0.59}$ and $10^{0.59} \approx 3.9$, so the number is
about $3.9 \times 10^{609}$ and its leading digit is $3$. This is the scale/digit
split of §5.

**21.** Work outward. $\log_2(\cdot) = 0$ means the argument is $1$, so
$\log_3(\log_4 x) = 1$. Then $\log_4 x = 3$, so $x = 4^3 = 64$.

**22.** Use $1/\log_k N = \log_N k$ (the reciprocal of change of base). The sum
becomes $\log_N 2 + \log_N 3 + \cdots + \log_N 100 = \log_N(2 \cdot 3 \cdots 100) = \log_N(100!)$.
With $N = 100!$ this is $\log_{100!}(100!) = 1$.

</details>
