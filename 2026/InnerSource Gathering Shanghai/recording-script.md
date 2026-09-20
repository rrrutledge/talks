# Recording script - InnerSource Gathering Shanghai 2026

**Talk:** InnerSource in the AI Era - A Global Update and What Comes Next
**Speaker:** Russell Rutledge, Executive Director, InnerSource Commons
**Runtime target:** ~13-14 minutes for the main talk; the appendix slides are reference only.

This mirrors the deck's speaker notes, in slide order - the deck itself is the prompter when you record, advancing a slide at each `---`.

---

## Open

Good morning, and thank you - to Jerry Tan, and to the whole InnerSource China Community - for inviting me back.

Last year Jerry invited me to give a video keynote to the Beijing Gathering; this year I'm glad to be with you again for Shanghai. I'm joining remotely, but I'm very much with you.

---

Here's where we're headed today, in two halves. First, a global update on where InnerSource stands. Then, the question the whole community is asking at once: what is AI doing to all of it?

---

## Part 1 - The global update

Let's start with where the movement stands.

---

InnerSource has moved from a promising practice to a core strategy for how large enterprises build software together - and the community around it keeps compounding.

One clean line: our LinkedIn following is up roughly thirty-fold over the life of the Foundation, and it's still growing about fifteen percent year over year. It's our fastest-growing channel by far.

---

And it's a truly worldwide movement - one that runs right through China. Foundation membership is individual and merit-based - you're elected in, the way Apache does it - and China's bench is deep: Jerry Tan, who leads the InnerSource China Community; Willem Jiang at Huawei; Ada Dai at Tencent. At our 2025 Global Summit in Yokohama, Chen Wei of Huawei's InnerSource Office presented "Huawei InnerSource Culture and Value Closed-Loop Practice." And two of this year's Summit speakers come from China. China isn't following this movement; it's helping lead it.

---

Why does it spread? The most recent State of InnerSource report is clear: the top reasons are code reuse, at eighty-four percent; development speed, eighty-one; knowledge sharing, seventy-nine; and breaking down silos, seventy-seven.

Formal programs or program offices now exist at about a third of organizations, with another third running informally.

---

Across the largest InnerSource journeys, I see three patterns worth naming. The first is consolidation.

InnerSource is increasingly funded and housed alongside a partner function rather than as a standalone line item - an OSPO, a developer-experience team, a platform-engineering org. Those are natural partners. The thing to get right is scope: a host function tends to fund InnerSource for what helps its own remit, but the whole premise is that it serves every team. The programs that land this well fund through a partner while keeping the mandate company-wide.

---

The second pattern - scaffolding beats enthusiasm. What separates programs that scale from ones that stall isn't grassroots energy; it's concrete scaffolding: consistent tooling, contribution guidelines, governance - and, just as much, manager and HR support, so that contributing actually counts on someone's career ladder.

And here's the challenge that goes with it: the number-one blocker to building that scaffolding is no longer culture - it's time. For the first time, "lack of time and resources," at eighty-four percent, overtook culture and silo thinking, at seventy-four. Only about twenty-two percent of organizations give employees time to contribute, about fifteen percent reward it, and fourteen percent factor it into promotion. People are convinced; they just have no room to act on it.

---

The third challenge - ROI. The value is obvious, but the investment isn't, largely because it's hard to measure: under fifty percent of organizations measure InnerSource at all.

And there's a deeper reason. The cost and the payoff land in different boxes. In time: you invest this quarter, but the return dribbles in across the year. In scope: the team that invests often isn't the team that reaps the benefit. Measured quarter-by-quarter, team-by-team, InnerSource never quite pencils out - so the fix is to reward and recognize contribution beyond the quarter, and beyond the team. If you need the rigorous ROI reference, that's de Silva and Izquierdo's "Measuring InnerSource Value."

---

What are we investing in next? The flagship is the 2026 Summit, and it's built for exactly this room: a single continuous twenty-two-hour follow-the-sun virtual event on November twelfth, opening in APAC before handing off to EMEA and then the Americas. Your region kicks off the global day.

The theme is "InnerSource in Motion: Navigating the Shifting Tides," with three tracks and AI running through all of them. Scott Hanselman is a confirmed keynote. If you scan that code, it takes you straight to signing up.

---

## Part 2 - How AI is reshaping InnerSource

Let's turn to the second half of what I promised - what I'm actually seeing, across the community, as AI meets InnerSource in practice.

---

Here's a story a lot of us are telling ourselves, and I want to name it directly before I push back. InnerSource exists because writing code used to be expensive. If two teams need the same thing, it's cheaper if one builds it and the other reuses it. That was the whole premise: don't duplicate, because duplication was costly.

Now AI writes code in seconds. So the myth goes: if creating code is basically free, what are we saving by not duplicating anymore? Doesn't AI just quietly end the argument for InnerSource?

Here's why that's wrong. AI collapses the cost of writing code that compiles and looks right. It does nothing - nothing - about the cost of code that's actually correct: available, secure, tested against every edge case your organization already learned the hard way. And when you make something cheap, you get more of it. That includes duplication. The myth mistakes "cheap to write" for "cheap," full stop. It just moved the bill to later, and to someone else.

---

And this isn't just one anecdote. A large-scale code-change analysis - over six hundred million changes - found duplicated code blocks up eighty-one percent, while refactored and reused code collapsed from twenty-one percent to under four percent of all changes. Google's own DORA research found increased AI usage paired with a measurable drop in delivery stability. The pattern in that one team's story is showing up in the aggregate.

---

Let's be exact about why that decision is still a problem, because "it's technically inefficient" won't move anyone. Two concrete costs.

First: tokens. Every time an agent duplicates something instead of finding it, it's burning real compute, reasoning its way through a problem the company already solved, from scratch, on every team, on every task. That compounds, sprint over sprint.

Second: correctness. The original component didn't just compile - it earned years of hardening. Every edge case, every security patch, every outage that taught somebody something. None of that transfers to a duplicate. The copy starts back at zero, no matter how confident it looks on day one. Someone has to patch it and secure it for years - re-earning correctness the original already paid for once.

That's the trap, precisely: cheap to write, expensive to own, and the bill arrives after everyone's stopped paying attention.

---

So if the temptation to duplicate is understandable, the honest question is: why is the review path so heavy in the first place? Here's the core of it, and it's almost universal across the community I surveyed: the cost of producing a contribution has dropped to near zero, but the cost of reviewing one hasn't moved at all. AI can now produce contributions faster than any organization can review them. One respondent told me about a high-profile internal project that shut down entirely - closed its source - because it couldn't handle the flood of AI-generated pull requests.

This isn't just internal. Take curl - one of the most widely used pieces of software on Earth. By last year, roughly one in five security reports to curl were AI-assisted. Of all reports, about one in twenty was a genuine vulnerability - and every one of those real ones came from a human. Across six years, the number of AI-generated reports that found a real vulnerability is zero. In January of this year, curl shut its bug bounty program down - though it later reopened as the AI slop subsided.

---

And that's really the frontier. Not managing the flood - that's triage, that's plumbing. The real prize is teaching agents themselves the InnerSource habit: look before you build, pull the shared piece instead of re-deriving it, and when you build something genuinely new and reusable, push it back.

I've found real, live examples already, without anyone calling it InnerSource - a shared-spec pattern where one team owns requirements and others consume them read-only, right where their coding agent can read them. Shell's own AI-powered discovery tool, finding code that's merely adjacent to what you asked for.

Two of the three legs - reuse, and publishing back - are already being built, right now. The third leg - agents that actually search before they build - is still wide open. That's not a gap to be anxious about. That's the opportunity in front of this community, starting today.

---

So where does this leave us? Agents that search before they build - that's the frontier still wide open. And it points at the real evolution: the "Source" in InnerSource is becoming a "Source of Knowledge." Not just code, but the context, the patterns, the decisions a team accumulates - which is exactly the substrate agents need too. Several people in this community have converged on that framing independently, unprompted. It isn't just my read.

---

If you take two things from today, take these. First: InnerSource isn't obsolete in the AI era. AI makes the problem InnerSource solves bigger and faster, not smaller. Second: the next frontier isn't managing the flood - it's teaching AI agents themselves the InnerSource habit. Search before building, reuse, and contribute back.

---

Where to go next: the InnerSource Commons site, and the 2026 Summit on November twelfth - follow-the-sun, and your region opens the global day. Scan the code, and I'd love to see you there.

Thank you again - to Jerry Tan, and to the entire InnerSource China Community. It's an honor to be part of what you're building here. Enjoy the rest of the Gathering.

---

## Appendix - reference slides

Reference slides - the maturity-gap data and the anonymized duplication story - available if the conversation calls for them.

---

The survey shows the gap plainly. About eighty-six percent share code in shared repositories - the basic move. But only about sixty percent have written InnerSource documentation, and it drops from there: discovery portals at forty-six percent, training at forty-four, monitoring and metrics at thirty-two.

In plain terms: teams are sharing code faster than they're building the support system - the docs, the portals, the training - that keeps that code usable.

---

I want to give you a real example, from inside a large e-commerce company I talked to preparing this talk. A team needed a capability. Their own AI tooling found it - it already existed, built and working, somewhere else in the company. And the team built it again anyway. Here's how the person put it: "the friction of contributing back felt too high." So they had AI spin up a duplicate from scratch instead.

Their own words on what that cost the organization: "raw AI efficiency can inadvertently bypass and starve out collaboration loops if governance isn't adapted to match the speed." And then, almost as an aside, the line that's stuck with me: "the value of cooperating and participating alongside communities is no longer recognized, making it practically prohibitive during working hours." That's someone who cares about this, watching it happen, and saying so.

Now - the question worth sitting with. Was that team's call actually wrong? In the moment, on that day, on deadline - probably not. They shipped. Which is what makes the next point land.
