import sys
import argparse
from funker import *

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

# Сабпарсер копирования файла
parser_copy = subparsers.add_parser('copy', help="Copy file <from> to <destanation>")
parser_copy.add_argument('filename', type=str, help="Source file")
parser_copy.add_argument('destanation', type=str, help="Destanation folder")

# Сабпарсер удаления файла
parser_del = subparsers.add_parser('del', help="Delete file")
parser_del.add_argument('filename', type=str, help="File name")

# Сабпарсер подсчета файлов
parser_count = subparsers.add_parser('count', help="Count files in directory")
parser_count.add_argument('folder', type=str, help="Folder name")
parser_count.add_argument('-r', '--recursive', action='store_true', help="Count files recursively")

# Сабпарсер поиска фалов по регулярному выражению
parser_search = subparsers.add_parser('search', help="Search for files by regex pattern")
parser_search.add_argument('folder', type=str, help="Folder name")
parser_search.add_argument('pattern', type=str, help="Regex pattern to match file names")

# Сабпарсер генерации тестового набора файлов и папок
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
elif args.command == 'gentest':
    print(f"Generating test data in {args.folder} ...")
    generate_data(args.folder, args.count)
else:
    parser.print_help()


print("Done!")