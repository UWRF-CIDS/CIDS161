import check50
import check50.py
import random

python_command = "python3.11"
submitted_file = "printStairs_function.py"
driver_file = "printStairs_function_driver.py"
solution_file = "printStairs_function_solution.pyc"


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
    """Is output correct for printStairs1 with a random stair size between sizes 4 to 15?"""
    size = random.randrange(4, 15)
    
    option = "1"
    expected = check50.run(f"{python_command} {solution_file} {option} {size}").stdout()
    actual   = check50.run(f"{python_command} {submitted_file} {option} {size}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual)


@check50.check(compiles)
def check2():
    """Is output correct for printStairs2 with a random stair size between sizes 4 to 15?"""
    size = random.randrange(4, 15)
    
    option = "2"
    expected = check50.run(f"{python_command} {solution_file} {option} {size}").stdout()
    actual   = check50.run(f"{python_command} {submitted_file} {option} {size}").stdout()
    
    if expected != actual:
        raise check50.Mismatch(expected, actual)

