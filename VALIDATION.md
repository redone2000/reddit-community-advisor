# Validation record

Executed 2026-10-08 on local Python 3.10. Commands from repository root:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests -p 'test_*.py'
```

- Package/local links/frontmatter/basic fixture privacy checks: PASS.
- 14 synthetic fixture contracts: PASS, including all 10 requested scenarios plus security escalation, own-post substantive question, locked target and incomplete replies.
- Validator regression checks: 4 PASS (clean package, broken-link rejection, non-synthetic rejection, inconsistent draft-gate rejection).
- Skill-creator bundled `quick_validate.py` on `skills/reddit-community-advisor`: “Skill is valid!” This authoring helper is not a project dependency.

The commands above produce static format/package/validator results only. Separately, five actual independent-subagent outputs were generated and reviewed; see MODEL_EVALUATION.md for that limited pilot. Hand-authored examples remain separate from those outputs. No live community interaction or growth experiment occurred. See EVALUATION.md for the extended manual assessment protocol.

Reference URLs were reviewed on the date above but remain mutable, unpinned main-branch URLs. User-approved publication uses MIT, Copyright (c) 2026 redone2000, and only the documented public files. An authorized existing GitHub connection confirmed that identity. The project has no CI workflow; tests reported here are local checks, not CI results.
