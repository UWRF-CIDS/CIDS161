import check50
import check50.py
import random
import string

python_command = "python3.11"
submission = "caesar_cipher.py"
solution   = "caesar_cipher_solution.pyc"

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
   
@check50.check(check1)
def check2():
    """Is output correct for input hello -5?"""
    
    inputs = ["hello", "-5"]
    
    expected = check50.run(f"{python_command} {solution}").stdin(inputs[0]).stdin(inputs[1]).stdout()
    actual   = check50.run(f"{python_command} {submission}").stdin(inputs[0]).stdin(inputs[1]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)


@check50.check(check2)
def check3():
    """Is output correct for input UPPERlower 6?"""
    
    inputs = ["UPPERlower", "6"]
    
    expected = check50.run(f"{python_command} {solution}").stdin(inputs[0]).stdin(inputs[1]).stdout()
    actual   = check50.run(f"{python_command} {submission}").stdin(inputs[0]).stdin(inputs[1]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
   

@check50.check(check3)
def check4():
    """Is output correct for input digits123 3?"""
    
    inputs = ["digits123", "3"]
    
    expected = check50.run(f"{python_command} {solution}").stdin(inputs[0]).stdin(inputs[1]).stdout()
    actual   = check50.run(f"{python_command} {submission}").stdin(inputs[0]).stdin(inputs[1]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)




@check50.check(check4)
def check5():
    """Is output correct for input special..;()*&^ 5?"""
    
    inputs = ["special..;()*&^", "5"]
    
    expected = check50.run(f"{python_command} {solution}").stdin(inputs[0]).stdin(inputs[1]).stdout()
    actual   = check50.run(f"{python_command} {submission}").stdin(inputs[0]).stdin(inputs[1]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
   

@check50.check(check5)
def check6():
    """Is output correct for a random strings and random rotations?"""

    letters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(letters) for i in range(random.randint(10, 20)))
    random_rotation = str(random.randint(-20, 20))
    inputs = [random_string, random_rotation]
    
    expected = check50.run(f"{python_command} {solution}").stdin(inputs[0]).stdin(inputs[1]).stdout()
    actual   = check50.run(f"{python_command} {submission}").stdin(inputs[0]).stdin(inputs[1]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
   
@check50.check(check5)
def check7():
    """Is output correct for a random strings and random rotations?"""

    letters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(letters) for i in range(random.randint(10, 20)))
    random_rotation = str(random.randint(-20, 20))
    inputs = [random_string, random_rotation]
    
    expected = check50.run(f"{python_command} {solution}").stdin(inputs[0]).stdin(inputs[1]).stdout()
    actual   = check50.run(f"{python_command} {submission}").stdin(inputs[0]).stdin(inputs[1]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
   

@check50.check(check5)
def check8():
    """Is output correct for a random strings and random rotations?"""

    letters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(letters) for i in range(random.randint(10, 20)))
    random_rotation = str(random.randint(-20, 20))
    inputs = [random_string, random_rotation]
    
    expected = check50.run(f"{python_command} {solution}").stdin(inputs[0]).stdin(inputs[1]).stdout()
    actual   = check50.run(f"{python_command} {submission}").stdin(inputs[0]).stdin(inputs[1]).stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
   


