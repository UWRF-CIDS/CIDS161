import check50
import check50.py
import random
import string

python_command = "python"
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
    """Is output correct for encrypting "hello" with key 3?"""
    
    inputs = ["1", "hello", "3", "[ENTER]", "3"]
    
    expected = check50.run(f"{python_command} {solution}")
    for s in inputs:
        expected = expected.stdin(s)
    expected = expected.stdout()
    
    actual   = check50.run(f"{python_command} {submission}")
    for s in inputs:
        actual = actual.stdin(s)
    actual = actual.stdout()    
    
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)



@check50.check(check1)
def check2():
    """Is output correct for encrypting "hello" with key 5?"""
    
    inputs = ["1", "hello", "5", "[ENTER]", "3"]
    
    expected = check50.run(f"{python_command} {solution}")
    for s in inputs:
        expected = expected.stdin(s)
    expected = expected.stdout()
    
    actual   = check50.run(f"{python_command} {submission}")
    for s in inputs:
        actual = actual.stdin(s)
    actual = actual.stdout()   
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
   
@check50.check(check2)
def check3():
    """Is output correct for decrypting "khoor" with key 3?"""
    
    inputs = ["2", "khoor", "3", "[ENTER]", "3"]
    
    expected = check50.run(f"{python_command} {solution}")
    for s in inputs:
        expected = expected.stdin(s)
    expected = expected.stdout()
    
    actual   = check50.run(f"{python_command} {submission}")
    for s in inputs:
        actual = actual.stdin(s)
    actual = actual.stdout()   
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
   

@check50.check(check3)
def check4():
    """Is output correct for decrypting "mjqqt" with key 5?"""
    
    inputs = ["2", "mjqqt", "5", "[ENTER]", "3"]
    
    expected = check50.run(f"{python_command} {solution}")
    for s in inputs:
        expected = expected.stdin(s)
    expected = expected.stdout()
    
    actual   = check50.run(f"{python_command} {submission}")
    for s in inputs:
        actual = actual.stdin(s)
    actual = actual.stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
   

@check50.check(check4)
def check5():
    """Is output correct for encrypting "xyz" with key 3?"""
    
    inputs = ["1", "xyz", "3", "[ENTER]", "3"]
    
    expected = check50.run(f"{python_command} {solution}")
    for s in inputs:
        expected = expected.stdin(s)
    expected = expected.stdout()
    
    actual   = check50.run(f"{python_command} {submission}")
    for s in inputs:
        actual = actual.stdin(s)
    actual = actual.stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
   
@check50.check(check5)
def check6():
    """Is output correct for decrypting "abc" with key 3?"""
    
    inputs = ["2", "abc", "3", "[ENTER]", "3"]
    
    expected = check50.run(f"{python_command} {solution}")
    for s in inputs:
        expected = expected.stdin(s)
    expected = expected.stdout()
    
    actual   = check50.run(f"{python_command} {submission}")
    for s in inputs:
        actual = actual.stdin(s)
    actual = actual.stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)


@check50.check(check4)
def check7():
    """Is output correct for encrypting "UPPERlower" with key 6?"""
    
    inputs = ["1", "UPPERlower", "6", "[ENTER]", "3"]
    
    expected = check50.run(f"{python_command} {solution}")
    for s in inputs:
        expected = expected.stdin(s)
    expected = expected.stdout()
    
    actual   = check50.run(f"{python_command} {submission}")
    for s in inputs:
        actual = actual.stdin(s)
    actual = actual.stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
   

@check50.check(check4)
def check8():
    """Is output correct for encrypting "123digits123" with key 3?"""
    
    inputs = ["1", "123digits123", "3", "[ENTER]", "3"]
    
    expected = check50.run(f"{python_command} {solution}")
    for s in inputs:
        expected = expected.stdin(s)
    expected = expected.stdout()
    
    actual   = check50.run(f"{python_command} {submission}")
    for s in inputs:
        actual = actual.stdin(s)
    actual = actual.stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)




@check50.check(check4)
def check9():
    """Is output correct for encrypting "special..;()*&^" with key 5?"""
    
    inputs = ["1", "special..;()*&^", "5", "[ENTER]", "3"]
    
    expected = check50.run(f"{python_command} {solution}")
    for s in inputs:
        expected = expected.stdin(s)
    expected = expected.stdout()
    
    actual   = check50.run(f"{python_command} {submission}")
    for s in inputs:
        actual = actual.stdin(s)
    actual = actual.stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
   

@check50.check(check7)
def check10():
    """Is output correct for encrypting a random strings and random rotations?"""

    letters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(letters) for i in range(random.randint(10, 20)))
    random_rotation = str(random.randint(-20, 20))
    inputs = ["1", random_string, random_rotation, "[ENTER]", "3"]
    
    expected = check50.run(f"{python_command} {solution}")
    for s in inputs:
        expected = expected.stdin(s)
    expected = expected.stdout()
    
    actual   = check50.run(f"{python_command} {submission}")
    for s in inputs:
        actual = actual.stdin(s)
    actual = actual.stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
   
@check50.check(check7)
def check11():
    """Is output correct for decrypting a random strings and random rotations?"""

    letters = string.ascii_letters + string.digits + string.punctuation
    random_string = ''.join(random.choice(letters) for i in range(random.randint(10, 20)))
    random_rotation = str(random.randint(-20, 20))
    inputs = ["2", random_string, random_rotation, "[ENTER]", "3"]
    
    expected = check50.run(f"{python_command} {solution}")
    for s in inputs:
        expected = expected.stdin(s)
    expected = expected.stdout()
    
    actual   = check50.run(f"{python_command} {submission}")
    for s in inputs:
        actual = actual.stdin(s)
    actual = actual.stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual, help=help_message)
   
