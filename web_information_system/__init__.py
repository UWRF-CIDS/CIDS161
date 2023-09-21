import check50
import check50.py
import check50.flask
import random
import string

python_command = "python3.11"
submission = "app.py"
solution   = "app_solution.pyc"
file1 = "todos.json"
file2 = "todos2.json"
original = "original.json"


help_message = "Check to make sure that your output is formatted exactly including any space, tab, and newline characters."


@check50.check()
def exists():
    """Does the solution .py exist?"""
    check50.exists(submission)
    #check50.include(solution)
    check50.include(file1)
    #check50.include(file2)
    #check50.include(original)

@check50.check(exists)
def compiles():
    """Does your .py file compile?"""
    check50.py.compile(submission)

@check50.check(compiles)
def check1():
    """Does app load?"""

    check50.flask.app(submission).get("/").status(200)
    
@check50.check(check1)
def check2():
    """Is page title "Todos"?"""
    check50.flask.app(submission).get("/").content(output="Todos", name="title")
    
@check50.check(check2)
def check3():
    """Is there a "Todos" h1 header?"""
    check50.flask.app(submission).get("/").content(output="Todos", name="h1")
    
@check50.check(check3)
def check4():
    """Is there a "Add a Todo" h2 header?"""
    check50.flask.app(submission).get("/").content(output="Add a Todo", name="h2")
    
@check50.check(check4)
def check5():
    """Is there a "All Todos" h2 header?"""
    check50.flask.app(submission).get("/").content(output="Add a Todo", name="h2")
    
@check50.check(check5)
def check6():
    """Are the todos on the page?"""
    check50.flask.app(submission).get("/").content(output="Todo Title")
    
@check50.check(check6)
def check7():
    """Can a new todo be created?"""
    check50.flask.app(submission).post("/", data={"title": "new todo", "tasks": ["new task 1", "new task 2", "new task 3"]}).status(200)
    check50.flask.app(submission).get("/").content(output="new todo")
    
@check50.check(check7)
def check8():
    """Can a todo be deleted?"""
    check50.flask.app(submission).post("/delete", data={"todoId": "1"}).status(200)
    
    




