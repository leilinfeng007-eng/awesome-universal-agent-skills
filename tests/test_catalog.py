"""Meaningful checks for editorial drift, broken navigation and safe generated output."""
import copy
import importlib.util
import json
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('build',ROOT/'tools/build.py')
build = importlib.util.module_from_spec(spec);spec.loader.exec_module(build)

class CatalogTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data=build.load_catalog()
        cls.old=json.loads((ROOT/'archive/v1.2/catalog.json').read_text())

    def test_pin_license_and_evidence_are_not_rewritten(self):
        old={s['id']:s for s in self.old['skills']}
        for s in self.data['skills']:
            for field in ['upstream','license','dependencies','limitations','adoption_gate','validation']:
                self.assertEqual(s[field],old[s['id']][field],(s['id'],field))
        self.assertEqual(set(old),{s['id'] for s in self.data['skills']}|{s['id'] for s in self.data['archived']})

    def test_data_integrity(self):
        build.check_catalog(self.data)
        self.assertEqual(20,len(self.data['skills']))
        self.assertEqual(12,len(self.data['archived']))
        self.assertEqual(8,sum(s['level']=='everyday' for s in self.data['skills']))
        self.assertEqual({'codex','opencode','claude','cursor','kimi','qoder','qoderwork','workbuddy'},{c['id'] for c in self.data['clients']})

    def test_duplicate_or_unpinned_record_is_rejected(self):
        bad=copy.deepcopy(self.data);bad['skills'].append(bad['skills'][0])
        with self.assertRaises(AssertionError):build.check_catalog(bad)
        bad=copy.deepcopy(self.data);bad['skills'][0]['upstream']['commit']='main'
        with self.assertRaises(AssertionError):build.check_catalog(bad)

    def test_generated_outputs_current(self):
        for path,text in build.outputs(self.data).items():self.assertEqual(text,path.read_text(),str(path))
        self.assertEqual({s['detail_url'] for s in self.data['skills']},{str(f.relative_to(ROOT)) for f in (ROOT/'skills').glob('*.md')})

    def test_current_markdown_links_and_explicit_anchors(self):
        pages=[ROOT/'README.md',ROOT/'CONTRIBUTING.md',ROOT/'LICENSE-NOTICE.md',ROOT/'archive/README.md',*list((ROOT/'docs').glob('*.md')),*list((ROOT/'skills').glob('*.md'))]
        for page in pages:
            for url in re.findall(r'\[[^\]]*\]\(([^)]+)\)',page.read_text()):
                u=urlsplit(url)
                if u.scheme or u.netloc:continue
                target=(page.parent/unquote(u.path)).resolve() if u.path else page
                self.assertTrue(target.is_relative_to(ROOT),url)
                self.assertTrue(target.is_file(),(page.name,url))
                if u.fragment:
                    self.assertIn('id="'+unquote(u.fragment)+'"',target.read_text(),(page.name,url))

    def test_complete_one_stop_cards(self):
        for s in self.data['skills']:
            card=(ROOT/s['detail_url']).read_text()
            for c in self.data['clients']:
                self.assertIn(c['label'],card)
                if c['mode']=='folder':self.assertIn(c['directory']+'/'+s['name']+'/SKILL.md',card)
            self.assertIn(s['prompt'],card)
            self.assertIn('怎么知道生效了',card)
            self.assertIn('想撤销',card)
            self.assertIn(s['upstream']['commit'],card)

    def test_home_tables_are_contiguous(self):
        self.assertNotRegex((ROOT/'README.md').read_text(),r'\|\n\n\|')

    def test_page_is_offline_and_embedded_json_safe(self):
        page=(ROOT/'index.html').read_text()
        self.assertNotRegex(page,r'<script[^>]+src=')
        self.assertNotRegex(page,r'<link[^>]+(?:href=|rel="stylesheet")')
        self.assertNotRegex(page,r'\b(?:fetch|XMLHttpRequest)\s*\(')
        embedded=re.search(r'<script id="catalog-data" type="application/json">(.*?)</script>',page,re.S).group(1)
        parsed=json.loads(embedded)
        self.assertEqual(20,len(parsed['skills']))
        self.assertNotIn('<',embedded)
        for s in parsed['skills']:
            self.assertIn('noopener noreferrer',s['detail_html'])

if __name__=='__main__':unittest.main()
