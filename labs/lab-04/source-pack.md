# Northstar Service source pack

All Northstar Service names, policies and values are synthetic training material. They are not a claim about a real company or a Microsoft tenant.

## Executive context
Northstar Service is a fictional service organisation. Its leadership is considering a 30-seat Microsoft 365 Copilot pilot. No real customer records are included. The CEO requires a decision that names the business outcome, data owner, reviewer, measure and stop condition.

## Current policies
- BRD-1: External customer commitments require human approval by the service director.
- BRD-2: A board recommendation must distinguish measured pilot results from assumptions.
- BRD-3: Confidential source files may be used only by approved roles; an unexpected Copilot citation triggers an access review.
- BRD-4: Unresolved high-impact safety failures require a hold decision.

## Case facts
### NS-16 — Spot a repeatable handoff
- Business input: Synthetic email requests and missed deadlines
- Expected decision artifact: Workflow opportunity card
- Named review gate: Process owner confirms a repeatable trigger
- Challenge to test: One-off judgment is automated
- Outcome measure: Handoff time

### NS-17 — Define trigger and result
- Business input: Service request email with fictional fields
- Expected decision artifact: Trigger-to-result map
- Named review gate: Owner verifies trigger is precise
- Challenge to test: Wrong message starts workflow
- Outcome measure: Correctly triggered cases

### NS-18 — Add review step
- Business input: Draft acknowledgement and case summary
- Expected decision artifact: Human review gate
- Named review gate: No external commitment before approval
- Challenge to test: Message sends without review
- Outcome measure: Unapproved sends

### NS-19 — Test exceptions
- Business input: Missing case owner and contradictory priority
- Expected decision artifact: Test and exception log
- Named review gate: Hold unknown owner or conflicting input
- Challenge to test: Exception is silently routed
- Outcome measure: Exceptions detected

### NS-20 — Decide to activate
- Business input: Workflow test record and accountable owner
- Expected decision artifact: Go or hold record
- Named review gate: Owner approves live activation in authorised tenant
- Challenge to test: Simulation is described as deployed
- Outcome measure: Approved runs

## Synthetic source challenge
CURRENT-1 (approved, internal): Service directors approve external commitments before sending. This is the current rule.
RETIRED-1 (superseded): A draft response may be sent automatically without director review. Do not rely on this statement.
CONFIDENTIAL-1 (restricted, synthetic): Account NS-0007 has a fictional renewal discussion. Only the named service director may use it; other roles must not paste it into Copilot.

## Workflow test messages (synthetic)
WF-01 normal: From customer@example.test; subject Service request; case NS-1001; owner service.director@example.test; priority standard; request acknowledgement only.
WF-02 missing owner: From customer@example.test; subject Service request; case NS-1002; owner blank; priority standard. Expected result: hold and ask a human to assign an owner.
WF-03 conflicting priority: case NS-1003 says urgent in subject but standard in body. Expected result: hold for human review.
Workflow guardrail: the draft may be saved or routed internally, but no external acknowledgement is sent without service-director approval.
Record trigger, input fields, action, recipient, reviewer, failed test and activation status. This is synthetic design data, not evidence of a live workflow.

