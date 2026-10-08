"""Repeatable offline negative controls; does not test agent decisions."""
import importlib.util
import json
from pathlib import Path
import shutil
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('validator', ROOT / 'scripts/validate.py')
validator = importlib.util.module_from_spec(spec)
spec.loader.exec_module(validator)


class ValidatorTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory(prefix='reddit-advisor-static-')
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name) / 'package'
        shutil.copytree(ROOT, self.root, ignore=shutil.ignore_patterns('__pycache__'))

    def test_clean_package(self):
        issues, count = validator.validate(self.root)
        self.assertEqual(issues, [])
        self.assertEqual(count, 14)

    def test_broken_link_rejected(self):
        (self.root / 'README.md').write_text('[broken](missing.md)')
        issues, _ = validator.validate(self.root)
        self.assertTrue(any('Broken/outside local link' in x for x in issues))

    def test_non_synthetic_rejected(self):
        p = self.root / 'tests/cases.json'
        cases = json.loads(p.read_text())
        cases[0]['input']['synthetic'] = False
        p.write_text(json.dumps(cases))
        issues, _ = validator.validate(self.root)
        self.assertTrue(any('Non-synthetic fixture' in x for x in issues))

    def test_draft_gate_rejected(self):
        p = self.root / 'tests/cases.json'
        cases = json.loads(p.read_text())
        cases[0]['expected']['draft_allowed'] = True
        p.write_text(json.dumps(cases))
        issues, _ = validator.validate(self.root)
        self.assertTrue(any('Inconsistent draft gate' in x for x in issues))


if __name__ == '__main__':
    unittest.main()
