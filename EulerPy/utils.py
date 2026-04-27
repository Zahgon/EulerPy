# -*- coding: utf-8 -*-

from __future__ import unicode_literals

import sys
import glob
import math

from EulerPy.problem import ProblemFile


def problem_glob(extension='.py'):
    """Returns ProblemFile objects for all valid problem files"""
    pass

# Use the resource module instead of time.clock() if possible (on Unix)
try:
    import resource

except ImportError:
    import time

    def clock():
        """
        Under Windows, system CPU time can't be measured. Return
        time.process_time() as user time and None as system time.
        """
        pass

else:
    def clock():
        """
        Returns a tuple (t_user, t_system) since the start of the process.
        This is done via a call to resource.getrusage, so it avoids the
        wraparound problems in time.clock().
        """
        pass


def human_time(timespan, precision=3):
    """Formats the timespan in a human readable format"""
    pass


def format_time(start, end):
    """Returns string with relevant time information formatted properly"""
    pass
