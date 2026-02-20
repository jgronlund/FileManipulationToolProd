__author__ = "Jacob Gronlund"

""""
CLI script for filetool
"""
import argparse
import logging

from filetool.file_operations import (
    create_file,
    copy_file,
    combine_files,
    delete_file,
)

LOGGER = logging.getLogger(__name__)

def build_parser() -> argparse.Namespace:
    
    # Argument parsing
    parser = argparse.ArgumentParser(
        prog="file_manipulation_tool_prod",
        description="A file manipulation CLI tool."
    )

    parser.add_argument("-v","--verbose", action="store_true", help="Add to show debug logs")
    
    subparsers = parser.add_subparsers(dest="command", required=True)

    # create file
    create_parser = subparsers.add_parser("create", help="Create an empty file e.g. 'filetool create filename.txt' or create a file with content 'filetool create --content 'this is content'")
    create_parser.add_argument("filepath", type=str, help="filepath to create file at. If you just type the filename it will be created in the working directory")
    create_parser.add_argument("--content", default="", type=str, help="add this optional paramater and include text content you would like in the file")

    # copy file
    copy_parser = subparsers.add_parser("copy", help="Copy and paste a file to a destination e.g. filetool copy /a/b/filename.txt a/c/filename.txt")
    copy_parser.add_argument("source", type=str, help="filepath to the file you would like to copy")
    copy_parser.add_argument("destination", type=str, help="filepath to the destination you would like the file to go to")


    # combine 2 files
    combine_parser = subparsers.add_parser("combine", help="Combine two files to make a third file e.g. filetool combine /a/filename.txt /b/file2.txt /c/file3.txt")
    combine_parser.add_argument("filepath1", type=str, help="filepath for file that will be written first when combining")
    combine_parser.add_argument("filepath2", type=str, help="filepath for file that will be written second when combining")
    combine_parser.add_argument("destination", type=str, help="filepath for the desired file destination")

    # delete file
    delete_parser = subparsers.add_parser("delete", help="Delete the file e.g. filetool delete /a/b/filename.txt")
    delete_parser.add_argument("filepath", type=str, help="filepath for file that will be deleted")

    return parser
    
    
def main() -> int:
    """ Main entry point for file manipulation cli command"""

    # Build parser for cli
    parser = build_parser()
    args = parser.parse_args()
    
    # setup logging
    logging.basicConfig(level=logging.DEBUG if args.verbose else logging.INFO, 
                        format="%(asctime)s %(name)s %(levelname)s %(message)s")
    
    if args.command == "create":
        create_file(args.filepath, args.content)
    
    elif args.command == "copy":
        copy_file(args.source, args.destination)
    
    elif args.command == "combine":
        combine_files(args.filepath1, args.filepath2, args.destination)

    elif args.command == "delete":
        delete_file(args.filepath)
    
    return 0
