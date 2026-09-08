# Q1 synthesis: How is AI changing how teams discover and reuse internal code?

Twenty answers to the same question split into three real camps, not one consensus - and the
split itself is the finding.

**The discovery-layer optimists are the loudest group.** For them, AI is finally solving the
oldest InnerSource problem: you can't reuse what you can't find. An engineer at a global tech
company describes internal MCP servers making discovery "completely transparent and
frictionless." A UK bank's open-source program office puts it cleanly: AI is "increasingly acting
as a discovery and navigation layer for internal engineering knowledge," lowering the effort to
get started outside your home team and surfacing existing patterns "before teams create something
new." Shell's Christian DeFeo names the sharpest version of this publicly - Project Fleming
(projectfleming.tech) uses AI to find code that's *adjacent and useful*, not just a keyword match,
which is exactly what standard search always failed to do. A contact at an open source foundation
frames the shift well: "instead of knowing what to search for, you could increasingly describe
what you need and have an agent identify what already exists."

**The skeptics are answering a different question, and it's the one your blog post already named.**
A banking respondent puts it in five words: "Why discover when I can create?" Code is
now cheap enough that searching for a reusable component can cost more than just writing a new
one, and they're blunt that this produces "many copies of very similar products." A US financial
services respondent independently confirms the damage: AI "has definitely led to a lot of re-implementation and
arbitrary uniqueness which has hurt InnerSource practices." A contact at a Brazilian e-commerce
platform has the concrete version of this failure: a team found the exact capability they needed
through the company's own AI-powered discovery tooling, and still built a duplicate from scratch
because contributing back felt harder than starting over. A great discovery layer doesn't fix
reuse if the incentive still points toward creation.

**A third group hasn't gotten to code reuse at all - because the foundation isn't there yet.**
Two automotive-sector respondents said flatly they don't use agents to crawl InnerSource repos.
A Japanese industrial conglomerate's sharpest respondent quantifies the gap: less than 1% of the company's design
and development knowledge is currently captured in their InnerSource environment, and "AI can make
existing knowledge easier to use, but it cannot retrieve knowledge that has not yet been shared or
documented." AI discovery is an amplifier of curation that already exists, not a substitute for it.

**The most interesting pattern is how many people answered "discover and reuse code" with
"discover and reuse knowledge" instead.** A banking respondent pivoted straight to documentation. Two respondents
from the same European auto supplier redirected Q1's code question to their AI-assisted documentation work. One respondent
stated the reframe outright: "the 'Source' in 'InnerSource' is evolving into a 'Source of
Knowledge,' a broad concept that encompasses source code as a subset." A smaller company's respondent's
succession story fits here too - when a long-time maintainer retired, the team fed all his
architectural context to AI so it could serve as the first tier of institutional memory in his
place. If this shift is real, the field's actual current win with AI isn't code reuse yet. It's
AI making the tacit knowledge behind InnerSource projects findable and reusable for the first time
- a precondition for code reuse, not a competitor to it.
