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
    p = Problem(num)

    filename = filename or p.filename()

    if not os.path.isfile(filename):
        # Attempt to verify the first problem file matched by glob
        if p.glob:
            filename = str(p.file)
        else:
            click.secho('No file found for problem %i.' % p.num, fg='red')
            sys.exit(1)

    solution = p.solution
    click.echo('Checking "{}" against solution: '.format(filename), nl=False)

    cmd = (sys.executable or 'python', filename)
    start = clock()
    proc = subprocess.Popen(cmd, stdout=subprocess.PIPE)
    stdout = proc.communicate()[0]
    end = clock()
    time_info = format_time(start, end)

    # Return value of anything other than 0 indicates an error
    if proc.poll() != 0:
        click.secho('Error calling "{}".'.format(filename), fg='red')
        click.secho(time_info, fg='cyan')

        # Return None if option is not --verify-all, otherwise exit
        return sys.exit(1) if exit else None

    # Decode output if returned as bytes (Python 3)
    if isinstance(stdout, bytes):
        output = stdout.decode('ascii')

    # Split output lines into array; make empty output more readable
    output_lines = output.splitlines() if output else ['[no output]']

    # If output is multi-lined, print the first line of the output on a
    # separate line from the "checking against solution" message, and
    # skip the solution check (multi-line solution won't be correct)
    if len(output_lines) > 1:
        is_correct = False
        click.echo()  # force output to start on next line
        click.secho('\n'.join(output_lines), bold=True, fg='red')
    else:
        is_correct = output_lines[0] == solution
        fg_colour = 'green' if is_correct else 'red'
        click.secho(output_lines[0], bold=True, fg=fg_colour)

    click.secho(time_info, fg='cyan')

    # Remove any suffix from the filename if its solution is correct
    if is_correct:
        p.file.change_suffix('')

    # Exit here if answer was incorrect, otherwise return is_correct value
    return sys.exit(1) if exit and not is_correct else is_correct


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


@click.command(name='euler', options_metavar='[OPTION]')
@click.argument('problem', default=0, type=click.IntRange(0, None))
@euler_options
@click.version_option(version=__version__, message="EulerPy %(version)s")
def main(option, problem):
    """Python-based Project Euler command line tool."""
    # No problem given (or given option ignores the problem argument)
    if problem == 0 or option in {skip, verify_all}:
        # Determine the highest problem number in the current directory
        files = problem_glob()
        problem = max(file.num for file in files) if files else 0

        # No Project Euler files in current directory (no glob results)
        if problem == 0:
            # Generate the first problem file if option is appropriate
            if option not in {cheat, preview, verify_all}:
                msg = "No Project Euler files found in the current directory."
                click.echo(msg)
                option = generate

            # Set problem number to 1
            problem = 1

        # --preview and no problem; preview the next problem
        elif option is preview:
            problem += 1

        # No option and no problem; generate next file if answer is
        # correct (verify() will exit if the solution is incorrect)
        if option is None:
            verify(problem)
            problem += 1
            option = generate

    # Problem given but no option; decide between generate and verify
    elif option is None:
        option = verify if Problem(problem).glob else generate

    # Execute function based on option
    option(problem)
    sys.exit(0)
