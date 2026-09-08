# Part 2 spoken draft — How AI is Reshaping InnerSource (~6 min / ~950 words)

Let's turn to the second half of what I promised - what I'm actually seeing, across the community, as
AI meets InnerSource in practice.

## The myth - and why it doesn't hold

Here's a story a lot of us are telling ourselves right now, and I want to name it directly before I
push back on it. InnerSource exists because writing code used to be expensive. If two teams both need
the same thing, it's cheaper for the company if one team builds it and the other reuses it. That was
the whole premise: don't duplicate, work together, because duplication was costly.

Now AI comes along and writes code in seconds. So the myth goes: if creating code is basically free,
what exactly are we saving by not duplicating it anymore? Doesn't AI just quietly end the argument for
InnerSource?

Here's why that's wrong. AI collapses the cost of writing code that compiles and looks right. It does
nothing - nothing - about the cost of writing code that's actually correct: available, secure, and
tested against every edge case your organization already learned the hard way. And when you make
something cheap, you get more of it. That includes duplication. The myth mistakes "cheap to write" for
"cheap," full stop. It isn't. It just moved the bill to later, and to someone else.

## The trap is already happening - in their own words

I want to give you a real example, from inside a large e-commerce company I talked to preparing this
talk. A team needed a capability. Their own AI tooling found it - it already existed, built and
working, somewhere else in the company. And the team built it again anyway. Here's how the person who
told me this put it: "the friction of contributing back felt too high." So they had AI spin up a
duplicate from scratch instead.

Their own words on what that actually cost the organization: "raw AI efficiency can inadvertently
bypass and starve out collaboration loops if governance isn't adapted to match the speed." And then,
almost as an aside, the line that's stuck with me since I read it: "the value of cooperating and
participating alongside communities is no longer recognized, making it practically prohibitive during
working hours." That's not a system failing quietly in the background. That's someone who cares about
this, watching it happen, and saying so.

Now - here's the question worth sitting with. Was that team's call actually wrong? In the moment, for
them, on that day - probably not. They had a deadline. They shipped.

## Why this actually matters - be precise about the cost

Let's be exact about why that decision is still a problem, because "it's technically inefficient" isn't
going to move anyone. Two concrete costs.

First: tokens. Every time an agent duplicates something instead of finding it, it's burning real
compute, reasoning its way through a problem the company already solved, from scratch, on every team,
on every task. That's not a rounding error. That compounds, sprint over sprint, across a company the
size of the one in that story.

Second: correctness. The original component didn't just compile - it earned years of hardening. Every
edge case, every security patch, every outage that taught somebody something, all baked in. None of
that transfers to a duplicate. The copy starts back at zero, no matter how confident it looks on day
one. That duplicate has a lifespan. Someone has to patch it, secure it, keep it running for years - and
they're re-earning correctness the original component already paid for once.

That's the trap, precisely: cheap to write, expensive to own, and the bill arrives after everyone's
stopped paying attention.

## Where it's breaking things: review capacity

So if the temptation to duplicate is understandable, the honest question is: why is the review path so
heavy in the first place? Here the answer is almost universal. I surveyed people across this community
preparing for today, and the single loudest theme, independent of industry, independent of company
size, was this: AI can now produce contributions faster than any organization can review them. One
respondent told me about a high-profile internal project that shut down entirely - closed its source -
because it couldn't handle the flood of AI-generated pull requests hitting it.

This isn't just an internal problem. It's happening in public, right now, in open source. Take curl -
one of the most widely used pieces of software on Earth. By last year, roughly one in five security
reports to curl were AI-assisted. The real vulnerability rate in that same pile had fallen to about one
in twenty. And across six years of watching this, the maintainer's own count is zero - zero
AI-generated reports that ever found a real vulnerability. In January of this year, curl shut its bug
bounty program down entirely.

## What actually helps

So does better tooling fix this? I went looking. The honest answer is: sometimes, and the line is
sharp. Where automation works, it's doing the boring part - reproducing an issue, verifying it,
narrowing it down - before a human ever has to look. One team building AI tooling reported an agent
pipeline authoring a third of their merged pull requests and closing three-quarters of incoming issues,
in a month, just by doing that first pass.

Where it doesn't work is asking AI to replace the judgment call. One open source project tried an AI
reviewer, found half of what it said was noise and a quarter was pointless nitpicking, and turned it
off. A survey of seven thousand engineers this year found two-thirds of them won't merge code on an AI
review's word alone.

So here's the line: automation is a genuine force multiplier for a human's attention. It is not, yet, a
replacement for a human's judgment. You still need someone accountable for the call. No tool has
changed that.

## Bridge to what's next

And that's really the frontier. Not managing the flood - that's triage, that's plumbing. The real prize
is teaching agents themselves the InnerSource habit: look before you build, pull the shared piece
instead of re-deriving it, and when you build something genuinely new and reusable, push it back. I've
found real, live examples of parts of that happening already, without anyone calling it InnerSource - a
shared-spec pattern where one team owns requirements and others consume them read-only, right where
their coding agent can read them. Shell's own AI-powered discovery tool, finding code that's merely
adjacent to what you asked for, not just a keyword match.

Two of the three legs - reuse, and publishing back - are already being built, out there, right now. The
third leg - agents that actually search before they build - is still wide open. That's not a gap to be
anxious about. That's the opportunity in front of this community, starting today.
