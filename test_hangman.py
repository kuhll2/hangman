#! /usr/bin/python
import unittest
import subprocess


class TestHangman(unittest.TestCase):
    """
    test class for hangman
    """

    @classmethod
    def setUpClass(cls):
        # runs before ANY tests are executed
        cls.command = "python hangman.py"
        pass

    @classmethod
    def tearDownClass(cls):
        # runs after ALL tests are executed
        pass

    def setUp(self):
        # runs before EACH test
        pass

    def tearDown(self):
        # runs after EACH test
        pass

    def test_run_hangman(self):
        """
        test running the hangman program
        """
        # setup

        # execute
        subprocess.run(self.command)

        # assert

        # teardown
