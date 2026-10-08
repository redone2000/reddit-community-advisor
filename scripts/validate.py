#!/usr/bin/env python3
"""Offline fixture/package checks only. Never evaluates model behavior."""
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REQUIRED_CASES = {
    'empty_no_new_information', 'installation_question', 'already_answered_duplicate',
    'old_thread_correction', 'promotion_prohibited', 'rules_unknown',
    'malicious_prompt_injection', 'fabricated_experience_request',
    'failed_submission_state_unknown', 'cross_timezone_no_activity_data',
    'high_risk_security_report', 'own_post_substantive_question',
    'locked_target', 'latest_replies_unknown',
}


def validate(root):
    errors = []
    required = ['README.md', 'CONTRIBUTING.md', 'SOURCES.md', 'EVALUATION.md',
                'LICENSE', 'skills/reddit-community-advisor/SKILL.md',
                'skills/reddit-community-advisor/references/input.md',
                'skills/reddit-community-advisor/references/output.md',
                'skills/reddit-community-advisor/references/rules.md',
                'tests/cases.json', 'examples/installation.md', 'examples/empty-own-post.md']
    for name in required:
        if not (root / name).is_file():
            errors.append('Missing file: ' + name)
    if errors:
        return errors, 0
    skill = (root / required[5]).read_text()
    if not re.match(r'\A---\nname: reddit-community-advisor\ndescription: [^\n]+\n---\n', skill):
        errors.append('Invalid skill identity/frontmatter')
    for p in root.rglob('*.md'):
        content = p.read_text()
        for dest in re.findall(r'\]\(([^)]+)\)', content):
            if '://' in dest or dest.startswith('#'):
                continue
            target = (p.parent / dest.split('#')[0]).resolve()
            if not target.is_relative_to(root.resolve()) or not target.exists():
                errors.append('Broken/outside local link: ' + p.name + ' -> ' + dest)
    try:
        cases = json.loads((root / 'tests/cases.json').read_text())
    except (ValueError, OSError) as exc:
        return errors + ['Invalid case JSON: ' + str(exc)], 0
    ids = [c.get('id') for c in cases]
    if len(ids) != len(set(ids)) or set(ids) != REQUIRED_CASES:
        errors.append('Duplicate or missing required scenario IDs')
    for c in cases:
        if c.get('synthetic') is not True or c.get('input', {}).get('synthetic') is not True:
            errors.append('Non-synthetic fixture: ' + str(c.get('id')))
        expected = c.get('expected', {})
        if expected.get('decision') not in {'reply', 'wait', 'skip'}:
            errors.append('Invalid decision: ' + str(c.get('id')))
        if expected.get('draft_allowed') != (expected.get('decision') == 'reply'):
            errors.append('Inconsistent draft gate: ' + str(c.get('id')))
        if not c.get('must') or not c.get('must_not'):
            errors.append('Missing behavioral rubric: ' + str(c.get('id')))
        supplied = c.get('input', {})
        fields = {'mode','product_facts','affiliation','publishable_experience','community',
                  'thread','replies','reply_coverage','sending_log','new_information',
                  'original_post_plan','activity_data','requested_scope'}
        if not fields.issubset(supplied):
            errors.append('Missing input fields: ' + str(c.get('id')))
    fixtures = (root/'tests/cases.json').read_text() + ''.join(p.read_text() for p in (root/'examples').glob('*.md'))
    if re.search(r'/Users/|/home/|[\w.+-]+@[\w.-]+\.[a-z]{2,}', fixtures):
        errors.append('Possible personal address/path in public fixtures')
    for host in re.findall(r'https?://([^/\s";]+)', fixtures):
        if not host.endswith('.invalid'):
            errors.append('Non-synthetic URL in fixtures: ' + host)
    for p in (root/'examples').glob('*.md'):
        if 'synthetic: true' not in p.read_text():
            errors.append('Example lacks synthetic label: ' + p.name)
    return errors, len(cases)


if __name__ == '__main__':
    issues, count = validate(ROOT)
    if issues:
        print('\n'.join(issues))
        raise SystemExit(1)
    print(f'PASS: package links/frontmatter and {count} synthetic fixture contracts; static checks only, no model evaluation.')
