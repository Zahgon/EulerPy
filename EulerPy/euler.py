# -*- coding: utf-8 -*-

import os
import sys
import subprocess
from collections import OrderedDict

import click

from EulerPy import __version__
from EulerPy.problem import Problem
from EulerPy.utils import clock, format_time, problem_glob


# --cheat / -c
def cheat(num):
    """View the answer to a problem."""
    pass


# --generate / -g
def generate(num, prompt_default=True):
    """Generates Python file for a problem."""
    pass


# --preview / -p
def preview(num):
    """Prints the text of a problem."""
    pass


# --skip / -s
def skip(num):
    """Generates Python file for the next problem."""
    pass


# --verify / -v
def verify(num, filename=None, exit=True):
    """Verifies the solution to a problem."""
    pass


# --verify-all
def verify_all(num):
    """
    Verifies all problem files in the current directory and
    prints an overview of the status of each problem.
    """
    pass


def euler_options(fn):
    """Decorator to link CLI options with their appropriate functions"""
    pass


@click.command(name="euler", options_metavar="[OPTION]")
@click.argument("problem", default=0, type=click.IntRange(0, None))
@euler_options
@click.version_option(version=__version__, message="EulerPy %(version)s")
def main(option, problem):
    """Python-based Project Euler command line tool."""
    pass
