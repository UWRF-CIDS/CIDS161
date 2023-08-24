import check50
import check50.py

submission = "hello_world.py"

@check50.check()
def exists():
    """Does your .py file exist?"""
    check50.exists(submission)

@check50.check(exists)
def compiles():
    """Does your .py file compile?"""
    check50.py.compile(submission)

@check50.check(compiles)
def hello_world():
    """Is the output correct?"""
    check50.run("python3 hello_world.py").stdout("Hello, World!", regex=False).exit(0)
