import check50
import check50.py
import random

python_command = "python3.11"
submitted_file = "error_checking.py"
solution_file = "error_checking_solution.pyc"


import string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

@check50.check()
def exists():
    """Does the solution .py exist?"""
    check50.exists(submitted_file)
    check50.include(solution_file)
    
@check50.check(exists)
def compiles():
    """Does your .py file compile?"""
    check50.py.compile(submitted_file)
    
@check50.check(compiles)
def check1():
    """Is output correct for valid input?"""

    inputs = ["1 + 2", "1 - 2", "1 * 2", "1 / 2"]    
    for test_input in inputs:
        expected = check50.run(f"{python_command} {solution_file}").stdin(test_input).stdout()
        actual   = check50.run(f"{python_command} {submitted_file}").stdin(test_input).stdout()
    
        if expected != actual:
            raise check50.Mismatch(expected, actual)


@check50.check(compiles)
def check2():
    """Is error message correct for input A + 2?"""
    
    test_input = "A + 2"
    
    expected = check50.run(f"{python_command} {solution_file}").stdin(test_input).stdout()
    actual   = check50.run(f"{python_command} {submitted_file}").stdin(test_input).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual)
    

@check50.check(compiles)
def check3():
    """Is error message correct for input 1 + A?"""
    
    test_input = "1 + A"
    
    expected = check50.run(f"{python_command} {solution_file}").stdin(test_input).stdout()
    actual   = check50.run(f"{python_command} {submitted_file}").stdin(test_input).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual)
    


@check50.check(compiles)
def check4():
    """Is error message correct for input 1 A 2?"""
    
    test_input = "1 A 2"
    
    expected = check50.run(f"{python_command} {solution_file}").stdin(test_input).stdout()
    actual   = check50.run(f"{python_command} {submitted_file}").stdin(test_input).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual)
    

@check50.check(compiles)
def check5():
    """Is error message correct for input 1 / 0?"""
    
    test_input = "1 / 0"
    
    expected = check50.run(f"{python_command} {solution_file}").stdin(test_input).stdout()
    actual   = check50.run(f"{python_command} {submitted_file}").stdin(test_input).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual)