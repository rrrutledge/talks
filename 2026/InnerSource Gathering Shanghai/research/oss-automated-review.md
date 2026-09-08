# Does automated review actually help open source with this?

Yes and no, and the line between the two cases is sharp: automation that does the grunt work of triage and reproduction before a human ever looks is genuinely working. Automation that tries to replace human judgment about whether a contribution is good is not, and several teams have already tried it and turned it off.

## Where it's working: agents doing the first pass, not the final call

Vercel's AI SDK team deployed an agent pipeline that reproduces issues, verifies them, and drafts fixes before a maintainer sees them. Four weeks in, they reported the system authoring 25-35% of merged PRs and closing 70-80% of incoming issues, cutting a backlog of 1,000+ open issues and ~800 open PRs. Astro's creator, Fred Schott, describes the same shift: issues now arrive "faster than we could handle them," but agents triage, reproduce, and verify each one before a maintainer looks, something he says he'd "never seen... in my entire decade-plus experience with open source." The common thread: the agent's job is narrowing and verifying, not deciding. A human still makes the merge call. That division of labor is exactly what's missing from the InnerSource survey responses that describe pure volume overwhelming reviewers.

Two projects, Flue and tldraw, took a blunter structural path: auto-close every external PR and convert it to an issue or discussion instead. That's not automated review solving the problem. It's a project deciding the review queue isn't the place to fight this battle at all.

## Where it's not: AI reviewing AI's work

The commercial AI-code-review category (CodeRabbit, Greptile, Cursor Bugbot, GitHub's own Copilot review) is well funded and growing fast, but real deployment data tells a much rockier story than the vendor comparisons suggest. The Cockpit project (Red Hat/GNOME) tried GitHub Copilot for automated review and found about half the output was noise and a quarter was bikeshedding, nitpicks and unfounded or actively bad suggestions. They switched it off. SonarSource's 2026 survey of 7,000 engineers backs that up at scale: 66% refuse to merge without a manual review regardless of what an AI reviewer says, and only 3% actually trust AI review output. The core failure mode is that without a reliable filter, a real bug, a hallucinated bug, and a style nit all get the same one-click dismissal, because a human reviewer can't tell them apart fast enough to trust the tool's judgment. Teams that start out auto-publishing these reviews tend to mute the bot within months, and the handful of legitimate findings get buried with the noise. That's the "blind leading the blind" problem in its purest form: an unreliable generator being checked by an unreliable checker doesn't multiply out to reliable.

## curl didn't reach for automation either

Worth noting for the talk: curl, the project with the most public and most quantified version of this crisis, didn't try an automated triage layer as its fix. Daniel Stenberg's actual sequence was a lighter human-facing intervention first, a May 2025 mandatory disclosure checkbox asking every HackerOne submitter whether AI was used, before giving up on the program entirely in January 2026. The most sophisticated security team in this whole story didn't lean on an AI reviewer to save the queue. They asked humans to self-report, and when that didn't hold, they shut the door.

## The honest line for the room

Automation helps exactly where it stays a force multiplier for a human's attention, doing the reproducing and narrowing that used to eat a maintainer's morning. It does not yet help, and arguably makes things worse, the moment it's asked to render judgment on whether a contribution is trustworthy. That's not a tooling gap that better prompts will close soon. It's the same trust problem the whole survey keeps circling, just pushed one layer deeper: you still need a human who's accountable for the call, and no bot has changed that yet.
