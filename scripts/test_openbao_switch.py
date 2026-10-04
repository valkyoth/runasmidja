"""Persistent switch checkpoint keeps failed retries bound to original custody."""
import hashlib
import json
import os
import tempfile
import unittest
from contextlib import ExitStack
from pathlib import Path
from unittest.mock import patch
import switch_openbao as switch
import stack
from custody import read_private


class SwitchRetryTests(unittest.TestCase):
    def test_failure_retry_preserves_checkpoint_and_removes_only_captured_container(self):
        for fault in ('stop', 'identity', 'running', 'remove', 'startup', 'custody', 'values'):
            with self.subTest(fault=fault), tempfile.TemporaryDirectory() as directory, ExitStack() as patches:
                root = Path(directory); active = [fault]; exists = [True]; custody_calls = [0]
                runtime = {'key':'credential'}; info = {'Id':'owned-id','State':{'Running':False}}
                def fail(stage):
                    if active[0] == stage: raise RuntimeError(stage)
                def owned(*args):
                    if not exists[0]: return None
                    return {**info, 'Id':'wrong' if active[0]=='identity' and custody_calls[0]>1 else 'owned-id',
                            'State':{'Running':active[0]=='running'}}
                def stop(): fail('stop'); custody_calls[0] += 1
                def podman(*args):
                    self.assertEqual(args, ('rm','owned-id')); fail('remove'); exists[0] = False
                def up(): fail('startup'); exists[0] = True
                def custody():
                    custody_calls[0] += 1
                    return {'hash':'wrong' if active[0]=='custody' and custody_calls[0]>1 else 'original'}
                def private(path):
                    return json.dumps({'image':'wolfi'}) if path.name=='receipt.json' else read_private(path)
                patches.enter_context(patch.dict(os.environ, {'RUNASMIDJA_OPENBAO_PROFILE':'wolfi'}))
                patches.enter_context(patch.object(switch, 'STATE', root))
                patches.enter_context(patch.object(switch, 'INSTANCE', 'v023-wolfi-bao'))
                for name in ('selected_image', 'verify_images', 'fixture_images', 'preflight', 'removable'):
                    patches.enter_context(patch.object(switch, name))
                patches.enter_context(patch.object(switch, 'cached_image', return_value='wolfi'))
                patches.enter_context(patch.object(switch, 'pins', return_value={'upstream':{'image':'official'}}))
                patches.enter_context(patch.object(switch, 'runtime_values', side_effect=[runtime, {'key':'changed'}] if fault=='values' else None, return_value=runtime))
                for name, function in {'owned':owned,'stop':stop,'podman':podman,'custody':custody,'read_private':private}.items():
                    patches.enter_context(patch.object(switch, name, side_effect=function))
                patches.enter_context(patch.object(stack, 'up', side_effect=up))
                with self.assertRaises(RuntimeError): switch.switch('official')
                record = json.loads(read_private(root/'bao-switch.json'))
                self.assertEqual(record['custody'], {'hash':'original'})
                self.assertEqual(record['values'], hashlib.sha256(json.dumps(runtime,sort_keys=True).encode()).hexdigest())
                active[0] = None; custody_calls[0] = 0
                with patch.object(switch, 'runtime_values', return_value=runtime): switch.switch('official')
                self.assertFalse((root/'bao-switch.json').exists())
                self.assertTrue(exists[0])


if __name__ == '__main__': unittest.main()
