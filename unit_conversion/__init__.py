import check50
import check50.py
import random

submission = "unit_conversion.py"
solution   = "unit_conversion_solution.pyc"

help_message = "Check to make sure you are doing the calculations correctly and that your output is formatted exactly."

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
    """Does unit_conversion.py exist?"""
    check50.exists("unit_conversion.py")
    check50.include("unit_conversion_solution.pyc")

@check50.check(exists)
def compiles():
    """Does your .py file compile?"""
    check50.py.compile("unit_conversion.py")

@check50.check(compiles)
def check1():
    """Is output correct for input 10 feet, 20 pounds, and 30 days?"""
    
    commands = ["10", "20", "30"]
    
    expected = check50.run(f"python {solution}").stdin(commands[0]).stdin(commands[1]).stdin(commands[2]).stdout()
    actual   = check50.run(f"python {submission}").stdin(commands[0]).stdin(commands[1]).stdin(commands[2]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
    
@check50.check(check1)
def check2():
    """Is output correct for random input?"""
    
    commands = []
    for i in range(3):
        commands.append(f"{random.randint(100,1000)}")
    
    
    expected = check50.run(f"python {solution}").stdin(commands[0]).stdin(commands[1]).stdin(commands[2]).stdout()
    actual   = check50.run(f"python {submission}").stdin(commands[0]).stdin(commands[1]).stdin(commands[2]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)


