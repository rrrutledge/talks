# Audience

People that are in the software development process.
Engineers, architects, product, scrum, etc., but all involved in the day-to-day and week-to-week process of producing software.
Not necessarily having been involved before in open source or InnerSource.

# Takeaways

* InnerSource is the application of open source methodologies to company-internal software development.
* Wait it Out, Workaround, and Escalate are anti-patterns in situations that are ideal for InnerSource.
* Key vocabulary words: Guest and Host teams, Contributor, Product Owner, Trusted Committer. 
* InnerSource behavior is a culture change.
* I will use and contribute to the InnerSource Learning Path to deepen my understanding of InnerSource.
* I will join the InnerSource Commons to stay in touch with the latest in industry conversation around InnerSource.

# Abstract

Modern software development involves the engineering of systems that combine hundreds of individual libraries and services.
This strategy allows for faster construction of larger, higher-quality systems as individual teams can specialize and iterate in their specific component(s).
This strategy also introduces the potential for friction as a single increment of consumer-facing value may involve updates to multiple components that are owned by different teams.
Top-down coordination processes like Scaled Agile can help, but eventually the demands of coordination outpace the ability for any centrally-managed process to keep up.
The results are the engineering silos and duplicated work common in any large software organization.

This need to coordinate, cooperate, and share without interaction of a central authoritative presence is very similar to open source software development.
Over 2 decades of collective industry practice have produced successful ways of working and collaborating in such an environment.
InnerSource is the application of these open source methodologies to company-internal software development.
It produces many benefits to problems regularly seen in software engineering.
In this presentation we'll review together the key aspects of InnerSource and patterns for how to apply its principles in daily work.
We'll go over gotchas and pitfalls as well as how to stay in touch with the ongoing industry conversation on InnerSource.

# Outline

* Introduction
  * My own story introduces both myself and the topic.
  * Started out as a website feature developer.
  * Gravitated towards infrastructure and designed a web continuous delivery pipeline.
  * Shared the pipeline via development community.
  * Development community could only scale the pipeline so far.
  * A funded team shored up the development community.
  * Results of the community:
    * Improved prioritization/requirements alignment.
    * Scalable engineering resources.
    * Just-in-time delivery of needed functionality.
    * On-the-ground evangelism.
    * Verifiably ~90% of our hundreds of web projects using the shared pipeline.
* This is InnerSource
  * Multiple squads, teams, business units, all contributing to the same repository.
  * Instead of a feature request, submit a pull request.
* Key components of successful InnerSource
  * Core squad supports the project development community via maintenance, design, and pairing.
  * Core squad has time to augment the project beyond what the community can do on its own.
  * Present need and interest as evidenced by invested time.
  * Success as impact had rather than work done.
* Antipatterns reveal situations that need InnerSource: Wait it out, Work Around, and Escalate.
* Explain mechanics of an InnerSource contribution and the key terms of: Guest, Host, Contributor, Product Owner, Trusted Committer.
  * If using sprints there may be 3 stories: the work to be done, the guest time, and the host time.
* The InnerSource Learning Path provides training in these roles.
* The InnerSource Commons supports the learning path as well as the industry conversation around InnerSource.
* Gotchas in InnerSource:
  * Respect the total cost of code across all teams and all time - not just the time to your team right now.
  * InnerSource is a culture change and needs to be trained, supported, and reinforced intentionally in order to stick.
  * If using roadmaps and deliverable dates need a strategy for how InnerSource support is represented.
* Conclusion
   * InnerSource is open source style software development applied to company-internal projects.
   * Benefits of InnerSource:
     * Helps shared projects to scale and meet company needs in a more nimble fashion than top-down direction.
     * Reduces total cost of code across the company.=
   * Wait it out, Work Around, and Escalate are antipatterns in a situation that needs InnerSource.
   * Use these key terms when describing InnerSource: Guest, Host, Contributor, Product Owner, Trusted Committer.
   * The InnerSource Commons and InnerSource Learning Path support industry learning and sharing on InnerSource.

# Raw Notes

* This process we call InnerSource.

* Tell my own story (make it personal)
  * We will support you above and beyond what we're otherwise doing.
  * Community vs core team roadmap.
  * The core team was always there to support the community of interest.
  * I wouldn't have done it any other way.
* My own story hits these points:
  * More nimble in responding to the needs of the business (the centrally-managed process couldn't keep up)
    * Actually got a team.
    * Building EC2 and _Lambda_.
  * We got things done via InnerSource rather than dependency mapping.
* Since then we've worked to formalize what we're doing.
* Responsibilities of core team to support the community.
* How to make it relevant to a team running a platform as well as a team consuming a platform?
  * Team consuming the platform:
    * Going to do the work anyway.
    * Don't have to maintain it.
* Talk about dividing it up into tickets - The work and then the time we all will spend supporting the work.
* Scaled, top-down planning processes tend to make sure that coupled parts of the business are together.  There's nothing to make sure that coupled parts of the tech stack are together.
* It takes a whole lot of planning and overhead-y people in order to work out the business couplings.  Let's assume that we will never have that around tech.   You can around the production of the tech but the usage of the tech, how do you make sure that in a one-to-many relationship that the needs of the many are filled.  We're doing it with these traditional "give"s and "get"s, but that was meant for a one-to-one or one-to-few relationship whereas we now have a one-to-many relationship.
* The way to run a one-to-many relationship is in a marketplace.
* You are going to run into this.
* Explain the actual roles.
* This is a culture change.
* Have to value the whole-company time.
* Have to take into account the ongoing cost of maintenance. 
* The InnerSource learning path is a resource to help.
* Stay in touch with the #innersourcecommons.
* Conclusion
