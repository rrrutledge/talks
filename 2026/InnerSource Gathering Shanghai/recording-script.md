# Recording script - InnerSource Gathering Shanghai 2026

**Talk:** InnerSource in the AI Era - A Global Update and What Comes Next
**Speaker:** Russell Rutledge, Executive Director, InnerSource Commons
**Runtime target:** ~15 minutes (Open ~1 &middot; Part 1 ~6 &middot; Part 2 ~6 &middot; Close ~2)

One flowing teleprompter read.
The same text lives in the Reveal.js speaker notes, so the deck itself is the prompter when you record - advance a slide at each `---`.

---

## Open (~1 min)

Good morning, and thank you - to Jerry Tan, and to the whole InnerSource China Community - for inviting me back.
Last year Jerry invited me to give a video keynote to the Beijing Gathering; this year I'm glad to be with you again for Shanghai.
I'm joining remotely, but I'm very much with you.

---

I'll say this plainly: I'm proud of what the InnerSource China Community has built, and I feel a genuine affinity for this community.
And that pride connects to something bigger.
InnerSource is a genuinely global movement now - and this region isn't on the edge of it, it's near the center.
I want to give you the view from that vantage point.

---

Here's where we're headed today, in two halves.
First, a global update on where InnerSource stands.
Then, the question the whole community is asking at once: what is AI doing to all of it?

---

## Part 1 - The global update (~6 min)

Let's start with where the movement stands.

---

InnerSource has moved from a promising practice to a core strategy for how large enterprises build software together - and the community around it keeps compounding.
One clean line: our LinkedIn following is up roughly thirty-fold over the life of the Foundation, and it's still growing about fifteen percent year over year.
It's our fastest-growing channel by far.

---

And it's a genuinely global movement, with this region out in front rather than catching up.
In our own audience data, Japan is consistently one of our top two countries for engagement - trading the number-one spot with the United States month to month, and well ahead of everyone else.
Germany, the UK, and India round out the leading set.
And our Japanese-language content is among the most-read we publish.

---

The community's own bench reflects that.
Foundation membership is individual and merit-based - you're elected in, the way Apache does it - and the APAC contingent is deep.
Chen Wei, Senior Project Director of Huawei's InnerSource Office, presented "Huawei InnerSource Culture and Value Closed-Loop Practice" at our 2025 Summit in Yokohama.
Shingo Oidate, who runs Mitsubishi Electric's Open Source Program Office, was elected a Foundation Member just this month.
They join a strong roster - Jerry Tan, Yuki Hattori, Yoshitake Kobayashi, Ada Dai, Willem Jiang, and others.
This region isn't just consuming InnerSource; it's helping lead the Foundation.

---

Why does it spread?
The most recent State of InnerSource report - about 120 organizations - is clear: the top reasons are code reuse, at eighty-four percent; development speed, eighty-one; knowledge sharing, seventy-nine; and breaking down silos, seventy-seven.
Formal programs or program offices now exist at about a third of organizations, with another third running informally.

---

Across the largest InnerSource journeys, I see three patterns worth naming.

First - consolidation.
InnerSource is increasingly funded and housed alongside a partner function rather than as a standalone line item.
As budgets tighten and AI reshapes where engineering effort goes, InnerSource more and more sits with a related group - an OSPO, a developer-experience team, a platform-engineering org.
Those are natural partners; they share InnerSource's cross-team, reuse-first instincts.
The thing to get right is scope.
A host function tends to fund InnerSource for what helps its own remit - but the whole premise of InnerSource is that it serves every team, not just the one paying for it.
The programs that land this well fund through a partner function while keeping the mandate company-wide.

Second - scaffolding beats enthusiasm.
What separates programs that scale from ones that stall isn't grassroots energy; it's concrete scaffolding: consistent tooling and process, clear contribution guidelines, a discoverability layer, explicit governance.

Third - InnerSource is becoming the substrate for AI-native development.
The community increasingly frames InnerSource less as a nice-to-have and more as essential infrastructure for building well with AI: shared prompts and context, collaboratively built internal AI tooling, and well-structured internal code that agents can actually find and reuse.
Hold onto that one - it's where the second half of this talk goes.

---

The survey shows the scaffolding gap plainly - about eighty-six percent run shared repositories, but only about sixty percent have InnerSource documentation, and portals, training, and metrics lag further behind.
Adoption is running ahead of operational maturity.

---

What are we investing in next?
The flagship is the 2026 Summit, and it's built for exactly this room: a single continuous twenty-two-hour follow-the-sun virtual event on November twelfth, opening in APAC before handing off to EMEA and then the Americas.
Your region kicks off the global day.
The theme is "InnerSource in Motion: Navigating the Shifting Tides," across three tracks - Cultural Elasticity, Follow-the-Sun Collaboration, and the Evolving Developer Experience - with AI running through all of them.
Scott Hanselman is a confirmed keynote.

---

Beyond the Summit, the community is actively building: a new public InnerSource Pattern for keeping AI-generated code aligned with a project's own conventions, and standing peer working groups for practice and for program offices.
And the direction is toward getting back in the room together - the aim for 2027 is more regular in-person regional events, including a presence here in this region.

---

Two challenges to prepare for.
The first is a real shift: the number-one blocker is no longer culture - it's time.
For the first time, "lack of time and resources," at eighty-four percent, overtook culture and silo thinking, at seventy-four, as the top perceived blocker.
And the supporting numbers are stark: only about twenty-two percent of organizations give employees time to contribute, about fifteen percent reward it, and about fourteen percent factor it into promotion.
People are convinced.
They just have no room to act on it.

---

The second: the value is obvious, but the investment isn't - largely because it's hard to measure.
Fewer than half of organizations measure InnerSource at all, and the methods that exist are immature.
Without a credible ROI story, programs stall - roughly one in seven were ramping down last year.
The encouraging part is that the community is building the answer: Chamindra de Silva and Daniel Izquierdo have put real rigor into quantifying the business impact of InnerSource.
If you need the ROI reference this challenge has been missing, that's it.

---

Every one of these - the patterns, the investments, the challenges - now runs into a single question the whole community is asking at once: what does AI do to all of it?
That's the second half.

---

## Part 2 - How AI is reshaping InnerSource (~6 min)

Let's turn to the second half of what I promised - what I'm actually seeing, across the community, as AI meets InnerSource in practice.

---

Here's a story a lot of us are telling ourselves right now, and I want to name it directly before I push back on it.
InnerSource exists because writing code used to be expensive.
If two teams both need the same thing, it's cheaper for the company if one team builds it and the other reuses it.
That was the whole premise: don't duplicate, work together, because duplication was costly.

Now AI comes along and writes code in seconds.
So the myth goes: if creating code is basically free, what exactly are we saving by not duplicating it anymore?
Doesn't AI just quietly end the argument for InnerSource?

Here's why that's wrong.
AI collapses the cost of writing code that compiles and looks right.
It does nothing - nothing - about the cost of writing code that's actually correct: available, secure, and tested against every edge case your organization already learned the hard way.
And when you make something cheap, you get more of it.
That includes duplication.
The myth mistakes "cheap to write" for "cheap," full stop.
It isn't.
It just moved the bill to later, and to someone else.

---

I want to give you a real example, from inside a large e-commerce company I talked to preparing this talk.
A team needed a capability.
Their own AI tooling found it - it already existed, built and working, somewhere else in the company.
And the team built it again anyway.
Here's how the person who told me this put it: "the friction of contributing back felt too high."
So they had AI spin up a duplicate from scratch instead.

Their own words on what that actually cost the organization: "raw AI efficiency can inadvertently bypass and starve out collaboration loops if governance isn't adapted to match the speed."
And then, almost as an aside, the line that's stuck with me since I read it: "the value of cooperating and participating alongside communities is no longer recognized, making it practically prohibitive during working hours."
That's not a system failing quietly in the background.
That's someone who cares about this, watching it happen, and saying so.

Now - here's the question worth sitting with.
Was that team's call actually wrong?
In the moment, for them, on that day - probably not.
They had a deadline.
They shipped.

---

Let's be exact about why that decision is still a problem, because "it's technically inefficient" isn't going to move anyone.
Two concrete costs.

First: tokens.
Every time an agent duplicates something instead of finding it, it's burning real compute, reasoning its way through a problem the company already solved, from scratch, on every team, on every task.
That's not a rounding error.
That compounds, sprint over sprint, across a company the size of the one in that story.

Second: correctness.
The original component didn't just compile - it earned years of hardening.
Every edge case, every security patch, every outage that taught somebody something, all baked in.
None of that transfers to a duplicate.
The copy starts back at zero, no matter how confident it looks on day one.
That duplicate has a lifespan.
Someone has to patch it, secure it, keep it running for years - and they're re-earning correctness the original component already paid for once.

That's the trap, precisely: cheap to write, expensive to own, and the bill arrives after everyone's stopped paying attention.

---

And this isn't just one anecdote.
A large-scale code-change analysis found duplicated code blocks up eighty-one percent, while refactored and reused code collapsed from twenty-one percent to under four percent of all changes over three years.
Google's own DORA research found increased AI usage paired with a measurable drop in delivery stability.
The pattern in that one team's story is showing up in the aggregate.

---

So if the temptation to duplicate is understandable, the honest question is: why is the review path so heavy in the first place?
Here the answer is almost universal.
I surveyed people across this community preparing for today, and the single loudest theme, independent of industry, independent of company size, was this: AI can now produce contributions faster than any organization can review them.
One respondent told me about a high-profile internal project that shut down entirely - closed its source - because it couldn't handle the flood of AI-generated pull requests hitting it.

This isn't just an internal problem.
It's happening in public, right now, in open source.
Take curl - one of the most widely used pieces of software on Earth.
By last year, roughly one in five security reports to curl were AI-assisted.
The real vulnerability rate in that same pile had fallen to about one in twenty.
And across six years of watching this, the maintainer's own count is zero - zero AI-generated reports that ever found a real vulnerability.
In January of this year, curl shut its bug bounty program down entirely.

---

So does better tooling fix this?
I went looking.
The honest answer is: sometimes, and the line is sharp.
Where automation works, it's doing the boring part - reproducing an issue, verifying it, narrowing it down - before a human ever has to look.
One team building AI tooling reported an agent pipeline authoring a third of their merged pull requests and closing three-quarters of incoming issues, in a month, just by doing that first pass.

Where it doesn't work is asking AI to replace the judgment call.
One open source project tried an AI reviewer, found half of what it said was noise and a quarter was pointless nitpicking, and turned it off.
A survey of seven thousand engineers this year found two-thirds of them won't merge code on an AI review's word alone.

So here's the line: automation is a genuine force multiplier for a human's attention.
It is not, yet, a replacement for a human's judgment.
You still need someone accountable for the call.
No tool has changed that.

---

And that's really the frontier.
Not managing the flood - that's triage, that's plumbing.
The real prize is teaching agents themselves the InnerSource habit: look before you build, pull the shared piece instead of re-deriving it, and when you build something genuinely new and reusable, push it back.
I've found real, live examples of parts of that happening already, without anyone calling it InnerSource - a shared-spec pattern where one team owns requirements and others consume them read-only, right where their coding agent can read them.
Shell's own AI-powered discovery tool, finding code that's merely adjacent to what you asked for, not just a keyword match.

Two of the three legs - reuse, and publishing back - are already being built, out there, right now.
The third leg - agents that actually search before they build - is still wide open.
That's not a gap to be anxious about.
That's the opportunity in front of this community, starting today.

---

## Close - what comes next (~2 min)

So where does this leave us?
Agents that search before they build - that's the frontier still wide open.
And it points at the real evolution: the "Source" in InnerSource is becoming a "Source of Knowledge."
Not just code, but the context, the patterns, the decisions a team accumulates - which is exactly the substrate agents need too.
Several people in this community have converged on that framing independently, unprompted.
It isn't just my read.

---

If you take two things from today, take these.
First: InnerSource isn't obsolete in the AI era.
AI makes the problem InnerSource solves bigger and faster, not smaller.
Second: the next frontier isn't managing the flood - it's teaching AI agents themselves the InnerSource habit.
Search before building, reuse, and contribute back.

---

Where to go next: the InnerSource Commons site, and the 2026 Summit on November twelfth - follow-the-sun, and your region opens the global day.
I'd love to see you there.

Thank you again - to Jerry Tan, and to the entire InnerSource China Community.
It's an honor to be part of what you're building here.
Enjoy the rest of the Gathering.
