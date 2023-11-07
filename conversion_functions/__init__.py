import check50
import check50.py
import random

python_command = "python3.11"
submitted_file = "conversion_functions.py"
driver_file = "conversion_functions_driver.py"
solution_file = "conversion_functions_solution.pyc"


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
    """Is output correct for when converting from feet to furlongs?"""
    feet = random.uniform(2, 100)

    expected = check50.run(f"{python_command} {solution_file} feet {feet}").stdout()
    actual   = check50.run(f"{python_command} {submitted_file} feet {feet}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual)
    
@check50.check(compiles)
def check2():
    """Is output correct for when converting from pounds to firkins?"""
    pounds = random.uniform(2, 100)

    expected = check50.run(f"{python_command} {solution_file} pounds {pounds}").stdout()
    actual   = check50.run(f"{python_command} {submitted_file} pounds {pounds}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual)

@check50.check(compiles)
def check3():
    """Is output correct for when converting from days to fortnights?"""
    days = random.uniform(2, 100)

    expected = check50.run(f"{python_command} {solution_file} days {days}").stdout()
    actual   = check50.run(f"{python_command} {submitted_file} days {days}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual)
   