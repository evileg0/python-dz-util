import sys
import argparse

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(dest="command")

# Сабпарсер для копирования файла
parser_copy = subparsers.add_parser('copy', help="Copy file <from> to <destanation>")
parser_copy.add_argument('filename', type=str, help="Source file")
parser_copy.add_argument('destanation', type=str, help="Destanation folder")

args = parser.parse_args()
print (args)

if args.command == 'copy':
    print(f"Copying file {args.filename} to {args.destanation}")
elif args.command == 'delete':
    print(f"Deleting file...")
elif args.command == 'count':
    print(f"Counting files...")
else:
    parser.print_help()


print("Dz-statrt...")