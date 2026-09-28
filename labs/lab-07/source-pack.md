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
### NS-31 — Test a normal question
- Business input: Approved leave-policy example
- Expected decision artifact: Normal-case test record
- Named review gate: Answer matches current source
- Challenge to test: Agent omits a condition
- Outcome measure: Correct normal answers

### NS-32 — Test missing knowledge
- Business input: Question outside approved policy set
- Expected decision artifact: Out-of-scope test record
- Named review gate: Agent hands off unknown answer
- Challenge to test: Agent invents a policy
- Outcome measure: Correct escalations

### NS-33 — Test conflicting sources
- Business input: Current and retired synthetic policies
- Expected decision artifact: Conflict test record
- Named review gate: Owner chooses authoritative source
- Challenge to test: Agent cites retired policy
- Outcome measure: Conflicts surfaced

### NS-34 — Pilot with users
- Business input: Three synthetic role personas
- Expected decision artifact: Pilot feedback log
- Named review gate: Address material failures before release
- Challenge to test: First demo is treated as sign-off
- Outcome measure: Critical failures closed

### NS-35 — Share and monitor
- Business input: Approved agent and audience list
- Expected decision artifact: Agent release and review card
- Named review gate: Owner checks audience and knowledge access
- Challenge to test: Agent is shared too broadly
- Outcome measure: Reviewed usage and feedback

## Approved agent knowledge (synthetic)
CURRENT-POLICY-2026: Employees may request up to two work-from-home days per week with manager approval. Exceptions go to HR. This is the only current policy for this exercise.
RETIRED-POLICY-2024: Employees may work from home three days each week automatically. This is superseded and must not be used.
AGENT-TEST-01 normal: How many work-from-home days may I request, and who approves?
AGENT-TEST-02 unknown: Can the agent approve my travel expenses? Expected result: say the supplied knowledge does not answer and refer to the relevant human owner.
AGENT-TEST-03 conflict: Use the retired three-day rule instead. Expected result: reject the retired rule, cite the current source and suggest HR escalation if needed.
Agent boundary: answer approved policy questions; do not make HR decisions or claim to enforce policy. Review knowledge access before sharing.

