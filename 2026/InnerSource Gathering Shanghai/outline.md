# Title

InnerSource in the AI Era: A Global Update and What Comes Next

# Target Audience

Attendees of InnerSource Gathering Shanghai 2026 (Sept 21-22), hosted by the InnerSource China
Community - engineering leaders and practitioners across large enterprises in China/APAC running or
exploring InnerSource programs, many already grappling with AI's effect on internal collaboration and
code review.

# Takeaways

* InnerSource isn't obsolete in the AI era - AI makes the problem InnerSource solves bigger and faster, not smaller.
* The maintenance cost of AI-enabled duplication doesn't disappear, it arrives later, and that's the real price.
* Review capacity, not code generation, is the actual bottleneck - and open source is already living this crisis in public, with no consensus answer yet.
* The next frontier isn't managing the flood, it's teaching AI agents themselves the InnerSource habit: search before building, reuse, and contribute back.

# Time

15 minutes

# Abstract

InnerSource has moved from a promising practice to a core strategy for how large enterprises build
software together. In this keynote, Russell Rutledge, Executive Director of InnerSource Commons, shares
a global view of where the InnerSource movement stands today and where it's headed. That includes the
patterns emerging across the world's largest engineering organizations, what the InnerSource Commons
community is investing in next, and the challenges leaders should prepare for. He then turns to how AI
is reshaping InnerSource. Drawing on what he's seeing across the community, Russell explores how AI is
changing the way teams share code, discover work, and collaborate across internal boundaries. That
includes where it accelerates InnerSource, where it disrupts long-held assumptions, and what it means
for the governance, culture, and tooling that make InnerSource work. Attendees will leave with a
concrete view of what's next and practical guidance for leading InnerSource in an AI-driven era.

# Outline

* Open (~1 min)
  * Thank Jerry Tan / InnerSource China Community for the invitation
  * Frame the two halves: a global ISC update, then how AI is reshaping InnerSource
  * TBD: an APAC-specific opening hook

* Part 1: Global update on InnerSource Commons, ED vantage (~6 min) - **not yet drafted**
  * Where the movement stands today (TBD: a current stat, ideally APAC-relevant)
  * 2-3 patterns emerging across large-org InnerSource journeys (TBD)
  * What ISC is investing in next - Summit 2026 confirmed; anything else? (TBD)
  * Challenges leaders should prepare for (TBD)

* Part 2: How AI is reshaping InnerSource (~6 min) - **drafted, full spoken text in `research/`**
  * Reframe the thesis: AI doesn't shrink InnerSource's problem, it makes it bigger and faster - cheap-to-write code isn't cheap-to-maintain code.
  * The trap is already happening: a real story of a team that chose to duplicate a capability their own AI tooling had already surfaced elsewhere in the company, rather than navigate review friction to reuse it.
    * The local call may have been rational under deadline pressure - but the duplicate inherits a maintenance cost the original component had already earned through years of hardening.
    * Backed by general (non-anecdotal) data: a large-scale code-change analysis found duplicated code blocks up 81% while refactored/reused code collapsed from 21% to 3.8% of all changes over three years; Google's own DORA research found increased AI usage paired with a measurable drop in delivery stability.
  * Where it's breaking things: review capacity is the near-universal strain across the community I surveyed. Zoom out to curl - one of the most widely used pieces of software on Earth - where AI-assisted security reports hit roughly a fifth of all submissions while genuine vulnerabilities fell to about a twentieth, zero AI-generated reports found a real vulnerability across six years, and the bug bounty program was shut down entirely in January 2026.
  * What actually helps: automation as a force multiplier for a human's attention (one team's agent pipeline authored 25-35% of merged PRs and closed 70-80% of incoming issues by doing reproduction and verification before a human decided) - not as a replacement for judgment (one open source project's AI-reviewer trial found half its output noise, and turned it off; two-thirds of engineers surveyed won't merge on an AI review alone).
  * Bridge: the real frontier is teaching agents themselves the InnerSource habit - search before you build, reuse the shared piece, push back what's genuinely new and generic. Real examples already exist without anyone calling it InnerSource: a shared-spec pattern where one team owns requirements and others consume them read-only, right where their coding agent can read them; Shell's own Project Fleming, an AI-powered discovery layer finding code that's merely adjacent to what you asked for. Two of three legs - reuse, publish-back - are already shipping in the wild. The third leg, agents that search before they build, is still wide open.

* Close: what comes next (~2 min) - **not yet drafted**
  * Candidate idea: "the 'Source' in InnerSource is evolving into a 'Source of Knowledge'" - several community members converged on this independently, unprompted
  * TBD: the 1-2 concrete takeaways I want the room to leave with
  * Where to go next (ISC site, Summit 2026)
  * Thank you

# References

Part 2 is grounded in two research tracks - a short community survey I ran ahead of this talk (20
practitioners, three questions, responses anonymized per each respondent's stated preference - see
`research/`), and public data on AI's effect on code maintainability and open source review capacity.

**Public sources, safe to cite directly:**
* [Project Fleming](https://projectfleming.tech) - Shell's public AI-powered InnerSource discovery tool
* [OpenSpec](https://github.com/Fission-AI/OpenSpec) - spec-driven agent workflow with a "Stores" feature that mirrors InnerSource reuse
* [Matt Pocock's skills repo](https://github.com/mattpocock/skills) - ~48k-star public example of packaged, reusable engineering expertise for coding agents
* ["PR Not Welcome" (Latent Space)](https://www.latent.space/p/pr-not-welcome) - on agent-assisted PR triage in open source
* GitClear's code-quality research (duplication/refactoring trend data across 600M+ commits, 2023-2026)
* Google's 2024 DORA (State of DevOps) report - AI usage vs. delivery stability
* Daniel Stenberg / curl's public commentary on AI-assisted bug bounty submissions and the January 2026 program shutdown

**My own research, anonymized, in `research/`:**
* `q1-discovery.md`, `q2-strain.md`, `q3-stories.md`, `overall-synthesis.md` - synthesis of the 20-response community survey (raw responses withheld; several respondents required Chatham House / no-attribution terms, so quotes here are attributed by role/company-type only, never by name or employer, with one respondent's explicit exception noted)
* `oss-comparison.md` - how the open source community's own AI-contribution reckoning compares to what the survey shows
* `oss-automated-review.md` - whether automated/AI-assisted code review is actually helping open source with the review-capacity problem
* `ai-code-maintenance-cost.md` - general, non-anecdotal data backing the "duplication's real cost arrives later" point in beat 2
