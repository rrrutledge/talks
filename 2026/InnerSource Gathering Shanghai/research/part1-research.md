# Part 1 research - global InnerSource Commons update

Part 1 (the global ISC update) is grounded in the Foundation's own data and in published, citable sources.
This note records what backs each claim in the Part 1 outline and where it came from, and flags what was
generalized to keep out of this public repo - the same judgment Part 2's survey material required.

## Where the movement stands today

* **Community growth.**
  ISC's LinkedIn following grew from about 92 people in 2020 to roughly 2,700 in mid-2026, still climbing
  around 15% a year - about a 30x rise over the Foundation's life, and the fastest-growing of ISC's channels.
  YouTube and X/Twitter grew far more slowly, and X was flat-to-negative through 2025, so LinkedIn is the
  clean line to cite.
  Source: ISC's own marketing-metrics tracking; the follower counts themselves are publicly visible on the
  profiles.
* **APAC is out in front.**
  In ISC's own audience analytics, this region - Japan and India especially - is consistently among the top
  countries for engagement, regularly ahead of the US, and ISC's Japanese-language content is among its
  most-read. APAC engagement is long-standing (an APAC-region Summit ran as far back as 2020).
  The exact traffic figures are internal analytics and are deliberately kept out of this file and out of the
  committed outline; only the qualitative pattern is used.
* **APAC adoption.**
  Huawei presented its own InnerSource program in person at ISC's 2025 Summit in Yokohama, Japan (a public,
  delivered talk). Many of the region's largest engineering organizations appear on ISC's public list of
  companies practicing InnerSource. The outline names Huawei only because that talk was public; other
  in-region adopters are referred to generally.
* **Adoption reasons and program maturity.**
  State of InnerSource 2025 (published report, roughly 120 organizations surveyed, foreword by ISC President
  Yuki Hattori): top adoption drivers are code reuse (84%), development speed (81%), knowledge sharing (79%),
  and breaking down silos (77%); formal InnerSource programs or program offices exist at about 35% of orgs,
  with another ~29% running informally.

## Patterns across large-org journeys (candidates)

These are drafted as candidates for Russell to confirm, reorder, or replace against his own ED vantage -
not asserted as settled findings.

* **Pattern A - OSPO / program-office-led enablement.**
  Mature programs increasingly run InnerSource through a central OSPO or InnerSource Program Office that
  enables teams (playbooks, repository blueprints, contribution pathways, education) rather than owning the
  shared code. Recurring theme across ISC community calls, and matched by the survey's rise in formal
  program offices.
  Generalization: the clearest single example is a large bank's OSPO talk scheduled for an ISC community call
  *after* the Shanghai date, so it is not yet public. The pattern is therefore told generically, with no
  company named, until that talk airs.
* **Pattern B - scaffolding over spontaneity.**
  What lets programs scale is concrete scaffolding - consistent tooling/process, contribution guidelines, a
  discoverability/portal layer, explicit governance - more than grassroots enthusiasm. The 2025 survey shows
  the maturity gap directly: ~86% run shared repositories but only ~60% have InnerSource documentation, with
  portals, training, and metrics lagging further behind.
* **Pattern C - InnerSource as the substrate for AI-native development.**
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
* **Planned but not yet locked (flagged NEEDS RUSSELL in the outline):**
  an AI-and-InnerSource panel is in planning but not confirmed; a second keynote and the APAC keynote slot
  were still open in the most recent notes - none of those names are used here.
* **Ongoing programs worth naming (public):**
  a new public InnerSource Pattern for keeping AI-generated code aligned with a project's own conventions
  (drafted in the public InnerSourcePatterns repo); standing peer working groups for InnerSource practice and
  for program offices (ISPO); and a formal Foundation membership.
* **Direction, not commitment:**
  in-person regional Summits are the aim for 2027, including an InnerSource presence at a major regional
  open-source event. These plans are still forming and are flagged as direction in the outline.
* **FINOS:** a real, longstanding partnership (the FINOS InnerSource SIG), but no distinct *new* 2026 activity
  surfaced - so it is not overstated as a 2026 investment.
* **Certification/training product:** none found; not claimed.

## Challenges leaders should prepare for

All three are grounded in the published State of InnerSource 2024/2025 reports.

* **Time/resources overtook culture as the #1 blocker.**
  In 2025, "lack of time and resources" (84%) overtook organizational culture / silo thinking (74%) as the top
  perceived blocker - a clean year-over-year shift, since culture led in 2024. Supporting: only ~22% of orgs
  give employees time to contribute, ~15% reward contributions, ~14% factor InnerSource into promotion.
* **The value is obvious; the investment isn't (ROI/measurement).**
  Fewer than half of orgs measure InnerSource at all, and existing methods are immature (manual tracking ~42%,
  surveys ~38%, portal metrics ~28%). About 1 in 7 programs were ramping down in 2025. This is the most
  differentiated, best-evidenced challenge in the data - sharper than a generic "proving ROI."
* **Structural and human blockers (optional third).**
  Past the top blocker: awareness gaps (~70%), missing executive sponsorship (~67%), missing middle-manager
  support (~66%), and discoverability (~65%). Overlaps with the time/resources challenge (both are the
  culture/people family), so Russell can pick whichever framing suits the room.

## The opening hook

* **The reciprocal relationship with the InnerSource China Community.**
  Jerry Tan leads the InnerSource China Community and sits on ISC's board. Last year he invited Russell to
  give a video keynote to InnerSource Gathering Beijing 2025; this year the Shanghai Gathering brings Russell
  in person. That, plus ISC's own APAC-heavy audience data, makes the honest opening: this region has been
  near the center of the InnerSource movement, not on its edge.
  Individual contact details and internal China-strategy discussion (e.g. building a presence on regional
  platforms) were found in email but are kept out of this repo.

## What is deliberately excluded from this public repo

* Exact internal web-analytics figures (only the qualitative "APAC leads engagement" pattern is used).
* Any company named only in a not-yet-public source (e.g. the OSPO community-call talk scheduled after
  Shanghai) - generalized until public.
* Summit sponsor names, tiers, and amounts; internal event-health/status; personnel changes; and unconfirmed
  keynote names.
* All individual email addresses and internal China-strategy specifics.
* Part 2's AI-interview inputs remain anonymized per those respondents' terms; Part 1 does not draw on them.
