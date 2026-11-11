# Recording script - GOTC 2026 (Beijing)

**Talk:** InnerSource in the AI Era: A Global Update and What Comes Next
**Speaker:** Russell Rutledge, Executive Director, InnerSource Commons Foundation
**Event:** GOTC 2026 - Global Open Source Technology Summit, Beijing, November 14, 2026 (organized by OSCHINA; theme "Open Source x AI Ecosystem Innovation")
**Format:** pre-recorded video, 10 minutes (organizer's ask; 5 minutes acceptable)
**Runtime target:** 9:30-10:00, about 1,200 spoken words.

A 10-minute cut of the Shanghai keynote (same title, same research).
Advance one slide at each `---`.
Shanghai slide numbers are in brackets so the deck cut can be built from them.

---

## Open  [Shanghai 1, retitled for GOTC]

Hello, GOTC - and thank you to Gao Kun and the whole OSCHINA team, and to the GOTC organizing committee, for inviting InnerSource Commons to be part of this summit.
I'm Russell Rutledge, Executive Director of the InnerSource Commons Foundation.
I can't be with you in Beijing, but I'm very glad to be with you this way.

---

## Agenda  [Shanghai 2]

In the next ten minutes: a quick global update on where InnerSource stands, and then the question this whole summit is about - what is AI doing to how we build software together?

---

## Part 1 - The global update  [Shanghai 3 divider, then 4]

InnerSource means bringing open source ways of working inside a company - shared code, open contribution, transparent collaboration across team boundaries.
It has moved from a promising practice to a core strategy for how large enterprises build software together.
And the community keeps compounding: our LinkedIn following is up roughly thirty-fold over the life of the Foundation, and still growing about fifteen percent a year.

---

## China  [Shanghai 6]

It's a truly worldwide movement, and it runs right through China.
Jerry Tan leads the InnerSource China Community; Willem Jiang at Huawei and Ada Dai at Tencent are Foundation members; and Wiky Li from HSBC Technology China is speaking at our 2026 Summit about AI adoption through InnerSource.
China isn't following this movement; it's helping lead it.

---

## Why it spreads  [Shanghai 7]

Why does it spread?
The State of InnerSource report is clear: code reuse, eighty-four percent; development speed, eighty-one; knowledge sharing, seventy-nine; breaking down silos, seventy-seven.

---

## The blocker is time  [Shanghai 9, trimmed]

But here's the challenge.
For the first time, the number-one blocker isn't culture - it's time.
"Lack of time and resources," at eighty-four percent, overtook culture and silo thinking.
Only about twenty-two percent of organizations give people time to contribute, and fourteen percent factor it into promotion.
People are convinced; they just have no room to act on it.
Keep that in mind, because it's exactly where AI comes in.

---

## Part 2 - How AI is reshaping InnerSource  [Shanghai Part 2 divider]

Now to the second half - what I'm actually seeing as AI meets InnerSource in practice.

---

## The myth  [Shanghai myth slide]

Here's a story a lot of us are telling ourselves.
InnerSource exists because writing code used to be expensive: if two teams need the same thing, it's cheaper for one to build it and the other to reuse it.
Now AI writes code in seconds.
So the myth goes: if creating code is basically free, why bother reusing anything?
Doesn't AI quietly end the argument for InnerSource?

Here's why that's wrong.
AI collapses the cost of writing code that compiles and looks right.
It does nothing about the cost of code that's actually correct - secure, tested against every edge case your organization already learned the hard way.
And when you make something cheap, you get more of it.
That includes duplication.

---

## The data  [Shanghai data slide]

This isn't one anecdote.
An analysis of over six hundred million code changes found duplicated code blocks up eighty-one percent, while refactored and reused code collapsed from twenty-one percent to under four percent of all changes.
Google's DORA research found increased AI usage paired with a measurable drop in delivery stability.

---

## Two costs  [Shanghai two-costs slide]

Two concrete costs.
First, tokens: every time an agent rebuilds something instead of finding it, it burns real compute re-solving a problem the company already solved - on every team, on every task.
Second, correctness: the original component earned years of hardening - every edge case, every security patch, every outage that taught somebody something.
None of that transfers to a duplicate.
Cheap to write, expensive to own - and the bill arrives after everyone has stopped paying attention.

---

## The review flood  [Shanghai review-flood slide]

There's a second strain, and it's almost universal across the practitioners I surveyed: the cost of producing a contribution has dropped to near zero, but the cost of reviewing one hasn't moved at all.
One respondent described a high-profile internal project that closed its source entirely because it couldn't handle the flood of AI-generated pull requests.
The open source world sees it too: curl, one of the most widely used pieces of software on Earth, shut down its bug bounty in January under a wave of AI-generated reports - across six years, not one AI-generated report found a real vulnerability.

---

## The frontier  [Shanghai frontier slide]

So that's the frontier.
Not just managing the flood - the real prize is teaching agents themselves the InnerSource habit: look before you build, pull the shared piece instead of re-deriving it, and when you build something genuinely reusable, contribute it back.

We're already seeing pieces of it, without anyone calling it InnerSource: teams publishing shared specs right where other teams' coding agents can read them, and AI-powered discovery tools that surface the code you didn't know existed.
Reuse and publishing back are being built right now.
The third leg - agents that reliably search before they build - is still wide open.
For a community like this one, building the platforms that open source and AI run on, that's the opportunity in front of us.

---

## Takeaways  [Shanghai takeaways slide]

If you take two things from today, take these.
First: InnerSource isn't obsolete in the AI era - AI makes the problem InnerSource solves bigger and faster, not smaller.
Second: the next frontier is teaching AI agents the InnerSource habit - search before you build, reuse, and contribute back.

---

## Close  [Shanghai 26, rewritten for GOTC]

You can find all of our patterns, research, and community at innersourcecommons.org - everything there is free and open, and we'd love for you to join in.
Thank you again to Gao Kun, to OSCHINA, and to everyone at GOTC.
I'd love to hear what you're building - and I hope to meet many of you in person next year.
Enjoy the summit.
