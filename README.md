# Reddit Community Advisor

一个供 Codex、Claude 等现有 AI 读取的 Markdown 判断技能：帮助决定是否参与 Reddit 讨论，产出英文待审草稿和中文释义。仓库：[redone2000/reddit-community-advisor](https://github.com/redone2000/reddit-community-advisor)。采用 MIT 许可证，版权署名 redone2000。

不提供读帖或发帖能力；使用者自行提供合规获取的数据，并遵循平台与目标社区当前规则。无 Reddit 官方背书、无增长保证。没有 SaaS、爬虫、账号自动化、凭据接入或自动调度。所有输出仅为草稿；不自动发送、编辑、投票、私信或跨帖发布。

## 使用

1. 将 [SKILL.md](skills/reddit-community-advisor/SKILL.md) 与其 references 一起提供给现有 AI，要求按技能分析你提供的上下文。也可把整个 `skills/reddit-community-advisor` 目录放进你所用工具支持的项目级技能目录；具体加载方式以该工具文档为准。本项目不会安装或修改全局配置。
2. 填写 [输入模板](skills/reddit-community-advisor/references/input.md)，选择 `reply`、`original_post` 或 `own_post_followup` 模式。为证据分配 ID，给规则和帖子快照标注采集时间与覆盖范围。不要提交凭据或无关个人资料。
3. 要求按 [输出模板](skills/reddit-community-advisor/references/output.md) 返回 `reply/wait/skip`、证据与未知、缺失贡献、角度、披露、英文草稿、中文释义和后续检查触发条件。
4. 人工检查事实、上下文是否最新、版规、披露与隐私，再自行决定是否发布。不要把草稿加入已发送记录；只有已确认发送的内容才标为 confirmed。

直接调用示例：

> Read skills/reddit-community-advisor/SKILL.md and its linked references. Analyze the synthetic input in examples/installation.md. Produce the required output only; use no tools or external actions.

英文技能正文方便跨工具复用；中文释义用于人工审核。`reply` 是决策枚举，在原创主帖模式表示“可准备该主帖草稿”，不代表已经回复或发帖。

## 文件与验证

- `skills/`：入口、决策规则、输入和输出模板。
- `examples/`：完全合成的输入与人工编写预期输出。
- `tests/cases.json`：14 个合成基准，附可观察的通过/失败标准。
- `scripts/validate.py`：标准库离线静态检查，无网络或模型调用。
- [EVALUATION.md](EVALUATION.md)：真实模型评估方法与目前限制。
- [VALIDATION.md](VALIDATION.md)：已执行的静态检查记录。
- [MODEL_EVALUATION.md](MODEL_EVALUATION.md)：实际独立输出的试测结果与限制。
- [PRIVACY_REVIEW.md](PRIVACY_REVIEW.md)：公开文件的隐私和来源审查。
- [PUBLIC_FILES.md](PUBLIC_FILES.md)：拟公开文件清单。
- [SOURCES.md](SOURCES.md)：来源、许可证、已拒绝的参考做法。
- [CONTRIBUTING.md](CONTRIBUTING.md)：贡献与合成样例要求。

运行 `python3 scripts/validate.py` 与 `python3 -m unittest discover -s tests`。通过仅证明文件、链接和基准结构满足静态合同，不证明模型判断正确、安全或与 Codex/Claude 自动集成成功。另已完成 5 个案例、每案一次的独立子代理盲测，见 [MODEL_EVALUATION.md](MODEL_EVALUATION.md)；仅为小规模试测，不代表跨模型兼容性或稳定性保证。

## 发布状态

用户已批准在 redone2000 账号下公开本项目。许可证为 [MIT](LICENSE)，Copyright (c) 2026 redone2000。公开范围仅限 [文件清单](PUBLIC_FILES.md)，本地试评原始材料不随仓库发布。验证记录分别说明本地静态检查和有限模型试测；本项目未配置 CI。
