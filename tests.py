# coding=utf-8
"""
    Testing the folder
"""
import subprocess
import unittest


class MyTestCase(unittest.TestCase):
    def test_python2(self):
        val = subprocess.run(["python2", "-m", "unittest", "discover", "-s", "source",
                              "-p", "tests.py"])
        self.assertEqual(val.returncode, 0)
