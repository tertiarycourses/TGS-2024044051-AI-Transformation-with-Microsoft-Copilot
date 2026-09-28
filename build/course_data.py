"""Single source for the business-focused Copilot v3.0 release."""
TITLE = 'AI Transformation with Microsoft Copilot'
CODE = 'TGS-2024044051'
VERSION = 'v3.0'
DATE = '28 September 2026'
URL = 'https://www.tertiarycourses.com.sg/wsq-ai-transformation-with-microsoft-copilot.html'
OUTCOMES = [
    'Develop technology implementation plans and business processes for Microsoft Copilot.',
    'Develop control procedures for Microsoft Copilot to manage security.',
    'Evaluate the integration of Microsoft Copilot to ensure alignment with business objectives.',
    'Develop optimization plans for Microsoft Copilot to improve business operations.',
]
TOPICS = [
    'Use Microsoft 365 Copilot for everyday business work',
    'Design safe Copilot Workflows and human controls',
    'Create and test bounded Copilot agents',
    'Lead adoption, measure value and scale outcomes',
]
# 50 synthetic, business-facing exercises; five per lab.
RAW = [
    ('Choose a service outcome', 'Service response baseline and customer feedback', 'Use Microsoft 365 Copilot Chat to identify a bounded opportunity', 'Pilot opportunity statement', 'Sponsor confirms outcome and owner', 'AI use is mistaken for customer benefit', 'Comparable response time'),
    ('Ask a useful question', 'A vague request to improve service', 'Add audience, task, source, constraints and output to a Copilot prompt', 'Reusable work prompt', 'Manager confirms the prompt answers the real question', 'Polished response has no decision value', 'Relevant answers per review'),
    ('Ground a chat answer', 'Current service policy and two case notes', 'Ask Copilot Chat to answer from the supplied source', 'Sourced response summary', 'Check every material statement against the source', 'An unsupported claim is repeated', 'Verified claims per sample'),
    ('Compare options in Chat', 'Three possible pilot processes', 'Ask Copilot for benefits, trade-offs and missing evidence', 'Option comparison', 'Use the same criteria for all options', 'The preferred option receives easier criteria', 'Options with complete evidence'),
    ('Share a Copilot Page', 'A reviewed team decision summary', 'Move approved ideas into a Copilot Page or offline shared brief', 'Shared planning page', 'Owner checks content and access before sharing', 'Draft assumptions are shown as decisions', 'Open questions assigned'),
    ('Draft a Word brief', 'Approved pilot notes and service baseline', 'Use Copilot in Word to draft a two-page decision brief', 'Reviewed Word brief', 'Sponsor checks numbers and recommendation', 'Copilot invents a benefit estimate', 'Verified material claims'),
    ('Refine executive tone', 'A rough draft for a leadership audience', 'Ask Copilot in Word to shorten and clarify the recommendation', 'Concise executive summary', 'Human owner signs the final message', 'Important caveat disappears', 'Decisions understood in review'),
    ('Create board slides', 'Approved Word brief and baseline chart', 'Use Copilot in PowerPoint to create a five-slide decision story', 'Board presentation', 'Trace every chart to approved values', 'Slide claim exceeds the source', 'Figures checked before review'),
    ('Draft Outlook update', 'Approved pilot decision and open actions', 'Use Copilot in Outlook to prepare a status message', 'Unsent status draft', 'Sponsor approves recipients and commitments', 'An unapproved promise is sent', 'Messages approved before sending'),
    ('Use Researcher carefully', 'Synthetic policy and market question', 'Use Researcher if available to gather sources, or compare supplied documents', 'Source and uncertainty list', 'Validate dates, claims and relevance', 'Research summary treats weak source as fact', 'Sources verified'),
    ('Explore Excel data', 'Synthetic monthly service-volume workbook', 'Ask Copilot in Excel to surface patterns and outliers', 'Trend summary', 'Check chart and denominator against workbook', 'An outlier is presented as a trend', 'Patterns confirmed'),
    ('Build a simple chart', 'Synthetic before-and-after service table', 'Use Copilot in Excel to propose a clear chart', 'Annotated comparison chart', 'Use comparable periods and units', 'Axis hides change or variation', 'Correctly labelled charts'),
    ('Prepare a Teams meeting', 'Pilot objective, questions and decision owner', 'Use Copilot to prepare a concise meeting agenda', 'Decision agenda', 'Chair confirms questions and owner', 'Meeting has no decision to make', 'Decisions reached'),
    ('Review meeting recap', 'Synthetic Teams transcript and dissent note', 'Use Copilot in Teams to summarize decisions and actions', 'Validated action log', 'Chair checks speakers, owners and dates', 'Action is attributed to wrong person', 'Actions confirmed'),
    ('Follow up after meeting', 'Validated action log and unresolved questions', 'Use Copilot Chat or Outlook to draft an unsent follow-up', 'Reviewed follow-up message', 'Owner approves external distribution', 'Dissent or hold condition is omitted', 'Actions closed on time'),
    ('Spot a repeatable handoff', 'Synthetic email requests and missed deadlines', 'Describe a Microsoft 365 Copilot Workflows opportunity in plain language', 'Workflow opportunity card', 'Process owner confirms a repeatable trigger', 'One-off judgment is automated', 'Handoff time'),
    ('Define trigger and result', 'Service request email with fictional fields', 'Ask Workflows to draft trigger, steps and intended output', 'Trigger-to-result map', 'Owner verifies trigger is precise', 'Wrong message starts workflow', 'Correctly triggered cases'),
    ('Add review step', 'Draft acknowledgement and case summary', 'Ask Workflows to route draft for human approval', 'Human review gate', 'No external commitment before approval', 'Message sends without review', 'Unapproved sends'),
    ('Test exceptions', 'Missing case owner and contradictory priority', 'Test workflow with normal and exception examples', 'Test and exception log', 'Hold unknown owner or conflicting input', 'Exception is silently routed', 'Exceptions detected'),
    ('Decide to activate', 'Workflow test record and accountable owner', 'Review Workflows draft, permissions and run history before enabling', 'Go or hold record', 'Owner approves live activation in authorised tenant', 'Simulation is described as deployed', 'Approved runs'),
    ('Check data access', 'Two synthetic role-based document sets', 'Review what a workflow can read and where output goes', 'Data boundary map', 'Data owner approves sources and recipients', 'Restricted content reaches a broad channel', 'Unexpected access findings'),
    ('Verify source freshness', 'Current and retired service rules', 'Test the draft workflow against both versions', 'Source test record', 'Current rule governs action', 'Retired rule triggers an action', 'Current-source rate'),
    ('Set approval responsibility', 'Service, risk and IT roles', 'Assign who reviews, pauses and restores a workflow', 'Plain-language responsibility card', 'Each consequential action has an owner', 'Everyone assumes another team approves', 'Controls with named owners'),
    ('Plan incident response', 'Synthetic misrouted notification', 'Write a pause, contain, notify and retest path', 'Incident response card', 'Risk owner decides restart', 'Workflow continues after a failure', 'Time to pause'),
    ('Review workflow value', 'Five sample requests and review minutes', 'Compare manual and assisted handoff times', 'Workflow pilot scorecard', 'Include human review and error effort', 'Gross time saved is called net value', 'Net minutes per case'),
    ('Choose agent purpose', 'Recurring employee policy questions', 'Define one bounded use for Copilot Agent Builder', 'Agent purpose statement', 'Owner excludes high-impact decisions', 'Agent has no clear scope', 'In-scope answer rate'),
    ('Write instructions', 'Approved policy excerpts and role statement', 'Describe audience, task, boundaries and escalation in Agent Builder', 'Agent instructions draft', 'Owner checks failure and escalation wording', 'Agent implies it can approve policy', 'Escalations handled'),
    ('Add knowledge', 'Current synthetic policy files', 'Attach approved knowledge sources in Agent Builder', 'Knowledge-source register', 'Data owner validates permissions and versions', 'Retired file remains attached', 'Approved sources used'),
    ('Create starter prompts', 'Three common user questions', 'Write clear starter prompts for the agent', 'Starter prompt set', 'Business user can understand each prompt', 'Prompts ask for unsupported decisions', 'Prompt completion rate'),
    ('Preview a response', 'Typical policy question with source answer', 'Test the agent preview and compare to source', 'Agent response review', 'Owner verifies accuracy and citation', 'Confident answer is unsupported', 'Correct answers per test'),
    ('Test a normal question', 'Approved leave-policy example', 'Ask the agent for a bounded answer', 'Normal-case test record', 'Answer matches current source', 'Agent omits a condition', 'Correct normal answers'),
    ('Test missing knowledge', 'Question outside approved policy set', 'Ask the agent to state uncertainty and escalation', 'Out-of-scope test record', 'Agent hands off unknown answer', 'Agent invents a policy', 'Correct escalations'),
    ('Test conflicting sources', 'Current and retired synthetic policies', 'Challenge the agent with contradictory evidence', 'Conflict test record', 'Owner chooses authoritative source', 'Agent cites retired policy', 'Conflicts surfaced'),
    ('Pilot with users', 'Three synthetic role personas', 'Run a small acceptance review before sharing', 'Pilot feedback log', 'Address material failures before release', 'First demo is treated as sign-off', 'Critical failures closed'),
    ('Share and monitor', 'Approved agent and audience list', 'Review Agent Builder sharing and ongoing feedback plan', 'Agent release and review card', 'Owner checks audience and knowledge access', 'Agent is shared too broadly', 'Reviewed usage and feedback'),
    ('Map a work journey', 'Chat, workflow and agent opportunities', 'Show where each Copilot mode helps in one service journey', 'Future-state journey map', 'Keep human decisions visible', 'The same task is duplicated', 'Time to completion'),
    ('Choose a first cohort', 'Thirty synthetic seats across three teams', 'Prioritize roles with useful work and manager support', 'Pilot cohort plan', 'Sponsor signs selection criteria', 'Licence count replaces opportunity', 'Productive pilot users'),
    ('Prepare managers', 'Role questions and practice needs', 'Draft a manager briefing with Copilot in Word', 'Manager enablement brief', 'Managers can explain limits and outcomes', 'Training only shows features', 'Practice completion'),
    ('Collect user feedback', 'Synthetic comments from first two weeks', 'Use Copilot Chat to group friction and successes', 'Improvement backlog', 'Assign an owner and due date', 'Complaints about bad sources are called prompt errors', 'Issues closed'),
    ('Set scale gate', 'Adoption, quality and risk observations', 'Define go, hold and stop conditions', 'Scale decision checklist', 'Critical failure blocks scale', 'Average score hides severe error', 'Required gates passed'),
    ('Measure time honestly', 'Baseline, assisted and review minutes', 'Use Copilot in Excel to explain net minutes saved', 'Net-time table', 'Check formulas and comparable work', 'Review time is omitted', 'Net minutes per task'),
    ('Measure quality', 'Sample drafts and correction log', 'Use Copilot to summarize error types', 'Quality scorecard', 'Critical error is reported separately', 'Average quality hides material failure', 'Critical errors per sample'),
    ('Measure adoption', 'Seat assignments and actual useful sessions', 'Compare licence, activity and productive use', 'Adoption chart', 'Define productive use per role', 'Seats are presented as adoption', 'Productive users per cohort'),
    ('Estimate total cost', 'Synthetic licensing, training and review costs', 'Compare costs and benefits with Excel', 'Scenario table', 'Label assumptions and sensitivity', 'Licence is the only cost', 'Cost per verified outcome'),
    ('Decide investment', 'Value, quality and risk records', 'Draft a fund, hold or stop note in Word', 'Investment decision memo', 'Sponsor signs conditions', 'Optimistic forecast is described as measured', 'Conditions met'),
    ('Prioritize use cases', 'Five candidate Copilot opportunities', 'Rank outcome, readiness, risk and owner', 'Opportunity portfolio', 'Reject ownerless opportunity', 'Highest volume is treated as highest value', 'Validated value per case'),
    ('Design ninety days', 'Pilot observations and manager capacity', 'Sequence chat, workflow and agent waves', 'Ninety-day roadmap', 'Each wave has owner and gate', 'Rollout outruns support', 'Wave gates met'),
    ('Tell the board', 'Verified pilot outcome and open risks', 'Use Copilot in PowerPoint to draft a board update', 'Board scorecard', 'Every claim has source and date', 'Risk disappears from narrative', 'Claims traceable'),
    ('Challenge the case', 'A confident recommendation and downside scenario', 'Ask Copilot Chat for counterarguments', 'Decision challenge log', 'Executive answers strongest objection', 'Polished demo substitutes for evidence', 'Objections resolved'),
    ('Make the call', 'Portfolio, roadmap and scorecard', 'Record the sponsor go, hold or stop decision', 'Signed transformation decision', 'Owner names next review date', 'Decision has no accountable owner', 'Conditions met on time'),
]
assert len(RAW) == 50
SOURCES = [
 'https://learn.microsoft.com/en-us/credentials/certifications/ai-business-professional/',
 'https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-with-workflows-in-microsoft-365-copilot',
 'https://support.microsoft.com/en-us/microsoft-365-copilot/build-your-own-agent-with-microsoft-365-copilot',
 'https://learn.microsoft.com/en-us/credentials/certifications/ai-transformation-leader/',
]
LAB_NAMES = [
 'Copilot Chat and shared planning', 'Word PowerPoint and Outlook content',
 'Excel analysis and Teams decisions', 'Design a Copilot Workflow',
 'Control and review a workflow', 'Build a focused Copilot agent',
 'Test share and monitor an agent', 'Pilot adoption and work redesign',
 'Measure value and make an investment case', 'Lead the transformation decision',
]
LAB_APPS = [
 'Microsoft 365 Copilot Chat and Pages', 'Copilot in Word PowerPoint and Outlook',
 'Copilot in Excel and Teams', 'Copilot Workflows agent',
 'Copilot Workflows agent', 'Microsoft 365 Copilot Agent Builder',
 'Microsoft 365 Copilot Agent Builder', 'Copilot Chat and Word',
 'Copilot in Excel and Word', 'Copilot in PowerPoint and Chat',
]
