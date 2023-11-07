import check50
import check50.py
import random

python_command = "python3.11"
submitted_file = "isPalindrome_function.py"
driver_file = "isPalindrome_function_driver.py"
solution_file = "isPalindrome_function_solution.pyc"


import string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

def randomPalindrome(length):
    if length % 2 == 0:
        word = randomword(length//2)
        return word + word[::-1]
    else:
        word = randomword(length//2)
        return word + randomword(1) + word[::-1]


@check50.check()
def exists():
    """Does the solution .py exist?"""
    check50.exists(submitted_file)
    check50.include(driver_file)
    check50.include(solution_file)
    
@check50.check(exists)
def compiles():
    """Does your .py file compile?"""
    check50.py.compile(submitted_file)
    check50.py.append_code(submitted_file, driver_file)

    
@check50.check(compiles)
def check1():
    """Is output correct for a "racecar"?"""
    word = "racecar"
    
    expected = check50.run(f"{python_command} {solution_file} {word}").stdout()
    actual   = check50.run(f"{python_command} {submitted_file} {word}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual)


@check50.check(compiles)
def check2():
    """Is output correct for a random word?"""
    word = randomword(8)
    
    expected = check50.run(f"{python_command} {solution_file} {word}").stdout()
    actual   = check50.run(f"{python_command} {submitted_file} {word}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual)


@check50.check(compiles)
def check3():
    """Is output correct for a random even length palindrome?"""
    word = randomPalindrome(8)
    
    expected = check50.run(f"{python_command} {solution_file} {word}").stdout()
    actual   = check50.run(f"{python_command} {submitted_file} {word}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual)


@check50.check(compiles)
def check3():
    """Is output correct for a random odd length palindrome?"""
    word = randomPalindrome(7)
    
    expected = check50.run(f"{python_command} {solution_file} {word}").stdout()
    actual   = check50.run(f"{python_command} {submitted_file} {word}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual)
