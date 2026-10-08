# Synthetic empty own-post example

synthetic: true. All facts below are invented.

## Input

See `empty_no_new_information` in [cases.json](../tests/cases.json). The user's original walkthrough is confirmed sent as T1. There are zero replies and no new findings. Current rules and reply coverage are supplied.

## Hand-authored expected output (not a model test)

Decision: wait
Mode: own_post_followup
Target: T1
Escalation: none
Reason: No question, correction or new finding warrants another comment.
Evidence: T1, complete empty replies and the confirmed sending log show only the original walkthrough.
Unknowns: Future reader questions and future useful findings; silence does not prove a timing failure.
Missing contribution: none
Angle: none
Product mention: Name omitted; link omitted because there is no contribution to draft.
Disclosure: Developer relationship known; no draft requires disclosure now.
English draft (human review only): none
Chinese explanation: 暂不补评。没有新问题或实质更新，不应为顶帖而回复。
Follow-up trigger: A substantive unanswered question, verified correction or useful new result. Manually recheck when that event is supplied; any chosen check window is a convenience, not a Reddit activity rule or automatic schedule.
Human review checks: Recheck latest replies and confirmed log if a new event arrives.
