import sys
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

# Сабпарсер для копирования файла
parser_copy = subparsers.add_parser('copy', help="Copy file <from> to <destanation>")
parser_copy.add_argument('filename', type=str, help="Source file")
parser_copy.add_argument('destanation', type=str, help="Destanation folder")

# Сабпарсер удаления файла
parser_copy = subparsers.add_parser('del', help="Delete file")
parser_copy.add_argument('filename', type=str, help="File name")

# Сабпарсер для подсчета файлов
parser_copy = subparsers.add_parser('count', help="Count files in directory")
parser_copy.add_argument('folder', type=str, help="Folder name")

args = parser.parse_args()
print (args)

if args.command == 'copy':
    print(f"Copying file {args.filename} to {args.destanation}")
elif args.command == 'del':
    print(f"Deleting file {args.filename} ...")
elif args.command == 'count':
    print(f"Counting files in {args.folder} ...")
else:
    parser.print_help()


print("Done!")