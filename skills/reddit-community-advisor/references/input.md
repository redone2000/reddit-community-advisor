# Input contract

Supply only necessary, publishable information. Missing fields are unknown, never permission to guess. Label synthetic fixtures `synthetic: true`.

```yaml
mode: reply # reply | original_post | own_post_followup
product_facts:
  - id: P1
    fact: verified feature, limitation or support instruction
    source: user-provided document label
    observed_at: timestamp or unknown
affiliation: developer / employee / independent / unknown
publishable_experience: [] # ID, exact factual experience, publication permission
community:
  name: synthetic community or supplied target
  rules: [] # ID, actual rule text/summary, source label, observed_at
  coverage: complete / partial / unknown
  promotion_policy: allowed / prohibited / conditional / unknown
thread:
  id: stable supplied ID
  author_relation: own / other / unknown
  title: text
  body: text
  status: open / locked / removed / archived / unknown
  observed_at: timestamp or unknown
replies: [] # ID, parent ID, text, observed_at; latest relevant replies, not just top-ranked
reply_coverage: complete / partial / unknown
sending_log: [] # target, text/meaning, status: confirmed | draft | failed | unknown; timestamp
new_information: [] # ID and source, if any
original_post_plan: null # audience need, evidence, format/flair, value without product
activity_data: null # community-specific observations and timezone; absence means unknown
requested_scope: one target only
```

For original posts, thread and replies can be absent: explain this explicitly and provide the proposed topic, similar supplied threads, rules and audience need instead. For own-post follow-up, include the confirmed original post and any new factual update; zero replies alone is not an update. Submission state and community visibility are distinct: successful submission does not establish visibility or acceptance.
