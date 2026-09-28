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
### NS-21 — Check data access
- Business input: Two synthetic role-based document sets
- Expected decision artifact: Data boundary map
- Named review gate: Data owner approves sources and recipients
- Challenge to test: Restricted content reaches a broad channel
- Outcome measure: Unexpected access findings

### NS-22 — Verify source freshness
- Business input: Current and retired service rules
- Expected decision artifact: Source test record
- Named review gate: Current rule governs action
- Challenge to test: Retired rule triggers an action
- Outcome measure: Current-source rate

### NS-23 — Set approval responsibility
- Business input: Service, risk and IT roles
- Expected decision artifact: Plain-language responsibility card
- Named review gate: Each consequential action has an owner
- Challenge to test: Everyone assumes another team approves
- Outcome measure: Controls with named owners

### NS-24 — Plan incident response
- Business input: Synthetic misrouted notification
- Expected decision artifact: Incident response card
- Named review gate: Risk owner decides restart
- Challenge to test: Workflow continues after a failure
- Outcome measure: Time to pause

### NS-25 — Review workflow value
- Business input: Five sample requests and review minutes
- Expected decision artifact: Workflow pilot scorecard
- Named review gate: Include human review and error effort
- Challenge to test: Gross time saved is called net value
- Outcome measure: Net minutes per case

## Workflow test messages (synthetic)
WF-01 normal: From customer@example.test; subject Service request; case NS-1001; owner service.director@example.test; priority standard; request acknowledgement only.
WF-02 missing owner: From customer@example.test; subject Service request; case NS-1002; owner blank; priority standard. Expected result: hold and ask a human to assign an owner.
WF-03 conflicting priority: case NS-1003 says urgent in subject but standard in body. Expected result: hold for human review.
Workflow guardrail: the draft may be saved or routed internally, but no external acknowledgement is sent without service-director approval.
Record trigger, input fields, action, recipient, reviewer, failed test and activation status. This is synthetic design data, not evidence of a live workflow.

