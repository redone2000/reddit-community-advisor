# Synthetic installation example

synthetic: true. All identities, product facts and thread text below are invented.

## Input

See the complete synthetic `installation_question` input in [cases.json](../tests/cases.json). P1 says FableCrate version 2 requires an empty destination directory; R1 permits disclosed developer support. T1 asks about the missing destination. Latest reply coverage is complete; no replies or confirmed answers exist. No publishable customer experience is supplied. No link is needed.

## Hand-authored expected output (not a model test)

Decision: reply
Mode: reply
Target: T1
Escalation: none
Reason: An unanswered installation question has a supported fix.
Evidence: P1 supports the version 2 directory requirement; R1 permits disclosed support; T1 asks about this error. Snapshots observed 2026-10-08T10:00:00Z, complete rule/reply coverage.
Unknowns: Whether creating the directory resolves this person's installation is unknown.
Missing contribution: No reply or confirmed sending record supplies the directory requirement.
Angle: Direct version-specific instruction, followed by a minimal clarification if needed.
Product mention: Name allowed by R1 and relevant to T1/P1; link omitted as unnecessary.
Disclosure: Developer — “I'm a developer of FableCrate.”
English draft (human review only): I'm a developer of FableCrate. For version 2, create an empty destination directory before installing. If you still get the error, which version are you installing? Please leave out any private file paths.
Chinese explanation: 我是 FableCrate 的开发者。安装第 2 版前请创建一个空的目标目录。如果仍然报错，请确认安装的是哪个版本，不要提供私人文件路径。这段话没有宣称问题已解决，也没有声称自己是客户。
Follow-up trigger: A new report that the error persists or a different version is involved; manually inspect that response and the latest answers before another draft. No automatic schedule.
Human review checks: Reconfirm P1, current R1 and T1 status, absence of duplicate answers, disclosure and privacy wording.
