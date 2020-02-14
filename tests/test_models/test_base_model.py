#!/usr/bin/python3
# -*- coding: utf-8 -*-
"""Unittest for base model module.

This unittest is a collection of possible edge cases
on which this module should not be expected to fail,
and cases on which it is expected to fail.

"""
from models.base_model import BaseModel
from datetime import datetime
import pep8
import unittest


class TestBaseModel(unittest.TestCase):
    """...

    ...
    ...
    """
    def test_pep8_of_base_model(self):
        """pep8 test.

        This test is designed to make sure the Python code
        is up to the pep8 standard.

        """
        syntax = pep8.StyleGuide(quit=True)
        check = syntax.check_files(['models/base_model.py'])
        self.assertEqual(
            check.total_errors, 0,
            "Found code style errors (and warnings)."
        )

    def test_base_model_id_is_string(self):
        """UUID format testing.

        This test is designed to check if any generated UUID
        is correctly generated and has the propper format.

        """
        bm = BaseModel()
        self.assertIsInstance(bm.id, str)

    def test_base_model_created_at_is_datetime(self):
        """Datetime test.

        This test is designed to check if the date and time in which a
        class was created are correctly assigned.

        """
        bm = BaseModel()
        self.assertIsInstance(bm.created_at, datetime)

    def test_base_model_updated_at_is_datetime(self):
        """Datetime test.

        This test is designed to check if the date and time in which a
        class is updated are correctly assigned.

        """
        bm = BaseModel()
        self.assertIsInstance(bm.updated_at, datetime)
