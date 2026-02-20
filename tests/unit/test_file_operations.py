__author__ = "Jacob Gronlund"

""""
Unit tests for file_operations.py
"""

import shutil
import sys
import os
from unittest import TestCase
from pathlib import Path

from filetool.file_operations import create_file, copy_file, combine_files, delete_file


class TestFileOperations(TestCase):

    def setUp(self):
        self.tmp_folder = Path.cwd().absolute() / "tmp_folder"
        self.tmp_folder.mkdir(parents=True, exist_ok=True)
        
    def tearDown(self):
        if os.path.exists(self.tmp_folder):
            shutil.rmtree(self.tmp_folder)

    def test_create_file(self):
        f = self.tmp_folder / "test.txt"
        create_file(str(f), "hello")
        assert f.read_text() == "hello"


    def test_copy_file(self):
        src = self.tmp_folder / "a.txt"
        dst = self.tmp_folder / "b.txt"

        src.write_text("data")
        copy_file(str(src), str(dst))

        assert dst.read_text() == "data"


    def test_combine_files(self):
        f1 = self.tmp_folder / "f1.txt"
        f2 = self.tmp_folder / "f2.txt"
        dst = self.tmp_folder / "out.txt"

        f1.write_text("A")
        f2.write_text("B")

        combine_files(str(f1), str(f2), str(dst))

        assert dst.read_text() == "AB"


    def test_delete_file(self):
        f = self.tmp_folder / "delete.txt"
        f.write_text("x")

        delete_file(str(f))
        assert not f.exists()