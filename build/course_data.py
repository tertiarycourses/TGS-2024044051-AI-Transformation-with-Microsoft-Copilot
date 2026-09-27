"""Single source for the executive, outcomes-led v2.0 release."""
TITLE = 'AI Transformation with Microsoft Copilot'
CODE = 'TGS-2024044051'
VERSION = 'v2.0'
DATE = '27 September 2026'
URL = 'https://www.tertiarycourses.com.sg/wsq-ai-transformation-with-microsoft-copilot.html'
OUTCOMES = [
    'Develop technology implementation plans and business processes for Microsoft Copilot.',
    'Develop control procedures for Microsoft Copilot to manage security.',
    'Evaluate the integration of Microsoft Copilot to ensure alignment with business objectives.',
    'Develop optimization plans for Microsoft Copilot to improve business operations.',
]
TOPICS = [
    'Set the Copilot Transformation Strategy and Lead by Example',
    'Govern Copilot Use and Protect Business Decisions',
    'Integrate Copilot into the Executive Operating Model',
    'Measure Value, Scale Adoption and Report to the Board',
]
# Each executive case: decision | synthetic business input | Copilot use or management action |
# board-ready output | decision gate | failure to challenge | outcome measure.
RAW = [
('Transformation ambition','A service division misses response targets','Use Copilot Chat to compare three improvement ambitions','One-page transformation mandate','CEO approves a measurable business problem','Ambition is only a technology slogan','Target service-cycle reduction'),
('Value pool map','Five departments and task-volume estimates','Ask Copilot to cluster recurring knowledge-work opportunities','Value pool map with owner','Keep only opportunities tied to a named outcome','High-volume activity has no customer value','Annual addressable hours by pool'),
('Executive sponsor','Four competing leadership priorities','Draft a sponsor brief in Word with Copilot','Sponsor decision and named accountable owner','Sponsor commits a review cadence','No executive owns the benefit','Sponsor decisions closed on time'),
('Stakeholder alignment','Sales, service, finance and risk concerns','Summarise the competing positions with Copilot','Stakeholder trade-off matrix','Record dissent before selecting a pilot','Risk concern is omitted from the brief','Unresolved stakeholder objections'),
('Success definition','Baseline cycle time and quality scores','Use Copilot to draft a result statement','Outcome scorecard with baseline and target','Board accepts denominator and time window','Activity count is presented as impact','Target met on comparable work'),
('Copilot Chat briefing','Synthetic board pack and policy extract','Ask Copilot Chat for a sourced executive summary','Five-point decision brief','Verify each material claim against the pack','Plausible but unsupported claim','Supported claims divided by claims'),
('Question refinement','A broad request for better service','Refine goal, context, constraints and format in Copilot','Reusable executive prompt','Prompt names audience and decision','Response is polished but irrelevant','Decision-relevant points per answer'),
('Source challenge','Two contradictory policy versions','Ask Copilot to identify differences and uncertainty','Source conflict register','Owner resolves the authoritative version','Retired document becomes the basis','Current-source citation rate'),
('Scenario comparison','Three service improvement options','Ask Copilot for assumptions and trade-offs','Option comparison table','Compare options with the same criteria','One option gets a favourable metric','Criteria applied to all options'),
('Executive follow-up','A decision brief with open questions','Use Copilot to list evidence gaps and owners','Follow-up action register','No recommendation without missing facts','Open question disappears from summary','Critical gaps assigned to owners'),
('Word strategy memo','A synthetic service improvement brief','Draft a decision memo with Copilot in Word','Two-page strategy memo','Human executive signs the recommendation','Draft invents a savings figure','Verified material claims'),
('Recommendation logic','Three options and a cost ceiling','Ask Copilot to test the logic of a recommendation','Recommendation with assumptions','State rejected alternatives and rationale','Trade-off is hidden','Board questions answered with evidence'),
('PowerPoint board story','Approved strategy memo and metrics','Create a concise executive deck with Copilot in PowerPoint','Five-slide board narrative','Every chart traces to approved numbers','Slide claims exceed the source','Figures verified before review'),
('Decision appendix','Risk and sensitivity notes','Use Copilot to structure board Q&A','Board appendix and question log','Distinguish evidence from assumptions','Appendix repeats unsupported claims','Questions with grounded answers'),
('Leadership communication','Approved board decision','Draft a leader message with Copilot in Outlook','Change announcement for review','No send until approved by sponsor','Message promises unapproved outcomes','Message comprehension in pilot survey'),
('Information boundary','Synthetic confidential account file','Decide which content may be used with Copilot','Data-use decision table','Data owner approves permitted sources','Sensitive source is broadly shared','Restricted exposures found in review'),
('Permission reality','Two roles with different access','Request the same summary under each approved identity','Access-test evidence record','Security owner reviews unexpected access','User receives material outside role','Unexpected accessible files'),
('Source reliability','Current and retired policies','Compare Copilot answer with authoritative source','Claim-verification worksheet','Reviewer checks every material statement','Retired policy cited as current','Supported claims divided by claims'),
('Human approval','Draft external customer commitment','Assign a human approval point before release','Approval decision record','Named owner signs external commitment','Copilot text is sent without review','Unapproved external actions'),
('Responsible-use rule','A sensitive executive scenario','Draft a plain-language use rule in Word','One-page responsible-use charter','Legal and risk owners approve wording','Charter is too vague to apply','Exceptions resolved within SLA'),
('Risk appetite','Five use cases with different consequences','Rank harms, controls and owners with Copilot','Risk-tier matrix','High-impact uses require stronger review','All use cases share one weak gate','High-risk use cases with owner'),
('Incident response','Synthetic disclosure near miss','Ask Copilot to organise facts and response options','Incident decision timeline','Security owner determines escalation','Evidence is lost or blame is assigned early','Time to containment'),
('Quality challenge','Confident answer with two errors','Use Copilot as a critic, then verify manually','Red-team finding and correction','Release only after material errors corrected','Fluent answer is treated as proof','Critical errors per review set'),
('Policy ownership','Business, IT, legal and HR responsibilities','Draft a RACI with Copilot','Governance RACI','No control lacks a decision owner','Everyone assumes IT owns content quality','Controls with named owners'),
('Board assurance','Pilot results and unresolved risks','Summarise assurance evidence with Copilot','Board risk-and-control dashboard','Disclose unresolved material risks','Green status masks a severe issue','Critical issues overdue'),
('Executive meeting','Synthetic leadership meeting transcript','Use Copilot in Teams to extract decisions and dissent','Decision and action log','Chair validates speaker and decision','AI assigns an action to wrong owner','Confirmed actions divided by extracted'),
('Outlook decision flow','A crowded executive email thread','Use Copilot in Outlook to summarise asks and deadlines','Prioritised response draft','Executive reviews tone and commitments','Reply contains a false promise','Decisions made before deadline'),
('Cross-functional handoff','Service and finance joint request','Ask Copilot to map handoffs and delays','Future-state handoff map','Keep accountable human at each gate','AI summary blurs ownership','Handoff time reduction'),
('Copilot integration choice','Microsoft 365 and line-of-business options','Compare use-as-is, extend and build choices','Integration decision card','Sponsor accepts cost and risk trade-off','Custom build is chosen without need','Business fit score per option'),
('Agent opportunity','A repeatable policy-answer task','Describe where a bounded agent may help','Agent opportunity brief','Do not automate irreversible decisions','Agent scope expands beyond approval','In-scope resolution rate'),
('Vendor and partner review','Three proposed AI service options','Use Copilot to structure a due-diligence checklist','Partner decision matrix','Verify contractual and data claims','Marketing claims become evidence','Requirements with verified proof'),
('Pilot operating model','30-seat cross-functional cohort','Draft roles, support and review cadence','Pilot operating charter','Sponsor, data owner and risk lead sign off','Pilot has licences but no support','Weekly active pilot users'),
('Leadership role modelling','Three executive work patterns','Use Copilot to select visible leader practices','Leader demonstration plan','Leader shows reviewed outputs and limits','Leader promotes unverified output','Leaders demonstrating weekly'),
('Change communication','Employee concerns and benefits','Draft FAQ and manager briefing in Word','Change narrative and FAQ','Include limits and escalation route','Message implies job replacement decision','Employee understanding score'),
('Decision escalation','Pilot issue affecting customer outcome','Map pause, fix and restart decisions','Escalation playbook','Named sponsor owns pause decision','Issue remains open while rollout expands','Median time to decision'),
('Use-case portfolio','Twelve candidate workflows','Prioritise volume, value, feasibility and risk','Ranked opportunity portfolio','Reject ownerless or unsafe use case','Highest score hides weak data','Validated value per use case'),
('Adoption baseline','Usage by role and department','Compare active use with licensed seats','Adoption baseline chart','Separate sign-in from productive use','Licence assignment counted as adoption','Weekly active users per cohort'),
('Enablement design','Three role-specific skill gaps','Ask Copilot to draft role-based coaching plans','90-day enablement calendar','Manager commits time for practice','One generic training suits no one','Practice completion by role'),
('Feedback loop','Pilot questions and complaints','Cluster feedback themes with Copilot','Prioritised improvement backlog','Assign owner and due date','Prompt advice hides a source defect','Median defect closure time'),
('Scale gate','Pilot adoption, quality and risk data','Prepare go, hold or stop recommendation','Wave-two decision paper','Every critical threshold passes','Average score hides a severe failure','Criteria passed divided by required'),
('Excel value model','Synthetic task time and cost worksheet','Use Copilot in Excel to analyse observed changes','Net time-saved table','Review time is deducted from gross saving','Gross saving is sold as net value','Net minutes saved per task'),
('Benefit confidence','Observed sample and management estimates','Ask Copilot to label evidence strength','Benefit confidence register','Assumption is never described as measured','Weak sample is extrapolated widely','Measured share of claimed value'),
('Cost of ownership','Seats, enablement and support costs','Use Copilot to compare total cost scenarios','Total-cost table','Include recurring change and review effort','License fee is the only cost','Cost per realised outcome'),
('Sensitivity test','Low, base and high adoption scenarios','Ask Copilot to vary key assumptions','Sensitivity chart with break-even point','Decision holds under a credible downside','Single optimistic case drives approval','Break-even adoption threshold'),
('Investment decision','Value model and risk register','Draft a balanced investment memo in Word','Fund, hold or stop recommendation','Sponsor signs conditions and budget','Recommendation ignores risk-adjusted cost','Conditions met before release'),
('Quality scorecard','Sample outputs and evidence checks','Summarise quality results with Copilot','Quality trend chart','Any critical safety failure blocks scale','Good average masks one severe error','Critical failures per sample'),
('Customer outcome','Service response and satisfaction data','Compare customer metrics before and after pilot','Customer-impact summary','Control for work mix and seasonality','AI usage is mistaken for customer benefit','Comparable cycle-time change'),
('Board reporting','Adoption, value, quality and risk metrics','Use Copilot in PowerPoint to draft a board update','One-page board scorecard','Every number has source and date','Board pack hides uncertainty','Claims with traceable evidence'),
('Next-quarter roadmap','Pilot findings and capacity limits','Ask Copilot to sequence the next three waves','90-day roadmap with gates','Each wave has owner and stop rule','Scale outruns governance capacity','Wave gates met on schedule'),
('Executive decision rehearsal','Board challenge questions','Use Copilot to surface counterarguments','Final go, hold or stop record','Executive states assumptions and dissent','Decision is made on a polished demo','Decision quality rubric score'),
]
assert len(RAW) == 50
SOURCES = [
'https://learn.microsoft.com/en-us/credentials/certifications/exams/ab-100/',
'https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-controls/security-governance',
'https://support.microsoft.com/en-us/microsoft-365-copilot/get-started-writing-prompts-in-microsoft-365-copilot',
'https://learn.microsoft.com/en-us/microsoft-365/copilot/copilot-control-system/measurement-reporting',
]
LAB_NAMES = [
'Executive transformation mandate', 'Copilot Chat decision brief', 'Board memo and story',
'Information and decision boundaries', 'Governance and assurance charter',
'Executive meeting and communication', 'Integration and operating model',
'Adoption and scale plan', 'Investment and value case', 'Board scorecard and decision',
]
LAB_APPS = [
'Microsoft Copilot Chat', 'Microsoft Copilot Chat', 'Copilot in Word and PowerPoint',
'Microsoft Copilot Chat', 'Copilot in Word', 'Copilot in Teams and Outlook',
'Microsoft Copilot Chat and Word', 'Microsoft Copilot Chat and Word',
'Copilot in Excel and Word', 'Copilot in PowerPoint and Chat',
]
