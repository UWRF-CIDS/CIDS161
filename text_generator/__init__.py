import check50
import check50.py
import random
import string

python_command = "python3.11"
submission = "text_generator.py"
solution   = "text_generator_solution.pyc"

help_message = "Check to make sure that your output is formatted exactly including any space, tab, and newline characters."


@check50.check()
def exists():
    """Does the solution .py exist?"""
    check50.exists(submission)
    check50.include(solution)
    check50.include("corpus.txt")

@check50.check(exists)
def compiles():
    """Does your .py file compile?"""
    check50.py.compile(submission)

@check50.check(compiles)
def check1():
    """Is output correct for input seed 1, length 10, and staring words 'it was the'?"""
    
    inputs = ["1", "10", "it was the"]
    
    expected = check50.run(f"{python_command} {solution}").stdin(inputs[0]).stdin(inputs[1]).stdin(inputs[2]).stdout()
    actual   = check50.run(f"{python_command} {submission}").stdin(inputs[0]).stdin(inputs[1]).stdin(inputs[2]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
  

@check50.check(compiles)
def check2():
    """Is output correct for input seed 1, length 100, and staring words 'it was the'?"""
    
    inputs = ["1", "10", "it was the"]
    
    expected = check50.run(f"{python_command} {solution}").stdin(inputs[0]).stdin(inputs[1]).stdin(inputs[2]).stdout()
    actual   = check50.run(f"{python_command} {submission}").stdin(inputs[0]).stdin(inputs[1]).stdin(inputs[2]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
  


@check50.check(compiles)
def check3():
    """Is output correct for input seed 2, length 100, and staring words 'All day long'?"""
    
    inputs = ["2", "100", "All day long"]
    
    expected = check50.run(f"{python_command} {solution}").stdin(inputs[0]).stdin(inputs[1]).stdin(inputs[2]).stdout()
    actual   = check50.run(f"{python_command} {submission}").stdin(inputs[0]).stdin(inputs[1]).stdin(inputs[2]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
  


@check50.check(compiles)
def check4():
    """Is output correct for a random seed, random length, and staring words 'All day long'?"""
    
    inputs = [str(random.randint(0,100)), str(random.randint(100, 400)), "All day long"]
    
    expected = check50.run(f"{python_command} {solution}").stdin(inputs[0]).stdin(inputs[1]).stdin(inputs[2]).stdout()
    actual   = check50.run(f"{python_command} {submission}").stdin(inputs[0]).stdin(inputs[1]).stdin(inputs[2]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
  
