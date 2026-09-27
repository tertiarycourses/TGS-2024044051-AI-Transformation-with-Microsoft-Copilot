# AI Transformation with Microsoft Copilot — Learner Guide
TGS-2024044051 · v1.0 · 27 September 2026

## Learning outcomes
- LO1: Develop technology implementation plans and business processes for Microsoft Copilot.
- LO2: Develop control procedures for Microsoft Copilot to manage security.
- LO3: Evaluate the integration of Microsoft Copilot to ensure alignment with business objectives.
- LO4: Develop optimization plans for Microsoft Copilot to improve business operations.

## Topic 1: Microsoft 365 Copilot Implementation and Business Process Transformation

Official reference: https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-architecture

### 01. Tenant readiness
- Input: Microsoft 365 tenant inventory
- Method: Check identities, data estate and licensed workload availability
- Output: Readiness register with owner and gap
- Control: Admin signs off app and data prerequisites
- Failure test: Licensed user lacks a supported app or data source
- Measure: Eligible users divided by target users
- Practice: [Lab 01](labs/lab-01/README.md)

### 02. License allocation
- Input: 30 pilot seats and role list
- Method: Match entitlement to high-frequency document tasks
- Output: License assignment and cohort list
- Control: Approve seats against role and cost center
- Failure test: Seat assigned but service plan disabled
- Measure: Active pilot users divided by assigned seats
- Practice: [Lab 01](labs/lab-01/README.md)

### 03. Graph permission scope
- Input: SharePoint file ACL and test identities
- Method: Compare search results under user A and user B
- Output: Access matrix with allowed files
- Control: Least privilege and owner review
- Failure test: Overshared file appears in both result sets
- Measure: Unexpected accessible files count
- Practice: [Lab 01](labs/lab-01/README.md)

### 04. Business-process mapping
- Input: Service request intake with six handoffs
- Method: Mark drafting, lookup and approval steps
- Output: Current-to-future swimlane
- Control: Keep human approval on customer-facing send
- Failure test: Automation bypasses approval
- Measure: Median handoff time in minutes
- Practice: [Lab 01](labs/lab-01/README.md)

### 05. Opportunity scoring
- Input: Ten candidate workflows
- Method: Score volume, time, data quality and risk
- Output: Ranked use-case backlog
- Control: Reject use case with ungoverned sensitive data
- Failure test: High score hides missing data owner
- Measure: Weighted score per use case
- Practice: [Lab 01](labs/lab-01/README.md)

### 06. Prompt context window
- Input: Customer email and policy excerpts
- Method: Separate task, context, constraints and format
- Output: Reusable prompt card
- Control: Never paste personal data into unmanaged chat
- Failure test: Answer omits policy exception
- Measure: Grounded claims divided by claims
- Practice: [Lab 02](labs/lab-02/README.md)

### 07. Grounded retrieval
- Input: Approved policy file and user query
- Method: Retrieve accessible passages before generation
- Output: Answer with source citations
- Control: Verify source version and user permission
- Failure test: Citation points to superseded policy
- Measure: Supported answer statements divided by total
- Practice: [Lab 02](labs/lab-02/README.md)

### 08. Word proposal draft
- Input: Synthetic service improvement brief
- Method: Generate structure then compare to source register
- Output: Draft proposal with evidence comments
- Control: Human owns final facts and approval
- Failure test: Unsupported cost claim enters draft
- Measure: Verified claims divided by total claims
- Practice: [Lab 02](labs/lab-02/README.md)

### 09. Excel service analysis
- Input: Synthetic ticket table: 120 rows
- Method: Aggregate cycle time by issue category
- Output: Pivot table and chart
- Control: Check formula range and outliers
- Failure test: Blank dates skew mean
- Measure: Median cycle time by category
- Practice: [Lab 02](labs/lab-02/README.md)

### 10. PowerPoint executive story
- Input: Approved Word findings and Excel chart
- Method: Create a three-message decision deck
- Output: Five-slide review deck
- Control: Presenter validates every number
- Failure test: Chart title and source mismatch
- Measure: Correct figures divided by checked figures
- Practice: [Lab 02](labs/lab-02/README.md)

### 11. Outlook response workflow
- Input: Synthetic customer escalation email
- Method: Draft acknowledgement and response options
- Output: Reviewed reply with owner and deadline
- Control: Send remains a human action
- Failure test: Tone implies an unapproved commitment
- Measure: Replies with explicit next owner
- Practice: [Lab 03](labs/lab-03/README.md)

### 12. Teams meeting synthesis
- Input: Synthetic transcript with actions
- Method: Extract decisions, dissent and open questions
- Output: Action register with timestamps
- Control: Meeting owner confirms transcript accuracy
- Failure test: Speaker attribution is wrong
- Measure: Confirmed actions divided by extracted actions
- Practice: [Lab 03](labs/lab-03/README.md)

### 13. Adoption rollout
- Input: Three departments and pilot feedback
- Method: Sequence champions, learning and support
- Output: 30-60-90 day rollout plan
- Control: Gate wave two on measured quality
- Failure test: Low adoption despite licenses
- Measure: Weekly active usage by cohort
- Practice: [Lab 03](labs/lab-03/README.md)

## Topic 2: Microsoft Copilot Administration, Security and Responsible AI

Official reference: https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-faq

### 14. Identity and MFA
- Input: User roles and sign-in policy
- Method: Require appropriate identity assurance
- Output: Conditional-access decision log
- Control: Security team owns exception process
- Failure test: Shared account bypasses attribution
- Measure: Protected sign-ins divided by sign-ins
- Practice: [Lab 03](labs/lab-03/README.md)

### 15. Sensitivity labels
- Input: Public, internal and confidential files
- Method: Map labels to sharing and Copilot exposure
- Output: Label policy matrix
- Control: Data owner reviews label changes
- Failure test: Confidential file labelled public
- Measure: Mislabelled sampled files count
- Practice: [Lab 03](labs/lab-03/README.md)

### 16. DLP boundaries
- Input: Prompt containing synthetic account number
- Method: Block or warn for restricted data movement
- Output: DLP test evidence
- Control: Policy owner approves exceptions
- Failure test: Sensitive output leaves approved boundary
- Measure: Blocked risky attempts per test set
- Practice: [Lab 04](labs/lab-04/README.md)

### 17. SharePoint oversharing
- Input: Site members, visitors and anonymous links
- Method: Review inherited access and link types
- Output: Remediation ticket list
- Control: Owner removes broad access before pilot
- Failure test: Copilot surfaces a broadly shared secret
- Measure: High-risk links remediated
- Practice: [Lab 04](labs/lab-04/README.md)

### 18. Retention and records
- Input: Contract lifecycle and retention schedule
- Method: Apply record class to source documents
- Output: Retention decision table
- Control: Records officer approves disposal
- Failure test: Old draft retrieved as current policy
- Measure: Current-version retrieval rate
- Practice: [Lab 04](labs/lab-04/README.md)

### 19. Audit event trail
- Input: Agent action and user identity
- Method: Capture time, actor, source and action
- Output: Traceable audit record
- Control: Admin preserves logs per policy
- Failure test: Action cannot be attributed to a user
- Measure: Trace-complete actions divided by actions
- Practice: [Lab 04](labs/lab-04/README.md)

### 20. Prompt-injection boundary
- Input: Document with an embedded hostile instruction
- Method: Treat retrieved text as data, not instruction
- Output: Injection test and refusal trace
- Control: Tool action requires explicit authorization
- Failure test: Agent follows source text as a command
- Measure: Injected commands ignored per test set
- Practice: [Lab 04](labs/lab-04/README.md)

### 21. Fabrication review
- Input: Answer with five factual claims
- Method: Check each claim against current citations
- Output: Claim-verification worksheet
- Control: Human reviewer signs high-impact output
- Failure test: Plausible unsupported number survives
- Measure: Supported claims divided by claims
- Practice: [Lab 05](labs/lab-05/README.md)

### 22. Tool permission design
- Input: Read and write connector scopes
- Method: Separate read-only pilot from write actions
- Output: Permission grant register
- Control: Entra admin consents only minimum scope
- Failure test: Write tool used in a read workflow
- Measure: Unused privileged grants count
- Practice: [Lab 05](labs/lab-05/README.md)

### 23. Environment policy
- Input: Dev, test and production environments
- Method: Apply connector and publishing policy
- Output: Environment control matrix
- Control: Promote only after test evidence
- Failure test: Maker publishes from unrestricted default
- Measure: Policy violations by environment
- Practice: [Lab 05](labs/lab-05/README.md)

### 24. Incident response
- Input: Synthetic disclosure report
- Method: Contain, preserve evidence, notify owner
- Output: Incident timeline and action log
- Control: Security owner determines escalation
- Failure test: Evidence lost during agent disable
- Measure: Time to containment in minutes
- Practice: [Lab 05](labs/lab-05/README.md)

### 25. Human decision gate
- Input: Draft customer refund recommendation
- Method: Require reviewer before irreversible action
- Output: Approval record with rationale
- Control: Named business owner signs release
- Failure test: Workflow auto-issues refund
- Measure: Unapproved actions count
- Practice: [Lab 05](labs/lab-05/README.md)

## Topic 3: Copilot Integration, AI Agents and Cross-Platform Workflows

Official reference: https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-improve

### 26. Agent purpose contract
- Input: Helpdesk scope and user intents
- Method: Define allowed requests and refusals
- Output: Agent instruction card
- Control: Scope owner approves boundary
- Failure test: Agent answers outside approved domain
- Measure: In-scope resolution rate
- Practice: [Lab 06](labs/lab-06/README.md)

### 27. Knowledge-source curation
- Input: Policy PDFs and SharePoint site
- Method: Choose authoritative files with metadata
- Output: Source register and index plan
- Control: Remove stale or duplicate files
- Failure test: Agent cites archived policy
- Measure: Current-source citation rate
- Practice: [Lab 06](labs/lab-06/README.md)

### 28. Citation evaluation
- Input: Twenty grounded test questions
- Method: Compare answers to source passages
- Output: Evaluation scorecard
- Control: Fail release below evidence threshold
- Failure test: Citation exists but does not support claim
- Measure: Supported citations divided by citations
- Practice: [Lab 06](labs/lab-06/README.md)

### 29. Copilot Studio topic routing
- Input: Password reset and leave-query intents
- Method: Route to topic or generative answer
- Output: Topic decision flow
- Control: Escalate unsupported requests
- Failure test: Wrong topic triggers a tool
- Measure: Correct route per test case
- Practice: [Lab 06](labs/lab-06/README.md)

### 30. Connector action
- Input: Case-create API schema
- Method: Map validated input to action parameters
- Output: Action contract and sample payload
- Control: Validate inputs and consent
- Failure test: Missing case owner causes bad write
- Measure: Successful validated actions
- Practice: [Lab 06](labs/lab-06/README.md)

### 31. Approval action
- Input: Low and high value requests
- Method: Branch at amount threshold
- Output: Approval path with actor and timestamp
- Control: No silent auto-approval
- Failure test: High-value request takes fast path
- Measure: Threshold breaches count
- Practice: [Lab 07](labs/lab-07/README.md)

### 32. Power Automate flow
- Input: Form submission and structured fields
- Method: Trigger, validate, approve, write, notify
- Output: Flow run trace
- Control: Use service identity with least privilege
- Failure test: Duplicate trigger creates two tickets
- Measure: Idempotent completions divided by runs
- Practice: [Lab 07](labs/lab-07/README.md)

### 33. Dynamics 365 context
- Input: Synthetic account and case record
- Method: Ground response in permitted CRM fields
- Output: Case summary and next-step draft
- Control: Respect record-level access
- Failure test: Summary includes another account
- Measure: Cross-account leakage count
- Practice: [Lab 07](labs/lab-07/README.md)

### 34. Foundry model choice
- Input: Latency, quality and residency constraints
- Method: Compare candidate models on test set
- Output: Model decision card
- Control: Approve budget and data region
- Failure test: Cheaper model fails critical test
- Measure: Quality score per cost unit
- Practice: [Lab 07](labs/lab-07/README.md)

### 35. MCP tool registration
- Input: Tool schema and server identity
- Method: Expose a bounded tool to an agent
- Output: Tool catalog with scopes
- Control: Authenticate and log each invocation
- Failure test: Untrusted server gains broad access
- Measure: Authorized calls divided by all calls
- Practice: [Lab 07](labs/lab-07/README.md)

### 36. A2A handoff
- Input: Service agent and billing agent contract
- Method: Send task with identity and context limits
- Output: Handoff trace and result
- Control: Entra authorization at endpoint
- Failure test: Receiving agent loses context boundary
- Measure: Successful authorized handoffs
- Practice: [Lab 08](labs/lab-08/README.md)

### 37. Multi-agent orchestration
- Input: Research, policy and drafting subagents
- Method: Sequence outputs with conflict resolution
- Output: Orchestration map and provenance
- Control: Supervisor approves final answer
- Failure test: Agents amplify an unsupported claim
- Measure: Conflicts detected before release
- Practice: [Lab 08](labs/lab-08/README.md)

### 38. Cross-platform error handling
- Input: CRM timeout and retry policy
- Method: Retry safely then queue for human
- Output: Dead-letter record with correlation ID
- Control: No duplicate write on retry
- Failure test: Retry creates duplicate case
- Measure: Duplicate-free retries divided by retries
- Practice: [Lab 08](labs/lab-08/README.md)

## Topic 4: AI Optimization, Performance Monitoring and Business Value Assessment

Official reference: https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-control-system/measurement-reporting

### 39. Usage telemetry
- Input: Weekly usage export by cohort
- Method: Join license, active use and role
- Output: Adoption dashboard
- Control: Aggregate before sharing individual trends
- Failure test: Metric counts sign-in as productive use
- Measure: Weekly active users divided by licensed
- Practice: [Lab 08](labs/lab-08/README.md)

### 40. Agent quality rubric
- Input: Twenty task prompts with known answers
- Method: Score accuracy, evidence and safety
- Output: Evaluation matrix
- Control: Block release on critical safety failure
- Failure test: High average hides one severe error
- Measure: Pass rate per risk tier
- Practice: [Lab 08](labs/lab-08/README.md)

### 41. Golden test set
- Input: Representative questions and edge cases
- Method: Version expected results and sources
- Output: Regression test dataset
- Control: Data owner approves test updates
- Failure test: Test set contains stale expected answer
- Measure: Changed results per release
- Practice: [Lab 09](labs/lab-09/README.md)

### 42. Time-saved estimate
- Input: Baseline 18 min and assisted 11 min
- Method: Subtract review time and scale by volume
- Output: Net time-saving model
- Control: Validate observed samples
- Failure test: Gross saving ignores review effort
- Measure: Net minutes saved per task
- Practice: [Lab 09](labs/lab-09/README.md)

### 43. ROI model
- Input: Seats, license cost, volume and wage rate
- Method: Compare realized value to total costs
- Output: Conservative ROI worksheet
- Control: Separate measured from assumed inputs
- Failure test: Benefit double-counts the same task
- Measure: (Value minus cost) divided by cost
- Practice: [Lab 09](labs/lab-09/README.md)

### 44. License optimization
- Input: Seat use by department and month
- Method: Reclaim idle seats after review
- Output: Reallocation recommendation
- Control: Line manager confirms exceptions
- Failure test: Idle seats kept while pilot waits
- Measure: Active seats divided by assigned seats
- Practice: [Lab 09](labs/lab-09/README.md)

### 45. Latency budget
- Input: Prompt, retrieval and tool timings
- Method: Decompose p50 and p95 response time
- Output: Latency waterfall
- Control: Do not remove safety checks for speed
- Failure test: Tool call dominates p95
- Measure: p95 seconds per task
- Practice: [Lab 09](labs/lab-09/README.md)

### 46. Error budget
- Input: Failed action and unsafe answer logs
- Method: Set severity-weighted threshold
- Output: Error-budget burn chart
- Control: Pause rollout at threshold
- Failure test: Aggregate rate masks severe event
- Measure: Severe failures per 1000 tasks
- Practice: [Lab 10](labs/lab-10/README.md)

### 47. Feedback triage
- Input: User corrections and support tickets
- Method: Tag source, prompt, policy or tool cause
- Output: Prioritized defect backlog
- Control: Preserve evidence and owner
- Failure test: Prompt tweak hides source defect
- Measure: Median time to close defect
- Practice: [Lab 10](labs/lab-10/README.md)

### 48. Experiment design
- Input: Pilot and comparison cohorts
- Method: Hold task and measurement constant
- Output: Evaluation protocol
- Control: Avoid claiming causality from correlation
- Failure test: Different work mix biases result
- Measure: Adjusted change in cycle time
- Practice: [Lab 10](labs/lab-10/README.md)

### 49. Rollout wave gate
- Input: Pilot QA, security and adoption data
- Method: Evaluate go or hold criteria
- Output: Wave decision record
- Control: Named sponsor owns release
- Failure test: Wave launches without risk sign-off
- Measure: Criteria passed divided by required
- Practice: [Lab 10](labs/lab-10/README.md)

### 50. Retirement control
- Input: Unused agent and knowledge sources
- Method: Disable access and retain required records
- Output: Decommission checklist
- Control: Verify no dependent workflow remains
- Failure test: Connector remains active after agent removal
- Measure: Orphaned privileged grants count
- Practice: [Lab 10](labs/lab-10/README.md)
