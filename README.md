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
├── chapters/
│   ├── _TEMPLATE.md          # copy this to start a new chapter
│   └── 01-quadratic-functions.md
└── ...
```

Each chapter is a single Markdown file in `chapters/`, prefixed with a two-digit
number for ordering. Math is written in LaTeX between `$...$` (inline) and
`$$...$$` (display), which renders on GitHub and in most Markdown viewers.

## Chapter format

Every chapter follows the same skeleton (see `chapters/_TEMPLATE.md`):

1. **Overview** — what the topic is and why it matters.
2. **Prerequisites** — links to chapters the reader should know first.
3. **Exposition** — the theory, built up in numbered sections with examples.
4. **Summary** — key formulas and facts in one place.
5. **Exercises** — grouped by difficulty (warm-up → standard → challenge).
6. **Solutions** — full worked answers, collapsed so readers can try first.

## Index of chapters

| # | Chapter | Status |
|---|---------|--------|
| 01 | [Quadratic Functions](chapters/01-quadratic-functions.md) | needs revision — predates PHILOSOPHY.md |

## Contributing a chapter

1. Copy `chapters/_TEMPLATE.md` to `chapters/NN-your-topic.md`.
2. Fill in each section, keeping exposition and exercises in sync.
3. Add a row to the index table above.
