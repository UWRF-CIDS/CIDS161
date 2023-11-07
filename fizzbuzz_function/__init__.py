import check50
import check50.py
import random

python_command = "python3.11"
submitted_file = "fizzbuzz_function.py"
driver_file = "fizzbuzz_function_driver.py"
solution_file = "fizzbuzz_function_solution.pyc"


import string

def randomword(length):
   letters = string.ascii_lowercase
   return ''.join(random.choice(letters) for i in range(length))

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
    """Is output correct for when calling fizzbuzz with no arguments?"""
    fizz = randomword(4)
    buzz = randomword(4)
    fizzbuzz = fizz = randomword(8)
    count = random.randint(17, 31)

    option = 0
    expected = check50.run(f"{python_command} {solution_file} {option} {count} {fizz} {buzz} {fizzbuzz}").stdout()
    actual   = check50.run(f"{python_command} {submitted_file} {option} {count} {fizz} {buzz} {fizzbuzz}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual)

@check50.check(compiles)
def check2():
    """Is output correct for when calling fizzbuzz with only a count argument?"""
    fizz = randomword(4)
    buzz = randomword(4)
    fizzbuzz = fizz = randomword(8)
    count = random.randint(17, 31)

    option = 1
    expected = check50.run(f"{python_command} {solution_file} {option} {count} {fizz} {buzz} {fizzbuzz}").stdout()
    actual   = check50.run(f"{python_command} {submitted_file} {option} {count} {fizz} {buzz} {fizzbuzz}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual)

@check50.check(compiles)
def check3():
    """Is output correct for when calling fizzbuzz with 2 argument2?"""
    fizz = randomword(4)
    buzz = randomword(4)
    fizzbuzz = fizz = randomword(8)
    count = random.randint(17, 31)

    option = 2
    expected = check50.run(f"{python_command} {solution_file} {option} {count} {fizz} {buzz} {fizzbuzz}").stdout()
    actual   = check50.run(f"{python_command} {submitted_file} {option} {count} {fizz} {buzz} {fizzbuzz}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual)

@check50.check(compiles)
def check4():
    """Is output correct for when calling fizzbuzz with 3 arguments?"""
    fizz = randomword(4)
    buzz = randomword(4)
    fizzbuzz = fizz = randomword(8)
    count = random.randint(17, 31)

    option = 3
    expected = check50.run(f"{python_command} {solution_file} {option} {count} {fizz} {buzz} {fizzbuzz}").stdout()
    actual   = check50.run(f"{python_command} {submitted_file} {option} {count} {fizz} {buzz} {fizzbuzz}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual)

@check50.check(compiles)
def check5():
    """Is output correct for when calling fizzbuzz with 4 arguments?"""
    fizz = randomword(4)
    buzz = randomword(4)
    fizzbuzz = fizz = randomword(8)
    count = random.randint(17, 31)

    option = 4
    expected = check50.run(f"{python_command} {solution_file} {option} {count} {fizz} {buzz} {fizzbuzz}").stdout()
    actual   = check50.run(f"{python_command} {submitted_file} {option} {count} {fizz} {buzz} {fizzbuzz}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual)

@check50.check(compiles)
def check6():
    """Is output correct for when calling fizzbuzz all arguments set by variable name?"""
    fizz = randomword(4)
    buzz = randomword(4)
    fizzbuzz = fizz = randomword(8)
    count = random.randint(17, 31)

    option = 5
    expected = check50.run(f"{python_command} {solution_file} {option} {count} {fizz} {buzz} {fizzbuzz}").stdout()
    actual   = check50.run(f"{python_command} {submitted_file} {option} {count} {fizz} {buzz} {fizzbuzz}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual)
    