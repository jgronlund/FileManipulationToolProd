__author__ = "Jacob Gronlund"

""""
Unit tests for cli.py
"""

import sys
from unittest.mock import patch
from filetool import cli


def test_create_command_calls_create_file():
    test_args = ["filetool", "create", "test.txt", "--content", "hello"]

    with patch.object(sys, "argv", test_args):
        with patch("filetool.cli.create_file") as mock_create:
            exit_code = cli.main()

            mock_create.assert_called_once_with("test.txt", "hello")
            assert exit_code == 0

def test_copy_command_calls_copy_file():
    test_args = ["filetool", "copy", "a.txt", "b.txt"]

    with patch.object(sys, "argv", test_args):
        with patch("filetool.cli.copy_file") as mock_copy:
            exit_code = cli.main()

            mock_copy.assert_called_once_with("a.txt", "b.txt")
            assert exit_code == 0

def test_combine_command_calls_combine_files():
    test_args = ["filetool", "combine", "a.txt", "b.txt", "c.txt"]

    with patch.object(sys, "argv", test_args):
        with patch("filetool.cli.combine_files") as mock_combine:
            exit_code = cli.main()

            mock_combine.assert_called_once_with("a.txt", "b.txt", "c.txt")
            assert exit_code == 0

def test_delete_command_calls_delete_file():
    test_args = ["filetool", "delete", "a.txt"]

    with patch.object(sys, "argv", test_args):
        with patch("filetool.cli.delete_file") as mock_delete:
            exit_code = cli.main()

            mock_delete.assert_called_once_with("a.txt")
            assert exit_code == 0
            