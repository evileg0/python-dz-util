import sys
import argparse
from funker import *

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

# Subparser for file copy
parser_copy = subparsers.add_parser('copy', help="Copy file <from> to <destination>")
parser_copy.add_argument('filename', type=str, help="Source file")
parser_copy.add_argument('destination', type=str, help="Destination folder")

# Subparser for removing file
parser_del = subparsers.add_parser('del', help="Delete file")
parser_del.add_argument('filename', type=str, help="File name")

# Subparser for file counter
parser_count = subparsers.add_parser('count', help="Count files in directory")
parser_count.add_argument('folder', type=str, help="Folder name")
parser_count.add_argument('-r', '--recursive', action='store_true', help="Count files recursively")

# Subparser for serching files by regexp
parser_search = subparsers.add_parser('search', help="Search for files by regex pattern")
parser_search.add_argument('folder', type=str, help="Folder name")
parser_search.add_argument('pattern', type=str, help="Regex pattern to match file names")

# Subparser for adding creation date to filenames
parser_add_date = subparsers.add_parser('add_date', help="Add creation date to filenames in directory")
parser_add_date.add_argument('folder', type=str, help="Folder name")
parser_add_date.add_argument('-r', '--recursive', action='store_true', help="Process files recursively")

# Subparser for analysing folder sizes
parser_analyse = subparsers.add_parser('analyse', help="Analyse folder sizes")
parser_analyse.add_argument('folder', type=str, help="Folder name")

# Subparser for test data generation
parser_gen = subparsers.add_parser('gentest', help="Generate test data in a folder")
parser_gen.add_argument('folder', type=str, help="Folder name")
parser_gen.add_argument('--count', type=int, default=5, help="Number of folders to create")

args = parser.parse_args()
print (args)

if args.command == 'copy':
    print(f"Copying file {args.filename} to {args.destanation} ...")
    copy_file(args.filename, args.destanation)
elif args.command == 'del':
    print(f"Deleting file {args.filename} ...")
    delete_file(args.filename)
elif args.command == 'count':
    print(f"Counting files in {args.folder} ...")
    print(f"Files: {count_files(args.folder, args.recursive)}")
elif args.command == 'search':
    print(f"Searching for {args.pattern} in {args.folder} ...")
    print(f"{search_files(args.folder, args.pattern)}")
elif args.command == 'add_date':
    print(f"Adding file creation date for files in {args.folder} ...")
    add_creation_date_to_filename(args.folder, args.recursive)
elif args.command == 'analyse':
    analyse_folder(args.folder)
elif args.command == 'gentest':
    print(f"Generating test data in {args.folder} ...")
    generate_data(args.folder, args.count)
else:
    parser.print_help()


print("Done!")