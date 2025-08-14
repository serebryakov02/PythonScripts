#!/usr/bin/env python3

import sys

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print('Usage: python3 cutfile.py <file> <line_number>')
        sys.exit(1)

    file_name = sys.argv[1]

    try:
        line_number = int(sys.argv[2])
        if line_number <= 0:
            raise ValueError
    except ValueError:
        print('line_number must be a positive integer')
        sys.exit(1)

    try:
        with open(file_name) as f:
            content = f.readlines()

        if not content:
            print(f'File {file_name} is empty.')
            sys.exit(1)

        new_content = content[:line_number - 1]
        with open(file_name, 'w') as f:
            f.writelines(new_content)

        print(f"File '{file_name}' truncated from line {line_number}.")
    except FileNotFoundError:
        print(f'File {file_name} not found.')
    except PermissionError:
        print(f'Permission denied: {file_name}')