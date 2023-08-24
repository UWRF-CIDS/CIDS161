import check50
import check50.py
import random
import string
import numpy as np
import os


python_command = "python3.11"
submission = "image_processing.py"
solution = "image_processing_solution.pyc"
test_grayscale = "test_grayscale.py"
test_redify = "test_redify.py"
test_trippy = "test_trippy.py"
test_invert_color = "test_invert_color.py"
test_flip_horizontally = "test_flip_horizontally.py"
test_flip_vertically = "test_flip_vertically.py"


@check50.check()
def exists():
    """Does the solution .py exist?"""
    check50.exists(submission)
    check50.include(test_grayscale)
    check50.include(test_redify)
    check50.include(test_trippy)
    check50.include(test_invert_color)
    check50.include(test_flip_horizontally)
    check50.include(test_flip_vertically)
    check50.include(solution)

@check50.check(exists)
def compiles():
    """Does your .py file compile?"""
    check50.py.compile(submission)

@check50.check(compiles)
def check1():
    """Can the program make an image grayscale?"""
    
    check50.py.append_code(submission, test_grayscale)
    
    output = check50.run(f"{python_command} {submission}").stdout()
    
    if output.strip() != "grayscale":
        raise check50.Failure("Making the image grayscale did not seem to work...", help=output)

@check50.check(compiles)
def check2():
    """Can the program make an image \"redscale\"?"""
    
    check50.py.append_code(submission, test_redify)
    
    output = check50.run(f"{python_command} {submission}").stdout()
    
    if output.strip() != "redify":
        raise check50.Failure("Making the image \"redscale\" did not seem to work...", help="")
        
        
@check50.check(compiles)
def check3():
    """Can the program invert the color of an image?"""
    
    check50.py.append_code(submission, test_invert_color)
    
    output = check50.run(f"{python_command} {submission}").stdout()
    
    if output.strip() != "invert_color":
        raise check50.Failure("Inverting the color of an image did not seem to work...", help="")
        
    
        
@check50.check(compiles)
def check4():
    """Can the program flip an image horizontally?"""
    
    check50.py.append_code(submission, test_flip_horizontally)
    
    output = check50.run(f"{python_command} {submission}").stdout()
    
    if output.strip() != "flip_horizontally":
        raise check50.Failure("Flipping an image horizontally did not seem to work...", help="")
                
        
@check50.check(compiles)
def check5():
    """Can the program flip an image vertically?"""
    
    check50.py.append_code(submission, test_flip_vertically)
    
    output = check50.run(f"{python_command} {submission}").stdout()
    
    if output.strip() != "flip_vertically":
        raise check50.Failure("Flipping an image vertically did not seem to work...", help="")
                
        
        
        
@check50.check(compiles)
def check6():
    """Can the program make an image trippy?"""
    
    check50.py.append_code(submission, test_trippy)
    
    output = check50.run(f"{python_command} {submission}").stdout()
    
    if output.strip() != "trippy":
        raise check50.Failure("Making an image trippy did not seem to work...", help="")
                
                
        
        
        
