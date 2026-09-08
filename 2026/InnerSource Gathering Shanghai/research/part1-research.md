# Part 1 research - global InnerSource Commons update

Part 1 (the global ISC update) is grounded in the Foundation's own data and in published, citable sources.
This note records what backs each claim in the Part 1 outline and where it came from, and flags what was
generalized to keep out of this public repo - the same judgment Part 2's survey material required.

## Where the movement stands today

* **Community growth.**
  ISC's LinkedIn following is up roughly 30-fold over the Foundation's life (from about 92 in 2020 to ~2,700
  in mid-2026), still growing about 15% year over year, and is the fastest-growing of ISC's channels. Per
  Russell's steer, the outline cites this as percentages/multiples only - the small absolute follower counts
  land as less impressive than the growth rate, so they are kept out of the spoken framing. YouTube and
  X/Twitter grew far more slowly, and X was flat-to-negative through 2025, so LinkedIn is the clean line.
  Source: ISC's own marketing-metrics tracking; the follower counts themselves are publicly visible on the
  profiles.
* **APAC is out in front (Japan is the standout).**
  In ISC's own web-search analytics, Japan trades the number-one country spot with the United States month to
  month and sits well ahead of everyone else; through most of late 2025 Japan was clearly #1, peaking around
  490 monthly search clicks in November 2025 against roughly 190 for the US. In the two most recent months
  (mid-2026) the US is nominally back on top by a narrow margin (about 149 to Japan's 95 in July 2026), but the
  multi-year pattern is a clear Japan/US lead pair. Germany, the UK, and India round out the top five; India
  appears in the leading set but is usually #4-5, not top-two - so the headline claim is about Japan, not
  "Japan and India." ISC's Japanese-language pages (the `/ja/` homepage, the Japanese Patterns book, the Tokyo
  gathering pages) recur among the top-performing pages, and Japanese-language search queries recur among the
  top growing queries. APAC engagement is long-standing (an APAC-region Summit ran as far back as 2020).
  The exact monthly figures are internal analytics; the committed outline uses only the qualitative pattern.
  Open question (Russell to check with Jerry Tan): whether a China audience finds Japan/other-Asia activity
  compelling, or whether Japan carries no more weight for them than any other region. If the latter, the hook
  should lean on Russell's relationship with the China InnerSource Community plus the global picture, and the
  Japan data should sit in the body rather than the opening. Flagged NEEDS RUSSELL in the Open.
* **APAC adoption and the Huawei talk.**
  Chen Wei (family name Chen; credited by ISC as "Chenwei"), Senior Project Director of Huawei's InnerSource
  Office, presented **"Huawei InnerSource Culture and Value Closed-Loop Practice"** in person at ISC's 2025
  Summit in Yokohama, Japan on Nov 13, 2025 - a public, delivered talk. Many of the region's largest
  engineering organizations also appear on ISC's public list of companies practicing InnerSource.
  Kept out of this repo: Chen Wei's personal and `@huawei.com` email addresses, and an internal ISC legal
  discussion about Huawei sponsorship under US sanctions (unrelated and sensitive).
* **APAC membership - individual and merit-based (not organizational).**
  ISC Foundation membership works like Apache: individuals are elected in on merit; there is no "organizational
  membership," so the accurate framing is "Shingo Oidate was elected a Foundation Member," never "Mitsubishi
  Electric joined." Shingo Oidate (追立 真吾, Oidate Shingo), General Manager of Mitsubishi Electric's Open
  Source Program Office, was elected a Foundation Member in the public September 2026 announcement
  (innersourcecommons.org/about/announcements/2026-09-new-members/); Frédéric Sicot Mouret of Airbus's OSPO
  was elected in the same announcement. Verified APAC-based Foundation Members include Jerry Tan (China / the
  InnerSource China Community), Yuki Hattori (GitHub, Japan; ISC's immediate-past President), Yoshitake
  Kobayashi (Toshiba, Japan), Ada Dai (Tencent, China), Willem Jiang (Huawei, China), Shingo Oidate
  (Mitsubishi Electric, Japan), and Mishari Muqbil (Zymple, Thailand), among others.
  Governance corrections to avoid a stage error: Micaela Eller (EY) is the current President (not Yuki
  Hattori); Jerry Tan is a Foundation Member and community leader, not a board director. The members page,
  board page, and new-member announcement are all public.
* **Adoption reasons and program maturity.**
  State of InnerSource 2025 (published report, roughly 120 organizations surveyed, foreword by ISC President
  Yuki Hattori): top adoption drivers are code reuse (84%), development speed (81%), knowledge sharing (79%),
  and breaking down silos (77%); formal InnerSource programs or program offices exist at about 35% of orgs,
  with another ~29% running informally.

## Patterns across large-org journeys

Russell confirmed all three as the set to use, led by consolidation (his own observation), then scaffolding,
then the AI-native substrate. The latter two were drawn from the survey and community-call themes.

* **Pattern 1 - consolidation (Russell's own read; lead).**
  As budgets tighten and AI reshapes where engineering money and effort go, InnerSource is increasingly funded
  and housed alongside a partner function - an OSPO, a developer-experience team, or a platform-engineering
  group - rather than as a standalone line item. Those are natural partners (shared cross-team, reuse-first
  instincts); the risk to manage is that a host function funds InnerSource only for what serves its own remit,
  when InnerSource has to serve every team. This is Russell's direct ED observation, not a survey finding, and
  it subsumes the earlier "OSPO-led enablement" candidate (the OSPO becomes one of the partner functions). It
  is told generically, with no company named.
* **Pattern 2 - scaffolding over spontaneity.**
  What lets programs scale is concrete scaffolding - consistent tooling/process, contribution guidelines, a
  discoverability/portal layer, explicit governance - more than grassroots enthusiasm. The 2025 survey shows
  the maturity gap directly: ~86% run shared repositories but only ~60% have InnerSource documentation, with
  portals, training, and metrics lagging further behind.
* **Pattern 3 - InnerSource as the substrate for AI-native development.**
  ISC's 2025 report treats InnerSource as essential infrastructure for building with AI (shared prompts and
  context, collaboratively built internal AI tooling, well-structured internal code agents can reuse). This
  is ISC advocacy/thesis rather than a survey-proven causal claim, and is the natural bridge into Part 2, so
  it is framed as direction, not finding.

## What ISC is investing in next

All items below are public or safely generalizable. Sponsor names and amounts, internal event-health status,
personnel changes, and any unconfirmed keynote were found in planning material and are deliberately excluded.

* **Summit 2026 (confirmed, public).**
  A single continuous 22-hour "follow-the-sun" virtual event on **November 12, 2026** (event page live at
  innersourcecommons.org), opening in APAC before handing to EMEA and then the Americas. Theme: **"InnerSource
  in Motion: Navigating the Shifting Tides."** Three tracks: Cultural Elasticity, Follow-the-Sun
  Collaboration, and the Evolving Developer Experience, with AI woven throughout. Scott Hanselman is a
  confirmed keynote. After a hybrid 2025, ISC deliberately returned to fully virtual for 2026.
* **Planned but not yet locked (kept out of the talk):**
  an AI-and-InnerSource panel is in planning but not confirmed; a second keynote and the APAC keynote slot
  were still open in the most recent notes. Russell chose to leave the panel out of the keynote entirely
  until it is confirmed, and none of those unconfirmed names are used.
* **Ongoing programs worth naming (public):**
  a new public InnerSource Pattern for keeping AI-generated code aligned with a project's own conventions
  (drafted in the public InnerSourcePatterns repo); standing peer working groups for InnerSource practice and
  for program offices (ISPO); and a formal Foundation membership.
* **Direction, not commitment (in-person events, per Russell's steer):**
  ISC ran in-person Summits before the pandemic, went virtual through it, and returned to in person last year
  in Yokohama (2025); the aim for 2027 is more regular in-person regional events, including a presence in the
  APAC region. Paired with this is an investment in greater curation - focusing each gathering on the topics
  that matter to the participant companies so InnerSource knowledge spreads worldwide as fast as possible.
  Russell's steer is to state the 2027 in-person direction as a clear, confident intention. He also noted
  personal pride in and affinity for the InnerSource China Community, folded into the opening.
* **FINOS:** a real, longstanding partnership (the FINOS InnerSource SIG), but no distinct *new* 2026 activity
  surfaced - so it is not overstated as a 2026 investment.
* **Certification/training product:** none found; not claimed.

## Challenges leaders should prepare for

All three are grounded in the published State of InnerSource 2024/2025 reports. Russell's steer is to lead
with both of the first two, in order - time and resources first, then ROI - with the structural blockers as
an optional third.

* **Time/resources overtook culture as the #1 blocker.**
  In 2025, "lack of time and resources" (84%) overtook organizational culture / silo thinking (74%) as the top
  perceived blocker - a clean year-over-year shift, since culture led in 2024. Supporting: only ~22% of orgs
  give employees time to contribute, ~15% reward contributions, ~14% factor InnerSource into promotion.
* **The value is obvious; the investment isn't (ROI/measurement).**
  Fewer than half of orgs measure InnerSource at all, and existing methods are immature (manual tracking ~42%,
  surveys ~38%, portal metrics ~28%). About 1 in 7 programs were ramping down in 2025. This is the most
  differentiated, best-evidenced challenge in the data - sharper than a generic "proving ROI."
  ROI reference (confirmed by Russell): Chamindra de Silva (Citi, lead of the FINOS InnerSource SIG) and
  Daniel Izquierdo (Bitergia), *The Business Impact of Inner Source and How to Quantify It*
  (https://www.researchgate.net/publication/372758825_The_Business_Impact_of_Inner_Source_and_How_to_Quantify_It).
  This is the credible, InnerSource-specific ROI work to cite for this challenge - stronger than the generic
  engineering-ROI papers (DX's DX Core 4, McKinsey's Developer Velocity) because it is about InnerSource
  directly. Both authors are public InnerSource figures, so naming them is fine.
* **Structural and human blockers (optional third).**
  Past the top blocker: awareness gaps (~70%), missing executive sponsorship (~67%), missing middle-manager
  support (~66%), and discoverability (~65%). Overlaps with the time/resources challenge (both are the
  culture/people family), so Russell can pick whichever framing suits the room.

## The opening hook

* **The reciprocal relationship with the InnerSource China Community.**
  Jerry Tan (Zhongyi Tan) leads the InnerSource China Community and is an ISC Foundation Member - he is not a
  board director, so don't call him one on stage. Last year he invited Russell to give a video keynote to
  InnerSource Gathering Beijing 2025; this year the Shanghai Gathering brings Russell in person. That, plus
  ISC's own APAC-heavy audience data, makes the honest opening: this region has been near the center of the
  InnerSource movement, not on its edge.
  Individual contact details and internal China-strategy discussion (e.g. building a presence on regional
  platforms) were found in email but are kept out of this repo.

## What is deliberately excluded from this public repo

* Exact internal web-analytics figures (only the qualitative "APAC leads engagement" pattern is used).
* Any company named only in a not-yet-public source (e.g. the OSPO community-call talk scheduled after
  Shanghai) - generalized until public.
* Summit sponsor names, tiers, and amounts; internal event-health/status; personnel changes; and unconfirmed
  keynote names.
* All individual email addresses (including Chen Wei's), the internal Huawei-sponsorship/US-sanctions legal
  discussion, and internal China-strategy specifics.
* Part 2's AI-interview inputs remain anonymized per those respondents' terms; Part 1 does not draw on them.
