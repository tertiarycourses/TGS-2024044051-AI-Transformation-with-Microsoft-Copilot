TITLE='AI Transformation with Microsoft Copilot'
CODE='TGS-2024044051'
VERSION='v1.0'
DATE='27 September 2026'
URL='https://www.tertiarycourses.com.sg/wsq-ai-transformation-with-microsoft-copilot.html'
OUTCOMES=[
'Develop technology implementation plans and business processes for Microsoft Copilot.',
'Develop control procedures for Microsoft Copilot to manage security.',
'Evaluate the integration of Microsoft Copilot to ensure alignment with business objectives.',
'Develop optimization plans for Microsoft Copilot to improve business operations.']
TOPICS=[
'Microsoft 365 Copilot Implementation and Business Process Transformation',
'Microsoft Copilot Administration, Security and Responsible AI',
'Copilot Integration, AI Agents and Cross-Platform Workflows',
'AI Optimization, Performance Monitoring and Business Value Assessment']
# Each row: mechanism | input evidence | transformation or configuration | output artifact | gate or owner | failure signature | measurable test
RAW=[
# Topic 1
('Tenant readiness','Microsoft 365 tenant inventory','Check identities, data estate and licensed workload availability','Readiness register with owner and gap','Admin signs off app and data prerequisites','Licensed user lacks a supported app or data source','Eligible users divided by target users'),
('License allocation','30 pilot seats and role list','Match entitlement to high-frequency document tasks','License assignment and cohort list','Approve seats against role and cost center','Seat assigned but service plan disabled','Active pilot users divided by assigned seats'),
('Graph permission scope','SharePoint file ACL and test identities','Compare search results under user A and user B','Access matrix with allowed files','Least privilege and owner review','Overshared file appears in both result sets','Unexpected accessible files count'),
('Business-process mapping','Service request intake with six handoffs','Mark drafting, lookup and approval steps','Current-to-future swimlane','Keep human approval on customer-facing send','Automation bypasses approval','Median handoff time in minutes'),
('Opportunity scoring','Ten candidate workflows','Score volume, time, data quality and risk','Ranked use-case backlog','Reject use case with ungoverned sensitive data','High score hides missing data owner','Weighted score per use case'),
('Prompt context window','Customer email and policy excerpts','Separate task, context, constraints and format','Reusable prompt card','Never paste personal data into unmanaged chat','Answer omits policy exception','Grounded claims divided by claims'),
('Grounded retrieval','Approved policy file and user query','Retrieve accessible passages before generation','Answer with source citations','Verify source version and user permission','Citation points to superseded policy','Supported answer statements divided by total'),
('Word proposal draft','Synthetic service improvement brief','Generate structure then compare to source register','Draft proposal with evidence comments','Human owns final facts and approval','Unsupported cost claim enters draft','Verified claims divided by total claims'),
('Excel service analysis','Synthetic ticket table: 120 rows','Aggregate cycle time by issue category','Pivot table and chart','Check formula range and outliers','Blank dates skew mean','Median cycle time by category'),
('PowerPoint executive story','Approved Word findings and Excel chart','Create a three-message decision deck','Five-slide review deck','Presenter validates every number','Chart title and source mismatch','Correct figures divided by checked figures'),
('Outlook response workflow','Synthetic customer escalation email','Draft acknowledgement and response options','Reviewed reply with owner and deadline','Send remains a human action','Tone implies an unapproved commitment','Replies with explicit next owner'),
('Teams meeting synthesis','Synthetic transcript with actions','Extract decisions, dissent and open questions','Action register with timestamps','Meeting owner confirms transcript accuracy','Speaker attribution is wrong','Confirmed actions divided by extracted actions'),
('Adoption rollout','Three departments and pilot feedback','Sequence champions, learning and support','30-60-90 day rollout plan','Gate wave two on measured quality','Low adoption despite licenses','Weekly active usage by cohort'),
# Topic 2
('Identity and MFA','User roles and sign-in policy','Require appropriate identity assurance','Conditional-access decision log','Security team owns exception process','Shared account bypasses attribution','Protected sign-ins divided by sign-ins'),
('Sensitivity labels','Public, internal and confidential files','Map labels to sharing and Copilot exposure','Label policy matrix','Data owner reviews label changes','Confidential file labelled public','Mislabelled sampled files count'),
('DLP boundaries','Prompt containing synthetic account number','Block or warn for restricted data movement','DLP test evidence','Policy owner approves exceptions','Sensitive output leaves approved boundary','Blocked risky attempts per test set'),
('SharePoint oversharing','Site members, visitors and anonymous links','Review inherited access and link types','Remediation ticket list','Owner removes broad access before pilot','Copilot surfaces a broadly shared secret','High-risk links remediated'),
('Retention and records','Contract lifecycle and retention schedule','Apply record class to source documents','Retention decision table','Records officer approves disposal','Old draft retrieved as current policy','Current-version retrieval rate'),
('Audit event trail','Agent action and user identity','Capture time, actor, source and action','Traceable audit record','Admin preserves logs per policy','Action cannot be attributed to a user','Trace-complete actions divided by actions'),
('Prompt-injection boundary','Document with an embedded hostile instruction','Treat retrieved text as data, not instruction','Injection test and refusal trace','Tool action requires explicit authorization','Agent follows source text as a command','Injected commands ignored per test set'),
('Fabrication review','Answer with five factual claims','Check each claim against current citations','Claim-verification worksheet','Human reviewer signs high-impact output','Plausible unsupported number survives','Supported claims divided by claims'),
('Tool permission design','Read and write connector scopes','Separate read-only pilot from write actions','Permission grant register','Entra admin consents only minimum scope','Write tool used in a read workflow','Unused privileged grants count'),
('Environment policy','Dev, test and production environments','Apply connector and publishing policy','Environment control matrix','Promote only after test evidence','Maker publishes from unrestricted default','Policy violations by environment'),
('Incident response','Synthetic disclosure report','Contain, preserve evidence, notify owner','Incident timeline and action log','Security owner determines escalation','Evidence lost during agent disable','Time to containment in minutes'),
('Human decision gate','Draft customer refund recommendation','Require reviewer before irreversible action','Approval record with rationale','Named business owner signs release','Workflow auto-issues refund','Unapproved actions count'),
# Topic 3
('Agent purpose contract','Helpdesk scope and user intents','Define allowed requests and refusals','Agent instruction card','Scope owner approves boundary','Agent answers outside approved domain','In-scope resolution rate'),
('Knowledge-source curation','Policy PDFs and SharePoint site','Choose authoritative files with metadata','Source register and index plan','Remove stale or duplicate files','Agent cites archived policy','Current-source citation rate'),
('Citation evaluation','Twenty grounded test questions','Compare answers to source passages','Evaluation scorecard','Fail release below evidence threshold','Citation exists but does not support claim','Supported citations divided by citations'),
('Copilot Studio topic routing','Password reset and leave-query intents','Route to topic or generative answer','Topic decision flow','Escalate unsupported requests','Wrong topic triggers a tool','Correct route per test case'),
('Connector action','Case-create API schema','Map validated input to action parameters','Action contract and sample payload','Validate inputs and consent','Missing case owner causes bad write','Successful validated actions'),
('Approval action','Low and high value requests','Branch at amount threshold','Approval path with actor and timestamp','No silent auto-approval','High-value request takes fast path','Threshold breaches count'),
('Power Automate flow','Form submission and structured fields','Trigger, validate, approve, write, notify','Flow run trace','Use service identity with least privilege','Duplicate trigger creates two tickets','Idempotent completions divided by runs'),
('Dynamics 365 context','Synthetic account and case record','Ground response in permitted CRM fields','Case summary and next-step draft','Respect record-level access','Summary includes another account','Cross-account leakage count'),
('Foundry model choice','Latency, quality and residency constraints','Compare candidate models on test set','Model decision card','Approve budget and data region','Cheaper model fails critical test','Quality score per cost unit'),
('MCP tool registration','Tool schema and server identity','Expose a bounded tool to an agent','Tool catalog with scopes','Authenticate and log each invocation','Untrusted server gains broad access','Authorized calls divided by all calls'),
('A2A handoff','Service agent and billing agent contract','Send task with identity and context limits','Handoff trace and result','Entra authorization at endpoint','Receiving agent loses context boundary','Successful authorized handoffs'),
('Multi-agent orchestration','Research, policy and drafting subagents','Sequence outputs with conflict resolution','Orchestration map and provenance','Supervisor approves final answer','Agents amplify an unsupported claim','Conflicts detected before release'),
('Cross-platform error handling','CRM timeout and retry policy','Retry safely then queue for human','Dead-letter record with correlation ID','No duplicate write on retry','Retry creates duplicate case','Duplicate-free retries divided by retries'),
# Topic 4
('Usage telemetry','Weekly usage export by cohort','Join license, active use and role','Adoption dashboard','Aggregate before sharing individual trends','Metric counts sign-in as productive use','Weekly active users divided by licensed'),
('Agent quality rubric','Twenty task prompts with known answers','Score accuracy, evidence and safety','Evaluation matrix','Block release on critical safety failure','High average hides one severe error','Pass rate per risk tier'),
('Golden test set','Representative questions and edge cases','Version expected results and sources','Regression test dataset','Data owner approves test updates','Test set contains stale expected answer','Changed results per release'),
('Time-saved estimate','Baseline 18 min and assisted 11 min','Subtract review time and scale by volume','Net time-saving model','Validate observed samples','Gross saving ignores review effort','Net minutes saved per task'),
('ROI model','Seats, license cost, volume and wage rate','Compare realized value to total costs','Conservative ROI worksheet','Separate measured from assumed inputs','Benefit double-counts the same task','(Value minus cost) divided by cost'),
('License optimization','Seat use by department and month','Reclaim idle seats after review','Reallocation recommendation','Line manager confirms exceptions','Idle seats kept while pilot waits','Active seats divided by assigned seats'),
('Latency budget','Prompt, retrieval and tool timings','Decompose p50 and p95 response time','Latency waterfall','Do not remove safety checks for speed','Tool call dominates p95','p95 seconds per task'),
('Error budget','Failed action and unsafe answer logs','Set severity-weighted threshold','Error-budget burn chart','Pause rollout at threshold','Aggregate rate masks severe event','Severe failures per 1000 tasks'),
('Feedback triage','User corrections and support tickets','Tag source, prompt, policy or tool cause','Prioritized defect backlog','Preserve evidence and owner','Prompt tweak hides source defect','Median time to close defect'),
('Experiment design','Pilot and comparison cohorts','Hold task and measurement constant','Evaluation protocol','Avoid claiming causality from correlation','Different work mix biases result','Adjusted change in cycle time'),
('Rollout wave gate','Pilot QA, security and adoption data','Evaluate go or hold criteria','Wave decision record','Named sponsor owns release','Wave launches without risk sign-off','Criteria passed divided by required'),
('Retirement control','Unused agent and knowledge sources','Disable access and retain required records','Decommission checklist','Verify no dependent workflow remains','Connector remains active after agent removal','Orphaned privileged grants count'),
]
assert len(RAW)==50,len(RAW)
SOURCES=[
'https://learn.microsoft.com/en-us/copilot/microsoft-365/microsoft-365-copilot-architecture',
'https://learn.microsoft.com/en-us/microsoft-copilot-studio/security-faq',
'https://learn.microsoft.com/en-us/microsoft-copilot-studio/knowledge-improve',
'https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-control-system/measurement-reporting']
