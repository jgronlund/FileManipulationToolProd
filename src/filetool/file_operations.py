__author__ = "Jacob Gronlund"

""""
Script contains all file operation functions including:
- create file
- copy file
- combine two files
- delete file
"""

import os
import sys
import tempfile
import logging
from pathlib import Path

from filetool.exceptions import FileAlreadyExists, FileDoesNotExist

LOGGER = logging.getLogger(__name__)

def safe_write(filepath: Path, data: bytes) -> None:
    """
    Docstring for safe_write
    
    :param filepath: Description
    :type filepath: Path
    :param data: file content to be written
    :type data: bytes
    """

    dir_name = os.path.dirname(filepath)
    with tempfile.NamedTemporaryFile(delete=False, dir=dir_name) as tmp:
        tmp.write(data)
        temp_name = tmp.name
        LOGGER.debug(f"Wrote data to tmp file {temp_name}")

    os.replace(temp_name, filepath)
    LOGGER.debug(f"Successfully wrote content to {filepath}")


def create_file(filepath: str, content: str) -> None:
    """
    Creates file 
    
    :param filepath: filepath for file to be created at e.g. "/Documents/new_file.txt"
    :type filepath: str
    :param content: text to input into the file 
    :type content: Optional[str]
    """
    p = Path(filepath)

    if p.exists():
        raise FileAlreadyExists(f"File '{filepath}' already exists.")
    
    encoded_bytes = content.encode("utf-8")

    safe_write(p, encoded_bytes)
    LOGGER.info(f"Successfully created file: {filepath}")


def copy_file(source: str, destination: str) -> None:
    """
    Docstring for copy_file
    
    :param source: filepath to source file
    :type source: str
    :param destination: filepath to destination file
    :type destination: str
    """
    src = Path(source)
    dst = Path(destination)

    if not src.exists():
        raise FileDoesNotExist(f"Source file '{source}' does not exist.")

    safe_write(dst, src.read_bytes())
    LOGGER.info(f"Successfully copied content from {source} to {destination}")


def combine_files(filepath_1: str, filepath_2: str, destination: str) -> None:
    """
    Combine content of file 1 and file 2 and write it to the destination file
    
    :param filepath_1: Description
    :type filepath_1: str
    :param filepath_2: Description
    :type filepath_2: str
    :param destination: Description
    :type destination: str
    """
    p1 = Path(filepath_1)
    p2 = Path(filepath_2)
    dst = Path(destination)

    if not p1.exists() or not p2.exists():
        raise FileDoesNotExist("One or both input files do not exist.")

    combined_bytes = p1.read_bytes() + p2.read_bytes()
    safe_write(dst, combined_bytes)
    LOGGER.info(f"Successfully combined files to create file: {destination}")


def delete_file(filepath: str) -> None:
    """
    Delete inputted file

    :param filepath: filepath of file to be deleted
    :type filepath: str
    """
    p = Path(filepath)

    if not p.exists():
        raise FileDoesNotExist(f"File '{filepath}' does not exist.")

    p.unlink()
    LOGGER.info(f"Successfully deleted file: {filepath}")
