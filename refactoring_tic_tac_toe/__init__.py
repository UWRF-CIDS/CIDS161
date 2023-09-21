import check50
import check50.py
import random
import string

python_command = "python3.11"
submission = "CLI_information_system.py"
solution   = "CLI_information_system_solution.pyc"
file1 = "todos.json"
file2 = "todos2.json"
original = "original.json"


help_message = "Check to make sure that your output is formatted exactly including any space, tab, and newline characters."


@check50.check()
def exists():
    """Does the solution .py exist?"""
    check50.exists(submission)
    check50.include(solution)
    check50.include(file1)
    check50.include(file2)

@check50.check(exists)
def compiles():
    """Does your .py file compile?"""
    check50.py.compile(submission)

@check50.check(compiles)
def check1():
    """Does pressing 5 to exit work?"""
    
    inputs = ["5\n"]
    
    echo = "echo -e '"
    
    for s in inputs:
        echo += s
        
    echo += "'"
    
    check50.run(f"cp {original} {file1}").stdout()
    check50.run(f"cp {original} {file2}").stdout()
    
    expected = check50.run(f"{echo} | {python_command} {solution}").stdout()
    actual   = check50.run(f"{echo} | {python_command} {submission}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)

