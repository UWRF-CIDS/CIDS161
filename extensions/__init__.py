import check50
import check50.py
import random

submission = "extensions.py"
solution   = "extensions_solution.pyc"

help_message = "Check to make sure that your output is formatted exactly including any space, tab, and newline characters."

def get_help_message(expected, actual, commands):
    help_msg = f'''
Output was not as expected. Here are the exact outputs to help you debug.

Expected:
     
{expected}

Actual: 

{actual}

Test input was {format_commands(commands)}.
'''
    return help_msg


def format_commands(commands):
    formatted_input = ""
    for i in range(len(commands)-1):
        formatted_input += f"{commands[i]}, "
    formatted_input += f"and {commands[-1]}"
    return formatted_input
    


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
    """Is output correct for input cat.gif?"""
    
    inputs = ["cat.gif"]
    
    expected = check50.run(f"python {solution}").stdin(inputs[0]).stdout()
    actual   = check50.run(f"python {submission}").stdin(inputs[0]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
    
@check50.check(compiles)
def check2():
    """Is output correct for input dog.png?"""
    
    inputs = ["dog.png"]
    
    expected = check50.run(f"python {solution}").stdin(inputs[0]).stdout()
    actual   = check50.run(f"python {submission}").stdin(inputs[0]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
 
@check50.check(compiles)
def check3():
    """Is output correct for input index.htm?"""
    
    inputs = ["index.htm"]
    
    expected = check50.run(f"python {solution}").stdin(inputs[0]).stdout()
    actual   = check50.run(f"python {submission}").stdin(inputs[0]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
  
@check50.check(compiles)
def check4():
    """Is output correct for input homepage.html?"""
    
    inputs = ["homepage.html"]
    
    expected = check50.run(f"python {solution}").stdin(inputs[0]).stdout()
    actual   = check50.run(f"python {submission}").stdin(inputs[0]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
  

@check50.check(compiles)
def check5():
    """Is output correct for input image.jpg?"""
    
    inputs = ["image.jpg"]
    
    expected = check50.run(f"python {solution}").stdin(inputs[0]).stdout()
    actual   = check50.run(f"python {submission}").stdin(inputs[0]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
  

@check50.check(compiles)
def check5():
    """Is output correct for input file.pdf?"""
    
    inputs = ["file.pdf"]
    
    expected = check50.run(f"python {solution}").stdin(inputs[0]).stdout()
    actual   = check50.run(f"python {submission}").stdin(inputs[0]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
  


@check50.check(compiles)
def check5():
    """Is output correct for input compressed.zip?"""
    
    inputs = ["compressed.zip"]
    
    expected = check50.run(f"python {solution}").stdin(inputs[0]).stdout()
    actual   = check50.run(f"python {submission}").stdin(inputs[0]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
  




