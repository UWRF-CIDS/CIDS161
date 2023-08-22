import check50
import check50.py
import random

submission = "math_interpreter.py"
solution   = "math_interpreter_solution.pyc"

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
def check_add1():
    """Is output correct for input 1 + 2?"""
    
    test_input = "1 + 2"
    
    expected = check50.run(f"python ./{solution}").stdin(test_input).stdout()
    actual   = check50.run(f"python {submission}").stdin(test_input).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
    
@check50.check(check_add1)
def check_add2():
    """Is output correct for adding two random numbers?"""
    
    test_input = str(random.randint(-100, 100)) + " + " + str(random.randint(-100, 100))
    
    expected = check50.run(f"python {solution}").stdin(test_input).stdout()
    actual   = check50.run(f"python {submission}").stdin(test_input).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)



@check50.check(compiles)
def check_substract1():
    """Is output correct for input 1 - 2?"""
    
    test_input = "1 - 2"
    
    expected = check50.run(f"python {solution}").stdin(test_input).stdout()
    actual   = check50.run(f"python {submission}").stdin(test_input).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
    
@check50.check(check_substract1)
def check_substract2():
    """Is output correct for subtracting two random numbers?"""
    
    test_input = str(random.randint(-100, 100)) + " - " + str(random.randint(-100, 100))
    
    expected = check50.run(f"python {solution}").stdin(test_input).stdout()
    actual   = check50.run(f"python {submission}").stdin(test_input).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)



@check50.check(compiles)
def check_multiply1():
    """Is output correct for input 1 * 2?"""
    
    test_input = "1 * 2"
    
    expected = check50.run(f"python {solution}").stdin(test_input).stdout()
    actual   = check50.run(f"python {submission}").stdin(test_input).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
    
@check50.check(check_multiply1)
def check_multiply2():
    """Is output correct for subtracting two random numbers?"""
    
    test_input = str(random.randint(-100, 100)) + " * " + str(random.randint(-100, 100))
    
    expected = check50.run(f"python {solution}").stdin(test_input).stdout()
    actual   = check50.run(f"python {submission}").stdin(test_input).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)



@check50.check(compiles)
def check_divide1():
    """Is output correct for input 1 / 2?"""
    
    test_input = "1 / 2"
    
    expected = check50.run(f"python {solution}").stdin(test_input).stdout()
    actual   = check50.run(f"python {submission}").stdin(test_input).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
    
@check50.check(check_divide1)
def check_divide2():
    """Is output correct for dividing two random numbers?"""
    
    test_input = str(random.randint(-100, 100)) + " / " + (str(random.randint(1, 100)) if random.randint(0, 2) == 0 else str(random.randint(-100, 1)))
    
    expected = check50.run(f"python {solution}").stdin(test_input).stdout()
    actual   = check50.run(f"python {submission}").stdin(test_input).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
        
        
        

@check50.check(compiles)
def check_modulo1():
    """Is output correct for input 5 % 2?"""
    
    test_input = "5 % 2"
    
    expected = check50.run(f"python {solution}").stdin(test_input).stdout()
    actual   = check50.run(f"python {submission}").stdin(test_input).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
    
@check50.check(check_modulo1)
def check_modulo2():
    """Is output correct for finding the remainder of dividing two random numbers?"""
    
    test_input = str(random.randint(100, 1000)) + " % " + str(random.randint(10, 90))
    
    expected = check50.run(f"python {solution}").stdin(test_input).stdout()
    actual   = check50.run(f"python {submission}").stdin(test_input).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)


