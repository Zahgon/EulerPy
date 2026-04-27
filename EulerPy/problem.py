# -*- coding: utf-8 -*-

import os
import re
import sys
import glob
import json
import linecache
import shutil

import click


# Filenames follow the format (prefix, number, suffix, extension)
BASE_NAME = '{}{:03d}{}{}'
FILE_RE = re.compile(r'(.*)(\d{3})(.*)(\.\w+)')

EULER_DATA = os.path.join(os.path.dirname(__file__), 'data')

class Problem(object):
    """Represents a Project Euler problem of a given problem number"""
    def __init__(self, problem_number):
        self.num = problem_number

    def filename(self, prefix='', suffix='', extension='.py'):
        """Returns filename padded with leading zeros"""
        pass

    @property
    def glob(self):
        """Returns a sorted glob of files belonging to a given problem"""
        file_glob = glob.glob(BASE_NAME.format('*', self.num, '*', '.*'))

        # Sort globbed files by tuple (filename, extension)
        return sorted(file_glob, key=lambda f: os.path.splitext(f))

    @property
    def file(self):
        """Returns a ProblemFile instance of the first matching file"""
        pass

    @property
    def resources(self):
        """Returns a list of resources related to the problem (or None)"""
        pass

    def copy_resources(self):
        """Copies the relevant resources to a resources subdirectory"""
        pass

    @property
    def solution(self):
        """Returns the answer to a given problem"""
        pass

    @property
    def text(self):
        """Parses problems.txt and returns problem text"""
        pass


class ProblemFile(object):
    """Represents a file that belongs to a given Project Euler problem"""
    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return self.filename

    @property
    def _filename_parts(self):
        """Returns (prefix, number, suffix, extension)"""
        pass

    @property
    def prefix(self):
        pass

    @property
    def str_num(self):
        pass

    @property
    def suffix(self):
        pass

    @property
    def extension(self):
        pass

    @property
    def num(self):
        pass

    def change_suffix(self, suffix):
        pass
