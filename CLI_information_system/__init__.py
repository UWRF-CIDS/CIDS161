import check50
import check50.py
import random
import string

python_command = "python3.11"
submission = "CLI_information_system.py"
solution   = "CLI_information_system_solution.pyc"

help_message = "Check to make sure that your output is formatted exactly including any space, tab, and newline characters."


@check50.check()
def exists():
    """Does the solution .py exist?"""
    check50.exists(submission)
    check50.include(solution)

@check50.check(exists)
def compiles():
    """Does your .py file compile?"""
    check50.py.compile(submission)

@check50.check(compiles)
def check1():
    """Is output correct for input hello 5?"""
    
    inputs = ["hello", "5"]
    
    expected = check50.run(f"{python_command} {solution}").stdin(inputs[0]).stdin(inputs[1]).stdout()
    actual   = check50.run(f"{python_command} {submission}").stdin(inputs[0]).stdin(inputs[1]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
