# Does AI-generated code carry a real, measurable maintenance cost?

Yes, and the strongest data traces the exact mechanism the talk needs: AI isn't just producing more
code, it's specifically producing more **duplicated** code and less **reused/refactored** code, and
that shift shows up as measurable downstream cost.

## The headline number

**GitClear's 2026 "Maintainability Gap" report** analyzed 623 million code changes from 2023 to 2026,
across 600M+ commits. Two numbers from it carry the talk's exact argument:

- **Code block duplication rose 81%** (40.3 to 73.0 duplicated blocks per million changed lines).
- **Refactored ("moved") code collapsed from 21% of changes in 2022 to 3.8% in 2026** — copy/paste is
  now roughly **5x more prevalent than refactoring**. That's the data-level version of "why discover
  when I can create."

Their prior report (211M lines, 2020-2024) found the same trend earlier and sharper: **an 8-fold
increase** in duplicated code blocks in 2024 alone, with 2024 the first year on record where
within-commit copy/paste exceeded genuinely moved/reused code. GitClear also cites academic research
(a Central China Normal University study) finding cloned code blocks carry **15-50% more defects** than
non-cloned code — duplication isn't cosmetic, it's a defect-rate multiplier.

**Caveat:** GitClear sells code-quality analytics, so their business model benefits from an "AI is
creating a maintainability crisis" narrative. The trend direction across two independent reports and a
cited academic source is credible; treat the exact percentages as directional rather than gospel.

## The independent, harder-to-dismiss data point

**Google's own 2024 DORA report** (State of DevOps) — a large-scale, non-vendor-interested source — found
that increased AI usage came with a **7.2% decrease in delivery stability**, even as it sped up code
review. This is the cleanest "the bill arrives later" evidence in the research: faster now, less stable
downstream, from the industry's own most-cited delivery-performance research.

## Who actually pays the maintenance bill

A 2025 empirical study (Xu, Medappa, Tunc, Vroegindeweij, Fransoo — arXiv 2510.10165) tracked
developers around Copilot adoption and found the burden doesn't distribute evenly: junior developers'
raw output rises, but **experienced developers' own code productivity fell 19%** while they ended up
**reviewing 6.5% more code** overall. The authors' own framing: productivity gains "mask the growing
burden of maintenance on a shrinking pool of experts." That's a precise, quotable version of "the
maintenance cost doesn't disappear, it just gets reassigned to whoever's left to catch it."

## Supporting color

- **Harness's State of Software Delivery 2025**: a majority of developers report spending *more* time
  debugging AI-generated code and *more* time resolving security vulnerabilities than before.
- **Info-Tech Research Group**: AI-generated code shows 1.7x more total issues than human-written code
  in production systems studied; maintainability-specific debt accounts for ~89% of AI-introduced
  issues. (Industry analyst report, not peer-reviewed — treat as directional.)

## The line for the talk

GitClear CEO Bill Harding's own framing is close to ready-made: "If developer productivity continues
being measured by commit count or lines added, AI-driven maintainability decay will proliferate." That
pairs cleanly with the duplicate-code beat — the team that duplicated instead of reused wasn't
irrational, they were optimizing for exactly the metric (shipped, today) that the data shows the whole
industry is currently over-rewarding, while the maintenance bill compounds somewhere else, for someone
else, later.
