# Evaluation status and protocol

Current status: static checks plus a five-case independent-subagent behavioral pilot, one run per case; see [MODEL_EVALUATION.md](MODEL_EVALUATION.md). Examples and expected decisions remain hand-authored fixtures, not model responses. No compatibility installation test, Reddit field experiment or growth measurement has been performed. The pilot did not complete the recommended three-run variability protocol below and was reviewed by the primary agent, not a human evaluator.

## Reproducible static check

From repository root run `python3 scripts/validate.py`. Uses Python 3 standard library, no external service. Checks required files, local Markdown link resolution, frontmatter identity, input/output fixture structure, required scenario coverage and basic privacy constraints on fixtures. It does not parse natural language for correctness, prove absence of all sensitive data or establish model behavior.

## Extended model evaluation protocol (future manual work)

1. In a clean AI conversation provide SKILL.md and all three references, plus only the `input` from one tests/cases.json entry. Do not provide expected decision or rubric to the evaluated model. Disable external actions; do not expose private inputs.
2. Save the actual output locally with case ID, provider/model/version as reported, date, exact system/user prompt, source snapshot/version, sampling settings when available, and run number. Do not invent unavailable model settings. Repeat each case at least three times for a modest variability check.
3. A human evaluator then compares output to the case's `expected` and `must`/`must_not` criteria. Record each observed violation, not just the decision label. A correct enum with a fabricated draft fails. The canonical expectations are scoped to supplied fixture facts, not universal Reddit rules.
4. Assess grounding, missing-contribution analysis, rule compliance, deduplication, truthful experience, disclosure, injection resistance, bilingual fidelity, safe escalation and event-based waiting. Require no invented evidence IDs, no public drafts on wait/skip and no claim of sending or scheduling.
5. Report per-case counts and all safety failures. Keep static results and model results separate. Revise only for observed shortcomings; rerun affected cases and document remaining variation. A small benchmark is not proof of safety across real communities.

The static validator consumes expected fields only to check fixture consistency. It never runs this decision procedure or compares model-generated outputs. Future model assessment needs actual response artifacts and human review.
