#!/usr/bin/env python
import os
import re
import sys
import json

JSON_FILE_REGEX = '.+\\.json$'


def _print(_output):
    sys.stderr.write(_output + '\n')


def check_json(root_dir, file_regex):
    """
    Requires:
        root_dir    string  full path of directory to recursively check
        file_regex  string  regex of file extensions to match and check
    """
    for root, subs, files in os.walk(root_dir):
        for file in files:
            if re.match(file_regex, file, re.IGNORECASE):
                print('Checking %s' % os.path.join(root, file))
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    if os.stat(file_path).st_size > 0:
                        try:
                            data = json.load(f)
                        except Exception as _exception:
                            _error = '\n-- JSON parse error\n-- File: %s\n-- Info: %s' % (
                                file_path, _exception
                            )
                            _print(_error)
                            _print('\nCommit aborted by: %s' % sys.argv[0])
                            sys.exit(1)


if __name__ == '__main__':
    OS_CWD = os.getcwd()
    try:
        FILE_EXT = sys.argv[1]
        JSON_FILE_REGEX = '.+\\%s' % str(FILE_EXT)
    except:
        pass
    #  print('%s: Checking recursively in: %s' % (sys.argv[0], OS_CWD))
    check_json(OS_CWD, JSON_FILE_REGEX)
    print('No JSON errors detected.')
