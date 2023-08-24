import check50
import check50.py
import random
import string

python_command = "python3.11"
submission = "password_cracker.py"
solution = "password_cracker_solution.pyc"
file1 = "secret.zip"

help_message = "Check to make sure that your output is formatted exactly including any space, tab, and newline characters."


@check50.check()
def exists():
    """Does the solution .py exist?"""
    check50.exists(submission)
    check50.include(solution)
    check50.include(file1)

@check50.check(exists)
def compiles():
    """Does your .py file compile?"""
    check50.py.compile(submission)

@check50.check(compiles)
def check1():
    """Can crack a password protected .zip file?"""
        
    expected = check50.run(f"{python_command} {solution} {file1}").stdout()
    actual   = check50.run(f"{python_command} {submission} {file1}").stdout()
    
    file_content = check50.run("cat secret_message.txt").stdout()
    
    if expected != actual and file_content.strip() == "WOOHOO!":
        raise check50.Mismatch(expected, actual, help=help_message)
    


