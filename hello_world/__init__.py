import check50

@check50.check()
def hello_world():
    """check for correct output"""
    check50.run("python3 hello_world.py").stdout("Hello, world!", regex=False).exit(0)
