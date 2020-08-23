#!env/bin/python

"""Check for new versions of KSP modules"""

import os
import fnmatch
import json
# import requests

KSP_ROOT = '/Users/trosine/Library/Application Support/Steam/steamapps' \
    + '/common/Kerbal Space Program'


def find(pattern, path):
    """Recursively find files matching a pattern"""
    result = []
    for root, dirs, files in os.walk(path):
        del dirs
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


def check_version(filename):
    """Check the version from the version file with the one in the URL"""
    print('Loading', filename)
    with open(filename) as filehandle:
        try:
            version = json.load(filehandle)
        except ValueError as exc:
            print('Exception caught in', filename)
            print(' ', exc)
            return
        print(version['VERSION'])


def main():
    """Check for versions"""
    for name in find('*.version', KSP_ROOT):
        check_version(name)


if __name__ == '__main__':
    main()
