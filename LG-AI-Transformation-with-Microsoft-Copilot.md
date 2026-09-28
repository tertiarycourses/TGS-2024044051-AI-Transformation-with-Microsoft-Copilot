# AI Transformation with Microsoft Copilot — Learner Guide
TGS-2024044051 · v3.0 · 28 September 2026

## Learning outcomes
- LO1: Develop technology implementation plans and business processes for Microsoft Copilot.
- LO2: Develop control procedures for Microsoft Copilot to manage security.
- LO3: Evaluate the integration of Microsoft Copilot to ensure alignment with business objectives.
- LO4: Develop optimization plans for Microsoft Copilot to improve business operations.

## Topic 1: Use Microsoft 365 Copilot for everyday business work

Official reference: https://learn.microsoft.com/en-us/credentials/certifications/ai-business-professional/

### 01. Choose a service outcome
- Input: Service response baseline and customer feedback
- Method: Use Microsoft 365 Copilot Chat to identify a bounded opportunity
- Output: Pilot opportunity statement
- Control: Sponsor confirms outcome and owner
- Failure test: AI use is mistaken for customer benefit
- Measure: Comparable response time
- Practice: [Lab 01](labs/lab-01/README.md)

### 02. Ask a useful question
- Input: A vague request to improve service
- Method: Add audience, task, source, constraints and output to a Copilot prompt
- Output: Reusable work prompt
- Control: Manager confirms the prompt answers the real question
- Failure test: Polished response has no decision value
- Measure: Relevant answers per review
- Practice: [Lab 01](labs/lab-01/README.md)

### 03. Ground a chat answer
- Input: Current service policy and two case notes
- Method: Ask Copilot Chat to answer from the supplied source
- Output: Sourced response summary
- Control: Check every material statement against the source
- Failure test: An unsupported claim is repeated
- Measure: Verified claims per sample
- Practice: [Lab 01](labs/lab-01/README.md)

### 04. Compare options in Chat
- Input: Three possible pilot processes
- Method: Ask Copilot for benefits, trade-offs and missing evidence
- Output: Option comparison
- Control: Use the same criteria for all options
- Failure test: The preferred option receives easier criteria
- Measure: Options with complete evidence
- Practice: [Lab 01](labs/lab-01/README.md)

### 05. Share a Copilot Page
- Input: A reviewed team decision summary
- Method: Move approved ideas into a Copilot Page or offline shared brief
- Output: Shared planning page
- Control: Owner checks content and access before sharing
- Failure test: Draft assumptions are shown as decisions
- Measure: Open questions assigned
- Practice: [Lab 01](labs/lab-01/README.md)

### 06. Draft a Word brief
- Input: Approved pilot notes and service baseline
- Method: Use Copilot in Word to draft a two-page decision brief
- Output: Reviewed Word brief
- Control: Sponsor checks numbers and recommendation
- Failure test: Copilot invents a benefit estimate
- Measure: Verified material claims
- Practice: [Lab 02](labs/lab-02/README.md)

### 07. Refine executive tone
- Input: A rough draft for a leadership audience
- Method: Ask Copilot in Word to shorten and clarify the recommendation
- Output: Concise executive summary
- Control: Human owner signs the final message
- Failure test: Important caveat disappears
- Measure: Decisions understood in review
- Practice: [Lab 02](labs/lab-02/README.md)

### 08. Create board slides
- Input: Approved Word brief and baseline chart
- Method: Use Copilot in PowerPoint to create a five-slide decision story
- Output: Board presentation
- Control: Trace every chart to approved values
- Failure test: Slide claim exceeds the source
- Measure: Figures checked before review
- Practice: [Lab 02](labs/lab-02/README.md)

### 09. Draft Outlook update
- Input: Approved pilot decision and open actions
- Method: Use Copilot in Outlook to prepare a status message
- Output: Unsent status draft
- Control: Sponsor approves recipients and commitments
- Failure test: An unapproved promise is sent
- Measure: Messages approved before sending
- Practice: [Lab 02](labs/lab-02/README.md)

### 10. Use Researcher carefully
- Input: Synthetic policy and market question
- Method: Use Researcher if available to gather sources, or compare supplied documents
- Output: Source and uncertainty list
- Control: Validate dates, claims and relevance
- Failure test: Research summary treats weak source as fact
- Measure: Sources verified
- Practice: [Lab 02](labs/lab-02/README.md)

### 11. Explore Excel data
- Input: Synthetic monthly service-volume workbook
- Method: Ask Copilot in Excel to surface patterns and outliers
- Output: Trend summary
- Control: Check chart and denominator against workbook
- Failure test: An outlier is presented as a trend
- Measure: Patterns confirmed
- Practice: [Lab 03](labs/lab-03/README.md)

### 12. Build a simple chart
- Input: Synthetic before-and-after service table
- Method: Use Copilot in Excel to propose a clear chart
- Output: Annotated comparison chart
- Control: Use comparable periods and units
- Failure test: Axis hides change or variation
- Measure: Correctly labelled charts
- Practice: [Lab 03](labs/lab-03/README.md)

### 13. Prepare a Teams meeting
- Input: Pilot objective, questions and decision owner
- Method: Use Copilot to prepare a concise meeting agenda
- Output: Decision agenda
- Control: Chair confirms questions and owner
- Failure test: Meeting has no decision to make
- Measure: Decisions reached
- Practice: [Lab 03](labs/lab-03/README.md)

### 14. Review meeting recap
- Input: Synthetic Teams transcript and dissent note
- Method: Use Copilot in Teams to summarize decisions and actions
- Output: Validated action log
- Control: Chair checks speakers, owners and dates
- Failure test: Action is attributed to wrong person
- Measure: Actions confirmed
- Practice: [Lab 03](labs/lab-03/README.md)

### 15. Follow up after meeting
- Input: Validated action log and unresolved questions
- Method: Use Copilot Chat or Outlook to draft an unsent follow-up
- Output: Reviewed follow-up message
- Control: Owner approves external distribution
- Failure test: Dissent or hold condition is omitted
- Measure: Actions closed on time
- Practice: [Lab 03](labs/lab-03/README.md)

## Topic 2: Design safe Copilot Workflows and human controls

Official reference: https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-workflows-in-microsoft-365-copilot

### 16. Spot a repeatable handoff
- Input: Synthetic email requests and missed deadlines
- Method: Describe a Microsoft 365 Copilot Workflows opportunity in plain language
- Output: Workflow opportunity card
- Control: Process owner confirms a repeatable trigger
- Failure test: One-off judgment is automated
- Measure: Handoff time
- Practice: [Lab 04](labs/lab-04/README.md)

### 17. Define trigger and result
- Input: Service request email with fictional fields
- Method: Ask Workflows to draft trigger, steps and intended output
- Output: Trigger-to-result map
- Control: Owner verifies trigger is precise
- Failure test: Wrong message starts workflow
- Measure: Correctly triggered cases
- Practice: [Lab 04](labs/lab-04/README.md)

### 18. Add review step
- Input: Draft acknowledgement and case summary
- Method: Ask Workflows to route draft for human approval
- Output: Human review gate
- Control: No external commitment before approval
- Failure test: Message sends without review
- Measure: Unapproved sends
- Practice: [Lab 04](labs/lab-04/README.md)

### 19. Test exceptions
- Input: Missing case owner and contradictory priority
- Method: Test workflow with normal and exception examples
- Output: Test and exception log
- Control: Hold unknown owner or conflicting input
- Failure test: Exception is silently routed
- Measure: Exceptions detected
- Practice: [Lab 04](labs/lab-04/README.md)

### 20. Decide to activate
- Input: Workflow test record and accountable owner
- Method: Review Workflows draft, permissions and run history before enabling
- Output: Go or hold record
- Control: Owner approves live activation in authorised tenant
- Failure test: Simulation is described as deployed
- Measure: Approved runs
- Practice: [Lab 04](labs/lab-04/README.md)

### 21. Check data access
- Input: Two synthetic role-based document sets
- Method: Review what a workflow can read and where output goes
- Output: Data boundary map
- Control: Data owner approves sources and recipients
- Failure test: Restricted content reaches a broad channel
- Measure: Unexpected access findings
- Practice: [Lab 05](labs/lab-05/README.md)

### 22. Verify source freshness
- Input: Current and retired service rules
- Method: Test the draft workflow against both versions
- Output: Source test record
- Control: Current rule governs action
- Failure test: Retired rule triggers an action
- Measure: Current-source rate
- Practice: [Lab 05](labs/lab-05/README.md)

### 23. Set approval responsibility
- Input: Service, risk and IT roles
- Method: Assign who reviews, pauses and restores a workflow
- Output: Plain-language responsibility card
- Control: Each consequential action has an owner
- Failure test: Everyone assumes another team approves
- Measure: Controls with named owners
- Practice: [Lab 05](labs/lab-05/README.md)

### 24. Plan incident response
- Input: Synthetic misrouted notification
- Method: Write a pause, contain, notify and retest path
- Output: Incident response card
- Control: Risk owner decides restart
- Failure test: Workflow continues after a failure
- Measure: Time to pause
- Practice: [Lab 05](labs/lab-05/README.md)

### 25. Review workflow value
- Input: Five sample requests and review minutes
- Method: Compare manual and assisted handoff times
- Output: Workflow pilot scorecard
- Control: Include human review and error effort
- Failure test: Gross time saved is called net value
- Measure: Net minutes per case
- Practice: [Lab 05](labs/lab-05/README.md)

## Topic 3: Create and test bounded Copilot agents

Official reference: https://support.microsoft.com/en-us/microsoft-365-copilot/build-your-own-agent-with-microsoft-365-copilot

### 26. Choose agent purpose
- Input: Recurring employee policy questions
- Method: Define one bounded use for Copilot Agent Builder
- Output: Agent purpose statement
- Control: Owner excludes high-impact decisions
- Failure test: Agent has no clear scope
- Measure: In-scope answer rate
- Practice: [Lab 06](labs/lab-06/README.md)

### 27. Write instructions
- Input: Approved policy excerpts and role statement
- Method: Describe audience, task, boundaries and escalation in Agent Builder
- Output: Agent instructions draft
- Control: Owner checks failure and escalation wording
- Failure test: Agent implies it can approve policy
- Measure: Escalations handled
- Practice: [Lab 06](labs/lab-06/README.md)

### 28. Add knowledge
- Input: Current synthetic policy files
- Method: Attach approved knowledge sources in Agent Builder
- Output: Knowledge-source register
- Control: Data owner validates permissions and versions
- Failure test: Retired file remains attached
- Measure: Approved sources used
- Practice: [Lab 06](labs/lab-06/README.md)

### 29. Create starter prompts
- Input: Three common user questions
- Method: Write clear starter prompts for the agent
- Output: Starter prompt set
- Control: Business user can understand each prompt
- Failure test: Prompts ask for unsupported decisions
- Measure: Prompt completion rate
- Practice: [Lab 06](labs/lab-06/README.md)

### 30. Preview a response
- Input: Typical policy question with source answer
- Method: Test the agent preview and compare to source
- Output: Agent response review
- Control: Owner verifies accuracy and citation
- Failure test: Confident answer is unsupported
- Measure: Correct answers per test
- Practice: [Lab 06](labs/lab-06/README.md)

### 31. Test a normal question
- Input: Approved leave-policy example
- Method: Ask the agent for a bounded answer
- Output: Normal-case test record
- Control: Answer matches current source
- Failure test: Agent omits a condition
- Measure: Correct normal answers
- Practice: [Lab 07](labs/lab-07/README.md)

### 32. Test missing knowledge
- Input: Question outside approved policy set
- Method: Ask the agent to state uncertainty and escalation
- Output: Out-of-scope test record
- Control: Agent hands off unknown answer
- Failure test: Agent invents a policy
- Measure: Correct escalations
- Practice: [Lab 07](labs/lab-07/README.md)

### 33. Test conflicting sources
- Input: Current and retired synthetic policies
- Method: Challenge the agent with contradictory evidence
- Output: Conflict test record
- Control: Owner chooses authoritative source
- Failure test: Agent cites retired policy
- Measure: Conflicts surfaced
- Practice: [Lab 07](labs/lab-07/README.md)

### 34. Pilot with users
- Input: Three synthetic role personas
- Method: Run a small acceptance review before sharing
- Output: Pilot feedback log
- Control: Address material failures before release
- Failure test: First demo is treated as sign-off
- Measure: Critical failures closed
- Practice: [Lab 07](labs/lab-07/README.md)

### 35. Share and monitor
- Input: Approved agent and audience list
- Method: Review Agent Builder sharing and ongoing feedback plan
- Output: Agent release and review card
- Control: Owner checks audience and knowledge access
- Failure test: Agent is shared too broadly
- Measure: Reviewed usage and feedback
- Practice: [Lab 07](labs/lab-07/README.md)

## Topic 4: Lead adoption, measure value and scale outcomes

Official reference: https://learn.microsoft.com/en-us/credentials/certifications/ai-transformation-leader/

### 36. Map a work journey
- Input: Chat, workflow and agent opportunities
- Method: Show where each Copilot mode helps in one service journey
- Output: Future-state journey map
- Control: Keep human decisions visible
- Failure test: The same task is duplicated
- Measure: Time to completion
- Practice: [Lab 08](labs/lab-08/README.md)

### 37. Choose a first cohort
- Input: Thirty synthetic seats across three teams
- Method: Prioritize roles with useful work and manager support
- Output: Pilot cohort plan
- Control: Sponsor signs selection criteria
- Failure test: Licence count replaces opportunity
- Measure: Productive pilot users
- Practice: [Lab 08](labs/lab-08/README.md)

### 38. Prepare managers
- Input: Role questions and practice needs
- Method: Draft a manager briefing with Copilot in Word
- Output: Manager enablement brief
- Control: Managers can explain limits and outcomes
- Failure test: Training only shows features
- Measure: Practice completion
- Practice: [Lab 08](labs/lab-08/README.md)

### 39. Collect user feedback
- Input: Synthetic comments from first two weeks
- Method: Use Copilot Chat to group friction and successes
- Output: Improvement backlog
- Control: Assign an owner and due date
- Failure test: Complaints about bad sources are called prompt errors
- Measure: Issues closed
- Practice: [Lab 08](labs/lab-08/README.md)

### 40. Set scale gate
- Input: Adoption, quality and risk observations
- Method: Define go, hold and stop conditions
- Output: Scale decision checklist
- Control: Critical failure blocks scale
- Failure test: Average score hides severe error
- Measure: Required gates passed
- Practice: [Lab 08](labs/lab-08/README.md)

### 41. Measure time honestly
- Input: Baseline, assisted and review minutes
- Method: Use Copilot in Excel to explain net minutes saved
- Output: Net-time table
- Control: Check formulas and comparable work
- Failure test: Review time is omitted
- Measure: Net minutes per task
- Practice: [Lab 09](labs/lab-09/README.md)

### 42. Measure quality
- Input: Sample drafts and correction log
- Method: Use Copilot to summarize error types
- Output: Quality scorecard
- Control: Critical error is reported separately
- Failure test: Average quality hides material failure
- Measure: Critical errors per sample
- Practice: [Lab 09](labs/lab-09/README.md)

### 43. Measure adoption
- Input: Seat assignments and actual useful sessions
- Method: Compare licence, activity and productive use
- Output: Adoption chart
- Control: Define productive use per role
- Failure test: Seats are presented as adoption
- Measure: Productive users per cohort
- Practice: [Lab 09](labs/lab-09/README.md)

### 44. Estimate total cost
- Input: Synthetic licensing, training and review costs
- Method: Compare costs and benefits with Excel
- Output: Scenario table
- Control: Label assumptions and sensitivity
- Failure test: Licence is the only cost
- Measure: Cost per verified outcome
- Practice: [Lab 09](labs/lab-09/README.md)

### 45. Decide investment
- Input: Value, quality and risk records
- Method: Draft a fund, hold or stop note in Word
- Output: Investment decision memo
- Control: Sponsor signs conditions
- Failure test: Optimistic forecast is described as measured
- Measure: Conditions met
- Practice: [Lab 09](labs/lab-09/README.md)

### 46. Prioritize use cases
- Input: Five candidate Copilot opportunities
- Method: Rank outcome, readiness, risk and owner
- Output: Opportunity portfolio
- Control: Reject ownerless opportunity
- Failure test: Highest volume is treated as highest value
- Measure: Validated value per case
- Practice: [Lab 10](labs/lab-10/README.md)

### 47. Design ninety days
- Input: Pilot observations and manager capacity
- Method: Sequence chat, workflow and agent waves
- Output: Ninety-day roadmap
- Control: Each wave has owner and gate
- Failure test: Rollout outruns support
- Measure: Wave gates met
- Practice: [Lab 10](labs/lab-10/README.md)

### 48. Tell the board
- Input: Verified pilot outcome and open risks
- Method: Use Copilot in PowerPoint to draft a board update
- Output: Board scorecard
- Control: Every claim has source and date
- Failure test: Risk disappears from narrative
- Measure: Claims traceable
- Practice: [Lab 10](labs/lab-10/README.md)

### 49. Challenge the case
- Input: A confident recommendation and downside scenario
- Method: Ask Copilot Chat for counterarguments
- Output: Decision challenge log
- Control: Executive answers strongest objection
- Failure test: Polished demo substitutes for evidence
- Measure: Objections resolved
- Practice: [Lab 10](labs/lab-10/README.md)

### 50. Make the call
- Input: Portfolio, roadmap and scorecard
- Method: Record the sponsor go, hold or stop decision
- Output: Signed transformation decision
- Control: Owner names next review date
- Failure test: Decision has no accountable owner
- Measure: Conditions met on time
- Practice: [Lab 10](labs/lab-10/README.md)
