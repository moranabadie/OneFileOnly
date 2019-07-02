"""
    Testing the folder
"""
import unittest


class MyTestCase(unittest.TestCase):
    def test_import_run(self):
        import run
        self.assertNotEqual(run, None)
