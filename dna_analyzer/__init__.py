import check50
import check50.py
import random
import string

python_command = "python3.11"
submission = "dna_analyzer.py"
solution   = "dna_analyzer_solution.pyc"

help_message = "Check to make sure that your output is formatted exactly including any space, tab, and newline characters."


@check50.check()
def exists():
    """Does the solution .py exist?"""
    check50.exists(submission)
    check50.include(solution)
    check50.include("databases")
    check50.include("sequences")
    
    

@check50.check(exists)
def compiles():
    """Does your .py file compile?"""
    check50.py.compile(submission)

@check50.check(compiles)
def check1():
    """Is output correct small database sequence 1?"""

    inputs = ["databases/small.csv", "sequences/1.txt"]
    
    expected = check50.run(f"{python_command} {solution} {inputs[0]} {inputs[1]}").stdout()
    actual   = check50.run(f"{python_command} {submission}  {inputs[0]} {inputs[1]}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
  
   
@check50.check(compiles)
def check2():
    """Is output correct small database sequence 12?"""

    inputs = ["databases/small.csv", "sequences/12.txt"]
    
    expected = check50.run(f"{python_command} {solution} {inputs[0]} {inputs[1]}").stdout()
    actual   = check50.run(f"{python_command} {submission}  {inputs[0]} {inputs[1]}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)


@check50.check(compiles)
def check4():
    """Is output correct large database and sequence 1?"""

    inputs = ["databases/large.csv", f"sequences/1.txt"]
    
    expected = check50.run(f"{python_command} {solution} {inputs[0]} {inputs[1]}").stdout()
    actual   = check50.run(f"{python_command} {submission}  {inputs[0]} {inputs[1]}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
    return 2
  
  
@check50.check(check4)
def check5(seq):
    """Is output correct large database and sequence 2?"""

    inputs = ["databases/large.csv", f"sequences/{str(seq)}.txt"]
    
    expected = check50.run(f"{python_command} {solution} {inputs[0]} {inputs[1]}").stdout()
    actual   = check50.run(f"{python_command} {submission}  {inputs[0]} {inputs[1]}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
    return 3


@check50.check(check5)
def check6(seq):
    """Is output correct large database and sequence 3?"""

    inputs = ["databases/large.csv", f"sequences/{str(seq)}.txt"]
    
    expected = check50.run(f"{python_command} {solution} {inputs[0]} {inputs[1]}").stdout()
    actual   = check50.run(f"{python_command} {submission}  {inputs[0]} {inputs[1]}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
    return 4

@check50.check(check6)
def check7(seq):
    """Is output correct large database and sequence 4?"""

    inputs = ["databases/large.csv", f"sequences/{str(seq)}.txt"]
    
    expected = check50.run(f"{python_command} {solution} {inputs[0]} {inputs[1]}").stdout()
    actual   = check50.run(f"{python_command} {submission}  {inputs[0]} {inputs[1]}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
    return 5

@check50.check(check7)
def check8(seq):
    """Is output correct large database and sequence 5?"""

    inputs = ["databases/large.csv", f"sequences/{str(seq)}.txt"]
    
    expected = check50.run(f"{python_command} {solution} {inputs[0]} {inputs[1]}").stdout()
    actual   = check50.run(f"{python_command} {submission}  {inputs[0]} {inputs[1]}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message) 
    return 6
    
    
@check50.check(check8)
def check9(seq):
    """Is output correct large database and sequence 6?"""

    inputs = ["databases/large.csv", f"sequences/{str(seq)}.txt"]
    
    expected = check50.run(f"{python_command} {solution} {inputs[0]} {inputs[1]}").stdout()
    actual   = check50.run(f"{python_command} {submission}  {inputs[0]} {inputs[1]}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
    return 18


@check50.check(check9)
def check10(seq):
    """Is output correct large database and sequence 18?"""

    inputs = ["databases/large.csv", f"sequences/{str(seq)}.txt"]
    
    expected = check50.run(f"{python_command} {solution} {inputs[0]} {inputs[1]}").stdout()
    actual   = check50.run(f"{python_command} {submission}  {inputs[0]} {inputs[1]}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
    return 19


@check50.check(check10)
def check11(seq):
    """Is output correct large database and sequence 19?"""

    inputs = ["databases/large.csv", f"sequences/{str(seq)}.txt"]
    
    expected = check50.run(f"{python_command} {solution} {inputs[0]} {inputs[1]}").stdout()
    actual   = check50.run(f"{python_command} {submission}  {inputs[0]} {inputs[1]}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
    return 20
    
@check50.check(check11)
def check12(seq):
    """Is output correct large database and sequence 20?"""

    inputs = ["databases/large.csv", f"sequences/{str(seq)}.txt"]
    
    expected = check50.run(f"{python_command} {solution} {inputs[0]} {inputs[1]}").stdout()
    actual   = check50.run(f"{python_command} {submission}  {inputs[0]} {inputs[1]}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
    
