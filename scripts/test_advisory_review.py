"""Unknown advisories cannot acquire blanket/digest-independent admission."""
import copy
import hashlib
import json
import tempfile
import unittest
from datetime import date
from pathlib import Path
from advisory_review import disposition
from advisory_evidence import verified_reviews
from sbom_privacy import public_sbom, check_sboms


class AdvisoryTests(unittest.TestCase):
    def test_unknown_absent_rating_digest_expiry_and_module_binding(self):
        finding={'id':'GO-fixture','affects':[{'ref':'component'}]}
        review={'id':'GO-fixture','image':'exact','module':'module','version':'1.0',
                'status':'not_affected','reviewed_on':'2026-10-03','expires_on':'2026-11-02',
                'reason':'qualified absence','evidence_sha256':'verified'}
        components={'component':('module','1.0')};today=date(2026,10,3)
        self.assertEqual(disposition(finding,'exact',[],components,today=today),'blocked')
        self.assertEqual(disposition(finding,'exact',[review],components,today=today),'reviewed_not_affected')
        for change in [{'image':'other'},{'version':'2.0'},{'status':'ignored'},
                       {'expires_on':'2026-10-02'},{'expires_on':'2027-01-01'},
                       {'reason':''},{'evidence_sha256':''},{'reviewed_on':'2026-10-04'}]:
            self.assertEqual(disposition(finding,'exact',[{**review,**change}],components,today=today),'blocked')
        for severity in ('critical','high','unexpected'):
            altered={**finding,'ratings':[{'severity':severity}]}
            self.assertEqual(disposition(altered,'exact',[review],components,today=today),'blocked')
        self.assertEqual(disposition(finding,'exact',[review],components,today=date(2026,11,3)),'blocked')
        self.assertEqual(disposition(finding,'exact',[review],components,today=date(2026,11,2)),'blocked')
        self.assertEqual(disposition(finding,'exact',[review],components,today=date(2026,11,1)),'reviewed_not_affected')
        self.assertEqual(disposition({**finding,'affects':[]},'exact',[review],components,today=today),'blocked')

    def test_changed_missing_unsafe_or_positive_symbol_evidence_rejects(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder); (root/'security/advisories').mkdir(parents=True)
            path=root/'security/advisories/evidence.json'
            evidence={'id':'GO-fixture','image':'exact','analysis':'affected packages absent from complete binary symbol inventory',
                      'binary_sha256':'a'*64,'symbol_count':100,'affected_packages':['affected'], 'affected_package_symbols':0}
            def review(data):
                path.write_text(json.dumps(data))
                return {'id':'GO-fixture','image':'exact','evidence':'security/advisories/evidence.json',
                        'evidence_sha256':hashlib.sha256(path.read_bytes()).hexdigest()}
            valid=review(evidence);self.assertEqual(verified_reviews([valid],root),[valid])
            for change in [{'affected_package_symbols':1},{'symbol_count':0},{'binary_sha256':''},{'image':'other'}]:
                altered=review({**evidence,**change});self.assertEqual(verified_reviews([altered],root),[])
            valid=review(evidence);path.write_text('{}');self.assertEqual(verified_reviews([valid],root),[])
            self.assertEqual(verified_reviews([{**valid,'evidence':'../escape.json'}],root),[])


class PrivacyTests(unittest.TestCase):
    def test_root_name_is_stable_and_other_private_fields_fail_closed(self):
        root=Path('/home/developer/project')
        report={'metadata':{'component':{'name':str(root/'image.tar')}}}
        result=public_sbom(report,'postgres','sha256:abc',root)
        self.assertEqual(result['metadata']['component']['name'],'runasmidja/postgres@sha256:abc')
        for value in ('/home/other/file','/Users/other/file',r'C:\Users\other\file','D:/workspace/file',str(root)):
            with self.subTest(value=value), self.assertRaises(RuntimeError):
                public_sbom({'components':[{'name':value}]},'postgres','exact',root)

    def test_repository_gate_rejects_private_paths_anywhere_in_sboms(self):
        with tempfile.TemporaryDirectory() as folder:
            root=Path(folder);(root/'sbom/images').mkdir(parents=True);path=root/'sbom/images/fixture.json'
            for value in ('/home/person/project','/Users/person/project',r'C:\Work\project',str(root)):
                path.write_text(json.dumps({'metadata':{'properties':[{'value':value}]}}))
                self.assertTrue(check_sboms(root))
            path.write_text(json.dumps({'components':[{'name':'public-package'}]}));self.assertEqual(check_sboms(root),[])


if __name__=='__main__': unittest.main()
