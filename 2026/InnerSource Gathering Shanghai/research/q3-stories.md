# What concrete stories did respondents share about AI meeting InnerSource?

Twenty people answered the survey's third question, asking for one real story of AI meeting
InnerSource at their company. The stories cluster into four groups, and they're uneven in how much
new ground they cover.

## Discovery and knowledge crawlers — the strongest, most repeated pattern

The single most common story type is a system that turns scattered internal repositories into a
queryable knowledge layer. A Japanese industrial conglomerate presented one at InnerSource Summit
2025: a crawler that aggregated content from thousands of repositories across its GitHub Enterprise
into a single index that Copilot could query, deliberately shifting discovery from "find and read
the right repository" to "ask a question and get an answer that spans repositories." A European
enterprise software company described an internal marketplace where people contribute reusable
agent skills and MCP servers, calling it early but "becoming very popular." The clearest public
example is Shell's **Project Fleming** (projectfleming.tech), which its representative was explicit
about wanting named. Project Fleming solves the same problem standard search always had for
InnerSource: search is too literal, and it can't find code that's merely *adjacent* to what you
need. AI search can.

This cluster is real validation of a load-bearing claim in the existing blog post, but it isn't new
by itself. What's new is the second Japanese respondent's reframe: he argues "the 'Source' in
InnerSource is evolving into a 'Source of Knowledge,'" with code as one subset of a broader thing
being discovered and reused. That's a genuinely stage-worthy idea, not just a confirming anecdote,
because it reframes what InnerSource is *for* in an AI-native org rather than just describing a new
tool.

## Succession and tribal-knowledge capture — small but sharp

One respondent, running a smaller company's codebase, described a "benevolent dictator" maintainer
who had carried the project's architecture knowledge for years and wanted to retire. The team
dumped his accumulated conversations and guidance into documents, and now AI serves as the first
tier of answers about that architecture, letting him actually step away. This is a small story but
a sharp one: it's a case where AI didn't just help write code, it preserved and redistributed a
single person's irreplaceable context so the project could survive their departure. Worth using as
a human moment in the talk, not a system-architecture one.

## Cautionary tales — the sharpest new material

Two stories directly undercut the optimistic discovery narrative and deserve the most stage time.
An anonymous respondent at a large Latin American e-commerce company described a team that needed a
capability that AI tooling had already surfaced as existing elsewhere in the org, and *still* chose
to have AI regenerate a duplicate from scratch, because the review process for contributing back had
become so bureaucratic that duplication was cheaper than compliance. A US financial services
respondent described a real OTEL telemetry migration where AI-assisted cross-team contributions
landed with real quality problems, and the receiving team couldn't even fix them because they lacked
the context and couldn't run the project locally. Both are concrete, both are recent, and both are
exactly the "the trap is already happening" evidence the existing argument needs. These are the two
best candidates for a stage story in the whole set.

## What's genuinely new versus confirming

The discovery/crawler stories confirm the thesis; they're good color but not surprising. The
"source of knowledge" reframe, the succession story, and especially the two duplication/review
cautionary tales are the material that would make an audience sit up, because they show the failure
mode already playing out with real consequences, not as a hypothetical.
