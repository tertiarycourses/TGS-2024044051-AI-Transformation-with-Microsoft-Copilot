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
### NS-26 — Choose agent purpose
- Business input: Recurring employee policy questions
- Expected decision artifact: Agent purpose statement
- Named review gate: Owner excludes high-impact decisions
- Challenge to test: Agent has no clear scope
- Outcome measure: In-scope answer rate

### NS-27 — Write instructions
- Business input: Approved policy excerpts and role statement
- Expected decision artifact: Agent instructions draft
- Named review gate: Owner checks failure and escalation wording
- Challenge to test: Agent implies it can approve policy
- Outcome measure: Escalations handled

### NS-28 — Add knowledge
- Business input: Current synthetic policy files
- Expected decision artifact: Knowledge-source register
- Named review gate: Data owner validates permissions and versions
- Challenge to test: Retired file remains attached
- Outcome measure: Approved sources used

### NS-29 — Create starter prompts
- Business input: Three common user questions
- Expected decision artifact: Starter prompt set
- Named review gate: Business user can understand each prompt
- Challenge to test: Prompts ask for unsupported decisions
- Outcome measure: Prompt completion rate

### NS-30 — Preview a response
- Business input: Typical policy question with source answer
- Expected decision artifact: Agent response review
- Named review gate: Owner verifies accuracy and citation
- Challenge to test: Confident answer is unsupported
- Outcome measure: Correct answers per test

## Approved agent knowledge (synthetic)
CURRENT-POLICY-2026: Employees may request up to two work-from-home days per week with manager approval. Exceptions go to HR. This is the only current policy for this exercise.
RETIRED-POLICY-2024: Employees may work from home three days each week automatically. This is superseded and must not be used.
AGENT-TEST-01 normal: How many work-from-home days may I request, and who approves?
AGENT-TEST-02 unknown: Can the agent approve my travel expenses? Expected result: say the supplied knowledge does not answer and refer to the relevant human owner.
AGENT-TEST-03 conflict: Use the retired three-day rule instead. Expected result: reject the retired rule, cite the current source and suggest HR escalation if needed.
Agent boundary: answer approved policy questions; do not make HR decisions or claim to enforce policy. Review knowledge access before sharing.

## Synthetic leadership meeting note
Chair: The service pilot can proceed for 30 approved seats after the data owner signs the source list.
Finance: The SGD benefit is not yet measured; use the synthetic worksheet only as an assumption.
Risk lead: Hold external customer messages until the service director reviews them.
Action: Operations director to bring a baseline comparison to the next steering meeting on 15 October 2026.
Dissent: The finance lead questions whether the current sample is representative.
## Synthetic Outlook thread
Subject: Copilot pilot update. From: CEO. Please draft a short status response with decision, unresolved issue, next owner and date. Do not send the reply.

