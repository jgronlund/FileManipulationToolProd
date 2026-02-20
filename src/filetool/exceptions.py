__author__ = "Jacob Gronlund"

""""
Exceptions file
"""

class FileToolError(Exception):
    """Base exception for filetool."""


class FileAlreadyExists(FileToolError):
    pass


class FileDoesNotExist(FileToolError):
    pass


class PermissionDenied(FileToolError):
    pass