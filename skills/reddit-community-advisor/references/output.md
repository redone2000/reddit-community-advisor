# Output contract

Return this Markdown structure for every mode. Use explicit `none` for inapplicable items. No public draft on wait/skip. Evidence IDs must exist in the input; inference must be labeled.

```markdown
Decision: reply | wait | skip
Mode: reply | original_post | own_post_followup
Target: supplied single target or proposed original post
Escalation: none | user_first
Reason: concrete reason
Evidence: input IDs and supported conclusions; observation times/coverage
Unknowns: missing information and its decision impact, or none
Missing contribution: exact gap compared with existing replies and confirmed sending log, or none
Angle: selected useful approach and why, or none
Product mention: name allowed/omitted; link allowed/omitted; evidence for each gate
Disclosure: verified relationship and intended wording, or unknown/none
English draft (human review only): text, or none
Chinese explanation: faithful meaning of draft, including limitations/disclosure; no extra claims, or none
Follow-up trigger: observable new event/evidence or none; suggested manual recheck; never auto-scheduled
Human review checks: facts, fresh rules/thread, duplicates, privacy and disclosure needing review
```

For original posts place `Title:`, `Body:` and `Flair:` inside English draft. For own-post follow-up identify whether the draft proposes a reply or an edit; both remain unexecuted. Separate missing information from a permitted clarifying question: only reply with a question if rules and context are sufficiently known and it adds value. Chinese explanation should also explain wait/skip when there is no draft. Do not claim that human review has happened or the platform accepted a draft.
