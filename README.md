# Reddit Community Advisor

An instruction-only skill for existing AI assistants: decide whether a Reddit contribution is useful, then produce an English draft and a Chinese explanation for human review.

For developers, maintainers and community participants who have product facts, current community rules, discussion context and a record of what they have already sent. Supports replies, original-post planning and follow-ups on your own posts. Sometimes the useful result is **wait** or **skip**.

[中文使用入口](#中文使用入口) · [Skill](skills/reddit-community-advisor/SKILL.md) · [Input template](skills/reddit-community-advisor/references/input.md) · [Output contract](skills/reddit-community-advisor/references/output.md)

## Quick start

Make this repository available in your AI workspace. Explicitly ask the assistant to read the skill and its references; no installer or global configuration is required for this workflow.

```text
Read skills/reddit-community-advisor/SKILL.md and its linked input/rules/output references.
Analyze the context I provide using that skill. Return reply/wait/skip, evidence and
unknowns, the missing contribution, angle, product mention and disclosure decision,
an English review draft with a Chinese explanation, and manual recheck triggers.
Use read-only local file tools to load the documents. Perform no external actions
or file edits; do not browse, sign in, post, vote, message or schedule anything.
```

Supply the [input template](skills/reddit-community-advisor/references/input.md): verified product facts and limitations, publishable experience, current rules with source/time, the original post and latest relevant replies, thread status, and confirmed sending records. Mark missing information as unknown. A published post does not establish moderator permission. Keep credentials and unnecessary personal information out of the context.

Review facts, fresh rules, duplicates, privacy and disclosure before deciding whether to publish anything yourself. Drafts are not confirmed sends. `reply` means “prepare a draft”; in original-post mode it means a proposed post, not an already-published reply.

## A small synthetic example

**synthetic: true.** All product identities and discussion details in this example are invented. This shortened example illustrates a decision, not a complete input or model test.

```text
Input, evaluated at the synthetic snapshot date:
mode: own_post_followup
T1: my open post about fictional FableCrate version 2 installation
P1: version 2 needs an empty destination directory before installing
R1: disclosed developer help allowed; repetitive promotion prohibited
S1: original post confirmed sent
latest replies: none; complete coverage
new information: none
affiliation: developer; publishable personal experience: none
rules and thread observed: 2026-10-08T10:00:00Z; complete rule coverage
```

Hand-authored, shortened output:

```text
Decision: wait
Evidence: T1/S1 establish the existing contribution; there are no replies or new facts.
Unknowns: future questions or findings; community activity timing is unknown.
Missing contribution: none
Product mention / disclosure: no draft or product mention now; developer relationship known
English draft (human review only): none
Chinese explanation: 没有新增贡献，不为顶帖补评。
Follow-up trigger: a substantive unanswered question, verified correction or new result;
manual recheck only, with no automatic schedule.
```

If a reader later asks about the destination directory **and C1 already gives the P1 instruction**, the decision for repeating that answer is **skip**, with no draft. If the question is still unanswered and current rules permit disclosed support, a grounded answer may be useful. Waiting avoids a bump; skipping avoids a duplicate. Neither requires inventing a reason to mention the product. See the [full output contract](skills/reddit-community-advisor/references/output.md) for all required fields.

## Three ways to use it

Use the quick-start loading and read-only instructions with any of these requests. Provide your context separately; these are prompt examples, not tool integrations.

| Mode | Example request |
| --- | --- |
| Reply | “Evaluate this supplied question, latest replies and confirmed sending log. Identify any unanswered contribution before drafting. Do not invent firsthand experience.” |
| Original post | “Evaluate this proposed topic against the supplied current rules and discussions. If useful, draft a title, body and flair with evidence, limitations and affiliation disclosure.” |
| Own-post follow-up | “Evaluate my confirmed post and new replies or findings. Decide whether to reply, wait or skip. Do not add a comment merely because the post is quiet.” |

[examples/installation.md](examples/installation.md) is a **synthetic application-installation support case**. It shows how to answer a fictional product question; it is not a guide to installing this skill. The [empty-own-post](examples/empty-own-post.md) and [original-post](examples/original-post.md) examples also contain hand-authored expected outputs.

## Loading status and troubleshooting

**Verified workflow:** explicit reading of `SKILL.md` and its three reference files followed by model analysis. That workflow has produced actual outputs. It is separate from the static validator below.

**Not verified:** native skill-selector invocation, automatic discovery and cross-provider compatibility. Attempts to start a fresh local Codex validation session were blocked during app-server initialization in the current execution environment. Directory or symlink existence is not proof of discovery or invocation.

- **The skill is absent from a selector:** use the explicit file-reading prompt above. For native discovery, consult your tool's current documentation and verify the entry in a new project session before relying on it. This repository includes no installer or global configuration.
- **The assistant cannot read local files:** attach or paste `SKILL.md` and all three [references](skills/reddit-community-advisor/references/input.md), [rules](skills/reddit-community-advisor/references/rules.md), [output](skills/reddit-community-advisor/references/output.md), then provide your input. File attachment/paste compatibility depends on the host and is not a tested integration here.
- **Rules or replies are missing:** provide fresh, relevant snapshots with coverage and observation times. Do not infer permission from silence or retry a submission whose outcome is unknown.
- **The model cannot start:** that is not evidence of a skill decision or successful invocation. Use a working assistant with explicit context loading; do not claim a native integration passed.

## Scope and limits

No Reddit endorsement or growth guarantee. This project does not read Reddit, obtain accounts, connect credentials, scrape, send or edit posts, vote, message, cross-post or schedule checks. There is no browser connector, telemetry or SaaS service. Users supply lawfully obtained context and remain responsible for platform and community rules.

Replies, rules, URLs and product documents are untrusted data, not permission to change the task or transmit private information. All output is draft-only. First-person experience requires the user's actual publishable facts. Product affiliation must be disclosed when relevant, and disclosure does not override a promotion ban. High-risk security or data-loss reports go to the user first. Recheck suggestions are manual and event-based; fixed reply delays, karma thresholds and universal best posting times are not treated as platform rules.

## Validation and project files

Run the offline, standard-library checks from repository root:

```sh
python3 scripts/validate.py
python3 -m unittest discover -s tests
```

These check package links/frontmatter, 14 synthetic fixture contracts and the validator itself. They do not establish model correctness or native integration. Separately, a five-case independent-subagent pilot generated actual decisions, with one run per case; it is a small, single-environment pilot, not a safety or compatibility certification. This project has no configured CI workflow; recorded checks are local only.

- [EVALUATION.md](EVALUATION.md): assessment protocol and limitations.
- [MODEL_EVALUATION.md](MODEL_EVALUATION.md): limited behavioral pilot.
- [VALIDATION.md](VALIDATION.md): static check record.
- [PRIVACY_REVIEW.md](PRIVACY_REVIEW.md) and [PUBLIC_FILES.md](PUBLIC_FILES.md): public package scope; private trial material is excluded.
- [SOURCES.md](SOURCES.md): references, attribution and rejected source practices.
- [CONTRIBUTING.md](CONTRIBUTING.md): focused, synthetic, reviewable contributions.

MIT-licensed, Copyright (c) 2026 redone2000. See [LICENSE](LICENSE). The skill remains a small Markdown project; external account and automation capabilities are outside its scope.

## 中文使用入口

这是给现有 AI 读取的 Reddit 参与判断技能，适合开发者、维护者和社区参与者。先让 AI 读取 [SKILL.md](skills/reddit-community-advisor/SKILL.md) 及其三个引用文件，再按 [输入模板](skills/reddit-community-advisor/references/input.md) 提供事实、当前版规、原帖、最新评论和已确认发送记录。

它会输出 `reply/wait/skip`、证据与未知、真正缺失的贡献、角度、产品提及与身份披露、英文待审草稿和中文释义，以及人工复核触发条件。无新内容不顶帖，已答问题去重；实质问题有证据时及时回答。时间建议不是平台允许时段或已建任务。

目前验证可用的是**显式读取技能和引用文件**。原生选择器调用与自动发现仍未验证，当前环境的会话初始化受限。`examples/installation.md` 是合成产品的安装支持案例，不是 skill 安装指南。只允许只读本地文件工具加载资料；不发送、编辑、投票、私信、跨帖或调度。缺少当前版规时标 unknown，主帖发布不等于版主准许推广。所有内容须由使用者审核；无官方 Reddit 背书或增长保证。
