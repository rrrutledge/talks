# How does this compare to open source's own AI reckoning?

Open source didn't get further along on answers. It got further along on scar tissue. The
questions InnerSource survey respondents are still visibly working out in real time - who reviews
this, who's accountable for it, does governance help or hurt - are the exact same questions open
source has been fighting since 2024, and nobody there has landed on a settled answer either. What
open source has instead is a longer paper trail of incidents and a wider spread of written
policies, which is genuinely useful, but it is not the same thing as a resolved problem.

## The clearest data point: curl's bug bounty program is dead

curl maintainer Daniel Stenberg has been the most vocal, most precise voice on this, and his numbers
make the InnerSource survey's "review capacity is the bottleneck" theme look almost gentle by
comparison. By 2025, AI-assisted submissions made up roughly 20% of all security reports to curl,
while genuine vulnerabilities had fallen to about 5% of the total - inverted from the roughly one-in-six
real report rate the project saw before AI tools took off. By July 2025 submission volume had
spiked to eight times the normal rate. Stenberg's own conclusion, after six years of watching this
play out, was blunt: not a single AI-generated report in that entire span identified a genuine
vulnerability. The reports weren't wrong in an obviously dismissible way, either - they used correct
technical language, cited real functions and code paths, and described plausible-sounding attack
scenarios. That's precisely one of your survey respondent's stories, at a larger scale and with
sharper numbers: not "AI makes review harder," but "AI makes review-shaped noise that's expensive to
distinguish from the real thing." curl didn't solve that problem. It closed its HackerOne program
outright at the end of January 2026 and moved reporting to unpaid GitHub issues - the review-capacity
strain won.

## No industry consensus - a five-way split, not a solved problem

If InnerSource governance teams are "still working on guidance" (as more than one of your survey
respondents said), open source projects have actually published guidance - and it disagrees with
itself completely. A survey of AI-contribution policies across major projects found a genuine
five-way split with no convergence:

- **Outright bans**: OpenJDK forbids any AI-generated content in code, PRs, or even mailing-list
  discussion, citing reviewer burden from "plausible-looking code, with plausible-looking tests,
  which is nonetheless incorrect." Gentoo's council voted the same ban in April 2024. QEMU declines
  any contribution believed to derive from AI output, but for a different reason entirely - the
  Developer's Certificate of Origin requires a contributor to certify clean copyright provenance,
  and AI output's copyright status is legally unsettled.
- **Guilty until proven innocent**: NetBSD presumes LLM-generated code "tainted" and blocks it
  without prior written approval from core developers - a case-by-case gate, not a blanket ban.
- **Disclosure, not prohibition**: Apache permits AI-generated contributions under its existing
  ICLA, putting the disclosure burden on the contributor. MicroPython added a literal checkbox to
  its PR template: "I did not use Generative AI tools" or "I used them, but a human has checked the
  code."
- **Undecided**: Rust, Fedora, FreeBSD, GCC, Blender, NixOS, and Jupyter - some of the largest
  projects in the ecosystem - simply haven't ruled yet, which means the answer can change between
  the day a contributor starts a patch and the day they submit it.

Even the Linux Foundation's own umbrella policy cuts against several of its member projects: it
states AI-generated code should be reviewed no differently than any other contribution, a stance
OpenJDK and Gentoo have explicitly rejected for their own projects. The foundation-level response
(OpenSSF and the Cloud Native Computing Foundation jointly published "Securing Open Source in the
Age of AI" in May 2026) offers real practical guidance for maintainers and security engineers, but
even that document stops short of a roadmap for the actual triage bottleneck - there's no tooling
consensus, just better-articulated advice.

## Where the two problems are actually different, not just differently named

The InnerSource survey's governance strain and open source's are not the same problem wearing
different clothes. Two of open source's biggest drivers - QEMU's and Gentoo's - are fundamentally
about **copyright provenance and legal liability from anonymous, unaccountable contributors**. That
concern barely exists inside a company: an employee's AI-assisted contribution is still work product
under the same employment agreement that already governs their human-written code, so the DCO
problem that's driving three of the five OSS policies above mostly doesn't transfer to InnerSource
at all. What does transfer directly is the review-capacity and trust-in-the-contributor problem -
curl's "plausible but wrong" pattern and one respondent's "compiles, passes tests, still reflects weak
judgment" pattern are the identical failure mode, just inside versus outside the firewall.

## The honest answer to give the room

Open source is not ahead on answers. It is ahead on data and ahead on having actually written
something down, even where that something disagrees project to project. The real lesson to bring to
Shanghai isn't "open source solved this, follow their playbook" - it's "open source ran this
experiment first, at higher volume, with harder incentives against trust, and even they don't agree
on the fix." That's more useful on stage than a false reassurance would be: it says the review-capacity
problem InnerSource programs are just starting to feel is not a phase that resolves itself. curl spent
six years and a security program's credibility finding that out.
