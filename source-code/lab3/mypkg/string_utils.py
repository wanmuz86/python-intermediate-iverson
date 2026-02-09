#Absolute import
# from mypkg.math_utils import add

#Relative import 
from .math import add

def shout(text):
    return text.upper()

def repeat_and_add_text(text,a,b):
    return f"{text} {add(a,b)}"