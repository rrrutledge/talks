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
  * Thank Jerry Tan and the InnerSource China Community for the invitation
  * APAC opening hook - a real, reciprocal relationship, not a courtesy:
    last year Jerry invited me to give a video keynote to InnerSource Gathering Beijing 2025;
    this year I'm glad to be back with you for the Shanghai Gathering - joining remotely, but very much with you.
    I'll say it plainly: I'm proud of what the InnerSource China Community has built, and I feel a genuine
    affinity for this community.
    And this region hasn't been on the edge of the InnerSource movement - it's been near the center of it for years:
    in ISC's own audience data, Japan is consistently our number-one or number-two country for engagement,
    trading the top spot with the United States month to month and sitting well ahead of anywhere else, and our
    Japanese-language material is some of the most-read content we publish anywhere.
    * NEEDS RUSSELL / to check with Jerry: does emphasizing Japan and activity elsewhere in Asia land with a
      China audience, or is Japan no more relevant to them than any other region? If the latter, lean the hook
      on the China-community relationship above plus the global picture, and hold the Japan data for the body.
  * Frame the two halves: a global ISC update, then how AI is reshaping InnerSource

* Part 1: Global update on InnerSource Commons, ED vantage (~6 min) - **first pass drafted; see `research/part1-research.md` for sources**
  * Where the movement stands today
    * InnerSource has moved from a promising practice to a core strategy for how large enterprises build
      software together - and the community around it keeps compounding. One clean line: our LinkedIn
      following is up roughly 30-fold over the life of the Foundation and still growing about 15% year over
      year - our fastest-growing channel by far.
    * It's a genuinely global movement, and this region is out in front rather than catching up: in ISC's own
      audience data, Japan is consistently our number-one or number-two country for engagement - trading the top
      spot with the United States month to month, and well ahead of everyone else, with Germany, the UK, and
      India rounding out the leading set - and our Japanese-language content is among the most-read we publish.
    * And the community's own bench reflects that: ISC Foundation membership is individual and merit-based (you
      are elected in, the way Apache does it), and the APAC contingent is deep. Chen Wei, Senior Project
      Director of Huawei's InnerSource Office, presented "Huawei InnerSource Culture and Value Closed-Loop
      Practice" at our 2025 Summit in Yokohama; Shingo Oidate, who runs Mitsubishi Electric's Open Source
      Program Office, was elected a Foundation Member just this month (September 2026). They join a strong
      APAC roster of members - Jerry Tan (InnerSource China Community), Yuki Hattori (Japan), Yoshitake
      Kobayashi (Toshiba), Ada Dai (Tencent), Willem Jiang (Huawei), and others - so this region isn't just
      consuming InnerSource, it's helping lead the Foundation.
    * The most recent State of InnerSource report (2025, roughly 120 organizations surveyed) shows why it
      spreads: the top reasons orgs adopt are code reuse (84%), development speed (81%), knowledge sharing
      (79%), and breaking down silos (77%) - and formal InnerSource programs or program offices now exist at
      about a third of surveyed orgs, with another third running informally.
  * Three patterns emerging across large-org InnerSource journeys (lead with consolidation, then the other two)
    * Pattern 1 (lead) - consolidation: InnerSource is increasingly funded and
      housed alongside a partner function rather than as a standalone line item. As budgets tighten and AI
      reshapes where engineering money and effort go, InnerSource more and more sits with a related group - an
      OSPO, a developer-experience team, or a platform-engineering org. Those are natural partners; they share
      InnerSource's cross-team, reuse-first instincts. The thing to get right is scope: a host function tends
      to fund InnerSource for what helps its own remit, and the whole premise of InnerSource is that it has to
      serve *every* team, not just the one paying for it. The programs that land this well fund InnerSource
      through a partner function while keeping its mandate company-wide.
    * Pattern 2 - scaffolding beats enthusiasm. What separates programs that scale from ones that
      stall isn't grassroots energy, it's concrete scaffolding: consistent tooling and process, clear
      contribution guidelines, a discoverability or portal layer, and explicit governance. The 2025 survey
      shows the gap plainly - about 86% run shared repositories, but only about 60% have InnerSource
      documentation, and portals, training, and metrics lag further behind. Adoption is running ahead of
      operational maturity.
    * Pattern 3 - InnerSource is becoming the substrate for AI-native development. The community
      increasingly frames InnerSource less as a nice-to-have and more as essential infrastructure for building
      well with AI: shared prompts and context, collaboratively built internal AI tooling, and well-structured
      internal code that agents can actually find and reuse. (ISC's current thesis and the natural bridge into
      Part 2 - frame it as where the community is heading, not a settled survey finding.)
  * What ISC is investing in next
    * The 2026 Summit is the flagship, and it's built for exactly this room: a single continuous 22-hour
      "follow-the-sun" virtual event on November 12, 2026, opening in APAC before handing off to EMEA and then
      the Americas - your region kicks off the global day. Theme: "InnerSource in Motion: Navigating the
      Shifting Tides," across three tracks - Cultural Elasticity, Follow-the-Sun Collaboration, and the
      Evolving Developer Experience - with AI running through all of them. (Scott Hanselman is a confirmed
      keynote.)
    * Beyond the Summit, the community is actively building: a new public InnerSource Pattern for keeping
      AI-generated code aligned with a project's own conventions, and standing peer working groups for
      InnerSource practice and for program offices.
    * And the direction is toward getting back in the room together. We ran in-person Summits before the
      pandemic, went virtual through it, and returned to in person last year in Yokohama; the aim for 2027 is
      more regular in-person regional events, including a presence here in this region. And alongside the
      events, we're investing in greater curation - focusing each gathering on the topics that actually matter
      to the companies in the room, so that hard-won InnerSource knowledge spreads across the world as fast as
      possible.
  * Challenges leaders should prepare for - grounded in the 2025 survey; lead with both, in this order - time and resources first, then ROI
    * The number-one blocker is no longer culture - it's time. For the first time, "lack of time and resources"
      (84%) overtook organizational culture and silo thinking (74%) as the top perceived blocker. The
      supporting numbers are stark: only about 22% of orgs give employees time to contribute, about 15% reward
      contributions, and about 14% factor InnerSource into promotion. People are convinced; they just have no
      room to act on it.
    * The value is obvious; the investment isn't. Leaders endorse InnerSource and then under-fund it, largely
      because it's hard to measure: fewer than half of orgs measure InnerSource at all, and the methods that do
      exist are immature - manual tracking, surveys, basic portal metrics. Without a credible ROI story,
      programs stall - roughly 1 in 7 were ramping down in 2025. The encouraging part is that the community is
      building the answer: Chamindra de Silva (Citi, who leads the FINOS InnerSource SIG) and Daniel Izquierdo
      (Bitergia) have put real rigor into quantifying it, in their work on the business impact of InnerSource
      and how to measure it - the credible ROI reference this challenge has been missing, worth pointing the
      room to.
    * (Optional third) The remaining blockers are structural and human, not technical: awareness gaps, missing
      executive sponsorship, and - tellingly - missing middle-manager support, which is the exact layer that
      decides whether an engineer actually has the time the first challenge is about.
  * Bridge into Part 2: every one of these - the patterns, the investments, the challenges - now runs into a
    single question the whole community is asking at once. What does AI do to all of it? That's the second half.

* Part 2: How AI is reshaping InnerSource (~6 min) - **drafted, full spoken text in `part2-spoken-draft.md`**
  * The myth, named directly: InnerSource existed because writing code was expensive - if AI makes writing code nearly free, doesn't that quietly end the argument for InnerSource? State it plainly before rebutting it.
  * The rebuttal: AI collapses the cost of code that compiles, not the cost of code that's correct. Cheap code means more of it - including duplication. The myth mistakes "cheap to write" for "cheap, full stop."
  * The trap is already happening, in the source's own words: a real story of a team that chose to duplicate a capability their own AI tooling had already surfaced elsewhere in the company, rather than navigate review friction to reuse it. Direct anonymized quotes: "the friction of contributing back felt too high," and "raw AI efficiency can inadvertently bypass and starve out collaboration loops if governance isn't adapted to match the speed."
    * Was the team's call actually wrong, in the moment, under deadline pressure? Probably not - which is what makes the next point land.
  * Why this actually matters - two precise costs, stated explicitly: (1) token cost - an agent re-deriving something that already exists burns real compute, and that compounds across every team, every sprint; (2) correctness - the original component earned years of hardening (edge cases, security patches, outages) that a duplicate starts back at zero on, no matter how confident it looks on day one.
    * Backed by general (non-anecdotal) data: a large-scale code-change analysis found duplicated code blocks up 81% while refactored/reused code collapsed from 21% to 3.8% of all changes over three years; Google's own DORA research found increased AI usage paired with a measurable drop in delivery stability.
  * Where it's breaking things: review capacity is the near-universal strain across the community I surveyed. Zoom out to curl - one of the most widely used pieces of software on Earth - where AI-assisted security reports hit roughly a fifth of all submissions while genuine vulnerabilities fell to about a twentieth, zero AI-generated reports found a real vulnerability across six years, and the bug bounty program was shut down entirely in January 2026.
  * What actually helps: automation as a force multiplier for a human's attention (one team's agent pipeline authored 25-35% of merged PRs and closed 70-80% of incoming issues by doing reproduction and verification before a human decided) - not as a replacement for judgment (one open source project's AI-reviewer trial found half its output noise, and turned it off; two-thirds of engineers surveyed won't merge on an AI review alone).
  * Bridge: the real frontier is teaching agents themselves the InnerSource habit - search before you build, reuse the shared piece, push back what's genuinely new and generic. Real examples already exist without anyone calling it InnerSource: a shared-spec pattern where one team owns requirements and others consume them read-only, right where their coding agent can read them; Shell's own Project Fleming, an AI-powered discovery layer finding code that's merely adjacent to what you asked for. Two of three legs - reuse, publish-back - are already shipping in the wild. The third leg, agents that search before they build, is still wide open. (Note: this bridge material - agents InnerSourcing on their own, better review agents - echoes what's coming at Summit 2026; worth a light touch here rather than fully mining it.)

* Close: what comes next (~2 min) - **first pass drafted**
  * Bridge straight off Part 2's closing point - agents that search before they build is the frontier still wide
    open. That's the real evolution: the "Source" in InnerSource is becoming a "Source of Knowledge" - not just
    code, but the context, patterns, and decisions a team accumulates, which is exactly the substrate agents
    need too. Several community members have converged on this framing independently, unprompted - it isn't
    just my read.
    * NEEDS RUSSELL: does "Source of Knowledge" still feel right as the closing image, or is there a better
      way you'd put it?
  * The two things to leave the room with (pulled from the outline's own Takeaways, picking the two that carry
    furthest past the talk):
    1. InnerSource isn't obsolete in the AI era - AI makes the problem InnerSource solves bigger and faster,
       not smaller.
    2. The next frontier isn't managing the flood, it's teaching AI agents themselves the InnerSource habit:
       search before building, reuse, and contribute back.
    * NEEDS RUSSELL: are these the right two to leave the room with, or would you swap in one of the other two
      Takeaways (the maintenance-cost-arrives-later point, or the review-capacity-bottleneck point)?
  * Where to go next: the ISC site, and Summit 2026 - November 12, follow-the-sun, APAC opens the global day
  * Thank you - echo the opening: thank Jerry Tan and the InnerSource China Community again

# References

Part 1 (the global update) is grounded in ISC's own Foundation data and in published, citable sources - the
State of InnerSource 2024/2025 reports, ISC community-call topics, and the public Summit 2026 announcements.
For the ROI/measurement challenge it points to Chamindra de Silva and Daniel Izquierdo's
[The Business Impact of Inner Source and How to Quantify It](https://www.researchgate.net/publication/372758825_The_Business_Impact_of_Inner_Source_and_How_to_Quantify_It).
`research/part1-research.md` records what backs each claim and where it came from, and flags what was
generalized to keep out of this public repo (internal analytics figures, unannounced plans, and any
company named only in a not-yet-public source) - the same anonymization judgment Part 2's survey material
required.

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
