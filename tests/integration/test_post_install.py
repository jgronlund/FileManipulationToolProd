__author__ = "Jacob Gronlund"

""""
Integration tests for filetool application
"""

import subprocess
from pathlib import Path
import pytest


def run_cmd(cmd: list[str], cwd: Path):
    return subprocess.run(
        cmd,
        cwd=cwd,
        capture_output=True,
        text=True,
    )

@pytest.mark.integration()
def test_help_command():
    result = subprocess.run(
        ["filetool", "--help"],
        capture_output=True,
        text=True,
    )

    assert result.returncode == 0
    assert "usage" in result.stdout.lower()

@pytest.mark.integration()
def test_full_file_lifecycle(tmp_path: Path):
    # CREATE
    result = run_cmd(
        ["filetool", "create", "a.txt", "--content", "hello"],
        tmp_path,
    )
    assert result.returncode == 0

    a = tmp_path / "a.txt"
    assert a.exists()
    assert a.read_text() == "hello"

    # COPY
    result = run_cmd(
        ["filetool", "copy", "a.txt", "b.txt"],
        tmp_path,
    )
    assert result.returncode == 0

    b = tmp_path / "b.txt"
    assert b.exists()
    assert b.read_text() == "hello"

    # COMBINE
    result = run_cmd(
        ["filetool", "combine", "a.txt", "b.txt", "c.txt"],
        tmp_path,
    )
    assert result.returncode == 0

    c = tmp_path / "c.txt"
    assert c.exists()
    assert c.read_text() == "hellohello"

    # DELETE
    result = run_cmd(
        ["filetool", "delete", "b.txt"],
        tmp_path,
    )
    assert result.returncode == 0

    assert not b.exists()
