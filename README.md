# Math Topics

A collection of self-contained chapters on high school mathematics, written for a
mathematically mature audience. Each chapter presents the theory ("exposition")
as a coherent essay and then a graded set of exercises with worked solutions.

**Before writing or revising anything, read [PHILOSOPHY.md](PHILOSOPHY.md).** It
defines the audience, the purpose, and the standard of exposition (Courant,
Kolmogorov, AoPS) that every chapter is held to.

## Structure

```
math-topics/
├── README.md
├── PHILOSOPHY.md             # the measuring stick — read before writing
├── chapters/
│   ├── _TEMPLATE.md          # copy this to start a new chapter
│   ├── 01-exponents-and-logarithms.md
│   └── 03-quadratic-functions.md
└── ...
```

Each chapter is a single Markdown file in `chapters/`, prefixed with a two-digit
number for ordering. Math is written in LaTeX between `$...$` (inline) and
`$$...$$` (display), which renders on GitHub and in most Markdown viewers.

> **GitHub math gotchas.** GitHub's MathJax rendering has two traps that silently
> dump raw LaTeX instead of rendering:
>
> 1. **Display blocks need blank lines around them.** A `$$ … $$` block must have
>    a blank line *before and after* it (and, inside a blockquote or list, a `>`
>    or indented blank line), or GitHub fuses it into the surrounding paragraph
>    and won't render it. Inline `$…$` does not need this.
> 2. **No `\tag{…}`.** It is unsupported; put the label inside the math as text,
>    e.g. `$$ a^m a^n = a^{m+n}. \qquad \text{(L1)} $$`.
> 3. **A closing `$` may not touch a letter.** `$n$th` fails to render (the `t`
>    abuts the `$`); a hyphen or space is fine (`$x$-axis` works). For ordinals,
>    fold the suffix into the math: `$n^{\text{th}}$`, `$6^{\text{th}}$`.

## Chapter format

Every chapter follows the same skeleton (see `chapters/_TEMPLATE.md`):

1. **Overview** — what the topic is and why it matters.
2. **Prerequisites** — links to chapters the reader should know first.
3. **Exposition** — the theory, built up in numbered sections with examples.
4. **Summary** — key formulas and facts in one place.
5. **Exercises** — grouped by difficulty (warm-up → standard → challenge).
6. **Solutions** — full worked answers, collapsed so readers can try first.

## Roadmap

Chapters are organized around big ideas in three strands rather than a single
school syllabus. Numbering is provisional and easily re-sequenced.

**Strand A — The Algebra of Structure**

| # | Chapter | Status |
|---|---------|--------|
| 01 | [Exponents & Logarithms](chapters/01-exponents-and-logarithms.md) | draft (reference chapter) |
| 02 | Polynomials & Factoring | planned |
| 03 | [Quadratic Functions](chapters/03-quadratic-functions.md) | needs revision — predates PHILOSOPHY.md |
| 04 | Functions, Graphs & Transformations | planned |
| 05 | Sequences, Series & Induction | planned |
| 06 | Inequalities & Means (AM–GM) | planned |

**Strand B — Number & Counting** (AMC core)

| # | Chapter | Status |
|---|---------|--------|
| 07 | Divisibility & Modular Arithmetic | planned |
| 08 | Combinatorics: the Art of Counting | planned |
| 09 | Probability & Expectation | planned |

**Strand C — Geometry meets Algebra**

| # | Chapter | Status |
|---|---------|--------|
| 10 | Coordinate Geometry | planned |
| 11 | Trigonometry & the Unit Circle | planned |
| 12 | Complex Numbers | planned |

## Contributing a chapter

1. Copy `chapters/_TEMPLATE.md` to `chapters/NN-your-topic.md`.
2. Fill in each section, keeping exposition and exercises in sync.
3. Add a row to the index table above.
