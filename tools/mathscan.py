#!/usr/bin/env python3
"""Scan Markdown for GitHub-MathJax rendering hazards."""
import re, sys

OPEN_OK_BEFORE = set(' \t([{>—-–/~*_')      # chars allowed immediately before an opening $
CLOSE_OK_AFTER = set(' \t)]}.,;:?!—-–/~*_\n')  # chars allowed immediately after a closing $

def scan(path):
    src = open(path).read()
    lines = src.split('\n')
    issues = []

    # ---- mask fenced code blocks and inline code, but track positions per line ----
    # Build a per-line "masked" copy where inline code and display math are blanked,
    # so inline-$ detection doesn't trip on them.
    masked = list(lines)
    in_fence = False
    in_display = False            # multi-line $$ block
    display_open_line = None
    for i, ln in enumerate(lines):
        stripped = ln.lstrip('> ').strip()
        if stripped.startswith('```'):
            in_fence = not in_fence
            masked[i] = ''
            continue
        if in_fence:
            masked[i] = ''
            continue
        # inline code spans -> blank them
        masked[i] = re.sub(r'`[^`]*`', lambda m: ' '*len(m.group()), masked[i])
        # escaped \$ (literal dollar in prose) -> not a delimiter
        masked[i] = masked[i].replace('\\$', '\x01\x01')

    # ---- 1. \tag and \dfrac ----
    for i, ln in enumerate(lines):
        if '\\tag' in ln:
            issues.append((i+1, 'TAG', ln.strip()))
        if '\\dfrac' in ln:
            issues.append((i+1, 'DFRAC(inline-overflow risk)', ln.strip()))

    # ---- 2. display $$ blocks: blank line before & after ----
    # find lines that contain $$ ; classify open/close
    # A line may be a self-contained "$$ ... $$" or an opener/closer.
    i = 0
    def ctx_blank(idx):
        if idx < 0 or idx >= len(lines): return True   # file edge counts as blank
        return lines[idx].lstrip('> ').strip() == ''
    while i < len(lines):
        ln = lines[i]
        cnt = ln.count('$$')
        if cnt == 0:
            i += 1; continue
        if cnt >= 2:
            # self-contained display on one line
            if not ctx_blank(i-1):
                issues.append((i+1, 'DISPLAY no blank BEFORE', ln.strip()))
            if not ctx_blank(i+1):
                issues.append((i+1, 'DISPLAY no blank AFTER', ln.strip()))
            i += 1; continue
        # cnt == 1 -> opener; find closer
        j = i+1
        while j < len(lines) and lines[j].count('$$') == 0:
            j += 1
        if j < len(lines):
            if not ctx_blank(i-1):
                issues.append((i+1, 'DISPLAY no blank BEFORE', ln.strip()))
            if not ctx_blank(j+1):
                issues.append((j+1, 'DISPLAY no blank AFTER', lines[j].strip()))
            i = j+1
        else:
            issues.append((i+1, 'DISPLAY unmatched $$', ln.strip()))
            i += 1

    # ---- 3. inline $...$ adjacency + odd-dollar, on masked lines with $$ removed ----
    for i, ln in enumerate(masked):
        # remove $$...$$ (inline display) and lone $$ from consideration
        work = ln.replace('$$', '\x00\x00')
        # count single dollars
        singles = [m.start() for m in re.finditer(r'(?<!\x00)\$(?!\x00)', work)]
        if len(singles) % 2 == 1:
            issues.append((i+1, 'ODD number of $ on line', lines[i].strip()))
        # pair them up and check adjacency
        for k in range(0, len(singles)-1, 2):
            o = singles[k]; c = singles[k+1]
            before = work[o-1] if o-1 >= 0 else ' '
            after_open = work[o+1] if o+1 < len(work) else ' '
            before_close = work[c-1] if c-1 >= 0 else ' '
            after = work[c+1] if c+1 < len(work) else ' '
            if before not in OPEN_OK_BEFORE:
                issues.append((i+1, f'OPEN $ preceded by {before!r}', lines[i].strip()))
            if after_open == ' ':
                issues.append((i+1, 'OPEN $ followed by space', lines[i].strip()))
            if before_close == ' ':
                issues.append((i+1, 'CLOSE $ preceded by space', lines[i].strip()))
            if after not in CLOSE_OK_AFTER:
                issues.append((i+1, f'CLOSE $ followed by {after!r}', lines[i].strip()))

    # ---- 4. math inside emphasis ----
    for i, ln in enumerate(masked):
        # ** bold ** containing $
        for m in re.finditer(r'\*\*[^*]+\*\*', ln):
            if '$' in m.group():
                issues.append((i+1, 'MATH inside **bold**', lines[i].strip()))
        # * italic * containing $  (avoid ** by requiring non-* neighbours)
        for m in re.finditer(r'(?<!\*)\*(?!\*)([^*]+?)\*(?!\*)', ln):
            if '$' in m.group(1):
                issues.append((i+1, 'MATH inside *italics*', lines[i].strip()))
        # _ italic _ containing $
        for m in re.finditer(r'(?<!\w)_([^_]+)_(?!\w)', ln):
            if '$' in m.group(1):
                issues.append((i+1, 'MATH inside _italics_', lines[i].strip()))

    return issues

total = 0
for path in sys.argv[1:]:
    iss = scan(path)
    if iss:
        print(f'\n### {path}')
        for lineno, kind, txt in iss:
            print(f'  L{lineno:<4} [{kind}]  {txt[:90]}')
        total += len(iss)
print(f'\nTOTAL ISSUES: {total}')
