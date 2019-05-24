#! /usr/bin/python
import unittest
import subprocess
import hangman
import random


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

    def test_should_pick_word(self):
        """
        test running pick_word() fcn
        """
        # setup

        # execute
        actual = hangman.pick_word(hangman.read_file())

        # assert
        self.assertTrue(len(actual) > 0)

        # teardown

    def test_should_read_file(self):
        """
        test running read_file() fcn
        """
        # setup

        # execute
        actual = hangman.read_file()

        # assert
        self.assertTrue(len(actual) > 0)

        # teardown

    def test_should_get_word(self):
        """
        test running get_word() fcn
        """
        # setup

        # execute
        actual, actual2, actual3 = hangman.get_word(hangman.read_file())

        # assert
        self.assertTrue(len(actual) > 0 and len(actual2) > 0 and len(actual3) > 0)

        # teardown

    def test_should_get_indexes(self):
        """
        test running get_indexes() fcn
        """
        # setup
        letters = ['t', 'e', 's', 't']
        guess = 't'
        count = letters.count(guess)

        # execute
        actual = hangman.get_indexes(count, letters, guess)

        # assert
        self.assertTrue(len(actual) > 0)

        # teardown