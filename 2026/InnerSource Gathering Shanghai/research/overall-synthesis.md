# AI & InnerSource Survey — Overall Synthesis

Twenty people answered, spanning a large European bank, a major Australian bank, a global energy
company, several German automotive and industrial firms, two Japanese electronics/heavy-industry
companies, a US telecom, a UK bank, three US financial services firms, a Chinese-owned AI research
group, an open source foundation, and a scattering of independent practitioners. That spread matters:
this isn't twenty variations on one industry's anxiety, it's the same handful of forces showing up
across wildly different regulatory environments, company sizes, and AI maturity levels. When that
many unrelated people converge on the same three or four observations without being prompted toward
them, the convergence is the finding.

## Where the data confirms the blog post, hard

The blog post's central claim is that AI does not shrink the problem InnerSource solves, it makes it
bigger and faster, because cheap code production means more duplication, not less. The survey does not
just agree with this; it hands you a live case. One respondent at a large enterprise software company
reported that a high-profile internal project *closed its source entirely* because it could not handle
the volume of AI-generated pull requests hitting it. Another respondent, from a large e-commerce
platform, gave the mechanism in a single sentence: a team found the exact capability they needed
already built and easily discoverable through AI-powered internal search, and duplicated it anyway,
because the review process for contributing back had become too slow to bother with. A banking
respondent put the psychology behind both stories into one line: "Why discover when I can create?" The
blog post predicted the trap. The field data shows people falling into it in real time, at real
companies, this year.

The review-bottleneck argument fares the same way. Nearly every respondent who engages with AI's
downside at all lands on some version of it independently: contribution volume is outrunning review
capacity, and that gap is where trust, ownership, and quality all start to erode. This wasn't in the
original blog post as a headline point, but it is the single most repeated observation in twenty
independent answers, which makes it the most defensible claim in the entire data set.

## Where it sharpens the argument

The blog post frames governance as the fix for AI-accelerated duplication. The e-commerce respondent's
story complicates that: in his case, governance tightened *in response to* AI risk, and that tightening
is exactly what pushed the team toward duplication instead of contribution. Heavier gates did not
protect InnerSource, they starved it. The honest version of the argument is not "add more governance,"
it's "match the shape of your governance to the speed of the thing it's governing" — under-govern and
review collapses under volume, over-govern and people route around you entirely. That's a sharper,
harder-to-dismiss point than the original essay makes, and it came from the field, not from theory.

## Where it genuinely extends the argument

The most interesting pattern in the whole data set doesn't appear in the blog post at all: several
respondents, independently, reframed the entire question from "source code" to "source of knowledge."
One respondent said it explicitly: the "Source" in InnerSource is evolving into a "Source of
Knowledge," with code as one subset of it. Two companies in the same industrial sector both described
AI's *only* current InnerSource win at their organization as helping structure and reuse documentation,
explicitly stating they don't yet use AI for code discovery at all. A third gave a number that makes
the point concrete: over 1,100 shared repositories and 1,600 Copilot users, and still less than 1% of
the company's actual engineering knowledge captured anywhere AI could reach it. Put together, this says
something the blog post doesn't: for a meaningful slice of the field, the AI-InnerSource story right
now isn't primarily about agents writing and reusing code at all. It's about whether the underlying
knowledge exists in a form AI (or a human) can find in the first place. Discovery tooling is useless
against knowledge that was never externalized. That's arguably the more urgent problem for most
organizations than anything about agent-generated pull requests.

## What surprised me most

The size and seriousness of the response. This was a cold ask ("a 2-minute favor") and multiple people
came back with multi-paragraph, structured, clearly-thought-through essays, several explicitly citing
public artifacts (a published AI governance playbook, a conference talk from 2025, a working
open-source discovery tool) to back their answers. That is not what a perfunctory favor looks like.
It suggests this question is genuinely live and unresolved for a lot of practitioners right now, which
is exactly the kind of energy a keynote room responds to.

The other surprise: how little disagreement there actually was on the diagnosis. Almost nobody argued
that AI is *not* straining review, trust, or governance. The disagreement, where it existed, was about
whether InnerSource-as-code-reuse or InnerSource-as-knowledge-reuse is the bigger current opportunity,
not about whether there's a problem at all.

## Open tensions worth taking on stage unresolved

1. **Governance is simultaneously the fix and, done wrong, a cause.** The data supports both "more
   InnerSource discipline is the answer" and "the specific governance response we're reaching for is
   backfiring." Naming that tension live, rather than resolving it into a tidy takeaway, is more honest
   than picking a side.
2. **Is the frontier code or knowledge?** The blog post bets on agents learning to discover and
   contribute code. A real slice of the field says the harder, more immediate problem is that most
   institutional knowledge was never captured anywhere an agent (or a person) could find it, and no
   amount of AI-powered search fixes an empty well. Worth asking the room which one they're actually
   fighting this year.
3. **What happens to trust when the contributor is an agent and the reviewer is overwhelmed?** One
   respondent's framing (governance as the last human judgment in a system where agents write, review,
   and read the code) is a genuinely unresolved question, not a rhetorical one. Nobody in the data set,
   including Russell's own blog post, has a clean answer for it yet.
